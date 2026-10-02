"""Verify local archive consistency, not service authenticity or authorship."""
from pathlib import Path
from datetime import datetime
import hashlib, json, re

base=Path(__file__).resolve().parent/'deeper-trial'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
norm=lambda s:re.sub(r'\s+',' ',s).strip()
data=json.loads((base/'results.json').read_text('utf-8'))
seen=set()
frozen=json.loads((base/'frozen-inputs.json').read_text('utf-8'))
for rec in data['records']:
    assert rec['id'] not in seen,rec['id']
    seen.add(rec['id'])
    assert rec['status']=='completed' and 0<=rec['score']<=100
    datetime.fromisoformat(rec['observed_at'].replace('Z','+00:00'))
    for field,hashfield in [('input_path','input_sha256'),('receipt','receipt_sha256')]:
        p=(base/rec[field]).resolve()
        assert p.is_relative_to(base.resolve())
        assert sha(p)==rec[hashfield],(rec['id'],field)
    observation=json.loads((base/'observations'/f'{rec["id"]}.json').read_text('utf-8'))
    assert observation=={k:v for k,v in rec.items() if k not in ['status','receipt_sha256']}
    submitted=(base/rec['input_path']).read_bytes().decode('utf-8').strip()
    assert hashlib.sha256(submitted.encode()).hexdigest()==rec['submitted_sha256']
    assert frozen[rec['input_path']]==rec['input_sha256']
    raw=(base/rec['receipt']).read_text('utf-8')
    if rec['vendor']=='GPTZero':
        assert rec['input_verified_in_dom'] is True
        assert 'Text up-to-date' in raw and f'heading {rec["scan_type"]} Scan' in raw
        for field,label in [('ai','AI'),('human','Human'),('mixed','Mixed')]:
            assert int(re.search(r'button '+label+r' (\d+)%',raw)[1])==rec[field]
        assert rec['score']==rec['human'] and rec['metric']=='Human document probability'
        assert sum(rec[k] for k in ['ai','human','mixed'])==100
        assert re.search(r'Model\s+(\S+)',raw)[1]==rec['model']
    elif rec['vendor']=='QuillBot':
        assert rec['input_verified_in_dom'] is True and 'Outdated score' not in raw
        for field,label in [('ai','AI-generated'),('human','Human-written'),('refined','Human-written & AI-refined')]:
            assert int(re.search(r'text '+re.escape(label)+r'\r?\n[\s\S]*?text (\d+) %',raw)[1])==rec[field]
        assert rec['score']==rec['human'] and rec['metric']=='Human-written text percentage'
        assert sum(rec[k] for k in ['ai','human','refined'])==100
        assert re.search(r'Model (v[\d.]+)',raw)[1]==rec['model']
    elif rec['vendor']=='Sapling':
        assert rec['truncated'] is False
        while isinstance(raw,str):raw=json.loads(raw)
        assert raw['ai_probability_percent']==rec['score'] and raw['truncated'] is False
        assert norm(' '.join(x['sentence'] for x in raw['sentence_scores']))==norm(submitted)
    elif rec['vendor']=='ZeroGPT':
        assert rec['input_verified_in_result'] is True
        assert float(re.search(r'(\d+(?:\.\d+)?)%\s*AI GPT',raw)[1])==rec['score']
        assert norm(submitted) in norm(raw)
    else:raise AssertionError(rec['vendor'])
for rel,expected in frozen.items():assert sha(base/rel)==expected,rel
for mapping,folder,sources in [('blind-mapping.json','blind','sources'),('fresh-mapping.json','fresh-blind','fresh-sources')]:
    for case,entries in json.loads((base/mapping).read_text('utf-8')).items():
        assert sha(base/folder/case/'source.txt')==sha(base/sources/f'{case}.txt')
        for label,entry in entries.items():
            assert sha(base/entry['input'])==entry['sha256']
            assert sha(base/folder/case/f'{label}.txt')==entry['sha256']
repairs=json.loads((base/'repair-log.json').read_text('utf-8'))
for repair in repairs:
    before=(base/repair['input']).read_text('utf-8')
    assert before.count(repair['before'])==1
    assert before.replace(repair['before'],repair['after'])==(base/repair['output']).read_text('utf-8')
for method in ['a','b']:
    for p in (base/method).glob('*.txt'):
        rel=f'final/{method}-{p.name}'
        if not any(r['output']==rel for r in repairs):assert sha(p)==sha(base/rel)
for rel,expected in json.loads((base/'release-skill-hashes.json').read_text('utf-8')).items():
    assert sha(base.parents[1]/'skills/bilingual-humanizer'/rel)==expected,rel
assert data['all_detectors_native_human_above_50_achieved'] is False
assert any(r['vendor']=='GPTZero' and r['score']==0 for r in data['records'])
print(f'PASS: {len(seen)} deeper-trial observations; native scores, inputs, repairs, blind mappings and release hashes agree.')
