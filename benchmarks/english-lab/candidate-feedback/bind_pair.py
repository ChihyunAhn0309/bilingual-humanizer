"""Bind an authorized pair of supplied native results; never run inference."""
import hashlib
import json
import math
import subprocess
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
LAB=ROOT.parent
CID=sys.argv[1]
assert CID in {'T01','T02','T03'}
EVIDENCE=Path('C:/Users/ach18/.codex/skills/bilingual-ai-detector/scripts/evidence.py')
review_raw=(LAB/'blind-review/round-1.json').read_bytes()
freeze=json.loads((LAB/'blind-review/round-1.freeze.json').read_text(encoding='utf-8'))
assert hashlib.sha256(review_raw).hexdigest()==freeze['review_sha256']
review=json.loads(review_raw)
case=next(c for c in review['cases'] if c['case_id']==CID)
preparation=json.loads((ROOT/'qualitative-preparation.json').read_text(encoding='utf-8'))
pair={
 'schema_version':1,'case_id':CID,'completed_at_utc':datetime.now(timezone.utc).isoformat(),
 'method_identities_read':False,'inference_run_by_reviewer':False,
 'frozen_blind_review_sha256':freeze['review_sha256'],
 'pairwise_reader_preference_unchanged':case['pairwise_reader_preference'],
 'scope':'Final exact-candidate detector-skill feedback for the anonymous pair. Measurements are bound to frozen candidates; the pre-score fidelity and reader judgments remain unchanged.',
 'model_limit':'The local four-class scorer is experimental and independently uncalibrated; the installed skill reports high-confidence false positives on human writing. Outputs are neither quality scores nor verified authorship probabilities.',
 'candidates':{}
}

for label in ['A','B']:
 directory=ROOT/CID/label
 candidate=case['candidates'][label]
 path=Path(candidate['file']);raw=path.read_bytes();text=raw.decode('utf-8')
 assert hashlib.sha256(raw).hexdigest()==candidate['sha256']
 qpath=directory/'qualitative-ledger.json';qraw=qpath.read_bytes()
 assert hashlib.sha256(qraw).hexdigest()==preparation['files'][f'{CID}/{label}/qualitative-ledger.json']
 full=deepcopy(json.loads(qraw))
 mpath=LAB/'transfer-scores'/CID/label/'model-result.json'
 mraw=mpath.read_bytes();native=json.loads(mraw)
 assert native['mode']=='offline_local_model' and native['schema_version']==2
 assert native['text_sha256']==candidate['sha256']
 assert native['model']=='wasitaigeneratedcom/ai-text-detector-small'
 assert native['revision']=='f1795c86806e6838d4afa33d0b1427f8430c9615'
 assert native['weight_sha256']=='4a1561fadf44ec72934edd6158ff8c76e9388ade1384dbeeea6eb15f93251087'
 assert native['execution_guard']['worker_exit_code']==0 and native['execution_guard']['serialized_cli'] is True
 assert native['external_detector_calls']==0 and native['all_input_tokens_scored'] is True
 assert len(native['windows'])==1
 window=native['windows'][0]
 assert window['token_start']==0 and window['token_end']==native['token_count']
 assert text[window['start']:window['end']]==window['quote']
 assert not text[:window['start']].strip() and not text[window['end']:].strip()
 probs=native['document_class_probabilities']
 assert set(probs)=={'human','ai','ai_edited','humanized'} and probs==window['class_probabilities']
 assert all(math.isfinite(v) and 0<=v<=1 for v in probs.values()) and abs(sum(probs.values())-1)<1e-5
 involvement=window['ai_involvement_class_score']
 assert abs(involvement-(1-probs['human']))<1e-7
 assert abs(involvement-sum(probs[k] for k in ['ai','ai_edited','humanized']))<1e-5
 source_path=LAB/'transfer-scores'/CID/'source/model-result.json'
 source_raw=source_path.read_bytes();source_native=json.loads(source_raw)
 assert source_native['text_sha256']==case['original_sha256']
 assert source_native['model']==native['model'] and source_native['revision']==native['revision'] and source_native['weight_sha256']==native['weight_sha256']
 source_probs=source_native['document_class_probabilities']
 deltas={k:(probs[k]-source_probs[k])*100 for k in probs}
 highest=max(probs,key=probs.get)
 full['summary']=(f"Anonymous candidate {CID}/{label} remains faithful and reader-eligible after all {candidate['coverage']['reviewed']} paragraphs were reviewed. No necessary repair was identified. Supplied unvalidated model outputs: Human {probs['human']*100:.8f}%, AI {probs['ai']*100:.8f}%, AI-edited {probs['ai_edited']*100:.8f}%, Humanized {probs['humanized']*100:.8f}%. The recorded AI-involvement class score is {involvement*100:.8f}%. The highest model class is {highest}. These are experimental class responses, not verified authorship probabilities, word shares, or prose-quality ratings. The installed skill reports high-confidence false positives in its English pilot. Retain the candidate; the measured response does not create a prose defect.")
 full['document_analysis']['citations_provenance']+=' The supplied native result matches the exact candidate hash, pinned checkpoint, and one window covering all input tokens. Native model classification is separate from documented source history; method identity remains blind.'
 full['review_metadata']['native_results_read']=True
 full['review_metadata']['numeric_status']='Supplied native single-window output bound exactly; four-class semantics preserved.'
 full['review_metadata']['integrated_at_utc']=datetime.now(timezone.utc).isoformat()
 occ=native['occlusion'];assert occ['performed'] is True
 assert occ['unmeasured_due_to_limit']==0 and occ['total_paragraphs']==candidate['coverage']['paragraphs_total']
 assert len(occ['paragraphs'])==candidate['coverage']['paragraphs_total']
 for n,item in enumerate(occ['paragraphs'],1):
  original=next(p for p in candidate['paragraph_assessments'] if p['paragraph_id']==item['paragraph_id'])
  assert item['status']=='measured'
  assert item['start']==original['start'] and item['end']==original['end']
  assert item['quote']==original['quote']==text[item['start']:item['end']]
  b=item['baseline_ai_involvement'];a=item['after_removal_ai_involvement'];d=item['delta_percentage_points']
  assert all(math.isfinite(v) for v in [b,a,d]) and 0<=a<=1
  assert abs(b-involvement)<1e-7 and abs(d-(b-a)*100)<1e-7
  fid=f'O{n}'
  full['findings'].append({
   'id':fid,'basis':'local_occlusion','direction':'ai_like' if d>0 else 'human_compatible' if d<0 else 'neutral','strength':'weak',
   'spans':[{'start':item['start'],'end':item['end'],'quote':item['quote']}],
   'observation':f"For {item['paragraph_id']}, the supplied baseline AI-involvement score is {b!r}, the after-removal score is {a!r}, and baseline minus after-removal is {d!r} percentage points.",
   'interpretation':'This is sensitivity to removing the whole paragraph and rescoring the changed input. A positive delta means removal lowered the score; a negative delta means removal raised it. It is not a paragraph AI probability, the model\'s causal explanation, a defective-phrase location, or a reason to remove required content.',
   'human_alternative':'Changed length, remaining context, ordinary genre cues, and broken argument or narrative continuity can change the same scorer on human or AI prose. The experiment does not separate those effects.',
   'discriminating_evidence':'Matched-length controlled edits and independent validation would be needed to attribute the response to a particular wording choice. No such claim is made. The fixed blind review found the intact paragraph faithful and suitable.',
   'source_record':json.dumps({'file':str(mpath),'sha256':hashlib.sha256(mraw).hexdigest(),'field':f'occlusion.paragraphs[{n-1}]','conditions':'Supplied pinned local English checkpoint; one-window whole-input baseline; deletion of this entire paragraph changes length and context; no inference by reviewer.'}),
   'triage':{'action':'retain','reason':'Measured deletion sensitivity identifies no independently supported prose defect. The all-paragraph blind review passed this paragraph; required meanings must not be removed to lower a score.','repair_required':False,'unresolved_scope':'The causes of the model sensitivity remain unresolved. This is uncertainty about the measurement, not an unresolved editing defect.'}
  })
  next(p for p in full['paragraph_reviews'] if p['paragraph_id']==item['paragraph_id'])['finding_ids'].append(fid)
 full['measurement_record']={
  'native_result_file':str(mpath),'native_result_sha256':hashlib.sha256(mraw).hexdigest(),
  'candidate_sha256':candidate['sha256'],'model':native['model'],'revision':native['revision'],'weight_sha256':native['weight_sha256'],
  'measured_at_utc':native['measured_at_utc'],'language':'English, manually verified','window_count':1,'token_count':native['token_count'],'all_input_tokens_scored':True,
  'class_probabilities':probs,'ai_involvement_class_score':involvement,
  'semantics':'Unvalidated local four-class outputs. AI involvement = AI + AI-edited + Humanized; native 1-Human agrees within floating-point rounding. No value is a verified authorship probability or a fraction of words.',
  'source_native_sha256':hashlib.sha256(source_raw).hexdigest(),'source_class_probabilities':source_probs,
  'candidate_minus_source_percentage_points':deltas,
  'comparison_limit':'A rise in the Human class or fall in the AI class does not establish improved writing, human origin, or general detection performance. Movement into AI-edited or Humanized remains inside the AI-involvement aggregate.',
  'independently_calibrated_here':False,'authorship_verified_by_model':False,
  'occlusion':native['occlusion'],
  'guard_checks':'Successful serialized worker exit, pinned model and weight hashes, exact input hash, complete single-window token coverage, finite four-class outputs/sum, and exact deletion anchors/deltas checked.'
 }
 full['editorial_closure']['post_measurement_action']='retain'
 full['editorial_closure']['post_measurement_reason']='The new native feedback is bound and reviewed. It supplies no independently grounded repair need. Keep the passing candidate and the frozen reader judgment; do not begin a rewrite solely to chase an uncalibrated score.'
 full['editorial_closure']['measured_feedback_reviewed']=True
 full['editorial_closure']['next_action']='Return the measured evidence and retain decisions to the writer; any later revision requires a separately stated real defect or changed user requirement.'
 full['triage_summary']={k:sum(f['triage']['action']==k for f in full['findings']) for k in ['revise','retain','unresolved']}
 assert full['triage_summary']['retain']==len(full['findings'])
 for filename,data in [('full-ledger.json',full),('measurement-binding.json',full['measurement_record'])]:
  out=directory/filename;assert not out.exists(),out
  out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 native_copy=directory/'native-result.json';assert not native_copy.exists();native_copy.write_bytes(mraw)
 raw_validation=directory/'validation-native.json'
 assert not raw_validation.exists()
 subprocess.run([sys.executable,'-B','-X','utf8',str(EVIDENCE),'validate',str(path),str(directory/'full-ledger.json'),'--model-result',str(mpath),'--out',str(raw_validation),'--html',str(directory/'evidence.html')],check=True)
 validated=json.loads(raw_validation.read_text(encoding='utf-8'))
 assert validated['schema_version']==2 and validated['authorship_probabilities'] is None
 assert validated['text_sha256']==candidate['sha256']
 assert validated['coverage']['review_fraction']==1 and validated['coverage']['paragraphs_total']==candidate['coverage']['paragraphs_total']
 assert 'measured_output' in validated
 lookup={f['id']:f for f in full['findings']}
 assert len(validated['findings'])==len(lookup)
 for f in validated['findings']:
  f['triage']=lookup[f['id']]['triage']
  assert f['triage']['action'] in {'revise','retain','unresolved'}
 validated['triage_summary']=full['triage_summary']
 validated['measurement_record']=full['measurement_record']
 validated['editorial_closure']=full['editorial_closure']
 validated['review_metadata']=full['review_metadata']
 validated['full_constraint_coverage']=full['full_constraint_coverage']
 validated['voice_constraint_checks']=full['voice_constraint_checks']
 validated['triage_validation_scope']='Analyst triage was keyed to every validated finding and checked for a valid action/reason. Exact hashes, quotations, coordinates, complete coverage, and native model binding were validated by evidence.py. Semantic judgments and triage correctness are not automatically authenticated.'
 vpath=directory/'validated-full.json';assert not vpath.exists()
 vpath.write_text(json.dumps(validated,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 triage={'case_id':CID,'candidate':label,'candidate_sha256':candidate['sha256'],'findings':[{'id':f['id'],'basis':f['basis'],**f['triage']} for f in full['findings']],'summary':full['triage_summary'],'closure':full['editorial_closure']}
 (directory/'triage.json').write_text(json.dumps(triage,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 pair['candidates'][label]={'candidate_sha256':candidate['sha256'],'validated_full_file':str(vpath),'validated_full_sha256':hashlib.sha256(vpath.read_bytes()).hexdigest(),'feedback':validated,'triage':triage}
 print(CID,label,'validated',validated['coverage'],'triage',full['triage_summary'])

assert hashlib.sha256((LAB/'blind-review/round-1.json').read_bytes()).hexdigest()==freeze['review_sha256']
out=ROOT/CID/'pair-feedback.json';assert not out.exists()
out.write_text(json.dumps(pair,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
manifest={'case_id':CID,'completed_at_utc':datetime.now(timezone.utc).isoformat(),'pair_feedback_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'candidate_files':{label:{name:hashlib.sha256((ROOT/CID/label/name).read_bytes()).hexdigest() for name in ['full-ledger.json','native-result.json','measurement-binding.json','validation-native.json','validated-full.json','triage.json','evidence.html']} for label in ['A','B']},'blind_review_unchanged':True,'method_identities_read':False}
(ROOT/CID/'pair-feedback-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
print('PAIR PACKAGE',str(out),'SHA256',manifest['pair_feedback_sha256'])
