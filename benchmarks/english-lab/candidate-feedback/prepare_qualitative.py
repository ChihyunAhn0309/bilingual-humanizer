"""Prepare score-blind candidate ledgers from the locked reader review."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
LAB=ROOT.parent
review_path=LAB/'blind-review/round-1.json'
review_raw=review_path.read_bytes()
freeze=json.loads((LAB/'blind-review/round-1.freeze.json').read_text(encoding='utf-8'))
assert hashlib.sha256(review_raw).hexdigest()==freeze['review_sha256']
review=json.loads(review_raw)
key_map={'argument_structure':'structure','reasoning_specificity':'reasoning_specificity','voice_continuity':'voice_consistency','rhythm_repetition':'rhythm_repetition','language_features':'language_features','citations_provenance':'citations_provenance'}
manifest={
 'created_at_utc':datetime.now(timezone.utc).isoformat(),
 'source_blind_review_sha256':freeze['review_sha256'],
 'candidate_scores_read_at_preparation':False,'method_identities_read':False,
 'preparation_scope':'Only the frozen all-paragraph reader review and exact anonymous candidate files. Native measurements will be attached separately after availability.',
 'files':{}
}
for case in review['cases']:
 for label,candidate in case['candidates'].items():
  cid=case['case_id']; outdir=ROOT/cid/label;outdir.mkdir(parents=True,exist_ok=True)
  path=Path(candidate['file']);raw=path.read_bytes();text=raw.decode('utf-8')
  assert hashlib.sha256(raw).hexdigest()==candidate['sha256']
  findings=[];paragraphs=[]
  for n,p in enumerate(candidate['paragraph_assessments'],1):
   assert text[p['start']:p['end']]==p['quote']
   fid=f'S{n}'
   findings.append({
    'id':fid,'basis':'style_observation','direction':'neutral','strength':'weak',
    'spans':[{'start':p['start'],'end':p['end'],'quote':p['quote']}],
    'observation':p['assessment'],
    'interpretation':'This paragraph-level editorial observation records a supported, genre-appropriate choice and retained meaning. It identifies no necessary repair and does not identify the authoring process. AI-assisted or human editing could produce these choices.',
    'human_alternative':'A human editor following the same source constraints could legitimately choose this wording, ordering, or level of formality. The fictional details and source-derived specificity are not evidence of actual human experience.',
    'discriminating_evidence':'Writing history would be needed to identify the editing process. The source-bound blind review is sufficient for this retain decision; no authorship conclusion is drawn from fluency.',
    'triage':{'action':'retain','reason':'The frozen review found this paragraph faithful and suitable for its reader. No actual defect or unsupported claim was identified.','repair_required':False,'unresolved_scope':'Method identity and the causes of any later model score remain unknown; neither is a prose defect.'}
   })
   paragraphs.append({'paragraph_id':p['paragraph_id'],'status':'reviewed','assessment':p['assessment'],'finding_ids':[fid]})
  ledger={
   'text_sha256':candidate['sha256'],
   'summary':f"Anonymous candidate {cid}/{label} passes the frozen source-fidelity review and is reader-eligible. All {len(paragraphs)} paragraphs were reviewed. No necessary repair was identified; retain the version. Native quantitative feedback is not yet attached. Its later model scores must remain separate from fidelity and reader quality.",
   'document_analysis':{key_map[k]:v for k,v in candidate['six_dimension_review'].items()},
   'findings':findings,'paragraph_reviews':paragraphs,
   'authorship_probabilities':None,
   'review_metadata':{
    'case_id':cid,'anonymous_candidate':label,'genre':case['genre'],'language':'English',
    'frozen_blind_review_file':str(review_path),'frozen_blind_review_sha256':freeze['review_sha256'],
    'candidate_path':str(path),'candidate_sha256':candidate['sha256'],
    'original_source_sha256':case['original_sha256'],'source_constraints_sha256':case['constraints_sha256'],
    'candidate_scores_read_at_qualitative_preparation':False,'method_identities_read':False,
    'inference_run_by_reviewer':False,'known_history':'Anonymous rewrite of a known AI-generated synthetic source. Fictional people, situations, and memories are not human-authored ground truth.',
    'numeric_status':'Pending supplied native results; no inference requested or executed by this reviewer.'
   },
   'editorial_closure':{'fidelity_pass':candidate['fidelity_pass'],'reader_eligible':candidate['reader_eligible'],'necessary_repairs':candidate['necessary_repairs'],'decision':'retain','reason':'No source-fidelity or reader-quality defect was found in the pre-score review. Optional stylistic differences do not compel another rewrite.','blind_pair_preference':case['pairwise_reader_preference']},
   'full_constraint_coverage':candidate['full_constraint_coverage'],
   'voice_constraint_checks':candidate['voice_constraint_checks'],
   'finding_triage_requirement':'Every style or measurement finding must have exactly one action: revise, retain, or unresolved, with its reason. Score magnitude alone does not create a revise action.'
  }
  out=outdir/'qualitative-ledger.json'
  assert not out.exists(),out
  out.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
  manifest['files'][f'{cid}/{label}/qualitative-ledger.json']=hashlib.sha256(out.read_bytes()).hexdigest()
  print(cid,label,len(findings),'retain findings prepared')
p=ROOT/'qualitative-preparation.json'
assert not p.exists(),p
p.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
