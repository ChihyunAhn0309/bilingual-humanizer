from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
r=Path(__file__).resolve().parent/'development/exhibition-review'
source=(r/'source.txt').read_bytes();candidate=(r/'draft-3.txt').read_bytes()
assert hashlib.sha256(candidate).hexdigest()=='d5e79d5787e61d7a86c6018bff60a46ea9363235ee0d7e17cfc42cb0501d0269'
d={'review_type':'parent_separate_from_fresh_writer_prescore_review',
   'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(source).hexdigest(),
   'candidate_sha256':hashlib.sha256(candidate).hexdigest(),'eligible_for_scoring':False,'fidelity_pass':False,
   'candidate_score_seen':False,
   'necessary_repairs':[{'id':'EXPECTED-NOT-HOPED','source_quote':'I expected it to explain how the port had changed',
      'candidate_quote':'hoping to hear how the port had changed over time',
      'reason':'Expected explanatory content has become a wish. The meaning brief states expectation, and the source asserts expectation; hope does not preserve that mental stance.',
      'repair_direction':'Restore expectation about the guide explaining port change, without adding stronger assurance.'},
     {'id':'PRESENT-UNCERTAINTY','source_quote':'I cannot tell whether this was a permanent problem or the result of exhibits being moved.',
      'candidate_quote':"I couldn't tell whether the mismatch was permanent or had been caused by exhibits being moved.",
      'reason':'The source explicitly retains uncertainty at the time of the review. Could not tell only explicitly locates uncertainty in the past. Preserve the current knowledge limit while keeping the correctly retained causal relation.',
      'repair_direction':'Use current cannot/can\'t tell, keeping the uncertainty over permanence versus moving-exhibit cause.'}],
   'paragraph_reviews':['P1 keeps venue, Sunday, £4 hire, most recordings, six-minute interview, former operator, radio/hand-signals explanation, earlier photograph and interview recommendation. Repair expectation versus wish.',
     'P2 retains ease, individual replay, sequence mismatch, two backtracks and present-price refusal. Causality is correctly explicit, but preserve the present uncertainty of the review.',
     'P3 preserves positive visit judgment, approximate hour, conditional desire for a longer visit, upstairs closure and ticket desk nonstatement.'],
   'reader_assessment':'Coherent conventional review. Fresh-context writing alone has not established an advantage, and source comparison found two narrow semantic issues before measurement.',
   'independence_limit':'Parent reviewed source separately from fresh writer; knows previous scores and study purpose, not blind/human review.',
   'revision_note':'This is revision2 after the initial draft; one repair remains within the unchanged three-revision limit. Preserve this unscored file.'}
p=r/'draft-3-prescore.json';assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'eligible':False,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
