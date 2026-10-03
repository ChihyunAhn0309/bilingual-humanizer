# Checked feedback cycles: v1.10.0

The skill now returns each completed detector review to the writer, checks the accepted findings against the next exact candidate, and repeats when new justified work remains. A scan or an `applied` note cannot stand in for confirmed resolution. The new offline `feedback_cycle.py` validates the saved links, whole-document coverage, native measurements, source fidelity bindings, revision use and final selection. It does not generate prose or call a model: the assistant orchestrates rewriting and the existing detector within the active session.

Two actual English continuations applied all four accepted findings from the current review of the v1.9 drafts. The support email brings acknowledgement forward and removes redundant amount/scope wording. The reflection repairs the misleading `although`/`either` relations and restores the modest observed-benefit emphasis. Independent pre-score source review and post-score whole-document review confirmed these repairs. The later feedback reported no new justified defect; one explicitly requested complete-composition alternative per source was then reviewed within the same budget. The email alternative was measured. The reflection alternative weakened an expectation into a hope, so it was rejected before scoring and the closed r2 text was recovered.

## Actual local Human class values

| Synthetic case | Source (inherited) | r1 v1.9 draft (inherited, open findings) | r2 feedback repairs | r3 composition alternative | Delivery selection |
| --- | ---: | ---: | ---: | ---: | --- |
| support-email | 0.012120% | 0.314060% | 0.071305% | 0.065802% | r2 / 0.071305% |
| reading-reflection | 0.009758% | 0.014873% | 0.021194% | Not scored: fidelity rejected | r2 / 0.021194% |

Percentages are the unchanged English model's native Human class multiplied by 100. AI, AI-edited and Humanized remain separately preserved in every record; Humanized is not Human. The English model is uncalibrated and has high-confidence false positives in its saved pilot. These values are not verified probabilities of historical human authorship. The selected values remain below the user's 50% objective; this release demonstrates feedback application and checked selection, not a demonstrated English detection breakthrough or universal pass.

The best faithful checkpoint is stored separately from the delivery-eligible pool. A candidate with accepted edits still open cannot be called a completed final merely because its Human value is higher. For repeated reviews of identical text, the latest review controls eligibility, so an old clean review cannot erase a newly found defect. Retained drafts and their actual scores are not overwritten. Comparisons between r1 and later drafts therefore disclose both the score and the open/closed status, rather than silently substituting a lower value for the previous best.

## Evidence and counting

- Three new serial local measurements; four unchanged original/draft measurements reused with their real earlier timestamps. One further reflection candidate was rejected by the pre-score fidelity gate, with no invented result or execution receipt. Exact input and native-result hashes bind each review. No new commercial scan, paid service or hosted inference; all 179 earlier commercial observations remain available.
- Support email: initial draft plus two new revisions, 2/3 revisions used. Reflection: one inherited pre-freeze fidelity repair plus two new revisions, 3/3 used. The undocumented pre-repair text is not fabricated as a snapshot. Repeated reviews of unchanged text do not count as rewriting cycles.
- Source-to-r1 decisions and closure are explicitly reconstructed now from preserved writer records and current review, not claimed as an earlier automated loop. r1-to-r2 and r2-to-r3 are actual current feedback/revision/review steps. All four accepted r1 findings are closed. The email loop is complete. The reflection loop records a budget stop with the rejected r3 modality finding still visible, and selects the already closed r2 candidate. It does not falsely call the rejected latest attempt complete.
- The reviewer was separate from the writer, then saw its earlier findings during follow-up. This is same-model separate-context review, not fresh blind review on every round, human ratings, representative accuracy or an untouched holdout.
- Timing limitation: support r2 scoring began after the reviewer communicated approval with the exact candidate hash, but its complete prescore JSON was saved about 15.5 seconds after the native timestamp while inference was running. Neither timestamp is altered. That one pre-score assessment order rests on reported agent communication, not an independently timestamp-proven frozen-file gate. Later scans began after their prescore files existed; [exact note](scoring-readiness-notes.json).
- Full session manifests, native results, pre-score reviews, anchored whole-document ledgers, triage, exact resolution links and final statuses are in [cases/](cases/). [Protocol](PROTOCOL.md), [code audit](code-audit/code-audit.md), and [release audit](release-review.md) describe the checks and their limits.

The exact [v1.9 skill](retained-skill/) and earlier evidence remain intact. Model weights, calibration, English score interpretation and Korean editing guidance did not change.

The English composition reference now carries the reusable lessons from these actual findings: expectation and hope preserve different mental stances; an additive `either` must not falsely frame a compliant action as an earlier breach. These contextual checks supplement the general fidelity rule without a banned-word list or a new style quota.
