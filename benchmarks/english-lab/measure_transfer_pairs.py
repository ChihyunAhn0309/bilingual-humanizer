from pathlib import Path
import hashlib, json, subprocess, sys
root = Path(__file__).resolve().parent
plan = json.loads((root/'scoring-plan.json').read_text('utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
review = root/plan['blind_review']['path']
if sha(review) != plan['blind_review']['sha256']:
    raise RuntimeError('Pre-score blind review changed')
for item in plan['items']:
    source = root/item['input']
    if not item['eligible'] or sha(source) != item['sha256']:
        raise RuntimeError('Candidate lacks exact eligible pre-score review')
    out = root/item['output']
    if out.exists():
        raise RuntimeError('Never overwrite a measurement')
    result = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(root/'skill/scripts/local_feedback.py'), str(source), '--language', 'en', '--out-dir', str(out)], capture_output=True, text=True, encoding='utf-8')
    print(json.dumps({'case':item['case'],'alias':item['alias'],'returncode':result.returncode,'stdout':result.stdout[-1500:],'stderr':result.stderr[-1500:]},ensure_ascii=False), flush=True)
    if result.returncode:
        raise RuntimeError('Measurement failed; inspect before any retry')
