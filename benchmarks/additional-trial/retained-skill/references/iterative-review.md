# Iterative rewriting and review

Read this for a rewrite. The normal workflow has separate drafting, fidelity review, and reader review stages. Multiple stages inside one response are not multiple independent sessions. Actual tool-backed reviewers or user feedback create additional turns; describe which kind occurred accurately.

## Start and keep state

Retain an immutable original source and the user's scope, language/register, protected regions, factual constraints, and requested format. The original remains the authority throughout the loop. A previous rewrite and a voice sample are never substitute sources of facts.

For substantial or explicitly audited work, keep a compact working record: original and candidate IDs or file hashes; candidate text; open findings; changes made; review method; revision count; detector targets, settings, receipts and pending results. Write it only to an appropriate task workspace, not inside the installed skill. For short routine prose, a working comparison is enough.

Default budget: one initial candidate plus at most **3 revision cycles**. When external checks are requested, allow at most **3 detector rounds**, each of which checks a candidate against the selected services within existing authorization and cost limits. A smaller user limit wins; a larger explicit limit may be used. A ceiling is not a quota. Continue only while a specific remaining defect or new useful feedback justifies another revision. Required fidelity repairs must not be skipped merely because the budget is reached: recover a faithful earlier candidate or preserve the original affected passage and report the remaining limitation.

## The loop

1. Draft a complete candidate using the language and genre guidance. For substantial active rewriting, apply [structural-rewrite.md](structural-rewrite.md): map meaning and reader functions, choose a useful information order, and compose whole paragraphs rather than substituting words sentence by sentence. Preserve all source propositions and protected material.
2. Review candidate versus original for meaning, quantities and their referents, attribution, confidence, conditions, negation, coverage and file structure. Use the offline checker when useful; its clean result never replaces this semantic comparison.
3. Perform a reader review for natural collocations, translationese, paragraph logic, register, voice and unnecessary formulaic phrasing. Judge actual spans in context. Fluent formal prose, technical repetition and intentional punctuation are not defects by themselves.
4. Revise concrete findings. Fix semantic drift before stylistic preferences. Then repeat fidelity review against the original and a reader review of the completed candidate, including untouched transitions. Reject revisions that make the text smoother by losing information or fabricating experience.
5. If requested, incorporate actual external detector feedback under the rules below. Accept a revision only if fidelity and reader quality are retained. Preserve a best faithful candidate rather than blindly using the most recent one.

Even a candidate with no findings receives the fidelity and final reader checks; it does not need artificial edits. A light-edit request keeps its narrow scope throughout the loop. A review-only request produces findings and does not enter a rewrite loop.

## Independent review when available

For an explicitly requested independent review, or a substantial iterative rewrite where delegation is permitted, use a **fresh-context subagent reviewer** if available. Give it only the realistic user request, original source, candidate, applicable skill and needed raw resources. Do not provide intended answers, author self-ratings or a request to approve. Keep generated artifacts isolated and prohibit changes or external uploads by the reviewer unless those actions are in scope.

Ask for concrete findings with the source/candidate spans, importance, and explanation; allow no findings. Review factual fidelity and reader quality separately. The writer decides on justified fixes, then submit the changed candidate for another review when material findings warranted revision. A reviewer who sees their earlier findings is a follow-up reviewer, not a new blind reviewer; label this accurately. Same-model independent context is not independent human or cross-model validation.

When delegation is unavailable, use distinct self-review stages and identify them as self-review if the user asked about independence. Do not create a new sidebar task just to simulate review. Do not block ordinary editing on the lack of a reviewer.

## Actual detector feedback

Detector-guided iteration is enabled when the user requests it. A request to edit the skill is not permission to transmit arbitrary future documents or spend money. Reuse an already-authorized service/document scope instead of asking again. If the user supplies reports, work from those; do not pretend to call a detector.

Before submitting a text, establish the named services, document, language/length eligibility, available authenticated tool or API, and any cost or query limit. Use the product's current official definitions. Never paste private credentials into a report. No specific vendor API client or account is bundled with this skill. If access is unavailable, finish the useful local editing and return the candidate with the external checks marked pending. Resume when the user supplies a new report or grants usable access; elapsed time is not an answer.

Define acceptance **per service** before checking: a documented label or an explicit numerical threshold with its native unit and direction. A Human Score is not an AI percentage, and a probability is not a fraction of generated words. A displayed rounded zero or a suppressed range is not an exact zero. If “perfect” is requested without a product definition, explain the limit once, use a documented human classification when available, and state the criterion; ask only if a threshold decision remains material. Do not invent an industry-wide pass threshold.

Keep each result's vendor, product/model version if known, settings, timestamp, original returned label/score definition, exact input hash, whole-document/segment scope and raw receipt location or user-supplied provenance. Record errors, unsupported inputs, omitted services and stale reports. The final candidate must satisfy **all selected required services on that same candidate** to report their configured targets met. One missing, unsupported, failed, unverifiable or stale result makes the overall status incomplete or unmet; it is not a pass. Editing any text invalidates prior results for the full document. Never combine favourable results from different drafts.

Treat a highlighted span as a place to inspect, not proof of bad writing. Rework a passage when a source-faithful, natural alternative is justified; don't remove qualifications, shorten away hard sections, fabricate stories, add typos, or insert hidden characters to change a score. If a faithful and natural span still receives an adverse result, preserve quality and report the disagreement. Detector targets never override fidelity.

The optional offline `scripts/check_detector_report.py` checks a structured result bundle against the final file hash. It performs **no external calls** and cannot authenticate a supplied receipt or certify human authorship. Read [detector-report-format.md](detector-report-format.md) before using it.

## Stop and resume

Stop when the requested local editing is complete and all requested checks have either met their defined target or have a specific unresolved status. Stop further detector-driven revisions when the budget is exhausted, two consecutive cycles yield no defensible improvement, a service cannot evaluate the input, access fails, or further changes would damage meaning/voice. Never loop forever or report unmet targets as passed.

When the user continues in a later turn, retain the original source, compare the feedback with the candidate it actually checked, and resume within the remaining budget. A general request to continue uses the existing budget; increase it only when the user explicitly permits additional cycles or a higher total. Record the exact instruction that authorizes any increase alongside the previous limit, new limit and cumulative usage. Continuing cannot manufacture access or prior results. Before external use, recheck any changed service, document, cost or privacy scope.

For requested audit output, report the best faithful candidate, actual review/revision counts, remaining issues, and each target's status. Say `configured targets met on this candidate` only with supporting receipts; never `guaranteed undetectable` or `certified human-written`. Routine prose-only requests still receive just the finished prose unless an unresolved material issue needs a short note.
