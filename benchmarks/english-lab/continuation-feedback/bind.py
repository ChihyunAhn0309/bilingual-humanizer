"""Attach supplied continuation measurements and preserve prior eligible bests."""
import hashlib,json,math,subprocess,sys,stat
from pathlib import Path
from copy import deepcopy
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
LAB=ROOT.parent
EVIDENCE=Path('C:/Users/ach18/.codex/skills/bilingual-ai-detector/scripts/evidence.py')
prepared=json.loads((ROOT/'qualitative-review-manifest.json').read_text(encoding='utf-8'))
registry=json.loads((LAB/'transfer/registry.json').read_text(encoding='utf-8'))
prior_labels={'T01':'B','T02':'A'}
complete={'completed_at_utc':datetime.now(timezone.utc).isoformat(),'phase':'Explicitly disclosed feedback-driven prototype continuations; not untouched blind transfer','inference_run_by_reviewer':False,'cases':{},'files':{}}
for cid in ['T01','T02']:
 directory=ROOT/cid;qpath=directory/'qualitative-ledger.json';qraw=qpath.read_bytes()
 assert hashlib.sha256(qraw).hexdigest()==prepared['files'][f'{cid}/qualitative-ledger.json']
 full=deepcopy(json.loads(qraw));candidate_path=Path(full['review_metadata']['candidate_path'])
 raw=candidate_path.read_bytes();text=raw.decode('utf-8')
 assert hashlib.sha256(raw).hexdigest()==full['text_sha256']
 native_path=LAB/'continuation-scores'/cid/'model-result.json'
 nraw=native_path.read_bytes();native=json.loads(nraw)
 assert native['schema_version']==2 and native['mode']=='offline_local_model'
 assert native['text_sha256']==full['text_sha256']
 assert native['model']=='wasitaigeneratedcom/ai-text-detector-small'
 assert native['revision']=='f1795c86806e6838d4afa33d0b1427f8430c9615'
 assert native['weight_sha256']=='4a1561fadf44ec72934edd6158ff8c76e9388ade1384dbeeea6eb15f93251087'
 assert native['execution_guard']['worker_exit_code']==0 and native['execution_guard']['serialized_cli'] is True
 assert native['all_input_tokens_scored'] is True and native['external_detector_calls']==0
 assert len(native['windows'])==1
 w=native['windows'][0];probs=native['document_class_probabilities'];score=w['ai_involvement_class_score']
 assert w['token_start']==0 and w['token_end']==native['token_count']
 assert text[w['start']:w['end']]==w['quote'] and not text[:w['start']].strip() and not text[w['end']:].strip()
 assert set(probs)=={'human','ai','ai_edited','humanized'} and probs==w['class_probabilities']
 assert all(math.isfinite(v) and 0<=v<=1 for v in probs.values()) and abs(sum(probs.values())-1)<1e-5
 assert abs(score-(1-probs['human']))<1e-7 and abs(score-sum(probs[k] for k in ['ai','ai_edited','humanized']))<1e-5
 source_case=next(c for c in registry['cases'] if c['id']==cid)
 source_native=json.loads((LAB/'transfer-scores'/cid/'source/model-result.json').read_text(encoding='utf-8'))
 assert source_native['text_sha256']==source_case['source_sha256']
 prior_path=LAB/'blind-pairs'/cid/(prior_labels[cid]+'.txt')
 prior_native=json.loads((LAB/'transfer-scores'/cid/prior_labels[cid]/'model-result.json').read_text(encoding='utf-8'))
 assert hashlib.sha256(prior_path.read_bytes()).hexdigest()==prior_native['text_sha256']
 source_probs=source_native['document_class_probabilities'];prior_probs=prior_native['document_class_probabilities']
 for comparison in [source_native,prior_native]:
  assert all(comparison[k]==native[k] for k in ['model','revision','weight_sha256'])
 occ=native['occlusion'];assert occ['performed'] and occ['unmeasured_due_to_limit']==0
 assert len(occ['paragraphs'])==occ['total_paragraphs']==len(full['paragraph_reviews'])
 for n,item in enumerate(occ['paragraphs'],1):
  assert item['status']=='measured' and text[item['start']:item['end']]==item['quote']
  style=full['findings'][n-1]['spans'][0]
  assert all(style[k]==item[k] for k in ['start','end','quote'])
  b=item['baseline_ai_involvement'];a=item['after_removal_ai_involvement'];d=item['delta_percentage_points']
  assert all(math.isfinite(v) for v in [b,a,d]) and 0<=a<=1
  assert abs(b-score)<1e-7 and abs(d-(b-a)*100)<1e-7
  fid=f'O{n}'
  full['findings'].append({'id':fid,'basis':'local_occlusion','direction':'ai_like' if d>0 else 'human_compatible' if d<0 else 'neutral','strength':'weak','spans':[{'start':item['start'],'end':item['end'],'quote':item['quote']}],'observation':f"{item['paragraph_id']} supplied baseline AI-involvement {b!r}; after full-paragraph removal {a!r}; baseline-minus-removal delta {d!r} percentage points.",'interpretation':'This is sensitivity to deleting a paragraph, not a paragraph AI probability, a causal attribution to its wording, or a defect. Positive means removal lowered the score. Removal also changes length, context, and the completeness of the explanation or instructions.','human_alternative':'The same context and length effects can occur in human writing or any edited text. Ordinary clear instructions or specific examples can affect a model without being editorially defective.','discriminating_evidence':'Matched-length controlled changes and independent validation would be needed for a wording-causation claim. This independent source review found the intact paragraph faithful and readable, so the delta does not justify deleting or damaging it.','source_record':json.dumps({'file':str(native_path),'sha256':hashlib.sha256(nraw).hexdigest(),'field':f'occlusion.paragraphs[{n-1}]','conditions':'Supplied pinned local English model; whole-paragraph deletion from one complete window; no inference by this reviewer.'}),'triage':{'action':'retain','reason':'The measurement identifies no independent prose defect. Preserve all required meaning and the passing paragraph; a large delta is not a repair instruction.','repair_required':False,'unresolved_scope':'The source of model sensitivity is unresolved; this uncertainty does not require another rewrite.'}})
  next(p for p in full['paragraph_reviews'] if p['paragraph_id']==item['paragraph_id'])['finding_ids'].append(fid)
 selected_path=prior_path if cid=='T01' else LAB/'transfer'/source_case['source_file']
 selected_native=prior_native if cid=='T01' else source_native
 selection_reason=(
  'Preserve the earlier T01 B / prototype draft-1. Draft-2 is faithful but does not improve the reader route; the earlier concrete example-first version remains slightly preferred and has the higher Human-class score. This is retention of a previously passing version, not proof of human authorship.'
  if cid=='T01' else
  'Preserve the eligible original T02 source as the selected best under the recorded model statistic. Draft-2 is faithful and improves Human-class output over prototype draft-1, but remains below the already passing original. No decisive reader advantage was established to justify replacing the original. The small score difference is not a general quality or authorship verdict.'
 )
 full['summary']+=f" Supplied experimental four-class outputs: Human {probs['human']*100:.8f}%, AI {probs['ai']*100:.8f}%, AI-edited {probs['ai_edited']*100:.8f}%, Humanized {probs['humanized']*100:.8f}%; AI-involvement {score*100:.8f}%. These uncalibrated class responses are not authorship probabilities, word shares, or quality ratings. The installed English pilot contains high-confidence false positives. "+selection_reason
 full['measurement_record']={'native_result_file':str(native_path),'native_result_sha256':hashlib.sha256(nraw).hexdigest(),'candidate_sha256':full['text_sha256'],'model':native['model'],'revision':native['revision'],'weight_sha256':native['weight_sha256'],'measured_at_utc':native['measured_at_utc'],'language':'English, manually verified','window_count':1,'token_count':native['token_count'],'all_input_tokens_scored':True,'class_probabilities':probs,'ai_involvement_class_score':score,'semantics':'Four-class unvalidated experimental model response. AI involvement = AI + AI-edited + Humanized, native 1-Human agreeing within float rounding. No verified authorship probability.','source_class_probabilities':source_probs,'prototype_draft_1_class_probabilities':prior_probs,'draft_2_minus_source_percentage_points':{k:(probs[k]-source_probs[k])*100 for k in probs},'draft_2_minus_prototype_draft_1_percentage_points':{k:(probs[k]-prior_probs[k])*100 for k in probs},'occlusion':occ,'inference_run_by_reviewer':False}
 full['document_analysis']['citations_provenance']+=' The newly supplied native result matches this exact continuation hash and the same pinned checkpoint, with full one-window token coverage. Native measurements are separate from provenance and editorial quality.'
 full['editorial_closure'].update({'post_measurement_text_action':'retain as a valid alternative; no required repair','selected_best_file':str(selected_path),'selected_best_sha256':selected_native['text_sha256'],'selected_best_Human_class_probability':selected_native['document_class_probabilities']['human'],'selection_recommendation':selection_reason,'measured_feedback_reviewed':True,'next_action':'Return this actual bound feedback to the writer and close with the preserved eligible best; no new rewrite is requested.'})
 full['review_metadata']['integrated_at_utc']=datetime.now(timezone.utc).isoformat()
 full['review_metadata']['qualitative_snapshot_sha256']=hashlib.sha256(qraw).hexdigest()
 full['triage_summary']={k:sum(f['triage']['action']==k for f in full['findings']) for k in ['revise','retain','unresolved']}
 fp=directory/'full-ledger.json';assert not fp.exists();fp.write_text(json.dumps(full,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 nc=directory/'native-result.json';assert not nc.exists();nc.write_bytes(nraw)
 vr=directory/'validation-native.json';assert not vr.exists()
 subprocess.run([sys.executable,'-B','-X','utf8',str(EVIDENCE),'validate',str(candidate_path),str(fp),'--model-result',str(native_path),'--out',str(vr),'--html',str(directory/'evidence.html')],check=True)
 validated=json.loads(vr.read_text(encoding='utf-8'))
 assert validated['schema_version']==2 and validated['authorship_probabilities'] is None and validated['coverage']['review_fraction']==1
 assert validated['text_sha256']==full['text_sha256'] and 'measured_output' in validated
 fmap={f['id']:f for f in full['findings']};assert len(fmap)==len(validated['findings'])
 for finding in validated['findings']:
  finding['triage']=fmap[finding['id']]['triage']
  assert finding['triage']['action'] in {'revise','retain','unresolved'} and finding['triage']['reason']
 for key in ['measurement_record','editorial_closure','review_metadata','full_constraint_coverage','voice_constraint_checks','triage_summary']:
  validated[key]=full[key]
 validated['triage_validation_scope']='Exact anchors, hashes, native binding and coverage were validated by evidence.py. Triage was attached by exact finding ID and checked for complete valid actions. Semantic judgments and selection reasons remain independent analyst assessments.'
 vp=directory/'validated-full.json';assert not vp.exists();vp.write_text(json.dumps(validated,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 package={'case_id':cid,'candidate':'prototype draft-2','phase':'feedback-driven disclosed continuation','feedback':validated,'closure':full['editorial_closure'],'qualitative_snapshot_unchanged':True,'parent_chronology_unmodified':True,'no_inference_by_reviewer':True}
 pp=directory/'feedback-package.json';assert not pp.exists();pp.write_text(json.dumps(package,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 complete['cases'][cid]={'package_file':str(pp),'package_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),'candidate_sha256':full['text_sha256'],'coverage':validated['coverage'],'triage':full['triage_summary'],'fidelity_pass':True,'reader_eligible':True,'closure':full['editorial_closure']}
 for name in ['qualitative-ledger.json','full-ledger.json','native-result.json','validation-native.json','validated-full.json','evidence.html','feedback-package.json']:
  p=directory/name;complete['files'][f'{cid}/{name}']=hashlib.sha256(p.read_bytes()).hexdigest()
 print(cid,'all paragraphs validated;',full['triage_summary'],'selected',str(selected_path))
manifest=ROOT/'complete-feedback-manifest.json';assert not manifest.exists()
manifest.write_text(json.dumps(complete,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
for name in complete['files']:
 (ROOT/name).chmod(stat.S_IREAD)
manifest.chmod(stat.S_IREAD)
print('MANIFEST',str(manifest),'SHA256',hashlib.sha256(manifest.read_bytes()).hexdigest())
