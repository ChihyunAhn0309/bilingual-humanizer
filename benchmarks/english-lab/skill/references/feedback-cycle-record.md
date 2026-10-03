# Saved feedback-cycle records

Use `scripts/feedback_cycle.py` when a substantial rewrite needs a resumable audit trail. It checks saved records; it neither rewrites text nor calls a detector, model, API, or reviewer. The writer still interprets feedback and reviews meaning. A structurally valid record does not establish semantic truth, reviewer independence, authentic model execution, or human authorship.

Create the session directory in the task workspace. Freeze the original source once. Keep every candidate, native result, adapter feedback, and completed review as a separate file. Do not edit earlier artifacts to make a later validation pass. Preserve the initial revision ceiling across resumed turns; any increase requires the user's explicit instruction, including the old and new limits and cumulative use.

For resumed work, preserve reused native receipts byte for byte with their original timestamps. Disclose which reviews were performed earlier and which judgments are reconstructed now. A retrospectively assembled manifest cannot establish that source feedback preceded an inherited draft or that an independent resolution loop happened earlier. Do not rerun or rewrite authentic receipts to conceal that timing distinction.

## Record format

The manifest is UTF-8 JSON, version 1. Every file reference is an object with `path` and `sha256`; hashes are SHA-256 of exact file bytes, including BOM and line endings. Paths resolve relative to the manifest's directory and must stay inside it, including after resolving symlinks. Absolute paths are permitted only within that directory. JSON artifacts must be objects.

| Manifest field | Meaning |
| --- | --- |
| `schema_version` | Integer `1`. |
| `language` | `ko` or `en`, fixed across the session. |
| `source` | Reference to the immutable original UTF-8 snapshot. |
| `revision_limit` | At most 3 revisions after the initial draft by default; a smaller user limit wins. Omitted means 3. |
| `budget_authorization` | Exact explicit user instruction for a limit above 3. Also record any authorized increase and its previous limit here. The helper cannot authenticate user authorization or recover overwritten manifest history. |
| `prior_revisions_used` | Nonnegative integer, default 0, recording documented repairs used before the first frozen draft in this manifest. These consume the same existing revision allowance. |
| `prior_revision_note` | Required when the prior count is positive: identify the actual writer/reviewer record and repair, distinguishing reconstructed history from newly recorded cycles. |
| `rounds` | Ordered source review, initial draft, then zero to three revisions within the existing limit. |
| `stop` | Object with `reason` and nonempty `detail`. Reasons: `in_progress`, `complete`, `plateau`, `budget`, `resource`. Explain remaining issues and the next action or limitation. |

Each round has:

| Round field | Meaning |
| --- | --- |
| `id` | Unique nonempty round identifier, such as `r0`. |
| `candidate` | Exact candidate file reference. The first round must match `source` byte for byte. |
| `native` | Native `model-result.json` reference, or `null` when unavailable. A failed artifact can be preserved here but cannot supply scores. |
| `feedback` | Reference to the corresponding `local_feedback.py` feedback JSON. |
| `review` | Reference to `evidence.py validate` output: schema 2, `anchored_explanation`, exact candidate hash and findings, all paragraphs reviewed, all six document dimensions assessed. |
| `fidelity` | `{ "eligible": true, "reason": "Source comparison findings...", "source_sha256": "original file hash" }`. Use `false` for unrepaired meaning loss or fabrication. |
| `reader` | `{ "eligible": true, "reason": "Reader review findings..." }`. Assess the entire candidate, including transitions. |
| `triage` | One entry per review finding: `{ "finding_id": "F1", "decision": "revise", "reason": "Concrete reader problem and protected meaning..." }`. Decisions are `revise`, `retain`, or `unresolved`. Use `[]` when there are no findings. |
| `followup` | Outcomes for every actionable finding in the immediately preceding round, keyed by both parent round and finding ID. The source round uses `[]`. |
| `improvement` | Boolean declaring whether this revision provides a defensible editorial improvement. Source review may use `false`. |
| `improvement_reason` | Nonempty editorial explanation. This judgment is separate from any numerical change. |

All findings are triaged, including human-compatible findings that are retained. A finding ID has meaning only within its round. Do not rename or omit an open finding to make it disappear. New findings in a rescored draft receive new triage and can require another revision.

A `followup` entry has this shape:

```json
{
  "parent_round": "r1",
  "finding_id": "F2",
  "status": "resolved",
  "reason": "The follow-up review checked the revised passage against the source and found the stated problem repaired.",
  "before": {"start": 0, "end": 15, "quote": "Prior sentence."},
  "after": {"start": 0, "end": 17, "quote": "Revised sentence."},
  "finding_ids": []
}
```

Offsets are zero-based Unicode codepoints, end-exclusive, matching `evidence.py`. Use exact spans of the previous and current candidates. The before span must overlap the parent finding. Larger context can anchor a moved, split, combined, or deleted passage; record surrounding surviving text for deletions. The example above illustrates the schema, not evidence for a real manuscript.

For `resolved`, use an empty `finding_ids` list and a follow-up review reason. An accepted `revise` additionally requires changed candidate bytes and different before/after quotes; selecting a shorter quote of unchanged text cannot close it. Merely recording `applied` cannot close it. If the problem persists, use `status: "carried"` and link to one or more current review findings with `revise` or `unresolved` decisions. The after span must overlap every linked finding; larger surrounding context is allowed. Those findings must receive another outcome in the next round. A prior `unresolved` finding may close without a text change when a documented contextual review resolves it. Do not accept a revision prematurely when retaining the passage may be justified.

Every round needs fresh feedback and review artifacts even if a candidate's text is unchanged. A changed candidate invalidates earlier whole-document scores and review; update the actual evidence before recording it. The helper rechecks exact hashes, spans, review coverage and links, but cannot judge whether the claimed repair is persuasive.

## Scores and unavailable results

Completed feedback is normalized again through the unchanged `local_feedback.normalize` contract and compared with the saved adapter result and native result hash. English retains Human, AI, AI-edited and Humanized separately; Human is never `100 - AI`. Multiple English windows preserve unavailable document probabilities. Attached review measurements must match the native identity, timestamp, calibration, classes, limitations and cautions.

The validated review must explicitly retain `authorship_probabilities: null`, as emitted by the detector evidence validator. Its analytical review cannot introduce a separate invented authorship probability.

When scoring fails or is unavailable, preserve a real error receipt or an explicit unavailable feedback record with `input_sha256`, `status: "unavailable"`, `reason`, `human_percent: null`, and `native_class_probabilities: null`. Use `native: null` if no artifact exists. Complete and validate the review without attaching model output. Unavailable numbers never become an estimated score or successful target result. Keep an actual failure reason; a formatting workaround is not a model run.

## Selection and stopping

`selected_candidate` is the highest native document Human candidate among snapshots that are faithful, reader-eligible and have no actionable findings. A reviewed source can be recovered if it qualifies. With no numeric values in that eligible pool, selection is the latest eligible snapshot and the value remains null. Equal scores keep the earlier checkpoint. `best_faithful_checkpoint` is tracked separately and can have unresolved editorial issues or fail reader eligibility; it is not automatically a finished manuscript. Neither selection can include an unrepaired semantic error marked fidelity-ineligible.

For identical candidate bytes, the latest review's fidelity, reader eligibility and open findings govern both selection pools. A later finding cannot be bypassed by choosing an older closed review of the same text. Each selected/checkpoint record identifies `eligibility_review_round`; it may retain an earlier native score for those exact bytes, while its eligibility reflects the latest review. All original scores and historical review states remain unchanged in `rounds`. A later fidelity failure removes that text from both pools; a reader failure or open editorial finding removes it from finished-candidate eligibility.

`complete` requires at least one actual changed draft with its own feedback/review, plus a faithful, reader-eligible latest round without open findings. Source review alone cannot establish loop completion. Only text changes after the initial draft count as new revisions; review-only unchanged snapshots cannot exhaust the budget or trigger a plateau. `revisions_used` adds `prior_revisions_used` to those actual changes. `plateau` requires two consecutive newly recorded text revisions declared without defensible improvement; historical repairs without their own records do not supply plateau evidence. `budget` requires the existing allowance to be consumed. `resource` records a disclosed external/runtime/session limit. Those stopped statuses remain distinct from completion and carry current open finding IDs. If the latest draft loses meaning, recover a faithful earlier candidate and report the limitation.

The output labels editorial improvement as `declared_reader_improvement`, and computes `human_change_percentage_points` separately when both neighboring native document values exist. A positive delta does not establish a reader benefit or authentic authorship. Required external detector thresholds remain governed by the existing report validator and are not implemented here.

## Commands

From the skill directory, after creating actual evidence and a manifest under `work/session`:

```text
python scripts/feedback_cycle.py work/session/session.json --out work/session/status-1.json
python scripts/feedback_cycle.py work/session/session.json --out work/session/final-status-1.json --require-final
python -m unittest discover -s evals -p test_feedback_cycle.py -v
```

On the inspected Windows environment, `py -3.13 -B -X utf8` can replace `python`. Each output must be a new file inside the session directory; existing files are never overwritten. Exit 0 means the record is structurally valid, including explicitly disclosed limits. It does not mean a score target was met. Exit 2 indicates malformed, stale or inconsistent records, a false completion claim, or `--require-final` with an in-progress session. When an output can be safely created, invalid input produces a JSON error status with no numerical score.
