"""Validate and resume a P4/P5 work plan. No environment or approval is inferred."""
import argparse
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def require(condition, message):
    if not condition:
        raise ValueError(message)

def unique(items, label):
    ids = [item['id'] for item in items]
    require(all(isinstance(i, str) and i.strip() for i in ids), f'{label}: empty ID')
    require(len(ids) == len(set(ids)), f'{label}: duplicate ID')
    return set(ids)

def check(plan, catalog):
    require(isinstance(plan, dict), 'Plan must be an object')
    require(set(plan) == {'version','technology','project','catalog_version','p4','tasks','pending'}, 'Missing or extra plan fields')
    require(plan.get('version') == 'profuturo-handoff-v1', 'Unknown contract version')
    require(plan.get('technology') == catalog['technology'], 'Wrong technology')
    require(plan.get('project', '').strip(), 'Missing project')
    p4 = plan.get('p4', {})
    require(p4.get('source_refs') and p4.get('product_id'), 'Missing P4 source')
    require(re.fullmatch(r'[0-9a-fA-F]{64}', p4.get('sha256', '')), 'Invalid P4 SHA256')
    require(plan.get('catalog_version') == catalog['version'], 'Catalog version mismatch')
    tasks = plan.get('tasks', [])
    require(tasks, 'Empty task plan')
    tids = unique(tasks, 'tasks')
    pids = unique(plan.get('pending', []), 'pending')
    cids = {c['id'] for c in catalog['criteria']}
    roles = {r['id'] for r in catalog['roles']}
    owners = {}
    for pending in plan.get('pending', []):
        require(pending.get('question', '').strip(), 'Pending without question')
        require(set(pending.get('blocks', [])) <= tids, 'Pending blocks unknown task')
    for task in tasks:
        require(task.get('role') in roles, 'Unknown role')
        require(set(task) == {'id','role','depends_on','writes','criteria','source_refs','pending_ids'}, 'Missing or extra task fields')
        for key in ('depends_on','writes','criteria','source_refs','pending_ids'):
            require(isinstance(task.get(key), list) and all(isinstance(v,str) and v.strip() for v in task[key]), 'Task arrays require non-empty strings')
            require(len(task[key]) == len(set(task[key])), 'Duplicate task array value')
        require(task.get('source_refs'), 'Task without source')
        require(task.get('criteria') and set(task['criteria']) <= cids, 'Unknown or empty criteria')
        role = next(r for r in catalog['roles'] if r['id'] == task['role'])
        require(set(task['criteria']) <= set(role['criterion_ids']), 'Criteria outside assigned role')
        require(set(task.get('pending_ids', [])) <= pids, 'Unknown pending reference')
        require(set(task.get('depends_on', [])) <= tids, 'Unknown dependency')
        require(task['id'] not in task.get('depends_on', []), 'Self dependency')
        for obj in task.get('writes', []):
            require(obj not in owners, f'Multiple writers for {obj}')
            owners[obj] = task['id']
    visiting, visited = set(), set()
    by_id = {t['id']: t for t in tasks}
    def visit(tid):
        require(tid not in visiting, 'Dependency cycle')
        if tid in visited:
            return
        visiting.add(tid)
        for dep in by_id[tid].get('depends_on', []):
            visit(dep)
        visiting.remove(tid)
        visited.add(tid)
    for tid in by_id:
        visit(tid)
    return plan

def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def validate_result(plan, catalog, result, workspace):
    check(plan, catalog)
    require(result.get('plan_sha256') == hashlib.sha256(json.dumps(plan, sort_keys=True, ensure_ascii=False).encode()).hexdigest(), 'Result belongs to another plan')
    task = next((t for t in plan['tasks'] if t['id'] == result.get('task_id')), None)
    require(task is not None, 'Unknown result task')
    status = result.get('status')
    require(status in ('built', 'tested', 'reviewed', 'approved', 'partial'), 'Unknown result status')
    require(result.get('author'), 'Missing author')
    blockers = [p for p in plan.get('pending', []) if task['id'] in p.get('blocks', [])]
    require(not blockers or status == 'partial', 'Blocked task cannot claim completion')
    root = Path(workspace).resolve()
    artifacts = result.get('artifacts', [])
    require(artifacts, 'No evidence artifacts')
    aids = unique(artifacts, 'artifacts')
    for item in artifacts:
        path = (root / item['path']).resolve()
        require(path.is_relative_to(root) and path.is_file(), 'Artifact missing or outside workspace')
        require(file_hash(path) == item.get('sha256'), 'Artifact changed or hash mismatch')
    for obj in result.get('objects', []):
        require(plan['technology'] == 'appian', 'Object confirmation applies to Appian')
        require(re.fullmatch(r'[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}', obj.get('uuid', '')), 'Invalid object UUID')
        require(obj.get('confirmation_artifact') in aids, 'Object UUID lacks query evidence')
    if plan['technology'] == 'appian' and task.get('writes') and status != 'partial':
        require(len(result.get('objects', [])) == len(task['writes']), 'Missing Appian object confirmations')
    checks = result.get('checks', [])
    require(len({c['id'] for c in checks}) == len(checks), 'Duplicate criterion result')
    require({c['id'] for c in checks} <= set(task['criteria']), 'Unknown criterion result')
    definitions = {c['id']: c for c in catalog['criteria']}
    for c in checks:
        require(c.get('status') in ('pass', 'fail', 'pending', 'not_applicable'), 'Invalid check state')
        require(c.get('rationale', '').strip(), 'Check lacks rationale')
        if c['status'] == 'pass':
            require(c.get('artifact_ids') and set(c['artifact_ids']) <= aids, 'Pass without evidence')
            if definitions[c['id']].get('runtime_required'):
                require(c.get('method') == 'runtime' and c.get('environment') and c.get('run_id'), 'Runtime proof required')
        if c['status'] == 'pending':
            require(c.get('pending_id') in {p['id'] for p in plan.get('pending', [])}, 'Check pending not declared')
    if status in ('tested', 'reviewed', 'approved'):
        require({c['id'] for c in checks} == set(task['criteria']), 'Incomplete criterion review')
        require(all(c['status'] in ('pass', 'not_applicable') for c in checks), 'Unresolved checks')
    if status in ('reviewed', 'approved'):
        require(result.get('reviewer') and result['reviewer'] != result['author'], 'Independent reviewer required')
        require(result.get('review_artifact') in aids, 'Review evidence required')
    if status == 'approved':
        require(result.get('approval', {}).get('responsible'), 'Approval responsible missing')
        require(result.get('approval', {}).get('receipt_artifact') in aids, 'Approval receipt missing')
    return result

def plan_hash(plan):
    return hashlib.sha256(json.dumps(plan, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

def record(plan, catalog, result, workspace, state_path):
    validate_result(plan, catalog, result, workspace)
    target = Path(state_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lock = target.with_suffix(target.suffix + '.lock')
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise ValueError('State is locked by another writer') from None
    try:
        os.close(fd)
        state = load(target) if target.exists() else {'plan_sha256': plan_hash(plan), 'results': {}}
        require(state['plan_sha256'] == plan_hash(plan), 'State belongs to another plan')
        task = next(t for t in plan['tasks'] if t['id'] == result['task_id'])
        for dep in task.get('depends_on', []):
            dep_result = state['results'].get(dep)
            require(dep_result and dep_result['status'] in ('reviewed', 'approved'), 'Dependency not reviewed')
            validate_result(plan, catalog, dep_result, workspace)
        prior = state['results'].get(result['task_id'])
        order = {'partial': 0, 'built': 1, 'tested': 2, 'reviewed': 3, 'approved': 4}
        if prior:
            require(order[result['status']] >= order[prior['status']], 'Use a new plan revision for regressions')
            if prior['status'] in ('reviewed', 'approved'):
                require(all(result.get(k) == prior.get(k) for k in ('author','artifacts','objects','checks','reviewer','review_artifact')),
                        'Reviewed content changed; create a new plan revision and re-review dependents')
        state['results'][result['task_id']] = result
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=target.parent, delete=False) as temp:
            json.dump(state, temp, ensure_ascii=False, indent=2)
            temp_path = Path(temp.name)
        os.replace(temp_path, target)
        return state
    finally:
        lock.unlink(missing_ok=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'result', 'record', 'status'])
    parser.add_argument('--plan', required=True)
    parser.add_argument('--catalog', default=str(Path(__file__).resolve().parents[1] / 'contracts/catalog.json'))
    parser.add_argument('--result')
    parser.add_argument('--workspace', default='.')
    parser.add_argument('--state', default='.profuturo/state.json')
    args = parser.parse_args()
    try:
        plan, catalog = load(args.plan), load(args.catalog)
        check(plan, catalog)
        if args.command == 'check':
            output = {'valid': True, 'plan_sha256': plan_hash(plan)}
        elif args.command == 'result':
            validate_result(plan, catalog, load(args.result), args.workspace)
            output = {'valid': True, 'attestation': 'Evidence structure and hashes only; human review remains required'}
        elif args.command == 'record':
            output = record(plan, catalog, load(args.result), args.workspace, args.state)
        else:
            output = load(args.state) if Path(args.state).exists() else {'plan_sha256': plan_hash(plan), 'results': {}}
            require(output['plan_sha256'] == plan_hash(plan), 'State belongs to another plan')
            for result in output['results'].values():
                validate_result(plan, catalog, result, args.workspace)
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError, AttributeError) as exc:
        parser.exit(1, str(exc) + '\n')

if __name__ == '__main__':
    main()
