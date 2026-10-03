# Independent final review

Reviewed on 2026-10-03. Request assessed: natural, active rewriting in the original language while preserving facts, meaning and voice.

## Method and limits

I read the candidate `SKILL.md`, its Korean, English, structural rewriting, editing controls, iterative review, genre/voice, fidelity, detector/authorship and commercial feature references, then compared both forward-test final texts with their original sources. I also independently compared the incident source with the HIX output, followed by the additionally supplied Korean neighborhood notice and its Undetectable output. I did not read earlier review reports, audit JSON or any observation JSON, and did not use network/browser tools or run a detector. Only this report was written.

This assesses the supplied text and instructions. It does not independently verify the current vendor documentation, research tables, historical test receipts or authorship. No detector estimate is given.

Severity: **high** means an invented fact or materially misleading claim; **medium** means a substantive qualification, responsibility or commitment is lost; **low** means a readability problem without a material factual change.

## Forward-test findings

### Korean: no actionable fidelity or naturalness findings

The final preserves the announcement's substantive points: the planned application change from the next meeting, the reason involving two missed applications, the exemption for the three existing applicants, October 18 at 2 p.m., the same small room in the village hall, the two-book maximum, permission to attend without books, the writer's enjoyment of extended conversation, the shortage of cleanup time, the proposed 4 p.m. cleanup, its unsettled status, and the invitation to suggest alternatives in the application comment.

Concrete checks:

- Source `다음 모임부터는 게시판 댓글로만 받을 예정입니다` remains a plan in final `다음 모임부터는 게시판 댓글로만 받을 예정입니다`. The opening's `바꿔` is governed by this planned statement; it does not assert that the new process has already been implemented.
- Source `책은 한 사람당 두 권까지` and `교환할 책이 없어도` retain both the maximum and the inclusion of visitors without exchange books.
- Source `저는 책 이야기가 길어지는 게 좋았지만` becomes `저는 책 이야기를 길게 나누는 게 좋았습니다`. This preserves the personal positive reaction; the following sentence preserves the contrasting practical problem.
- Final `정리했으면 합니다` and `아직 정해진 규칙은 아니니` keep the cleanup request tentative, rather than turning it into a fixed rule.

Paragraphing gives applications, meeting details and the cleanup proposal separate jobs. The polite `합니다`/`주세요` relationship remains consistent. `모자랐던 만큼` is somewhat more written in tone than the source's `그래서`, but fits the notice and does not warrant a correction. The source was already clear, so the restrained amount of rewriting is not itself a failure of an active rewrite request.

### English: no actionable fidelity or naturalness findings

The final preserves the quantitative result and its referents, the absent longest-time measurement, the restriction to catalogued material, the absence of evidence about uncatalogued material, both personal preferences, the archive lead's pre-extension responsibility, the unapproved rota, the review and public notice's distinct duties, the denominator instruction and the absence of a permanent-service decision.

Concrete checks:

- Final `Across 24 requests ... median lookup time from 18 minutes to 11 minutes` retains the sample size, statistic and direction of change. The unrecorded longest lookup time stays beside the result.
- Final `The trial covered only material that had already been catalogued, so the results do not establish ... uncatalogued material` preserves the inference boundary; it does not turn missing evidence into evidence of failure.
- `I found the shared index easier to use, though I still prefer the paper cards for tracing earlier descriptions` retains the mixed judgment and its specific use case.
- Final `The review must distinguish ... and the public notice must explain that distinction` retains two actors, two actions and both obligations. It does not substitute the factual distinction for the instruction to communicate it.
- The report's `should retain the 24-request denominator` remains a recommendation and is moved next to the relevant result.

The grouping improves navigation while keeping British spelling and `rota`, the factual tone, and the personal voice in its own paragraph. The original already contained mostly effective sentences; preserving them where useful is appropriate. Neither this result nor the Korean result establishes broad performance beyond these two examples.

## Candidate instruction quality

No blocking instruction defect, harmful universal style rule, or unsupported detector guarantee was found in the inspected instructions.

The strongest safeguards are concrete rather than aspirational: mapping actor/action/object/occasion/force before consolidation; preserving document purpose and decision stage; checking qualification placement; allowing an effective passage to remain; and comparing each revision with the immutable original. The review budget is a ceiling, and the fallback for unrepaired fidelity problems is a faithful earlier version or the original affected span. Those choices support aggressive editing without making change volume the objective.

The language references explicitly reject punctuation blacklists, forced informality, random sentence variation, invented first-person agency and arbitrary frequency targets. For example, Korean `~할 수 있다` is reviewed by meaning rather than automatically converted to `한다`, and English passive voice is retained when the actor is unknown or irrelevant. These are conditional editorial judgments, not universal claims about how humans write.

The detector guidance separates fluency, fidelity, detector output and writing history. It rejects invented scores, metric conversion by subtraction, score averaging across services, guarantees, and treating a surface checker as semantic proof. The commercial reference distinguishes implementable editorial ideas from undisclosed trained models. These are appropriately bounded claims. The source-backed product descriptions and historical measurements were not externally reverified in this offline review, so this finding must not be presented as independent verification of those references.

The workflow is detailed for short prose, but it explicitly permits mental working maps and skips unnecessary structural changes. No instruction change is justified merely to reduce its length. Continued evaluation should use additional genres and independent source texts; the present cases demonstrate local success rather than universal effectiveness.

## Independent HIX incident comparison

Overall: the HIX output is less faithful and less readable than the source. It requires substantive correction before use as an incident communication. These findings apply to this exact supplied output, not to all HIX outputs or a detector's behavior.

| ID / severity | Source and output spans | Finding and justified correction |
| --- | --- | --- |
| H1 — high | Source has no month/year. Output adds `(Oct 2023)` after the PDF statement. | This is an unsupported date. Delete it; no replacement date can be inferred from the source. |
| H2 — high | Source: `Projects below that threshold were not affected, and PDF exports continued to work.` Output: `PDF exports continued to work for projects below that threshold ... and only projects above it were impacted.` | The output narrows the affirmative PDF assurance to smaller projects. The source says PDF exports continued working without that restriction, including the projects whose CSV export was affected. Restore both separate scope statements, for example `Projects below that threshold were not affected, and PDF exports continued to work.` The output's following affected-project statement does not recover this file-format distinction. |
| H3 — medium | Source: `We have not yet determined why the pre-release load test missed the fault.` Output: `So we still asked why the fault was not caught in the load test itself, as it happened pre-release.` | Asking a question is not the same as reporting that its answer remains unknown. The output loses the explicit unresolved investigation status and gives `it` an unclear referent. Restore `We have not yet determined why the pre-release load test missed the fault.` |
| H4 — medium | Source: the platform team `will report whether other paginated exports need the same coverage`. Output: `report back if any other paginated exports require this coverage`. | `Report back if` can mean that a report is required only when the answer is yes; the source promises a report of whether coverage is needed, including a negative answer. Use `report whether other paginated exports need the same coverage` and keep `By Friday` applying to both adding the test case and reporting. |
| H5 — medium | Source: `We disabled CSV export at 14:47`. Output: `CSV export was disabled at 14:47`. | The action and time survive, but explicit first-person responsibility is omitted. Incident communications can use passive voice, but preservation of this source's meaning and voice favors retaining `We disabled CSV export at 14:47`. This is a contextual ownership finding, not a blanket objection to passive voice. |
| H6 — low | Source: `The status page was updated at 15:05.` Output: `Updated at 15:05 PM on the status page.` | The output is a fragment and combines a 24-hour time with `PM`. Restore the complete sentence with `15:05`. The time itself should not be changed. |
| H7 — low | Source: `The team traced the issue to a pagination change released on Monday.` Output: `The root of the problem was a pagination change introduced on Monday, the team traced.` | The terminal `the team traced` is unidiomatic and leaves the transitive verb without a usable object. Restore the source's direct subject–verb structure or an equivalent grammatical sentence. |

Several other details survive: Tuesday at 14:20 UTC, the greater-than-10,000 threshold, Monday's change, rollback at 16:10, checking 25 previously affected projects, restoration at 16:35, and the instruction to re-export downloads from 14:20–14:47. `All` still refers to the preceding 25 projects, so removing the repeated second `25` is not a semantic loss by itself. The final general no-action statement plus its specific re-export exception is inherited from the source rather than invented by the rewrite.

The HIX errors reinforce the candidate skill's existing checks for unsupported additions, scope, unresolved status and speech-act force. They do not justify a new universal rule about punctuation, sentence length or vocabulary.

## Independent Undetectable Korean comparison

Files: `vendor/source-ko-neighborhood.txt` and `vendor/undetectable-ko-neighborhood.txt`. This assessment was formed from the two texts without reading an observation file.

Overall: the output is readable and preserves the core operational instructions. It is a modest line edit of an already clear notice, with no comparable invented fact or major scope error. Two small preservation issues are worth correcting under a strict requirement to retain every source detail and the source's courteous voice.

| ID / severity | Source and output spans | Finding and justified correction |
| --- | --- | --- |
| K1 — low | Source: `지난번에는 시작할 때 구역을 나누지 않아`. Output: `지난번에는 구역을 나누지 않아`. | The explicit timing of the earlier omission, `시작할 때`, is dropped. The practical reason for the new assignment procedure survives, but the output no longer specifies that the failure occurred at the start. Restore `시작할 때`; it is a meaningful time detail, not empty framing. |
| K2 — low | Source: `장갑과 작은 삽은 각자 가져오셔야 하고`. Output: `장갑과 작은 삽은 각자 가져오고`. | Context still makes this read as a supply instruction, so it would be excessive to claim that bringing the tools has become optional. Nevertheless, the explicit obligation and respectful address are less clear. Restoring `가져오셔야 하고` preserves both at little readability cost. The later change from `남으실 필요` to `남을 필요` similarly makes the address slightly less courteous; keeping the original honorific better matches the source voice. |

The main restrictions survive: this Saturday from 9 to 11 a.m.; heavy-rain postponement to the following Saturday at the same time; the Friday 6 p.m. response deadline and group-chat poll; residents providing gloves and a small shovel versus the association supplying rubbish bags; three areas with four people each in arrival order; excluding children from the count for households bringing children; those households doing only edge weeding; and permission to leave early and help only as much as possible. `다만` is deleted, but the child-count exception and restricted work assignment remain explicit, so the deletion is not itself a fidelity failure.

`정리하려고 합니다` becomes the firmer announcement `정리합니다`, while `배정하겠습니다` becomes `배정합니다`. Both still clearly refer to a future scheduled activity; neither reports completed work. The source's softer, personal organizer voice is slightly reduced, but the text remains polite and appropriate. These are modest stylistic shifts, not evidence of a failed announcement. No new rule or detector-performance inference follows from this single sample.
