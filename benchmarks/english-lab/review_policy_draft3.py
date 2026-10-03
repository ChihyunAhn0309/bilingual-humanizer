from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
r=Path(__file__).resolve().parent/'development/policy-note'
source=(r/'source.txt').read_bytes();candidate=(r/'draft-3.txt').read_bytes()
assert hashlib.sha256(candidate).hexdigest()=='34136cbcc5e27fa42a1e45cf32c38436fae71066a44d4317b5f63735ede80444'
s=source.decode('utf-8');c=candidate.decode('utf-8')
pairs=[
('Winter Wednesday recommendation rather than Saturday','I recommend retaining the Wednesday repair session during the winter rather than moving it to Saturday.',"For this winter, I'd keep Wednesday rather than move to Saturday."),
('Recommendation evidence basis, not a claim that no survey occurred','This recommendation is based on the attendance records from the last six sessions, rather than on a survey of everyone who might want to attend.',"I'm basing the recommendation on attendance records from the last six sessions, rather than on a survey of everyone who might want to attend."),
('Wednesday range and both Saturday trial counts','Wednesday attendance ranged from 11 to 18 people. The two Saturday trials attracted 20 and 23 people',"20 and 23 people, compared with 11 to 18 on Wednesdays"),
('More visitors welcomed, qualified volunteer still missing','Higher attendance is welcome, although it does not by itself resolve the staffing question.',"More visitors are welcome. What we don't yet have is another qualified volunteer for the electrical bench"),
('Second volunteer at electrical bench each Saturday','each required a second volunteer at the electrical bench',"another qualified volunteer for the electrical bench, where each Saturday trial needed a second person"),
('Mara Wednesday ability to end February; no Saturday commitment','Mara can continue to cover Wednesdays until the end of February. She has not committed to Saturdays',"Mara can cover Wednesdays until the end of February, but she hasn't committed to Saturdays"),
('Potential unavailable bench even with more visitors','Moving the session now could therefore leave the electrical bench unavailable even when more visitors arrive.',"Move the session now and we could have more visitors arriving while that bench is unavailable."),
('Conditional January review suggestion','I suggest reviewing the decision in January if another volunteer comes forward.',"I suggest we revisit the decision in January if another volunteer comes forward."),
('Unmet demand because of waiting','we should record how many people leave without a repair because they cannot wait',"we should count the people who leave without a repair because they can't wait"),
('Completed-repair counts do not measure convenience for nonattendees','We have counted completed repairs so far, but those totals cannot tell us whether Wednesday is convenient for people who have not attended.',"We've been counting completed repairs, but that doesn't tell us whether Wednesday is convenient for people who haven't attended.")]
coverage=[]
for label,a,b in pairs:
    assert a in s and b in c
    coverage.append({'constraint':label,'source_quote':a,'candidate_quote':b,'passed':True})
d={'review_type':'parent_separate_from_writer_prescore_fidelity_and_reader_review',
   'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(source).hexdigest(),
   'candidate_sha256':hashlib.sha256(candidate).hexdigest(),'eligible_for_scoring':True,'fidelity_pass':True,
   'necessary_repairs':[],'candidate_score_seen':False,'coverage':coverage,
   'independence_limit':'Same parent reviewer, separate from writer; knows earlier development score and proposed reader route, not blinded or human review.',
   'paragraph_reviews':['P1 begins with the genuine attendance advantage and then preserves the exact limited basis of the recommendation. It makes no claim about whether anyone has conducted a survey.',
      'P2 welcomes higher attendance before contrasting bench staffing. The second person refers to the needed qualified volunteer in the same sentence. Mara\'s capability and noncommitment, possible bench unavailability and winter recommendation remain distinct.',
      'P3 preserves all proposed follow-up actions, their January/volunteer condition and the inability to infer nonattendee convenience from completed repairs.'],
   'reader_assessment':'Eligible evidence-first alternative. The initial data give Saturday its fair case before the staffing constraint leads to Wednesday. The recommendation is delayed compared with draft-1, a reader-route tradeoff rather than a demonstrated overall improvement. Conditional imperative Move ... and we could is readable as a hypothetical, not an instruction to move.',
   'self_repair_checked':'The archived draft-2 survey-conduct overstatement is absent; the complete draft-3 explicitly concerns the recommendation\'s evidential basis. No new issue found.',
   'revision_count_note':'Initial draft-1; unscored alternative draft-2 revision1; repaired draft-3 revision2. Preserve the rejected draft and its erroneous self-review.'}
p=r/'draft-3-prescore.json';assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'eligible':True,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
