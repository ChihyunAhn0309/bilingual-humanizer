# Bilingual Humanizer v1.5.2 prototype — final local audit

Date: 2026-10-03. Package: `outputs/bilingual-humanizer`. Task: independently apply the supplied skill to the English support email and Korean essay, then to the subsequently authorized English museum memo and Korean library review; preserve every fact/condition/voice/language; perform separate fidelity and reader reviews; and run the available local validators. No browser, external upload, detector, or installed-skill edit was used.

Release scope: the tested object is the v1.5.2 prototype in `outputs/bilingual-humanizer`, at the hashes recorded here. This audit does not identify, inspect or validate whatever production release is retained, and does not recommend replacing that release. The parent owns the separate production/checkpoint decision. A later publication must not relabel these prototype results as tests of a different retained version.

## Outcome

The package passes structural validation and all 45 existing unit tests. All four locally completed rewrites have no unresolved substantive fidelity or reader finding in this review. This supports these four applications only; it is not evidence of general editing quality, detector performance, human authorship, or fresh held-out performance.

Final text files:

- `v152-check/en-support.txt` — identical to the reviewed English v1; zero post-draft revision cycles.
- `v152-check/ko-essay.txt` — identical to the reviewed Korean v2; one post-draft revision cycle.
- `v152-check/en-museum.txt` — identical to the reviewed museum v2; one post-draft revision cycle.
- `v152-check/ko-library.txt` — identical to the reviewed library v3; two post-draft revision cycles.

These are completed local candidates. This audit does not promote them over any earlier externally verified checkpoint: no earlier candidate or detector receipt was opened, and no detector comparison was conducted. All intermediate versions are retained.

The English edit moves the switch-off request directly after the acknowledgment, keeps findings with their uncertainty, gives recording status and its limit a separate paragraph, and closes with the existing progress-report commitment. The Korean edit keeps the already effective chronology and restrained voice, connects the February admission to the ensuing explanation, and changes “책 한 권을 완성하는 일” to the more natural reading collocation “책 한 권을 끝까지 읽는 일.” These are selective editorial changes; change volume was not an acceptance criterion.

The museum edit puts the three user groups’ needs before the queue evidence and separates the scheduling recommendation from unresolved exception authority. The library edit regroups dispersed instructions by their purpose: remit/proposal, temporary-policy boundary and its communication, opinion evidence, causal limits, volunteer feasibility, and room capacity. The review and communication obligations remain distinct.

## Actual drafting and review counts

| Measure | English support | Korean essay | English museum | Korean library |
| --- | --- | --- | --- | --- |
| Initial complete drafts | 1 | 1 | 1 | 1 |
| Post-draft revision cycles | 0 | 1 | 1 | 2 |
| Drafting-context fidelity passes | 1 | 2 | 2 | 3 |
| Drafting-context reader passes | 1 | 2 | 2 | 3 |
| Separate-reviewer fidelity passes | 1 | 2 | 2 | 2 |
| Separate-reviewer reader passes | 1 | 2 | 2 | 2 |
| External detector rounds | 0 | 0 | 0 | 0 |

Two additional AI reviewers each began with a fresh context containing only the task, applicable skill/references, their assigned originals and new candidates. The first reviewed support v1 and essay v1, then essay v2 in the same context. The second reviewed museum v1 and library v1, then museum v2 and library v3 in the same context. Both later rounds were follow-ups, not new blind reviews. Across the writer and these reviewers, 15 fidelity passes and 15 reader passes were completed: eight of each in the drafting context and seven of each in the two reviewer contexts. These are staged document-level passes, not 15 independent reviewers. Copying approved version files to final filenames did not count as revision.

Review evidence is in `v152-check/self-review-v1.md`, `v152-check/self-review-v2.md`, `v152-check/fresh-review.md`, `v152-check/added-cases-self-review-v1.md`, `v152-check/added-cases-self-review-v2.md`, `v152-check/ko-library-self-review-v3.md`, and `v152-check/added-cases-fresh-review.md`.

## Concrete fidelity and reader findings

The English semantic comparison retained the gratitude and apology, Tuesday workshop and twelve people, version 3.8 and all four event times, two shutdowns with responsive controls, one reproduction versus the other unit’s four hours, unresolved software/connector cause, immediate customer action and exemptions, both conditional replacement routes, delivery-charge scope, Thursday report deadline in the recipient’s local time, and the distinction between storage diagnostics and the unchecked recording. No repair was required.

The Korean comparison retained all scenes, spelled-out dates and quantities, 선주 and 민호’s distinct speech/actions, the unfinished/finished-book chronology, the narrator’s discomfort and continued disagreement, and the unresolved mix of reluctance and curiosity. One editing-induced ambiguity was identified in self-review: v1 changed “그날 나는 … 먼저 말했다. 그리고 … 이야기했다” to “그날은 … 먼저 말한 뒤, … 이야기했다.” Since the preceding sentence names 선주 as subject, omitting “나는” could momentarily obscure who makes the admission. Revision 1 restored “그날 나는” while retaining the connected sentence.

The separate reviewer considered the narrator recoverable from context in v1 and requested no repair. The writer chose the more explicit v2 because it preserved the original actor signal at negligible stylistic cost. Both the writer’s final review and the reviewer’s follow-up found no remaining defect. This records the small difference in judgment rather than claiming all reviewers independently found the same issue.

Reader review found the support email’s action and contact commitment easier to locate while preserving its courteous, precise tone. It found the essay’s concrete gestures and modest final curiosity worth retaining. The largely unchanged Korean text is consistent with the skill’s instruction to preserve effective writing; further rewriting was not justified by a concrete finding. No human reader study or randomized preference test was conducted in this audit.

The museum self-review identified one minor clarity issue in v1: “all three groups’ needs” appeared before the three groups were enumerated, while the opening had mentioned a different possible set of three. One revision restored the source’s clearer within-paragraph progression, naming the needs before the conclusion. The reviewer found the v1 referent recoverable and did not request the change; both its follow-up and the writer’s final review accepted v2. The temporary 60 percent allocation, 184-object queue, 25-entry oldest-record sample with 7 apparently unclear entries, sample caveat, request confirmation, 18 November recommendation, existing staff hours, and unresolved exception rule all remain.

The library self-review made three conservative fidelity/voice refinements across two actual revision cycles. Cycle 1 restored “확인해야 할” in the remit instead of “확인할” and replaced the unnecessary dismissive “분포일 뿐” with neutral wording. Cycle 2 removed the added “이용” from the general status-guidance obligation, while retaining “이용 안내” where the original explicitly applies it to hours/capacity. The independent reviewer found no substantive defect in v1 and no defect in the follow-up on v3; these are the writer’s stricter clarity/scope judgments, not unanimous independent findings of a failed initial draft. The final text retains the pre-proposal review stage, temporary-versus-permanent distinction, 42/28/9/5 response relationships and limits, absent causal evidence, unresolved volunteer participation, 12-person cap, and separate review/notice/document-wording actions.

## Instruction audit

Reviewed `SKILL.md`, the required iterative, structural, English, Korean, genre/voice and fidelity references, evaluation guidance, and `agents/openai.yaml`. The active-rewrite default is qualified coherently by selective editing for effective prose, no change quota, and repair of observed defects. The revision ceiling is not a quota; fidelity recovery remains required if the budget is exhausted. Separate self-review versus fresh-context review is explicitly distinguished. Source authority, voice preservation, modality and exact material are consistently prioritized in the inspected instructions.

One low-priority inconsistency was found in the structural guide’s instruction-consolidation example. The initial file said different actions should retain both verbs, but the example replaced “The notice must also explain that distinction” with a joint obligation for the review and notice to “distinguish.” The latter could erase the explicit explanation action. This finding was sent to the parent agent; this validator did not edit the package. During the audit, the shared file was corrected to:

> The review must distinguish the temporary arrangement from permanent policy, a distinction the notice must explain.

The final inspected `references/structural-rewrite.md:26` keeps the two obligations separate. The inconsistency is resolved in the file hash recorded below. No other material contradiction was found in the inspected editing instructions. Vendor descriptions and research claims were not externally verified in this offline task, and the audit does not claim to have examined every research reference.

Before drafting the additional cases, the current `iterative-review.md` was reread after the parent added the retained-checkpoint paragraph. It requires retaining the exact candidate, source/skill identity and per-service receipts, evaluating a challenger on matching definitions, and declining to overwrite the checkpoint when evidence is missing or services disagree. This is consistent with the existing fidelity-first rule, exact-hash result binding, and rejection of the latest draft as an automatic winner. Its wording was inspected; its external-service behavior was not exercised by this audit. No instruction contradiction was found in that addition.

## Local checks actually run

| Check | Actual result | What it establishes |
| --- | --- | --- |
| Installed skill-creator `quick_validate.py outputs/bilingual-humanizer` | Exit 0, “Skill is valid!”; three runs: initially, after the example correction, and after the checkpoint addition | Package structural/frontmatter validity, not editorial quality |
| `py -3 -m unittest discover -s outputs/bilingual-humanizer/evals -p 'test_*.py' -v` | 45 tests passed, exit 0, on each of two runs: initial package and final checkpoint-containing snapshot | Existing preservation-checker and detector-report-consistency behavior; 45 unique tests, not 90 independent cases |
| `audit_preservation.py` on English v1 | Exit 0, `no_surface_change_found` | No changes in the checker’s recognized surface inventory |
| `audit_preservation.py` on Korean v1 | Exit 0, `no_surface_change_found` | Same limited surface result |
| `audit_preservation.py` on Korean v2 | Exit 0, `no_surface_change_found` | Same limited surface result for the final Korean text |
| `audit_preservation.py` on museum v2 | Exit 0, `no_surface_change_found` | Same limited surface result for the final museum text |
| `audit_preservation.py` on library v2 | Exit 0, `no_surface_change_found` | Same limited surface result for an intermediate library text |
| `audit_preservation.py` on library v3 | Exit 0, `no_surface_change_found` | Same limited surface result for the final library text |

The unit tests do not execute rewrites, judge naturalness or query detectors. The surface checker cannot validate subject attribution, condition scope, natural-language facts or most spelled-out quantities; the semantic reviews supplied those checks. No semantic conclusion is inferred from exit code 0 alone. Initial and final tool output is retained in `v152-check/check-log.json` and `v152-check/final-check-log.json`; six surface-audit JSON files retain exact input/output hashes. Repeating structural/script checks after the package changes was not counted as additional behavioral evidence.

## Final file identity

| File | SHA-256 |
| --- | --- |
| Source English | `ad38f82dd1b3bf3fe068109a143a751b7b30e31c7df0336f724b53fa73fb8e76` |
| Final English | `c9bb2bbe75f2c66594faae43994939112b97c9edf485fd734a47e602eb3a2c1f` |
| Source Korean | `57867e23d1007a78fc924eae9ed8855ead51e3ea085771a249e55cc345621d9b` |
| Final Korean | `34a38bd708f318a9db060a1e16bb3b6bf01f98ca43799a918bf1f8f99b94ab33` |
| Source museum | `b9538869823413658db9f36d246411fb41efa0575aadcb2d789db987354e93b1` |
| Final museum | `7d3c0c794c960ffdb178af59e4ff102a7573cd99aab88d62af3c687739fc4f8f` |
| Source library | `b82f92389cf1c42ded62184eb359c87d81848723d44a2b9790b9fa0eb6dfd5b0` |
| Final library | `e5b16f3cafb7941e15f435480cef857405344b1eb535e54d6f1e8a4827250ff0` |
| Final inspected SKILL.md | `c8270c5ed781ad54a9798a7a3710827b5c6133f25e0b71ef70fc69c70f8bf556` |
| Corrected structural-rewrite.md | `387724271d278873e97f2a8f717d3d6d84b8c7726029cb0de66686f9bc4b5ae6` |
| Current iterative-review.md, including checkpoint paragraph | `a7a572fd381e2c95041a3f6791e852fd87d29b1f9375fdbb06b3428b8ba70c42` |

`v152-check/manifest.json` records the same file paths and byte hashes. `v152-check/skill-snapshot.json` hashes the final package’s non-`__pycache__` files. The final support/essay/museum/library files match v1/v2/v2/v3 respectively; no prose changes followed their final reviews. The first two cases were drafted before the checkpoint paragraph was added; the additional cases were drafted with it present. The final instruction audit and local script checks include that addition.

## Evidence boundaries

These are previously used development sources, with candidates unseen in this validator’s context when drafting began. They are not fresh held-out data. The support email and essay were already largely natural; the additional institutional texts broaden the local editing task but still provide little evidence about long manuscripts, formatted documents or mixed-language writing. Preservation was checked against the supplied originals, not against external truth.

There was one narrow context-contamination event: this validator queried the agent inventory to check review-slot availability, and the response incidentally included brief prior-review final summaries. No prior candidate text, full review/comparison document, mapping, PLAN, or other experiment file was read. That exposure means the drafting context should not be described as completely blind to all prior assessment. The separately spawned reviewer received none of those summaries and stated that prior assessment was unseen in its own context.

The writer and both reviewers are AI agents; fresh context is not independent human or cross-model validation. No detector calls were assigned to or performed by this validator, no detector results were read, and no score or authorship prediction is made. The parent’s broader detector experiment and retained checkpoint are outside this audit’s comparison scope. Sources, installed skills and prior experiment artifacts were not changed by this validator. All new outputs are confined to this audit file and `v152-check/`.
