# Independent v1.5 evidence audit

Audit date: 2026-10-02. Scope: the prepared public repository, its two READMEs, v1.5 report/records/receipts, referenced provenance and blind-review records, and the earlier v1.4 baseline. No public files were changed.

## Finding

- **P2 — Publish resolvable baseline paths in the blind mapping.** `benchmarks/2026-10-02-v15/blind-mapping.json` lines 8, 14, 28 and 38 refer to `work\\commercial-test\\corpus\\...`, which does not exist in the public package. Replace these with `../2026-10-02/corpus/<case>-v14.txt`, relative to the mapping directory, and preferably use forward slashes throughout the mapping. All four corresponding public corpus files exist and their SHA-256 values match the mapping, so this is a packaging defect rather than a score or identity mismatch.

## Verified

- `python benchmarks/verify_evidence.py` passes: 36 earlier observations and all 28 new observations have matching input/receipt hashes. The new submission hashes and native AI scores agree with the retained receipts.
- Supplementary Human/Mixed/AI-refined percentages, GPTZero Basic versus Advanced labels, exposed GPTZero/QuillBot model versions, and all 28 observation dates are consistent with the receipt metadata. No new record claims truncated input.
- The report's development comparisons match the v1.4 and v1.5 records. Final English cache results are Sapling 94.6%, GPTZero Basic 100%, and QuillBot 24%. The 88.2% Sapling result belongs to the earlier candidate. The final candidate changes only the documented fidelity wording, and its hashes match its final receipts.
- The blind preference mapping yields v1.4 in five cases and v1.5 in one, matching both READMEs and the report. The English-cache blind comparison concerns the pre-repair candidate, which the report's repair account explains.
- Holdout source hashes, word/character counts and recorded generation date agree. All 20 frozen skill-file hashes match the prepared package. The manifest contains 19 unique pinned repository entries, with internally consistent commit URLs and retrieval/commit dates.
- The report and READMEs disclose worsening scores, mixed holdout outcomes, adaptive development, synthetic authorship, absence of human/cross-model validation, and the lack of demonstrated general improvement. No material score overclaim was found.
- A textual scan of the prepared public repository found no account emails, recognizable credential patterns, or identifying local user paths. Public GitHub identities and synthetic example names were not treated as leaks.

## Scope limits

This is local evidence and publication-claim consistency review, not authentication of vendor outputs, verification of upstream GitHub history, proof of independent execution/blinding, or a scientific validation of detector accuracy. QuillBot input linkage depends on the recorded agent observations, as disclosed. No private browser/auth state or unpublished work-folder sources were inspected. Binary images/PPTX content and live account balances were not inspected in this pass.

Verdict: no score, hash, or material claim blocker found; fix the four public mapping paths before publication.

## Final mapping recheck — 2026-10-02

The packaging finding is resolved. All 12 public A/B mapping paths now use forward slashes, resolve to existing files, and match their recorded SHA-256 values. The four development baselines correctly reference `../2026-10-02/corpus/<case>-v14.txt`.

Final verdict: no unresolved findings within this audit's stated scope.
