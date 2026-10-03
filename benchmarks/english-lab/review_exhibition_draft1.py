from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
r=Path(__file__).resolve().parent/'development/exhibition-review'
source=(r/'source.txt').read_bytes();candidate=(r/'draft-1.txt').read_bytes()
assert hashlib.sha256(candidate).hexdigest()=='05cf11d7d0d26dd4ba049fd64f2ecdc94ef008e8291a9d70dcedde9bbe71f924'
d={'review_type':'parent_separate_from_writer_prescore_fidelity_and_reader_review',
   'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
   'source_sha256':hashlib.sha256(source).hexdigest(),'candidate_sha256':hashlib.sha256(candidate).hexdigest(),
   'eligible_for_scoring':False,'fidelity_pass':False,'candidate_score_seen':False,
   'independence_limit':'Parent coordinates the study and knows the hypothesis/source value; did not write this candidate, not blind or human review.',
   'necessary_repairs':[{'id':'CAUSE-VS-OCCURRENCE','source_quote':'I cannot tell whether this was a permanent problem or the result of exhibits being moved.',
     'candidate_quote':"I don't know whether the mismatch was permanent or whether exhibits were being moved.",
     'reason':'The source is uncertain whether moving exhibits caused the mismatch. The rewrite instead explicitly makes the occurrence of moving exhibits unknown; this drops the causal relation and shifts the scope of uncertainty. Readers may infer the cause, but preserving it directly avoids changing the stated knowledge.',
     'repair_direction':'Keep uncertainty about whether the mismatch was permanent or resulted from moving exhibits, rather than uncertainty merely about whether exhibits were moved.'}],
   'paragraph_reviews':['P1 preserves the Sunday harbour visit, positive exhibition judgment, approximate hour, desire to stay longer conditional on upstairs being open, and ticket desk not saying when it would reopen.',
     'P2 preserves the £4 hired audio guide, expectation of port-change explanation, most recordings duplicating labeled identification, six-minute exception, former crane operator, hand signals when radio failed, the previously passed photograph and interview recommendation.',
     'P3 retains usability, individual replay without restarting the sequence, case-number/order mismatch, two backtracks and refusal to hire again at current price. Required repair: preserve uncertainty about the cause of that mismatch.'],
   'reader_assessment':'The three paragraph functions distinguish exhibition value, the interview exception and the guide purchase verdict. This is a useful coherent alternative. No forced fragments or new persona are introduced; a narrow meaning repair is needed before scoring.',
   'retention':'Preserve this unscored draft and review. Count a changed post-draft repair within the existing revision allowance and review the complete corrected text.'}
p=r/'draft-1-prescore.json';assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'eligible':False,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
