from pathlib import Path
import hashlib, json, sys
r = Path(__file__).resolve().parent
sys.path.insert(0,str(r/'skill/scripts'))
import feedback_cycle
read = lambda p: json.loads(p.read_text('utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
ref = lambda p: {'path':p.relative_to(r).as_posix(),'sha256':sha(p)}
for cid in ('T01','T02'):
    session = read(r/f'{cid}-prototype-initial-session.json')
    prior = session['rounds'][-1]
    review = read(r/'continuation-feedback'/cid/'validated-full.json')
    entries = review['findings']
    item = dict(prior,id='draft-2',candidate=ref(r/'prototype-output'/cid/'draft-2.txt'),
       native=ref(r/'continuation-scores'/cid/'model-result.json'),
       feedback=ref(r/'continuation-scores'/cid/'feedback.json'),
       review=ref(r/'continuation-feedback'/cid/'validated-full.json'),
       triage=[{'finding_id':f['id'],'decision':f['triage']['action'],'reason':f['triage']['reason']} for f in entries],
       improvement=False,
       improvement_reason='Explicitly requested source-grounded alternate reader route. Independent review found it valid but no decisive reader advantage. Numeric movement remains separate from editorial quality.',
       fidelity={'eligible':True,'source_sha256':session['source']['sha256'],'reason':'Parent pre-score and separate full independent source/constraint reviews agree that every fact, qualification, agency and speech act is retained.'},
       reader={'eligible':True,'reason':'Independent full paragraph review found a coherent legitimate route and no required repair.'},followup=[])
    session['rounds'].append(item)
    session['stop']={'reason':'complete','detail':'The completed optional comparison received exact native output and whole-document feedback. No actionable finding remains; the best eligible earlier text is retained when the new route scores lower. This continuation is post-feedback development, not untouched transfer, and does not enlarge the revision budget.'}
    p = r/f'{cid}-prototype-final-session.json'
    assert not p.exists()
    p.write_text(json.dumps(session,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    state = feedback_cycle.validate(p)
    out = r/'cycle-status'/f'{cid}-prototype-final.json'
    assert not out.exists()
    out.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'case':cid,'status':state['status'],'revisions_used':state['revisions_used'],'selected':state['selected_candidate']['id'],'human':state['selected_candidate']['human_percent']}))
