# English runtime follow-up after the v1.7.0 release

2026-10-03. At the user's explicit request, the English native crash was handed to the existing **AI detector skill 만들기** session. That session reproduced the Windows weight-loading failure, changed the installed detector to v3.1.2, verified real inputs and published the repair. This follow-up records successful measurements **after** the earlier humanizer release; the earlier failure receipts remain unchanged.

The detector uses the `pread` weight-loading backend on Windows to avoid the reproduced memory-mapped loading path. Model weights, model revision and four-class semantics are unchanged. This is an application workaround tested on the reproduced failure, not proof of stability in every environment. The detector's [runtime verification](https://github.com/ChihyunAhn0309/bilingual-ai-detector/blob/main/references/verification.md) records its own checks.

## Actual results

| Exact text | Human | AI | AI-edited | Humanized |
| --- | ---: | ---: | ---: | ---: |
| English archive original | 0.083031% | 99.643207% | 0.011131% | 0.262634% |
| English revision 1 | 0.323491% | 98.873353% | 0.045136% | 0.758016% |

These are native, uncalibrated English class outputs. **Humanized is not added to Human.** The Human increase is **0.240460 percentage points**, and the user's Human >=50 target remains unmet on both texts. A modest terminology edit is not evidence of general detector-performance improvement. The known synthetic AI-generated/edited provenance is unchanged.

The repair session measured both exact texts with its supervised CLI. The humanizer session imported and normalized those native results, preserving their original timestamps and execution proofs. It then independently ran the **installed humanizer's adapter** on revision 1; that end-to-end run succeeded and returned exactly the same four values. This is three successful runs on two distinct texts, not three independent accuracy samples. No commercial service, paid API, new model, download or changed detector calibration was used in this follow-up.

## Feedback and editorial decision

The detector reviewer completed source and revision ledgers, including all four paragraphs in each, the native class values and paragraph-deletion measurements. This is a follow-up by the earlier reviewer, not a new blind review. Exact source/quote/index/coverage validation passed. The earlier independent fidelity review of the one-sentence edit remains applicable because the revision bytes have not changed.

The current ledgers are paired with `validated-final.json` and `analysis-final.html`. Earlier validation/render files are retained as review history and are not used as the final ledger validation.

The reviewer found no further concrete reader defect requiring another rewrite. The text distinguishes numerical results and their limits, a personal preference, staffing/approval conditions, and the review/public-notice duties. The reporting sentence in revision 1 makes the 24-request sample size clearer. It remains the editorial selection; the original and all prior commercial checkpoints remain available.

Deletion sensitivity changed greatly for paragraphs whose actual text did not change after the single-sentence edit elsewhere. For revision 1, deleting the personal-preference paragraph reduced AI involvement by approximately 8.477 percentage points, and deleting the final duties paragraph by 14.072 points. Those observations show context sensitivity, not newly discovered flaws in those unchanged paragraphs. Removing them would lose source meaning. No phrase ban, invented experience, omission or additional score-only rewrite was adopted.

[Original feedback](en-original/review-feedback.txt) · [Revision feedback](en-revision-1/review-feedback.txt) · [Actual adapter result](adapter-en-final/feedback.json) · [Exact result registry](results.json).

## Reconciliation with the previous report

The [initial integration report](../local-feedback/REPORT.md) accurately describes the state at its earlier release: repeated source failures, an unmeasured edited candidate and a pending repair handoff. This later follow-up supplies the new successful measurements without overwriting that chronology or pretending the original failures were successful.

Humanizer v1.7.0's **27 released skill files remain byte-identical**. The repaired detector preserved its supported contract, so no relaxation of input, model, class, coverage or failure validation was needed. Substantial rewriting still starts with the local detector, triages real feedback, checks fidelity and measures complete candidates; completed review is a stopping reason even when a detector threshold remains unmet.

A separate-context [follow-up audit](final-review.md) checked the native values, execution provenance, exact inputs, final ledger pairing, preserved failures and unchanged skill files. It found no actionable issue. The auditor did not run another model inference; this is an AI evidence review, not authorship certification.
