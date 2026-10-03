# Added cases: fresh-context review

Reviewed on 2026-10-03 against the supplied bilingual-humanizer 1.5.2 instructions. The task was to assess active rewriting while preserving facts, conditions, speech acts, voice, language and source function. This was a review only; no source, candidate or skill file was edited.

## Method and actual counts

For each text, I completed a semantic fidelity pass against its original and then a separate reader pass for naturalness, progression and voice. The sequence was English fidelity, English reader review, Korean fidelity, Korean reader review.

| Text | Fidelity passes | Reader passes | Revision cycles performed by this reviewer | Findings |
| --- | ---: | ---: | ---: | --- |
| en-museum-v1.txt | 1 | 1 | 0 | None |
| ko-library-v1.txt | 1 | 1 | 0 | None |
| Total | 2 | 2 | 0 | None |

These are four distinct review passes within one fresh-context subagent review, not four independent review sessions. No external tools, detectors or factual sources were used to assess the prose. No detector score or authorship conclusion is available.

I read only the two specified originals, their two specified candidates, `outputs/bilingual-humanizer/SKILL.md`, and its applicable editing references: `iterative-review.md`, `korean.md`, `english.md`, `genres-and-voice.md`, `structural-rewrite.md` and `fidelity-and-documents.md`. I did not consult previous candidates, reviews, mappings, results, briefs, plans or other experiment files.

## English museum memo

### Pass 1: semantic fidelity

No substantive fidelity defect found. Severity: not applicable.

The proposal remains a proposal by the collections team, with the same allocation, recipients, timing and reconsideration. The queue evidence retains its denominator, uncertainty and sampling limitation. The recommendation, staffing constraint, photography condition and unresolved authority all remain at their original strength.

| Source span | Candidate span | Assessment |
| --- | --- | --- |
| “proposes reserving 60 percent of next quarter's digitization capacity” and “one quarter before being reconsidered” | Same allocation and timing; “The allocation would apply for one quarter before being reconsidered.” | Proposed status, duration and review point retained; the remaining capacity still covers fragile items awaiting condition review and an education selection. |
| “In a sample of 25 entries reviewed last week, 7 appeared to need clarification.” | “Of the 25 entries reviewed last week, 7 appeared to need clarification.” | Count, denominator, time and uncertainty retained. The next sentence still identifies the oldest-record sample and possible overstatement across the full queue. |
| “Researchers need reliable delivery estimates” / “conservators need enough time” / “Educators have asked for images of ordinary household objects” | All three needs remain together in the second paragraph, following “A queue based only on request date would not reflect all three groups' needs.” | All three interests, safe-movement condition, fewer individual requests and planned lessons remain. Reordering does not turn a need into an approved allocation rule. |
| “the registrar prepare a provisional schedule by 18 November, using existing staff hours” | “the registrar use existing staff hours to prepare a provisional schedule by 18 November” | Actor, provisional status, deadline, resource constraint and first-person recommendation retained. |
| “Until that responsibility is assigned, disputed objects should remain on the provisional schedule without a promised completion date.” | Same sentence in a separate final paragraph. | Pending exception authority, conflict between exhibition deadline and conservation assessment, and the interim treatment of disputed objects retained. |

The current total of 184 objects, inconsistent active-versus-answered records, request confirmation before assigning photography dates, and starting photography with confirmed requests that have no outstanding handling concerns are also retained.

### Pass 2: reader review

No substantive naturalness, progression or voice defect found. Severity: not applicable.

The memo moves coherently from the proposed allocation to the competing needs, queue evidence, scheduling recommendation and remaining authority decision. The recommendation and unresolved exception policy now occupy separate paragraphs, making their different functions easier to locate. The formal, measured voice remains intact, including “Our current queue” and “I recommend”; no invented personality or stronger certainty appears. The introductory reference to “all three groups' needs” is resolved immediately by the sentences that follow and does not require a cosmetic revision.

The source was already reasonably direct. Retaining much of its wording is appropriate; a larger change percentage is not required.

## Korean library review

### Pass 1: semantic fidelity

No substantive fidelity defect found. Severity: not applicable.

The candidate retains the document's remit and its place before the operating proposal is made concrete. It also preserves the distinction between facts, interpretations, review requirements and communication requirements.

| Source span | Candidate span | Assessment |
| --- | --- | --- |
| “접수된 의견을 살펴보고, 운영안을 구체화하기 전에 확인해야 할 조건을 정리한다.” | “접수된 의견을 살펴보고, 지역 도서관의 시범 운영안을 구체화하기 전에 확인할 조건을 정리한다.” | Reviewing opinions, identifying conditions and the decision stage all remain explicit. |
| “6주 동안 화요일과 목요일 저녁 개관 시간을 20:00까지 연장” | Same duration, days and time. | The proposal's quantitative and temporal scope is unchanged. |
| “저녁 시간 연장에 관한 논의와 앞으로의 상시 운영 시간에 관한 논의를 구분할 필요가 있다. 안내 과정에서도 이 차이를 분명하게 전달해야 한다.” | “저녁 개관 연장과 앞으로의 상시 운영 시간은 논의에서 구분할 필요가 있고, 이용 안내에서도 그 차이를 분명하게 전달해야 한다.” | Both the review distinction and the separate communication obligation survive. The paragraph also retains the temporary status and the instruction to check wording for an unintended permanent-policy implication. |
| “의견서는 모두 42건” with 28 supporting, 9 preferring the current schedule and 5 without a preferred option | “의견서 42건 가운데 28건은 … 9건은 … 5건은 …” | Counts and categories retained, together with the limits on representativeness and inferring reasons. The instruction to consider preferences for the current schedule remains. |
| “현재 자료에는 … 인과적 근거가 없다” and “실제 방문으로 이어졌다는 증거와는 구분해야 한다” | Both statements remain in the fourth paragraph. | Absence of causal evidence is not changed into evidence of no effect. Expressed support remains a preference, distinct from demonstrated attendance. The purpose of avoiding overinterpretation is also retained. |
| “자원봉사자가 해당 시간에 참여할 수 있는지는 아직 해결되지 않았다” / “운영을 시작한 뒤 정리할 세부 사항으로 넘기기 어렵다” | Both statements remain, followed by “연장 개관에 대한 관심을 인정하면서 자원봉사자 참여 가능성을 확인해야 한다.” | Unresolved availability, its relevance to feasibility, the objection to deferring it, recognition of interest and the later verification obligation all remain. |
| “조용한 열람실의 정원은 12명” / “각각 설명해야 한다” / “두 조건을 함께 살펴볼 필요가 있다” | “정원은 12명으로 … 수용 인원은 늘지 않는다” / “함께 살펴볼 필요가 있다” / “두 조건을 각각 설명해야 한다” | Fixed capacity, the distinction from access hours, joint consideration during scope review and separate explanation in guidance are all retained. Reversing the final two instructions does not merge their functions or change their force. |

### Pass 2: reader review

No substantive naturalness, progression or voice defect found. Severity: not applicable.

The paragraph order separates the review's remit, temporary-policy boundary, submitted opinions, evidence limits, volunteer feasibility and room capacity. Each paragraph develops a distinct point. The original's dispersed instruction about checking permanent-policy wording is now beside the temporary-policy distinction; the later volunteer check is beside the unresolved participation condition. These moves make the relevant relationships easier to follow.

The Korean remains natural formal explanatory prose in `-다` style. “이는 제출된 의견의 분포일 뿐” has a clear referent, and the final “두 조건” refers directly to the access time and simultaneous room capacity stated immediately before it. The cautious recommendations and mandatory communication instructions retain their different force. There is no need to replace the document's appropriate institutional voice with a conversational style or to remove framing that carries its review function.

## Result and limits

Neither candidate needs a revision on the basis of this review. This means that this reviewer found no substantive defect in the two specified versions; it is not a guarantee that every possible reader will prefer them.

The sources had previously been used in development. The candidates and assessment were unseen in this reviewer's context, but this is fresh-context review of development material, not held-out evidence. It is also same-model review, not independent human or cross-model validation. No claim about general skill performance follows from two cases. Source preservation was assessed; the real-world truth of the source claims was not independently checked.

## Reviewed file identities

SHA-256 values identify the exact inputs reviewed:

| File | SHA-256 |
| --- | --- |
| work/renewal-trial/sources/en-museum.txt | B9538869823413658DB9F36D246411FB41EFA0575AADCB2D789DB987354E93B1 |
| work/renewal-trial/sources/ko-library.txt | B82F92389CF1C42DED62184EB359C87D81848723D44A2B9790B9FA0EB6DFD5B0 |
| work/renewal-trial/v152-check/en-museum-v1.txt | F6441886E969BD44FCDDED1476A4A0FAAD6AFFA44291123583B249197F405258 |
| work/renewal-trial/v152-check/ko-library-v1.txt | 91B4849A75B6D9E6E8AE1B9F2BC44F242B2DB325A948A5FF03E65715ACBD3BC6 |

## Follow-up review: English v2 and Korean v3

This follow-up was completed on 2026-10-03 in the same reviewer context. It is not a new blind or fresh-context review. The findings above remain the historical review of the v1 candidates; the results below apply to `en-museum-v2.txt` and `ko-library-v3.txt`.

I reread both full original sources and both requested completed candidates. I then performed one separate fidelity pass and one final reader pass per candidate, in the order English fidelity, English reader review, Korean fidelity, Korean reader review. I did not read self-reviews, briefs, intermediate Korean v2, other cases or other experiment files, and did not edit the sources, candidates or skill. The prior review remains in this conversation context.

### English v2 — fidelity pass

No substantive fidelity defect found. Severity: not applicable.

The source's proposed 60 percent allocation, recipients of the remaining capacity, next-quarter scope and reconsideration after one quarter remain unchanged. All three stakeholder needs remain, including the preparation required for safe object movement, the lower individual demand for ordinary household objects and their use in planned lessons.

The source span “In a sample of 25 entries reviewed last week, 7 appeared to need clarification” corresponds to “Of the 25 entries reviewed last week, 7 appeared to need clarification,” immediately followed by the oldest-record sampling limitation. The full-queue total of 184, active-versus-answered record problem and request confirmation before assigning photography dates are retained. No observed uncertainty becomes a confirmed finding.

The source recommendation “the registrar prepare a provisional schedule by 18 November, using existing staff hours” remains “the registrar use existing staff hours to prepare a provisional schedule by 18 November.” The candidate also preserves the handling-clearance condition for initial photography, unresolved authority for an exception, the exhibition-versus-conservation conflict and the requirement to keep disputed objects on the provisional schedule without a promised completion date until responsibility is assigned. The original's first-person recommendation and collective responsibility remain.

### English v2 — final reader pass

No substantive naturalness, progression or voice defect found. Severity: not applicable.

The stakeholder paragraph now names the three needs before stating “A queue based only on request date would not reflect all three needs.” The reference is clear. The memo proceeds coherently from allocation to stakeholder needs, queue evidence, scheduling and the unresolved exception decision. Qualifications stay beside the findings or actions they govern. Formal, restrained phrasing remains suitable for the decision memo, and the last paragraph gives a concrete interim action. These observations establish that v2 reads acceptably; they do not establish a necessary or general improvement over v1.

### Korean v3 — fidelity pass

No substantive fidelity defect found. Severity: not applicable.

The source's remit “접수된 의견을 살펴보고, 운영안을 구체화하기 전에 확인해야 할 조건을 정리한다” remains explicit as “접수된 의견을 살펴보고, 지역 도서관의 시범 운영안을 구체화하기 전에 확인해야 할 조건을 정리한다.” The 6-week proposal, Tuesday and Thursday evenings and 20:00 end time are all retained. Temporary status, distinction from future regular hours and the separate obligation to communicate the distinction remain. The source's general “안내 과정에서도 이 차이를 분명하게 전달해야 한다” is represented by “안내에서도 그 차이를 분명하게 전달해야 한다.” The instruction to check the document for an unintended permanent-policy implication also remains.

The 42 submissions and their 28/9/5 categories are unchanged. The source's statements that the figures describe submitted opinions but cannot represent every user's needs remain in “이 수치는 제출된 의견의 분포를 보여주지만, 도서관 이용자 모두의 요구를 그대로 나타낸다고 볼 수는 없다.” The reasons for opinions still cannot be assumed from the response counts, and support for the existing schedule must still be considered.

The candidate preserves the absence of causal evidence, the distinction between preference and actual-visit evidence, and the reason for maintaining that limit during discussion. It retains unresolved volunteer availability, its role in judging feasibility, the objection to deferring it until after opening, and the later obligation to verify availability while recognizing interest. The 12-person reading-room limit remains unchanged by longer hours. Finally, “함께 살펴볼 필요가 있다” retains joint consideration of the two conditions when reviewing the pilot's scope, while “이용 안내에서는 두 조건을 각각 설명해야 한다” retains the distinct communication obligation. Neither action is replaced by the other.

### Korean v3 — final reader pass

No substantive naturalness, progression or voice defect found. Severity: not applicable.

The prose maintains the source's formal `-다` register and measured institutional voice. The order gives the review remit and policy boundary first, then opinions and evidence limits, followed by the volunteer and capacity conditions. Each paragraph has a distinguishable function. “이 수치” refers clearly to the submission counts, and “두 조건” follows the explicit statement of access hours and simultaneous room capacity. Required distinctions, cautions and communication duties do not become generic filler simply because they recur in formal prose. The candidate is readable without further cosmetic changes; this is an assessment of v3 against its source, not an assumption that its revision label implies higher quality.

### Actual cumulative review counts and limits

| Case | Versions reviewed in this context | Cumulative fidelity passes | Cumulative reader passes | Review rounds per case | Writer post-draft revisions reported in the follow-up request | Revisions made by this reviewer |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| English museum | v1, v2 | 2 | 2 | 2 | 1 | 0 |
| Korean library | v1, v3 | 2 | 2 | 2 | 2 | 0 |
| Total | Four completed candidate versions | 4 | 4 | Four case-level reviews across two task turns | 3 | 0 |

This follow-up adds four passes to the previous four: eight actual passes in total, divided equally between fidelity and reader review. The writer revision counts are supplied task metadata; this reviewer did not observe those edits or review Korean v2. There were two review turns in one continuing subagent context, not two independent reviewers.

Neither current candidate has an unresolved substantive finding from this review. No further revision is requested. The earlier limitations still apply: these are previously used development sources, not held-out evidence; the review is same-model, with no human, cross-model, detector or external factual validation. No browser, upload, detector or subagent was used in this follow-up.

| Follow-up candidate | SHA-256 |
| --- | --- |
| work/renewal-trial/v152-check/en-museum-v2.txt | 7D3C0C794C960FFDB178AF59E4FF102A7573CD99AAB88D62AF3C687739FC4F8F |
| work/renewal-trial/v152-check/ko-library-v3.txt | E5B16F3CAFB7941E15F435480CEF857405344B1EB535E54D6F1E8A4827250FF0 |
