from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
r=Path(__file__).resolve().parent/'development/policy-note'
source=(r/'source.txt').read_bytes(); candidate=(r/'draft-1.txt').read_bytes()
assert hashlib.sha256(candidate).hexdigest()=='c7ad6b4a34578e1e0a67308ab88d10a6c4d776de1e143a195e3ce07f9eb25d80'
s=source.decode('utf-8'); c=candidate.decode('utf-8')
pairs=[
('Recommendation and timing','retaining the Wednesday repair session during the winter rather than moving it to Saturday',"keep the repair session on Wednesdays this winter rather than move it to Saturday"),
('Evidence basis and limit','attendance records from the last six sessions, rather than on a survey of everyone who might want to attend',"attendance records from the last six sessions, not a survey of everyone who might want to come"),
('Both attendance quantities','Wednesday attendance ranged from 11 to 18 people. The two Saturday trials attracted 20 and 23 people',"20 and 23 at the two trials, compared with 11 to 18 on Wednesdays"),
('Each Saturday needs second electrical volunteer','each required a second volunteer at the electrical bench',"Each Saturday trial needed a second volunteer at that bench"),
('Welcome attendance without solving staffing','Higher attendance is welcome, although it does not by itself resolve the staffing question',"Higher attendance is welcome, but moving now could leave the electrical bench unavailable just when more visitors arrive"),
('Named volunteer ability/time, noncommitment and missing qualified replacement','Mara can continue to cover Wednesdays until the end of February. She has not committed to Saturdays, and we do not yet have another qualified volunteer',"Mara can cover Wednesdays until the end of February, but she hasn't committed to Saturdays, and we don't yet have another qualified volunteer"),
('Potential consequence, not certainty','Moving the session now could therefore leave the electrical bench unavailable even when more visitors arrive',"moving now could leave the electrical bench unavailable just when more visitors arrive"),
('January review suggestion conditional on another volunteer','I suggest reviewing the decision in January if another volunteer comes forward',"If another volunteer comes forward, I suggest we review the decision in January"),
('Interim count of people leaving unrepaired because they cannot wait','we should record how many people leave without a repair because they cannot wait',"we should count the people who leave without a repair because they can't wait"),
('Existing repair counts cannot establish convenience for nonattendees','We have counted completed repairs so far, but those totals cannot tell us whether Wednesday is convenient for people who have not attended',"So far we've counted completed repairs, but those totals can't tell us whether Wednesday suits people who haven't attended")]
coverage=[]
for label,a,b in pairs:
    assert a in s and b in c
    coverage.append({'constraint':label,'source_quote':a,'candidate_quote':b,'passed':True})
d={'review_type':'parent_separate_from_writer_prescore_fidelity_and_reader_review',
   'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
   'source_sha256':hashlib.sha256(source).hexdigest(),'candidate_sha256':hashlib.sha256(candidate).hexdigest(),
   'eligible_for_scoring':True,'fidelity_pass':True,'necessary_repairs':[],
   'candidate_score_seen':False,'independence_limit':'Parent coordinates the study and knows the method hypothesis and source score; separate from writing, not blind or human review.',
   'coverage':coverage,
   'paragraph_reviews':['P1 moves the staffing trade-off next to a recognisable recommendation. It retains the welcome for increased attendance, possibility rather than certainty, the bench scope and Mara\'s limited commitment. It does not imply cancellation of the whole session.',
      'P2 preserves both Saturday trial counts, Wednesday range and exact last-six-session evidence scope. It does not turn six sessions into six Wednesdays plus two Saturdays. Survey absence is retained.',
      'P3 preserves a conditional January review, recommendation to count unmet repair demand and the limitation of existing completed-repair totals for nonattendees.'],
   'reader_assessment':'Eligible. The operational trade-off now drives the opening; observed attendance and the evidence limit follow as support, then the reader gets the proposed next steps. Contractions fit an internal recommendation without inventing a casual persona. No required new issue found.',
   'feedback_resolution':{'S1':'Recommendation and operational reason are adjacent; the exact evidence limit remains P2.','S2':'Attendance is welcomed and quantified; staffing remains a distinct feasibility constraint, without asserting Mara cannot do Saturdays.'}}
p=r/'draft-1-prescore.json'; assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'eligible':True,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
