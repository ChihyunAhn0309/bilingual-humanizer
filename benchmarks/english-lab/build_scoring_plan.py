from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
r = Path(__file__).resolve().parent
review_path = r/'blind-review/round-1.json'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
if sha(review_path) != 'dc87c8a1a42ccfd5575e6ae093e38f01a55fe2c584aa813a32686edd14e6494d':
    raise RuntimeError('Review changed after independent freeze')
review = json.loads(review_path.read_text('utf-8'))
items = []
for case in review['cases']:
    for alias, verdict in case['candidates'].items():
        path = r/'blind-pairs'/case['case_id']/f'{alias}.txt'
        if not (verdict['fidelity_pass'] and verdict['reader_eligible'] and not verdict['necessary_repairs'] and sha(path) == verdict['sha256']):
            raise RuntimeError('Blind review failed a candidate')
        items.append({'case':case['case_id'],'alias':alias,'input':path.relative_to(r).as_posix(),
           'sha256':sha(path),'eligible':True,'output':f"transfer-scores/{case['case_id']}/{alias}"})
plan = r/'scoring-plan.json'
if plan.exists():
    raise RuntimeError('Do not overwrite')
plan.write_text(json.dumps({'created_at_utc':datetime.now(timezone.utc).isoformat(),
 'blind_review':{'path':review_path.relative_to(r).as_posix(),'sha256':sha(review_path)},'items':items},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'eligible_candidates':len(items),'plan_sha256':sha(plan)}))
