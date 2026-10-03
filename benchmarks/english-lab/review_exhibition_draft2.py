from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
r=Path(__file__).resolve().parent/'development/exhibition-review'
old=(r/'draft-1.txt').read_bytes();new=(r/'draft-2.txt').read_bytes();source=(r/'source.txt').read_bytes()
assert hashlib.sha256(new).hexdigest()=='54e7d73ebd53161b4ce7c77bf613c75f3adb423e036f92bb75d397744cc3fdd4'
assert old.decode('utf-8').replace('or whether exhibits were being moved','or resulted from exhibits being moved') == new.decode('utf-8')
d={'review_type':'parent_separate_from_writer_prescore_fidelity_and_reader_followup',
   'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(source).hexdigest(),
   'candidate_sha256':hashlib.sha256(new).hexdigest(),'eligible_for_scoring':True,'fidelity_pass':True,
   'necessary_repairs':[],'candidate_score_seen':False,
   'independence_limit':'Parent did not write candidate; same follow-up reviewer, not a new blind or human review.',
   'resolved_findings':[{'id':'CAUSE-VS-OCCURRENCE','before':"I don't know whether the mismatch was permanent or whether exhibits were being moved.",
      'after':"I don't know whether the mismatch was permanent or resulted from exhibits being moved.",
      'assessment':'The uncertainty now concerns whether moving exhibits caused the mismatch; occurrence uncertainty is no longer substituted. Required causal relation is explicit and no stronger attribution is asserted.'}],
   'paragraph_reviews':['P1 retains Sunday, harbour, positive value, approximate hour, conditional desire to stay longer, upstairs closure and missing reopening information.',
      'P2 retains £4 audio guide, expected port history, repetitive object identification, six-minute operator interview, failed radio/hand signals, previous photograph experience and qualified interview recommendation.',
      'P3 retains ease of use, individual replay, sequence and label-number mismatch, exactly two backtracks, uncertainty over permanence versus moving-exhibit cause, and refusal to hire again at the current price.'],
   'reader_assessment':'Full draft reread against original after the narrow repair. The three-paragraph organization remains coherent, the mixed judgment intact and the repaired sentence idiomatic. No new issue warrants another edit.',
   'prior_review_sha256':hashlib.sha256((r/'draft-1-prescore.json').read_bytes()).hexdigest(),
   'revision_count_note':'One initial draft plus one post-draft fidelity repair; initial draft remains unscored.'}
p=r/'draft-2-prescore.json';assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'eligible':True,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
