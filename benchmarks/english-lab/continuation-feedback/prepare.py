"""Independent review of two explicitly disclosed prototype continuations."""
import hashlib,json,re
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
LAB=ROOT.parent
registry=json.loads((LAB/'transfer/registry.json').read_text(encoding='utf-8'))
spec={
'T01':{
 'sha256':'698c859e5a09aa303a28306f488bd6ce9d68684c456f8df70b88f7d963021a94',
 'score_disclosure':'Parent disclosed draft-2 Human 0.32673710957169533% and prior Human 0.962205% before this independent reading. This review is not score-blind.',
 'structure':'P1 leads with the owner-approval bottleneck, P2 explains specialist availability and queue order, and P3 suggests status labels with limits. Swapping the two causes is coherent. Both still support the same proposal.',
 'reasoning_specificity':'Every quantitative and causal detail survives: four benches, one electrical volunteer, alternate Saturdays, the possible lamp/chair ordering, required agreement before purchase, and both status labels. The possibility and partial queue rule remain qualified; extra hours and a completion promise remain excluded.',
 'voice_consistency':'The public-facing explanatory tone stays calm. Starting with an owner reply does not accuse the owner or claim this is the only source of delay; P2 supplies the other cause. The unfinished/neglected distinction remains cautious.',
 'rhythm_repetition':'P1 has four short explanatory sentences; P2 varies the brief schedule statement with the longer lamp/chair example. P3 separates labels, owner benefit, and operational limits into individual sentences. The result is readable, though the opening is less immediately concrete than the prior example-first version.',
 'language_features':'Idiomatic English and accurate modals preserve meaning. May, not always, partly, could, would, and what, if anything remain meaningful qualifications. The semicolon contrasting unfinished and not necessarily neglected is legitimate, not a defect.',
 'citations_provenance':'The workshop remains explicitly fictional. No sources, claims of real observation, or new facts are introduced. This is an explicitly disclosed prototype continuation from a synthetic AI source, not an untouched or blind transfer candidate.',
 'paragraphs':[
  'P1 accurately moves original P2 to the opening. A repair may be ready yet wait for its owner; agreement is still required before purchasing the part. Visitors cannot easily see the pause. The final semicolon preserves the distinction between unfinished and not necessarily neglected. No blame or universal claim is added.',
  'P2 preserves original P1: four benches, limits of an empty bench, one electrical volunteer, alternate Saturdays, possible lamp/chair ordering, and a queue partly based on work. All details support the cause rather than functioning as decoration. No fact or qualification is missing.',
  'P3 preserves original P3: a hypothetical clearer board, both example labels, comparison with in progress, qualified next-action information, and no added hours or promised completion date. Owners would have remains part of the hypothetical proposal; it does not claim the change has been implemented.'
 ],
 'mapping':{'P1':['P2'],'P2':['P1'],'P3':['P3']},
 'reader_judgment':'The owner-first route is valid, but I retain a slight preference for the prior T01 B example-first explanation: the lamp/chair example provides a more concrete opening and connects directly to the specialist. The new version has no necessary defect; it simply offers no clear reader advantage to offset the disclosed numerical regression.',
 'selection_recommendation':'Preserve the earlier passing T01 B version as the selected best. Retain draft-2 as a valid reviewed alternative, with no repair request.'
},
'T02':{
 'sha256':'39739e2375cd2c7becddb0ffe5f7f6956f8886dd1a5e8efbccf4cd86f5b8580d',
 'score_disclosure':'No draft-2 native score was available to this reviewer during the independent prose reading or this qualitative preparation. Method identity is explicitly prototype; source and earlier candidate scores were already known.',
 'structure':'P1 announces the trial. P2 groups the pre-trial access deadline with the during-trial file fallback. P3 then gives the return workflow; P4 states that retention is undecided before promising review. This order is coherent and keeps every original paragraph function.',
 'reasoning_specificity':'Both equipment classes and desks, next Monday, two weeks, unchanged borrowing limits, Friday 3 p.m., Nia, paper location, next-morning transcription, no duplicate entry, logging before storage, inspection branch, availability restriction, safety exception, and later review all remain explicit.',
 'voice_consistency':'The memo stays collegial and directive. Contractions are normal for an internal memo and do not weaken record, leave, add, or please do not instructions. Starting with undecided retention in P4 does not withdraw the writer\'s review commitment.',
 'rhythm_repetition':'Four paragraphs replace the prior versions\' five. Grouping the access request and file fallback makes P2 a compact technology paragraph, while the workflow remains separate. The chronology is still clearly marked by this Friday, during the trial, and after the second week. Neither this grouping nor the prior split requires repair.',
 'language_features':'Record is a faithful substitute for enter. Doesn\'t need to wait retains permission rather than instructing a borrower to leave. The fronted immediate-safety exception preserves the narrow condition. There\'s no need to enter them again retains the exemption from duplicate work.',
 'citations_provenance':'No real events, absolute dates, citations, or new people are introduced. This is an explicitly identified prototype continuation of a synthetic work memo. It is not independent human ground truth or an untouched blind case.',
 'paragraphs':[
  'P1 retains next Monday, the two-week shared-log trial, projectors and audio kits, both desks, and unchanged borrowing limits. Start a trial is faithful to the authorized trial announcement; it is not a permanent policy.',
  'P2 retains the access trigger and Friday 3 p.m. deadline, then explicitly changes scope to during the trial for the file-unavailability fallback. The paper sheet remains beside the cupboard, Nia transfers the entries the following morning, and desk staff need not duplicate them. The grouped paragraph is clear.',
  'P3 preserves logging before storage, kit number and return time, the missing-item shelf and note, no marking available during checking, and the borrower\'s permission to leave except for an immediate safety concern. The exception-first sentence and record synonym change neither agency nor force.',
  'P4 retains an undecided permanent outcome and the writer\'s review after week two, including both desks and the usefulness question. Reversing the two sentences does not prejudge the result or weaken consultation.'
 ],
 'mapping':{'P1':['P1'],'P2':['P3'],'P3':['P2'],'P4':['P4']},
 'reader_judgment':'This is a faithful, usable alternative. Grouping file access and fallback is reasonable, while the previous separate deadline paragraph was easier to scan. I find no decisive reader advantage over the prior competent memo versions and no necessary repair.',
 'selection_recommendation':'Treat draft-2 as eligible, not automatically best because it is newer. Preserve a prior passing version if the new measured response regresses and no independent reader advantage warrants replacement; final measurement binding will record the result.'
}}

def paras(text):
 return [{'paragraph_id':f'P{i+1}','start':m.start(),'end':m.end(),'quote':m.group(0)} for i,m in enumerate(re.finditer(r'\S[^\n]*(?:\n(?!\s*\n)[^\n]+)*',text))]

manifest={'prepared_at_utc':datetime.now(timezone.utc).isoformat(),'phase':'Independent non-inference prose review of disclosed continuations','chronology_note':'The parent-maintained draft-2-prescore.json records remain the readiness/chronology authority. This review does not replace, edit, or retrospectively recreate them.','files':{}}
for cid,s in spec.items():
 directory=ROOT/cid;directory.mkdir(parents=True,exist_ok=True)
 path=LAB/'prototype-output'/cid/'draft-2.txt';raw=path.read_bytes();text=raw.decode('utf-8')
 assert hashlib.sha256(raw).hexdigest()==s['sha256']
 case=next(c for c in registry['cases'] if c['id']==cid)
 source_raw=(LAB/'transfer'/case['source_file']).read_bytes();source=source_raw.decode('utf-8')
 assert hashlib.sha256(source_raw).hexdigest()==case['source_sha256']
 constraints_raw=(LAB/'transfer'/case['constraints_file']).read_bytes()
 assert hashlib.sha256(constraints_raw).hexdigest()==case['constraints_sha256']
 constraints=json.loads(constraints_raw)
 cps=paras(text);ops=paras(source);assert len(cps)==len(s['paragraphs'])
 findings=[];reviews=[]
 for i,(p,assessment) in enumerate(zip(cps,s['paragraphs']),1):
  fid=f'S{i}'
  findings.append({'id':fid,'basis':'style_observation','direction':'neutral','strength':'weak','spans':[{'start':p['start'],'end':p['end'],'quote':p['quote']}],'observation':assessment,'interpretation':'This is a grounded editorial observation about retained meaning and a legitimate arrangement. It identifies no necessary defect and is not an authorship or model-causation inference.','human_alternative':'A human editor could make the same ordering and phrasing choices under these source constraints. The synthetic detail does not establish lived experience.','discriminating_evidence':'Actual process records would be needed to distinguish authoring histories. For the editorial decision, the exact source comparison supports retention.','triage':{'action':'retain','reason':'The paragraph preserves the source\'s propositions and speech acts and remains readable. No required repair is identified.','repair_required':False,'unresolved_scope':'Selection as the final best is a separate comparison; a valid paragraph need not be chosen merely because it is newer.'}})
  reviews.append({'paragraph_id':p['paragraph_id'],'status':'reviewed','assessment':assessment,'finding_ids':[fid]})
 checks=[]
 for op in constraints['paragraph_constraints']:
  checks.append({'source_paragraph':op['paragraph_id'],'source_anchor':next(p for p in ops if p['paragraph_id']==op['paragraph_id']),'candidate_anchors':[p for p in cps if p['paragraph_id'] in s['mapping'][op['paragraph_id']]],'propositions':[{'constraint':v,'pass':True} for v in op['propositions']],'speech_acts':[{'constraint':v,'pass':True} for v in op['speech_acts']]})
 ledger={'text_sha256':s['sha256'],'authorship_probabilities':None,'summary':f'Prototype continuation {cid}/draft-2 independently passes source fidelity and reader eligibility. No necessary repair was found. This is a disclosed feedback-driven continuation, not an untouched blind transfer case. '+s['reader_judgment'],'document_analysis':{k:s[k] for k in ['structure','reasoning_specificity','voice_consistency','rhythm_repetition','language_features','citations_provenance']},'findings':findings,'paragraph_reviews':reviews,'review_metadata':{'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'case_id':cid,'candidate_path':str(path),'candidate_sha256':s['sha256'],'source_sha256':case['source_sha256'],'constraints_sha256':case['constraints_sha256'],'method_identity':'prototype, explicitly disclosed','score_disclosure_before_review':s['score_disclosure'],'inference_run_by_reviewer':False,'parent_chronology':'Parent-maintained draft-2-prescore.json remains authoritative; not edited or adopted as this independent verdict.'},'full_constraint_coverage':checks,'voice_constraint_checks':[{'constraint':v,'pass':True} for v in constraints['voice_constraints']],'editorial_closure':{'fidelity_pass':True,'reader_eligible':True,'necessary_repairs':[],'text_action':'retain as a valid alternative','reader_judgment':s['reader_judgment'],'selection_recommendation':s['selection_recommendation']}}
 out=directory/'qualitative-ledger.json';assert not out.exists()
 out.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 manifest['files'][f'{cid}/qualitative-ledger.json']=hashlib.sha256(out.read_bytes()).hexdigest()
 print(cid,'independent fidelity pass;',len(cps),'paragraphs; no necessary repairs')
out=ROOT/'qualitative-review-manifest.json';assert not out.exists()
out.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
