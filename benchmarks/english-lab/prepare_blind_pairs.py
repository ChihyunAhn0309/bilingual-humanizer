from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
root = Path(__file__).resolve().parent
# Fixed before any transfer candidate was available to the coordinator.
assignment = {'T01': {'A':'baseline','B':'prototype'},
              'T02': {'A':'prototype','B':'baseline'},
              'T03': {'A':'baseline','B':'prototype'}}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
items = []
for case, pair in assignment.items():
    for alias, method in pair.items():
        src = root/f'{method}-output'/case/'draft-1.txt'
        dst = root/'blind-pairs'/case/f'{alias}.txt'
        if dst.exists():
            raise RuntimeError('Do not overwrite a blind candidate')
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
        items.append({'case':case,'alias':alias,'method':method,
                      'candidate':src.relative_to(root).as_posix(),
                      'blind_candidate':dst.relative_to(root).as_posix(),
                      'sha256':sha(src)})
manifest = root/'pair-identities.json'
if manifest.exists():
    raise RuntimeError('Do not overwrite mapping')
manifest.write_text(json.dumps({'created_at_utc':datetime.now(timezone.utc).isoformat(),
 'assignment_rule':'Predetermined A/B assignment before coordinator saw any candidate; no model scores used.',
 'items':items},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pairs_prepared':3,'mapping_sha256':sha(manifest)}))
