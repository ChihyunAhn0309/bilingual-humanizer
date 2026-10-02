# Offline detector-result bundle

This schema records actual user-provided or authorized tool results. The checker does not call any service. Never invent receipts to populate it. The following example is a **synthetic schema illustration**, not a scan, vendor recommendation, or established pass threshold.

```json
{
  "schema_version": 1,
  "targets": [{
    "id": "chosen-detector",
    "required": true,
    "service": "Selected service",
    "model": "unknown",
    "settings": {"language": "ko", "mode": "document"},
    "metric": "ai_probability",
    "unit": "fraction",
    "operator": "lte",
    "value": 0.1
  }],
  "results": []
}
```

An empty results list produces `incomplete`. For a completed check, add one object per target with these fields:

| Field | Required value |
| --- | --- |
| `target_id` | Corresponding target ID |
| `status` | `ok`, `error`, `unsupported`, or `pending` |
| `input_sha256` | SHA-256 of exact candidate file bytes checked |
| `service`, `model`, `settings`, `metric`, `unit` | Match the agreed target; use `unknown` for an unexposed model |
| `checked_at` | ISO 8601 timestamp with timezone |
| `scope` | `whole_document` for a whole-document target |
| `eligible` | `true` only when the product accepts this input language/length/type |
| `origin` | `user_report` or `tool_result` |
| `evidence` | Actual report/receipt reference or user-message provenance; no credentials |
| `value` | Original returned label or numerical value in the stated unit |
| `value_is_exact` | `true` for numerical comparison only when not a rounded, censored or estimated value |

For errors or pending checks, `target_id` and `status` suffice. Retain diagnostic detail in the working receipt record. `label` uses operator `eq` and a literal documented classification; `fraction` (0–1) and `percent` (0–100) use `lte` or `gte`. Do not relabel a score to fit this schema. If a report only displays a rounded or suppressed value, keep the numeric target unresolved or use its documented category where applicable. Different service metrics are never averaged.

Run:

```text
python scripts/check_detector_report.py actual-results.json final.md --output target-status.json
```

Exit 0 means all required configured targets are met **according to the supplied data**. Exit 1 means at least one is unmet or incomplete. Exit 2 means malformed input or I/O error. Unknown and duplicate target IDs are invalid. Settings, eligibility, scope, receipt provenance and candidate-hash mismatches prevent a pass. Optional targets remain visible but do not gate required targets.

The script cannot authenticate reports, prove that a website received the hashed bytes, or evaluate the semantics of a vendor's labels. The agent must check those against the actual tool output or user-supplied evidence. If submitting text through a UI normalizes line endings or uses only an extract, keep the submitted artifact and transformation record; do not claim the original full file was checked. The utility is not an AI detector, a rewriting model, or proof of human authorship.
