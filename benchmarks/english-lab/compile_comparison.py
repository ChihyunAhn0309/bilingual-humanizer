from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
r = Path(__file__).resolve().parent
read = lambda p: json.loads(p.read_text('utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
ref = lambda p: {'path':p.relative_to(r).as_posix(),'sha256':sha(p)}
mapping = read(r/'pair-identities.json')['items']
registry = read(r/'transfer/registry.json')
blind = read(r/'blind-review/round-1.json')
def score(directory, candidate):
    native = read(directory/'model-result.json')
    feedback = read(directory/'feedback.json')
    assert native['text_sha256'] == sha(candidate) == feedback['input_sha256']
    assert (directory/'input.txt').read_bytes() == candidate.read_bytes()
    assert native['weight_sha256'] == '4a1561fadf44ec72934edd6158ff8c76e9388ade1384dbeeea6eb15f93251087'
    assert native['revision'] == 'f1795c86806e6838d4afa33d0b1427f8430c9615'
    assert feedback['status'] == 'completed' and feedback['scope'] == 'whole_document'
    assert native['authorship_verified'] is False
    assert feedback['human_percent'] == 100*native['document_class_probabilities']['human']
    return {'candidate':ref(candidate),'native':ref(directory/'model-result.json'),
      'feedback':ref(directory/'feedback.json'),'execution':ref(directory/'execution.json'),
      'human_percent':feedback['human_percent'],
      'classes':native['document_class_probabilities'],'measured_at_utc':native['measured_at_utc']}
cases = []
for case, review in zip(registry['cases'], blind['cases']):
    assert case['id'] == review['case_id']
    cid = case['id']
    item = {'case':cid,'genre':case['genre'],'source':score(r/'transfer-scores'/cid/'source',r/'transfer'/case['source_file'])}
    identities = {x['alias']:x for x in mapping if x['case']==cid}
    for alias, identity in identities.items():
        verdict = review['candidates'][alias]
        assert verdict['fidelity_pass'] and verdict['reader_eligible'] and not verdict['necessary_repairs']
        candidate = r/identity['candidate']
        assert sha(candidate) == identity['sha256'] == verdict['sha256']
        s = score(r/'transfer-scores'/cid/alias,candidate)
        assert datetime.fromisoformat(blind['reviewed_at_utc']) < datetime.fromisoformat(s['measured_at_utc'])
        s['alias'] = alias
        item[identity['method']] = s
    pref = review['pairwise_reader_preference']['choice']
    item['reader_preference'] = 'tie' if pref=='tie' else identities[pref]['method']
    item['reader_preference_strength'] = review['pairwise_reader_preference']['strength']
    item['prototype_minus_baseline_pp'] = item['prototype']['human_percent']-item['baseline']['human_percent']
    item['prototype_minus_source_pp'] = item['prototype']['human_percent']-item['source']['human_percent']
    cases.append(item)
data = {'schema_version':1,'created_at_utc':datetime.now(timezone.utc).isoformat(),
 'comparison':'First eligible drafts under a method frozen before source release. Synthetic fresh transfer probe; not representative or a formal statistical holdout.',
 'method_freeze':ref(r/'METHOD-FREEZE.json'),'source_registry':ref(r/'transfer/registry.json'),
 'blind_review':ref(r/'blind-review/round-1.json'),'identity_mapping':ref(r/'pair-identities.json'),
 'cases':cases,'local_measurements':9,'paid_actions':0,'commercial_calls':0,
 'prototype_human_wins':sum(x['prototype_minus_baseline_pp']>0 for x in cases),
 'prototype_reader_preferences':sum(x['reader_preference']=='prototype' for x in cases),
 'reader_ties':sum(x['reader_preference']=='tie' for x in cases),
 'prototype_human_ge_50':sum(x['prototype']['human_percent']>=50 for x in cases),
 'semantics':'Native uncalibrated Human class percentage; not 100 minus AI, word share or verified human authorship.',
 'limitations':['Three AI-generated fixtures and one draft per arm; no repeated draws or population inference.',
 'Same-model separate contexts. Baseline writer had fresh context; prototype writer also developed the method.',
 'Blind evaluator authored the original sources and knew their constraints; candidate identity and scores were hidden for the initial review.',
 'Development and transfer both happen to include repair-workshop topics; not a fully out-of-domain evaluation.',
 'No commercial detector transfer or human reader ratings measured.']}
out = r/'transfer-comparison.json'
assert not out.exists()
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':[{'case':x['case'],'source':x['source']['human_percent'],'baseline':x['baseline']['human_percent'],'prototype':x['prototype']['human_percent'],'reader':x['reader_preference']} for x in cases], 'prototype_human_wins':data['prototype_human_wins']}))
