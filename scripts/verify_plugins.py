"""Check plugin/catalog integrity without running agents or contacting environments."""
import json
import re
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
def load(path):
    return json.loads(path.read_text(encoding='utf-8'))
def main():
    marketplace=load(ROOT/'.claude-plugin/marketplace.json')
    plugins=marketplace['plugins']
    assert len({p['name'] for p in plugins})==len(plugins)
    skills_count=agents_count=0
    for item in plugins:
        root=(ROOT/item['source']).resolve()
        assert root.is_relative_to(ROOT)
        manifest=load(root/'.claude-plugin/plugin.json')
        assert manifest['name']==item['name']
        for path in list((root/'skills').glob('*/SKILL.md'))+list((root/'agents').glob('*.md')):
            content=path.read_text(encoding='utf-8')
            front=yaml.safe_load(content.split('---',2)[1])
            assert front['name'] and front['description'],path
            if path.name=='SKILL.md':skills_count+=1
            else:agents_count+=1
            for match in re.finditer(r'\]\(([^)]+)\)',content):
                target=match[1].split('#')[0]
                if not target or '://' in target or target.startswith(('/', '$')):continue
                # Inherited Appian reference has external example paths; inspect maintained files.
                if 'appian-referencia' in path.parts:continue
                assert (path.parent/target).resolve().exists(),(path,target)
        if (root/'contracts/catalog.json').exists():
            catalog=load(root/'contracts/catalog.json')
            cids={c['id'] for c in catalog['criteria']}
            assert len(cids)==len(catalog['criteria'])
            for role in catalog['roles']:
                assert set(role['criterion_ids'])<=cids
                assert (root/'agents'/f"{role['id']}.md").exists()
                assert (root/'skills'/f"{item['name']}-{role['id']}"/'SKILL.md').exists()
    docs=[]
    for file in (ROOT/'catalog').glob('*.yaml'):
        docs+=list(yaml.safe_load_all(file.read_text(encoding='utf-8')))
    entities={f"{e['kind'].lower()}:default/{e['metadata']['name']}":e for e in docs if e}
    assert len(entities)==len([e for e in docs if e]),'Duplicate catalog entity'
    for entity in entities.values():
        for field in ('plugins','skills','dependsOn'):
            for ref in entity.get('spec',{}).get(field,[]):
                if ref.startswith('airesource:'):assert ref in entities,ref
    print(json.dumps({'plugins':len(plugins),'skills':skills_count,'agents':agents_count,
                      'catalog_entities':len(entities),'valid':True}))

if __name__=='__main__':main()
