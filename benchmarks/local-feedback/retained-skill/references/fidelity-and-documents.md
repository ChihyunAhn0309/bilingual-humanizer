# Fidelity and document handling

## Proposition comparison

For a dense document, make a compact working ledger of source locations and propositions. Track actor, action, object, time/status, quantities and units, scope and exceptions, confidence, causal force, attribution, and the location of each proposition in the rewrite. For a short paragraph this can be done mentally. The ledger is working material unless the user asks for it.

Compare propositions, not just strings. These are editing failures even if every number remains present:

- `A rose from 8 to 12 while B fell from 12 to 8` becomes the opposite allocation.
- `No evidence of harm` becomes `evidence of no harm`.
- `Up to 20%` becomes `at least 20%`.
- `20%` becomes `20 percentage points`.
- `120 ms median` becomes `120 ms mean`.
- `다음 달 출시할 예정이다` becomes `다음 달 출시한다` where certainty changes.
- `일부 참가자는 만족하지 않았다` becomes `참가자는 만족하지 않았다`.
- A citation moves from one finding to a different assertion.
- `이번 검토는 접수된 의견을 살피고 운영안을 구체화하기 전에 조건을 정리한다` disappears because it was treated as an introduction. Even if the conditions remain elsewhere, the stated remit and decision stage have been lost.

Preservation is not fact verification. If the source itself makes an unsupported claim, do not strengthen it. Preserve and flag a material concern, or verify it when verification is part of the task. Do not quietly replace it with a plausible fact.

## Offline surface checker

Run from the skill directory, substituting actual source and rewrite paths:

```text
python scripts/audit_preservation.py source.md rewrite.md --output audit.json
python scripts/audit_preservation.py source.md rewrite.md --protect-json protected.json
```

On Windows, `py -3` may be the available Python launcher. The script uses Python 3.10+ standard library only. A protection file is a JSON array of exact strings or an object with a `protected` array. Protect names, defined terms, exact clauses, or formulas that the automatic extraction does not understand.

The checker compares inventories of numeric expressions, number-and-unit spans, URLs, simple citations, inline/fenced code, quoted passages, and explicitly protected strings. It also flags selected newly added invisible or control characters. It writes source and rewrite SHA-256 values to identify the compared files. It never uploads content.

Exit 0 means no changes were found in the recognized surface features; exit 1 means review candidates exist; exit 2 means input/usage failed. **None means semantic fidelity or human authorship has been established.** Review every candidate against the source; valid reorganization can alter counts. Do not corrupt good prose to make a regex pass. Hashes identify these files, not who authored them or when their content was originally written.

Known blind spots include paraphrased quotations, spelled-out numbers, complex LaTeX, complex nested Markdown, referent swaps, logical scope, hidden comments and fields in office formats, and natural-language facts. The script does not parse an entire document format or run a trained language model. Mandatory semantic comparison supplies what string comparison cannot.

## Files and long documents

For text and Markdown, edit prose while preserving link targets, code, frontmatter, anchors, machine-readable fields, tables, and intentional structure. Table-cell prose may be edited when within scope; numeric data, formulas, keys, and row relationships remain protected. Maintain the user's requested copy-versus-in-place workflow.

For DOCX, presentation, PDF, HWP/HWPX, or other formatted sources, use a capable format-aware tool if available. Do not overwrite a binary file with extracted text. Preserve styles, headings, footnotes, captions, comments, tracked changes, equations, and references. Inspect a rendered result when the format supports it; reflow may change page count. If the required format cannot be edited, provide the revised text and say which layout or file operations remain undone.

Work section by section when a whole document exceeds the available context. Keep a shared terminology/voice ledger, citation map, and coverage list; include adjacent context so transitions remain coherent. Track all sections and reconcile them at the end. Do not call a partial extract a full-document rewrite. If extraction is incomplete, identify the unreadable sections.

Review-only requests return findings. Requested tracked revisions must use the format's revision capability; a plain replacement is not tracked changes. Author metadata or fabricated revision history must not be added as a claim of human authorship.
