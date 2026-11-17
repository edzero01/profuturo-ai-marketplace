import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.workspace = Path(self.tmp.name)
        self.artifact = self.workspace / 'query.json'
        self.artifact.write_text('{"result":"fixture; not a real environment"}', encoding='utf-8')
        path = ROOT / 'plugins/profuturo-appian/scripts/handoff.py'
        spec = importlib.util.spec_from_file_location('handoff', path)
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)
        self.catalog = {'technology':'appian','version':'1.0.0',
            'criteria':[{'id':'APP-01-01','runtime_required':True}],
            'roles':[{'id':'arquitectura','criterion_ids':['APP-01-01']}]}
        self.plan = {'version':'profuturo-handoff-v1','technology':'appian','project':'fixture',
            'catalog_version':'1.0.0','p4':{'product_id':'fixture','sha256':'a'*64,'source_refs':['fixture:1']},
            'tasks':[{'id':'T1','role':'arquitectura','depends_on':[],'writes':['object-one'],
                      'criteria':['APP-01-01'],'source_refs':['fixture:1'],'pending_ids':[]}], 'pending':[]}

    def result(self, status='reviewed'):
        return {'task_id':'T1','plan_sha256':self.m.plan_hash(self.plan),'status':status,'author':'builder',
            'reviewer':'independent-reviewer','review_artifact':'E1',
            'artifacts':[{'id':'E1','path':'query.json','sha256':self.m.file_hash(self.artifact)}],
            'objects':[{'uuid':'12345678-1234-1234-1234-123456789012','confirmation_artifact':'E1'}],
            'checks':[{'id':'APP-01-01','status':'pass','rationale':'Synthetic validator fixture only',
                       'artifact_ids':['E1'],'method':'runtime','environment':'fixture','run_id':'fixture-run'}]}

    def invalid_plan(self, edit):
        edit(self.plan)
        with self.assertRaises((ValueError, KeyError, TypeError)):
            self.m.check(self.plan, self.catalog)

    def test_valid_review_and_resume_checks_artifact_hashes(self):
        state = self.workspace / 'state.json'
        self.m.record(self.plan,self.catalog,self.result(),self.workspace,state)
        self.assertEqual(self.m.load(state)['results']['T1']['status'],'reviewed')
        self.artifact.write_text('changed',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'hash mismatch'):
            self.m.validate_result(self.plan,self.catalog,self.m.load(state)['results']['T1'],self.workspace)

    def test_reject_unknown_criterion(self):
        self.invalid_plan(lambda p:p['tasks'][0].update(criteria=['FAKE']))

    def test_reject_role_outside_assignment(self):
        self.catalog['roles'][0]['criterion_ids']=[]
        with self.assertRaisesRegex(ValueError,'assigned role'):
            self.m.check(self.plan,self.catalog)

    def test_reject_cycle(self):
        task=copy.deepcopy(self.plan['tasks'][0]); task.update(id='T2',writes=['other'],depends_on=['T1'])
        self.plan['tasks'].append(task); self.plan['tasks'][0]['depends_on']=['T2']
        with self.assertRaisesRegex(ValueError,'cycle'):
            self.m.check(self.plan,self.catalog)

    def test_reject_duplicate_writer(self):
        self.invalid_plan(lambda p:p['tasks'].append({**p['tasks'][0],'id':'T2'}))

    def test_pending_blocks_only_affected_task(self):
        self.plan['pending']=[{'id':'Q1','question':'Unknown permission','blocks':['T1']}]
        self.plan['tasks'][0]['pending_ids']=['Q1']
        with self.assertRaisesRegex(ValueError,'Blocked task'):
            self.m.validate_result(self.plan,self.catalog,self.result(),self.workspace)
        self.m.validate_result(self.plan,self.catalog,self.result('partial'),self.workspace)

    def test_reject_unknown_pending(self):
        self.invalid_plan(lambda p:p['tasks'][0].update(pending_ids=['missing']))

    def test_reject_self_review(self):
        r=self.result(); r['reviewer']=r['author']
        with self.assertRaisesRegex(ValueError,'Independent'):
            self.m.validate_result(self.plan,self.catalog,r,self.workspace)

    def test_reject_approval_without_receipt(self):
        with self.assertRaisesRegex(ValueError,'Approval'):
            self.m.validate_result(self.plan,self.catalog,self.result('approved'),self.workspace)

    def test_reject_runtime_claim_from_synthetic_check(self):
        r=self.result(); r['checks'][0]['method']='synthetic'
        with self.assertRaisesRegex(ValueError,'Runtime'):
            self.m.validate_result(self.plan,self.catalog,r,self.workspace)

    def test_reject_uuid_without_query_reference(self):
        r=self.result(); r['objects'][0]['confirmation_artifact']='missing'
        with self.assertRaisesRegex(ValueError,'query evidence'):
            self.m.validate_result(self.plan,self.catalog,r,self.workspace)

    def test_reject_invalid_uuid(self):
        r=self.result(); r['objects'][0]['uuid']='fake'
        with self.assertRaisesRegex(ValueError,'UUID'):
            self.m.validate_result(self.plan,self.catalog,r,self.workspace)

    def test_reject_artifact_outside_workspace(self):
        r=self.result(); r['artifacts'][0]['path']='../query.json'
        with self.assertRaisesRegex(ValueError,'outside workspace'):
            self.m.validate_result(self.plan,self.catalog,r,self.workspace)

    def test_dependency_requires_independent_review(self):
        task=copy.deepcopy(self.plan['tasks'][0]); task.update(id='T2',writes=['other'],depends_on=['T1'])
        self.plan['tasks'].append(task)
        r=self.result('built'); self.m.record(self.plan,self.catalog,r,self.workspace,self.workspace/'state.json')
        r=self.result(); r['task_id']='T2'
        with self.assertRaisesRegex(ValueError,'Dependency not reviewed'):
            self.m.record(self.plan,self.catalog,r,self.workspace,self.workspace/'state.json')

    def test_lock_prevents_concurrent_write(self):
        state=self.workspace/'state.json'; state.with_suffix('.json.lock').touch()
        with self.assertRaisesRegex(ValueError,'locked'):
            self.m.record(self.plan,self.catalog,self.result(),self.workspace,state)

    def test_changed_plan_rejects_old_receipt(self):
        r=self.result(); self.plan['project']='new-project'
        with self.assertRaisesRegex(ValueError,'another plan'):
            self.m.validate_result(self.plan,self.catalog,r,self.workspace)

    def test_reviewed_content_cannot_change_under_existing_dependents(self):
        state=self.workspace/'state.json'
        self.m.record(self.plan,self.catalog,self.result(),self.workspace,state)
        self.artifact.write_text('updated output',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Reviewed content changed'):
            self.m.record(self.plan,self.catalog,self.result(),self.workspace,state)

    def test_duplicate_check_cannot_fake_complete_review(self):
        r=self.result(); r['checks'].append(copy.deepcopy(r['checks'][0]))
        with self.assertRaisesRegex(ValueError,'Duplicate criterion'):
            self.m.validate_result(self.plan,self.catalog,r,self.workspace)

    def test_catalog_versions_are_pinned(self):
        self.invalid_plan(lambda p:p.update(catalog_version='2.0.0'))

    def test_all_plugin_validators_are_identical(self):
        paths=list((ROOT/'plugins').glob('profuturo-*/scripts/handoff.py'))
        self.assertEqual(len(paths),3)
        self.assertEqual(len({p.read_bytes() for p in paths}),1)

    def test_each_catalog_id_has_a_role(self):
        for path in (ROOT/'plugins').glob('profuturo-*/contracts/catalog.json'):
            catalog=json.loads(path.read_text(encoding='utf-8'))
            ids={c['id'] for c in catalog['criteria']}
            assigned={c for role in catalog['roles'] for c in role['criterion_ids']}
            self.assertEqual(ids,assigned,path)

if __name__=='__main__':
    unittest.main()
