"""Verify archived inputs, receipts and retained production files, not authorship."""
from pathlib import Path
import json, hashlib, re
from datetime import datetime

base=Path(__file__).resolve().parent/'additional-trial'
data=json.loads((base/'results.json').read_text('utf-8'))
seen=set()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
norm=lambda text:re.sub(r'\s+',' ',text).strip()
for rec in data['records']:
    assert rec['id'] not in seen
    seen.add(rec['id'])
    assert rec['status']=='completed' and rec['input_verified'] is True
    assert 0<=rec['score']<=100 and rec.get('truncated') is not True
    datetime.fromisoformat(rec['capture_time_utc'].replace('Z','+00:00'))
    for field,hashfield in [('input_file','input_sha256'),('receipt','receipt_sha256')]:
        p=(base/rec[field]).resolve()
        assert p.is_relative_to(base.resolve())
        assert sha(p)==rec[hashfield],rec['id']
    receipt=json.loads((base/rec['receipt']).read_text('utf-8'))
    for key,value in rec.items():
        if key not in ['receipt','receipt_sha256']:assert receipt[key]==value,(rec['id'],key)
    submitted=(base/rec['input_file']).read_bytes().decode('utf-8').strip()
    assert hashlib.sha256(submitted.encode()).hexdigest()==rec['submission_sha256']
    raw=receipt['raw_receipt']
    if rec['vendor']=='GPTZero':
        assert 'heading Basic Scan' in raw and 'Text up-to-date' in raw
        for field,label in [('score','AI'),('human_percent','Human'),('mixed_percent','Mixed')]:
            assert int(re.search(r'button '+label+r' (\d+)%',raw)[1])==rec[field]
        assert sum(rec[k] for k in ['score','human_percent','mixed_percent'])==100
        assert re.search(r'Detection Model\s+([^ ]+)',raw)[1]==rec['model']
    elif rec['vendor']=='QuillBot':
        assert 'Outdated score' not in raw
        for field,label in [('score','AI-generated'),('human_percent','Human-written'),('ai_refined_percent','Human-written & AI-refined')]:
            pattern=r'text '+re.escape(label)+r'\r?\n[\s\S]*?text (\d+) %'
            assert int(re.search(pattern,raw)[1])==rec[field]
        assert sum(rec[k] for k in ['score','human_percent','ai_refined_percent'])==100
        assert re.search(r'Model v([\d.]+)',raw)[1]==rec['model']
    elif rec['vendor']=='Sapling':
        while isinstance(raw,str):raw=json.loads(raw)
        assert raw['ai_probability_percent']==rec['score'] and raw['truncated'] is False
        assert norm(' '.join(s['sentence'] for s in raw['sentence_scores']))==norm(submitted)
    elif rec['vendor']=='ZeroGPT':
        assert float(re.search(r'(\d+(?:\.\d+)?)%\s*AI GPT',raw)[1])==rec['score']
        assert norm(submitted) in norm(raw)
    else:raise AssertionError(rec['vendor'])
for rel,expected in json.loads((base/'frozen-inputs.json').read_text('utf-8')).items():
    assert sha(base/rel)==expected,rel
for filename,review,source in [('blind-mapping.json','review','sources'),('holdout-mapping.json','holdout-review','holdout')]:
    for case,entries in json.loads((base/filename).read_text('utf-8')).items():
        assert sha(base/review/case/'source.txt')==sha(base/source/f'{case}-source.txt')
        for label,entry in entries.items():
            assert sha(base/entry['path'])==entry['sha256']
            assert sha(base/review/case/f'{label}.txt')==entry['sha256']
for repair in json.loads((base/'repair-log.json').read_text('utf-8'))['records']:
    initial=base/'candidates'/f'{repair["case"]}-trial.txt'
    final=base/'candidates'/f'{repair["case"]}-trial-reviewed.txt'
    assert sha(initial)==repair['initial_sha256'] and sha(final)==repair['reviewed_sha256']
    text=initial.read_text('utf-8')
    for old,new in repair['changes']:
        assert text.count(old)==1
        text=text.replace(old,new)
    assert text==final.read_text('utf-8')
production=base.parents[1]/'skills/bilingual-humanizer'
retained=json.loads((base/'retained-production-files.json').read_text('utf-8'))
prior=json.loads((base.parent/'2026-10-02-v15/frozen-skill-hashes.json').read_text('utf-8'))
assert retained=={k.replace('\\','/'):v for k,v in prior.items()}
for rel,expected in retained.items():assert sha(production/rel)==expected,rel
assert len(seen)==17
print(f'PASS: {len(seen)} additional observations, frozen inputs and {len(retained)} unchanged production files.')
