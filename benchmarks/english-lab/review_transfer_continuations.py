from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
r = Path(__file__).resolve().parent
cid = sys.argv[1]
details = {
 'T01': {'sha256':'698c859e5a09aa303a28306f488bd6ce9d68684c456f8df70b88f7d963021a94',
 'paragraph_reviews':[
  'P1 preserves fictional Bell Street setting, possible ready repair awaiting owner reply, agreement before buying a replacement part, limited visitor visibility and unfinished versus not necessarily neglected. Moving this mechanism before specialist staffing does not introduce blame or certainty.',
  'P2 preserves four benches, qualified empty-bench capacity claim, one electrical volunteer, alternate Saturdays, possible lamp/later chair order with woodworking specialist, and partly work-dependent queue rather than solely arrival time.',
  'P3 retains a suggested status board change, all three exact label strings, comparative explanatory value, owner next action qualified by if anything, and no added volunteer hours or guaranteed completion date.'],
 'reader_assessment':'A coherent owner-reply-first route followed by the separate staffing constraint and joint communication proposal. All paragraphs and transitions reread against the original. The less visual opening is a legitimate trade-off; no further editorial defect found.'},
 'T02': {'sha256':'39739e2375cd2c7becddb0ffe5f7f6956f8886dd1a5e8efbccf4cd86f5b8580d',
 'paragraph_reviews':[
  'P1 preserves next-Monday two-week trial, shared return log, borrowed projectors/audio kits, North/Annex desks, recording change and unchanged borrowing limits. No dates or promised outcome invented.',
  'P2 retains inability-to-open trigger, Nia, Friday 3 p.m. deadline, separately marked during-trial unavailability, paper sheet beside cupboard, Nia next-morning transcription and reader exemption from duplicate entry. Grouping does not make the outage condition depend on missing the deadline.',
  'P3 retains return-time logging of kit number and time before cupboard placement, missing-item inspection shelf and short log note, prohibition during checking and permission for the returning person to leave unless an immediate safety concern exists.',
  'P4 keeps permanent continuation undecided and retains writer review after week two plus asking both desks whether the extra step was useful. Sequence of review and final decision is not changed into an adoption commitment.'],
 'reader_assessment':'The file-access responsibilities are grouped before the return procedure, with timing distinctions still explicit. The Friday request is less visually prominent than in draft1, but the four-paragraph route remains clear and suitable. Full source comparison and sequential reader review found no necessary repair.'}
}
detail = details[cid]
registry = json.loads((r/'transfer/registry.json').read_text('utf-8'))
case = next(c for c in registry['cases'] if c['id']==cid)
candidate = r/'prototype-output'/cid/'draft-2.txt'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate) == detail['sha256']
record = {'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
 'reviewer':'parent separate from writer, aware of earlier scores/method; not a new blind or human reviewer',
 'candidate_sha256':sha(candidate),'source_sha256':case['source_sha256'],
 'eligible_for_scoring':True,'fidelity_pass':True,'reader_eligible':True,'necessary_repairs':[],
 'candidate_score_seen':False,'paragraph_reviews':detail['paragraph_reviews'],
 'reader_assessment':detail['reader_assessment'],
 'scope':'Feedback-driven continuation after the frozen first comparison; not untouched transfer. Writer has disclosed limited other-arm excerpt exposure in released feedback.',
 'budget':'One initial draft plus one changed revision; the earlier candidate remains intact.'}
out = candidate.with_name('draft-2-prescore.json')
assert not out.exists()
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'case':cid,'eligible':True,'review_sha256':sha(out),'candidate_sha256':sha(candidate)}))
