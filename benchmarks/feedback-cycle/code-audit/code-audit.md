# Independent feedback-cycle code audit

The final reviewed implementation has no remaining actionable findings within this audit's structural scope. All five identified gaps were repaired and independently rechecked. The feature file hashes in `code-audit-results.json` identify the exact reviewed version.

## Scope and method

Reviewed `skill/scripts/feedback_cycle.py`, `skill/evals/test_feedback_cycle.py`, `skill/references/feedback-cycle-record.md`, `skill/references/local-detector-loop.md`, `skill/references/iterative-review.md`, and `skill/SKILL.md`. Also inspected the normalization adapter and installed detector evidence schema to check contract compatibility.

The audit used synthetic and saved JSON/text records only. It made no model inference, network request, document rewrite, or change to the feature implementation. Full probe fixtures and logs remain in the development workspace at `work/feedback-cycle/code-audit`; the public evidence bundle includes this report and summary JSON, while the packaged `evals/test_feedback_cycle.py` contains regression tests. The fixture suite was guarded against unexpected real subprocess execution.

## Findings repaired

| Finding | Original reproducer | Verified result after repair |
| --- | --- | --- |
| An accepted `revise` could close on byte-identical text by shortening the exact after quote. | `unchanged_resolved/session.json` | Rejected: accepted revisions require changed candidate bytes and different exact quotes. |
| Review-only duplicates consumed revision allowance and could establish a two-revision plateau. | `review_only_budget/session.json`, `review_only_plateau/session.json` | Both false stops rejected. In-progress versions report zero actual text revisions. |
| A review could assert fabricated `authorship_probabilities` while passing native-score validation. | `fabricated_authorship_probability/session.json` | Rejected. The standardized review field must explicitly be null. |
| A carried finding's after span could be unrelated to its linked current finding. | `unrelated_carried_anchor/session.json` | Rejected. The after span must overlap each linked carried finding. |
| An older positive review could restore a high-scoring exact-text candidate whose later review found an open defect, meaning loss, or reader failure. | `post-fix/same_hash_later_finding/session.json` and `observed.json` | Selection uses the latest review eligibility for each exact candidate hash. Later meaning loss removes the text from both delivery and faithful pools; open findings and reader failure remove delivery eligibility. Original exact-input score receipts remain preserved. |

The original first-failure fixtures, `probe_cycle.py`, and `probe-results.json` remain byte-for-byte unchanged. Because those fixtures predated the required `authorship_probabilities: null` field, their untouched copies now reject at that schema check. Separate copies under `post-fix` add only the missing null field before rerunning each targeted regression, so the intended fixes were verified independently of the new schema requirement.

## Additional verification

- Ran 61 feature/adapter fixture tests: zero failures, zero errors, one skip because an optional saved Korean baseline was absent. The live installed Korean inference test was explicitly excluded.
- Confirmed one documented inherited repair plus two newly recorded text revisions consumes the existing three-revision ceiling. A further revision rejects; missing prior provenance rejects. Historical usage cannot supply missing plateau evidence.
- Confirmed existing exact-input receipts retain their timestamps and hashes. This is a record-preservation check, not a claim that synthetic fixtures represent real execution.
- Confirmed the highest faithful checkpoint may remain open while the lower-scoring, repaired candidate is selected for delivery.
- Confirmed contextual review can close a prior `unresolved` finding without an artificial edit, while an accepted `revise` still requires changed text.
- Confirmed the docs distinguish reconstructed history and reused measurements from newly performed review/model work.

With the complete development workspace available, reproduce the post-fix checks from its root with:

```text
py -3.13 -B -X utf8 work/feedback-cycle/code-audit/verify_after_fix.py
```

Public machine-readable summary: `post-fix-results.json`; original failure summary: `probe-results.json`. Additional development-workspace artifacts are `code-audit-results.json`, `post-fix-tests.log`, and the first-stage repair results `post-fix-before-selection-fix-results.json`.

## Interpretation limit

This verifies saved-record structure, score/hash bindings, explicit finding continuity, stop accounting and selection eligibility. It does not establish the truth or completeness of a review, authenticate past execution, evaluate detector accuracy, certify human authorship, or prove that a reader problem was semantically repaired. Those distinctions remain explicit in the implementation and instructions.
