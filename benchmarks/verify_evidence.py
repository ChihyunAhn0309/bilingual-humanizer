"""Check local evidence integrity, not vendor authenticity or authorship."""
from pathlib import Path
import json, hashlib

BASE=Path(__file__).resolve().parent/'2026-10-02'
data=json.loads((BASE/'results.json').read_text(encoding='utf-8'))
seen=set()
for record in data['records']:
    key=(record['service'],record['case'],record['variant'])
    assert key not in seen, f'Duplicate observation: {key}'
    seen.add(key)
    assert record['status']=='completed'
    assert 0 <= record['displayed_ai_percent'] <= 100
    assert record.get('truncated') is not True
    for field, hashfield in [('input_file','input_sha256'),('receipt','receipt_sha256')]:
        path=(BASE/record[field]).resolve()
        assert path.is_relative_to(BASE.resolve())
        assert hashlib.sha256(path.read_bytes()).hexdigest()==record[hashfield], str(path)
    if record['service']=='GPTZero' and record.get('transport')=='authenticated Basic Scan UI':
        receipt=(BASE/record['receipt']).read_text(encoding='utf-8')
        assert 'Text up-to-date' in receipt
        assert f'AI {record["displayed_ai_percent"]}%' in receipt
print(f'PASS: {len(seen)} unique observations; input and receipt hashes match.')

# Version comparisons retain complete per-request receipts. These checks establish
# local consistency only; the records are agent observations, not signed reports.
import re
V15=BASE.parent/'2026-10-02-v15'
if (V15/'results.json').exists():
    new=json.loads((V15/'results.json').read_text(encoding='utf-8'))
    ids=set()
    for rec in new['records']:
        assert rec['id'] not in ids,rec['id']
        ids.add(rec['id'])
        assert rec['status']=='completed' and 0<=rec['score']<=100
        assert rec.get('truncated') is not True
        assert rec['input_verified'] is True
        for field,hashfield in [('input_file','input_sha256'),('receipt','receipt_sha256')]:
            path=(V15/rec[field]).resolve()
            assert path.is_relative_to(V15.resolve())
            assert hashlib.sha256(path.read_bytes()).hexdigest()==rec[hashfield],str(path)
        receipt=json.loads((V15/rec['receipt']).read_text(encoding='utf-8'))
        for key in ['id','vendor','input_file','input_sha256','submission_sha256','score','metric','model','status']:
            assert rec[key]==receipt[key],(rec['id'],key)
        submitted=(V15/rec['input_file']).read_bytes().decode('utf-8').strip()
        assert hashlib.sha256(submitted.encode('utf-8')).hexdigest()==rec['submission_sha256']
        raw=receipt['raw_receipt']
        if rec['vendor']=='Sapling':
            while isinstance(raw,str):raw=json.loads(raw)
            assert raw['ai_probability_percent']==rec['score']
            assert raw['truncated'] is False
        elif rec['vendor'].startswith('GPTZero'):
            assert 'Text up-to-date' in raw and f'AI {rec["score"]}%' in raw
        elif rec['vendor']=='QuillBot':
            assert int(re.search(r'AI-generated\s+(\d+)%',raw)[1])==rec['score']
        elif rec['vendor']=='ZeroGPT':
            assert float(re.search(r'(\d+(?:\.\d+)?)%\s*AI GPT',raw)[1])==rec['score']
            norm=lambda s:re.sub(r'\s+',' ',s).strip()
            assert norm(submitted) in norm(raw)
    print(f'PASS: {len(ids)} v1.5/development observations; hashes and recorded scores agree.')

if (BASE.parent/'additional-trial/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_additional_trial.py'),run_name='__main__')

if (BASE.parent/'deeper-trial/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_deeper_trial.py'),run_name='__main__')


if (BASE.parent/'renewal-trial/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_renewal_trial.py'),run_name='__main__')

if (BASE.parent/'continuation-e/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_continuation_e.py'),run_name='__main__')

if (BASE.parent/'continuation-g/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_continuation_g.py'),run_name='__main__')
    runpy.run_path(str(BASE.parent/'verify_current_observations.py'),run_name='__main__')

if (BASE.parent/'quill-renewal/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_quill_renewal.py'),run_name='__main__')

if (BASE.parent/'local-feedback/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_local_feedback.py'), run_name='__main__')

if (BASE.parent/'local-runtime-followup/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_local_runtime_followup.py'), run_name='__main__')

if (BASE.parent/'composition-feedback/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_composition_feedback.py'), run_name='__main__')

if (BASE.parent/'english-focus/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_english_focus.py'), run_name='__main__')

if (BASE.parent/'feedback-cycle/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_feedback_cycle.py'), run_name='__main__')

if (BASE.parent/'english-lab/results.json').exists():
    import runpy
    runpy.run_path(str(BASE.parent/'verify_english_lab.py'), run_name='__main__')
