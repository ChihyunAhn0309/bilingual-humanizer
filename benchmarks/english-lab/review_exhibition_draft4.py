from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
r = Path(__file__).resolve().parent / 'development/exhibition-review'
old = (r/'draft-3.txt').read_bytes()
new = (r/'draft-4.txt').read_bytes()
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha(new) == 'fd481b2dcafaacd3c65bb3e6af0dade075d407996b5ab2e421b59b4ebd5f1972'
assert new == old.replace(b'hoping to hear', b'expecting to hear').replace(b"I couldn't tell", b"I can't tell")
lead = old.replace(b'hoping to hear how the port had changed over time', b'expecting it to explain how the port had changed over time').replace(b"I couldn't tell", b"I can't tell")
assert sha(lead) == '0cf7560051216f642588619a6e4606f5e8415725cabf97b0e08fe943878a0b7c'
alternate = r/'draft-4-lead-parallel-repair-unscored.txt'
assert not alternate.exists()
alternate.write_bytes(lead)
d = {'review_type':'parent_separate_from_writer_prescore_fidelity_and_reader_followup',
 'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
 'source_sha256':sha((r/'source.txt').read_bytes()),'candidate_sha256':sha(new),
 'eligible_for_scoring':True,'fidelity_pass':True,'necessary_repairs':[], 'candidate_score_seen':False,
 'resolved_findings':[
  {'id':'EXPECTED-NOT-HOPED','after':'expecting to hear how the port had changed over time','assessment':'Expectation of the hired guide providing port history is restored; desire is no longer substituted.'},
  {'id':'PRESENT-UNCERTAINTY','after':"I can't tell whether the mismatch was permanent or had been caused by exhibits being moved.",'assessment':'Present uncertainty and the proposed cause both remain explicit.'}],
 'paragraph_reviews':[
  'P1 preserves Sunday, harbour exhibition, £4 hire, expected port history, most recordings and labels, six-minute former operator interview, radio failure/hand signals explanation, earlier photograph and interview recommendation.',
  'P2 preserves ease of operation, replay of one recording, whole-sequence distinction, intermittent numbering/order mismatch, two backtracks, present uncertainty over permanence versus relocation as cause, refusal to hire again at current price.',
  'P3 preserves positive visit assessment, approximate hour, conditional longer visit, upstairs closure and ticket desk nonstatement about reopening.'],
 'reader_assessment':'The guide content, usability and overall visit form a coherent review. Full reread found no material reader defect or additional semantic error. No score-based preference has been made.',
 'independence_limit':'Parent did not author either candidate; same model agents and parent aware of earlier results, not human or fully blind review.',
 'prior_review_sha256':sha((r/'draft-3-prescore.json').read_bytes()),
 'repair_collision':{'detail':'Two agents repaired the same feedback concurrently. Development writer saved the first repair, then the brief-only writer overwrote draft-4 before the stop message arrived. Its exact byte-identical first artifact is reconstructed from unchanged draft-3 and reported replacements, with its previously reported SHA verified. Both versions are retained. Current brief-writer version chosen before measurement because it preserves the brief-only drafting lineage; no selection by score.',
 'alternate_path':alternate.name,'alternate_sha256':sha(lead),'alternate_score':None,
 'budget_deviation':'Three planned revision stages after initial draft, but the duplicate parallel repair produced one extra distinct unscored artifact beyond the four-artifact cap. Disclose this orchestration error; no additional revision or measurement is authorized for the duplicate.'}}
p = r/'draft-4-prescore.json'
assert not p.exists()
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'eligible':True,'path':str(p),'sha256':sha(p.read_bytes()),'candidate_sha256':sha(new)}))
