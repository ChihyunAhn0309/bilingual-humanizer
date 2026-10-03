"""Check recorded evidence consistency; this does not call or validate a vendor."""
from pathlib import Path
from datetime import datetime
import hashlib, json, re

base=Path(__file__).resolve().parent/'continuation-e'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text('utf-8'))
date=lambda s:datetime.fromisoformat(s.replace('Z','+00:00'))
norm=lambda s:re.sub(r'\s+',' ',s).strip()
data=read(base/'results.json')
frozen=read(base/'frozen-inputs.json')
for path,digest in frozen['inputs'].items():assert sha(base/path)==digest,path
for path,entry in frozen['additional_freezes'].items():assert sha(base/path)==entry['sha256'],path
ids=set()
for rec in data['records']:
    assert rec['id'] not in ids;ids.add(rec['id'])
    assert rec['status']=='completed' and rec['input_verified_in_dom'] is True
    assert 0<=rec['score']<=100
    for pathkey,hashkey in [('input_path','input_sha256'),('receipt','receipt_sha256'),('source_path','source_sha256')]:
        path=(base/rec[pathkey]).resolve()
        assert path.is_relative_to(base.resolve()) and sha(path)==rec[hashkey]
    original=read(base/'observations'/f'{rec["id"]}.json')
    added={'status','receipt_sha256','source_path','source_sha256'}
    assert original=={k:v for k,v in rec.items() if k not in added}
    entry=frozen['additional_freezes'].get(rec['input_path'])
    frozen_date=entry['frozen_at'] if entry else frozen['frozen_at']
    digest=entry['sha256'] if entry else frozen['inputs'][rec['input_path']]
    assert rec['input_sha256']==digest and date(rec['observed_at'])>date(frozen_date)
    submitted=(base/rec['input_path']).read_bytes().decode('utf-8').strip()
    assert hashlib.sha256(submitted.encode()).hexdigest()==rec['submitted_sha256']
    raw=(base/rec['receipt']).read_text('utf-8')
    assert rec['metric']==data['targets'][rec['vendor']]['metric']
    if rec['vendor']=='GPTZero':
        assert rec['scan_type']=='Basic' and 'heading Basic Scan' in raw and 'Text up-to-date' in raw
        for field,label in [('ai','AI'),('human','Human'),('mixed','Mixed')]:
            assert int(re.search(r'button '+label+r' (\d+)%',raw)[1])==rec[field]
        assert sum(rec[k] for k in ['ai','human','mixed'])==100
        assert rec['score']==rec['human'] and re.search(r'Model\s+(\S+)',raw)[1]==rec['model']
    elif rec['vendor']=='QuillBot':
        assert 'Outdated score' not in raw
        for field,label in [('ai','AI-generated'),('human','Human-written'),('refined','Human-written & AI-refined')]:
            assert int(re.search(r'text '+re.escape(label)+r'\r?\n[\s\S]*?text (\d+) %',raw)[1])==rec[field]
        assert sum(rec[k] for k in ['ai','human','refined'])==100 and rec['score']==rec['human']
        assert re.search(r'Model (v[\d.]+)',raw)[1]==rec['model']
        assert int(re.search(r'got (\d+) AI scans? left',raw)[1])==rec['remaining_scans']
    elif rec['vendor']=='ZeroGPT':
        assert rec['input_verified_in_result'] is True and norm(submitted) in norm(raw)
        assert float(re.search(r'(\d+(?:\.\d+)?)%\s*AI GPT',raw)[1])==rec['score']
    else:raise AssertionError(rec['vendor'])
registry=read(base/'checkpoint-registry.json')
for case in registry['cases']:
    assert sha(base/case['source_path'])==case['source_sha256']
    options=case['alternatives']+[{'input_path':case['retained_input'],'sha256':case['retained_sha256'],'evidence':case['evidence']}]
    for choice in options:
        p=(base/choice['input_path']).resolve()
        assert p.is_relative_to(base.parent.resolve()) and sha(p)==choice['sha256']
        for vendor,ev in choice['evidence'].items():
            bundle=(base/ev['bundle']).resolve()
            assert bundle.is_relative_to(base.parent.resolve())
            rows=[r for r in read(bundle)['records'] if r['id']==ev['id']]
            assert len(rows)==1 and rows[0]['vendor']==vendor
            assert rows[0]['input_sha256']==choice['sha256']
            for key,value in ev.items():
                if key!='bundle':assert rows[0][key]==value,(ev['id'],key)
assert len(ids)==7 and not data['all_selected_targets_met'] and not registry['all_targets_met']
assert all(data['targets'][v]['operator']=='gte' for v in ['GPTZero','QuillBot'])
assert data['targets']['ZeroGPT']['operator']=='lte'
assert registry['production_version']=='1.5.1'
print('PASS: 7 continuation E/F observations; native metrics, dates, hashes, quota and checkpoint links agree.')
