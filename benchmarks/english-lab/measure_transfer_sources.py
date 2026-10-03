from pathlib import Path
import hashlib, json, subprocess, sys
root = Path(__file__).resolve().parent
registry = json.loads((root/'transfer/registry.json').read_text('utf-8'))
for case in registry['cases']:
    source = root/'transfer'/case['source_file']
    if hashlib.sha256(source.read_bytes()).hexdigest() != case['source_sha256']:
        raise RuntimeError('Frozen source changed')
    out = root/'transfer-scores'/case['id']/'source'
    if out.exists():
        raise RuntimeError('Never overwrite a measurement')
    result = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(root/'skill/scripts/local_feedback.py'), str(source), '--language', 'en', '--out-dir', str(out)], capture_output=True, text=True, encoding='utf-8')
    print(json.dumps({'case':case['id'],'returncode':result.returncode,'stdout':result.stdout[-1500:],'stderr':result.stderr[-1500:]},ensure_ascii=False), flush=True)
    if result.returncode:
        raise RuntimeError('Measurement failed; inspect before any retry')
