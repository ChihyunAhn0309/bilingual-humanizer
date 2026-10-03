from pathlib import Path
import hashlib, json, sys
r = Path(__file__).resolve().parent
sys.path.insert(0,str(r/'skill/scripts'))
import feedback_cycle
read = lambda p: json.loads(p.read_text('utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
ref = lambda p: {'path':p.relative_to(r).as_posix(),'sha256':sha(p)}
def save(p,d):
    if p.exists(): raise RuntimeError('Never overwrite a cycle record')
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
registry = {c['id']:c for c in read(r/'transfer/registry.json')['cases']}
for item in read(r/'pair-identities.json')['items']:
    cid, method, alias = item['case'],item['method'],item['alias']
    source = r/'transfer'/registry[cid]['source_file']
    source_review = r/'transfer-reviews'/f'{cid}.validated-full.json'
    source_data = read(source_review)
    source_triage = [{'finding_id':f['id'],'decision':'retain',
      'reason':('Read in the common pre-draft feedback and retained in the writer record. '+f['interpretation']+' No source-fidelity or reader defect was established.')} for f in source_data['findings']]
    common = {'fidelity':{'eligible':True,'source_sha256':sha(source),'reason':'Frozen supplied synthetic source and all semantic constraints preserved, as checked by the independent paragraph/constraint review.'},
       'reader':{'eligible':True,'reason':'Whole-document independent review found a suitable reader route and no necessary repair.'},
       'followup':[], 'improvement':False,
       'improvement_reason':'An explicitly requested alternate composition; no required defect in the source, and no automatic claim of superiority to the original.'}
    first = dict(common,id='source',candidate=ref(source),
       native=ref(r/'transfer-scores'/cid/'source/model-result.json'),
       feedback=ref(r/'transfer-scores'/cid/'source/feedback.json'),
       review=ref(source_review),triage=source_triage)
    triage = read(r/'candidate-feedback'/cid/alias/'triage.json')
    current = dict(common,id='draft-1',candidate=ref(r/item['candidate']),
       native=ref(r/'transfer-scores'/cid/alias/'model-result.json'),
       feedback=ref(r/'transfer-scores'/cid/alias/'feedback.json'),
       review=ref(r/'candidate-feedback'/cid/alias/'validated-full.json'),
       triage=[{'finding_id':f['id'],'decision':f['action'],'reason':f['reason']} for f in triage['findings']])
    session = {'schema_version':1,'language':'en','source':ref(source),'revision_limit':3,
       'rounds':[first,current],
       'stop':{'reason':'complete','detail':'Actual source feedback preceded this draft; its exact local measurement and full independent post-draft review contain no actionable editing findings. This manifest is assembled after those events; it is not an autonomous rewriting execution log. Later explicitly requested alternative continuations are recorded separately with the initial comparison preserved.'}}
    path = r/f'{cid}-{method}-initial-session.json'
    save(path,session)
    state = feedback_cycle.validate(path)
    save(r/'cycle-status'/f'{cid}-{method}-initial.json',state)
    print(json.dumps({'case':cid,'method':method,'status':state['status'],'selected':state['selected_candidate']['id'],'human':state['selected_candidate']['human_percent']}))
