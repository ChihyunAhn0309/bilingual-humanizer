# Independent publication audit: QuillBot renewal

Reviewed on 2026-10-03 in a separate AI-agent context after the evidence and publication prose had been assembled. This auditor did not write the candidate texts or conduct the commercial scans. Only this audit report was written by the auditor; the parent session made the reporting and verifier changes described below.

**Outcome: no release-blocking discrepancy found in the audited numerical and release claims.** The current README summaries and renewal report agree with the saved observations, exact-file links, model labels, original observation times and current packaged skill. Confidence is **high for local consistency**, with the submission-provenance limitations below. This is not vendor authentication, a new blind naturalness evaluation, a human review, or certification of historical human authorship.

## Scope and method

The audit covered the current v1.6.0 and QuillBot-renewal claims in both READMEs, `quill-renewal/REPORT.md`, `results.json`, `frozen-inputs.json`, all new observation/receipt records, the vendor records, the five writing/fidelity reports, and `verify_quill_renewal.py`. It followed the five earlier GPTZero links into `feature-trial` and `continuation-e`, checked the current skill against the saved v1.6.0 manifest, and inspected both local skill ZIPs. Paths below are relative to the repository unless stated otherwise.

I read the source, the two new local library rewrites, the raw vendor output and the repaired derivative to check that the report accurately describes the documented fidelity issues and repairs. I did not assign a new naturalness score or rerun a blind comparison. Historical README sections were read for context and their archived records were covered by the aggregate local validator; this was not a new external audit of every historical research, licensing, installation or diagram claim.

No browser, detector, payment, account-creation or publication action was performed by this auditor. The factual checks use the supplied local evidence, not model memory about the vendors.

## Verified claims

| Claim | Evidence and finding | Confidence |
| --- | --- | --- |
| Korean notice GPTZero 16% to 98%; QuillBot 100% to 100% | The four linked records and result panels agree. The original/final hashes match the earlier GPTZero files and current QuillBot files separately. GPTZero model is 4.1m; QuillBot is v6.2.1. | High for saved-record consistency |
| English memo GPTZero 0% to 0%; QuillBot 100% to 100% | The four linked records and panels agree, with GPTZero 4o and QuillBot v7.1.0. No QuillBot gain is shown. | High |
| Notice comparison crosses the GPTZero short-text boundary | Earlier receipts show source 101 words without the warning and final 98 words with `This text is under 100 words`. The warning is retained in the table and both READMEs. | High |
| Retained library E is 97% / 30% | Its GPTZero result retains its original time, `2026-10-03T02:26:29.092Z`; current QuillBot recheck is `2026-10-03T04:02:51.379Z`. Both are tied to SHA-256 `24ccfbae46622c5c5db7266f496dd478484a6b8963b9f2bc5c5f9f5ff7fa362c`. | High |
| New library readings are 47% / 14% and 61% / 17% | Native result panels, observation JSON and summaries agree. Their distinct input hashes are retained. GPTZero word counts are 249 and 252; neither panel contains the short-text warning. | High |
| Library source is 76% / 21%; repaired vendor derivative is 68% / 24% | The four second-period panels and exact-input links agree. The derivative is 8 points lower on GPTZero and 3 points higher on QuillBot than its source, and lower than retained E on both metrics. GPTZero is 4.1m and QuillBot v6.2.1. | High |
| Only the notice final meets both selected native Human >=50 thresholds | Independently recomputing the nine table rows gives exactly that result. This is limited to these two services and exact texts; it is not an all-detector or authorship claim. | High |
| Nine new QuillBot and four new GPTZero observations | There are 13 distinct new record IDs: 9 QuillBot and 4 GPTZero. The earlier five GPTZero links are not duplicated as new records. | High |
| The total is 179 external observations | Independent file counting gives 36 + 28 + 17 + 32 + 34 + 7 + 8 + 4 + 13 = 179. The first eight phases total 166. These are observations, including repeated checks, not 179 independent texts or successful rewrites. | High |
| First QuillBot period exhausted; second ended with five scans left | Chronological receipt quotas are 6, 5, 4, 3, 2, 1, 0, then 6 and 5. The seventh receipt says `No free AI scans left`; the last says five remain. The report does not claim the second access period was exhausted. | High |
| No cross-draft score merging | Each of the nine table pairs resolves to a single matching input-file hash. Earlier GPTZero dates remain earlier dates. E and F are described as separate checkpoints, and the 33% QuillBot result is not assigned to E. | High |
| The current portable skill remains v1.6.0 | All 24 distributable files match `feature-trial/release-skill-hashes.json`; the skill declares 1.6.0. Cache files are excluded. Both current skill ZIPs contain exactly those 24 matching files. | High |
| Review reports support the summary of three source reviews | The first report covers the v1.6.0 candidate, and the next two explicitly describe follow-up comparisons in the same separate reviewer session. The publication report correctly distinguishes these from new blind reviewers and from human review. | High for the saved reports; session conditions are reported, not independently reconstructed |
| Raw commercial output was distinct from the tested repaired derivative | Raw output and repaired input have different hashes; no new detector record uses the raw output hash. The raw output visibly weakens duties and changes the unresolved volunteer condition. The repaired file restores these items and is correctly labelled commercial output plus local editing. | High |
| Undetectable self-score is excluded | The saved UI shows 50% `AI / GPT`; metadata calls it a vendor self-score, sets the independent detector score to null, and the result count contains no such record. Whitespace-normalized full source and full raw output are both present in the saved UI excerpt. | High |
| QuillBot Humanizer showed a 125-word free limit and no Korean in the visible selector | The limit panel says `134/125 words. Limit exceeded.` and requires an upgrade; the language receipt lists the reported English dialects and other languages without Korean. These are dated visible-UI observations, not claims about every product tier or future support. | High for the displayed limitation; exact-input provenance is limited below |

The repaired library input has 245 whitespace-delimited words and its GPTZero panel reports 245; the source has 264 and its panel reports 264. Matching counts corroborate the records but do not establish exact submitted content.

## Findings and changes during the audit

1. **GPTZero input evidence was weaker than QuillBot's. Resolved as an explicit limitation.** The four new GPTZero receipts contain completed result panels, not the full input DOM. A source-file hash and `input_verified_in_dom: true` do not allow a third party to reconstruct that browser input. The parent added this limitation to `REPORT.md`; the final text accurately distinguishes the agent's contemporaneous comparison from a replayable saved DOM comparison. No new input snapshot was invented.

2. **The verifier originally treated the prior count as a constant. Resolved.** It now reads all eight earlier completed-observation result files and recomputes 166 before adding the new 13. Independent counting reached the same result.

3. **Vendor metadata originally lacked semantic cross-checks in this verifier. Resolved for the claimed saved fields.** It now checks source/output file hashes, the displayed Undetectable self-score and raw output, separation from detector records, and the QuillBot limit metadata against the saved panels. I also independently checked that the full normalized Undetectable source and raw output occur in the UI excerpt.

No score, source identity, native metric, model label, retained-checkpoint decision or packaged skill content needed correction as a result of this audit.

## Remaining evidence limits

- **QuillBot Humanizer blocked probe:** its saved limit receipt contains the limit/upgrade panel rather than the full English input. The metadata source hash matches the 134-word English source, and the UI count is 134, but exact submission identity relies on the recording agent's metadata. This probe is not counted as a completed detector observation and no restricted output is included.
- **Procedure claims:** the two rejected input preparations, the request to pause typing, login handoffs, absence of payments, writer/reviewer information restrictions and exact editing-turn counts are described in the local records. This audit did not independently replay complete execution logs, private account state or billing history. Those are reported workflow facts, not independently authenticated transaction evidence.
- **Review coverage:** the saved writing and fidelity reports support the stated findings; they do not make naturalness objective or prove that every semantic defect has been eliminated. The alternative and repaired-vendor reviews are follow-ups in one separate reviewer context. No new human or cross-model assessment was performed here.
- **Timing and integrity:** timestamps, hashes and before/after snapshots are locally recorded. Hash agreement detects inconsistency against the saved manifests, not coordinated alteration of records and manifests or vendor calculation errors. QuillBot's before/after DOM text is checked after whitespace normalization; it is not a vendor-signed byte-level submission certificate.
- **Validator coverage:** the script verifies machine-readable evidence and linked fields. It does not parse and prove every sentence in the Markdown publications, authenticate a scan, or infer naturalness. The prose/table comparisons in this audit supply a separate manual pass.
- **Scope of performance inference:** the library is an already-used development document; the notice and memo were generated in the prior phase. These results do not establish an unseen representative success rate or a general advantage over paid commercial products. The current documents state these limits.

The only unresolved local links found in the two READMEs and renewal report at audit time pointed to this forthcoming `publication-audit.md`. The publication step should copy this completed report to that linked location. This auditor has not verified remote publication.

## Checks executed

- `python benchmarks/verify_quill_renewal.py`: passed, before and after the parent corrections; 13 new observations and 9 exact-text pairs.
- `python benchmarks/verify_evidence.py`: passed, before and after corrections, covering all nine result archives and linked release/frozen-input checks.
- `python -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'`: 45 tests passed. The portable helper implementation did not change after this run.
- Independent Python reads: total counts, five earlier GPTZero receipt links, word counts, exact frozen-input inventory, vendor metadata hashes, normalized vendor source/output containment, local links and both ZIP member hashes checked.
- The parent supplied `work/quill-renewal/mutation-checks.json` reporting rejection of five corruptions: summary score, summary model, short-text warning, native panel score and submitted DOM text. I inspected that record and the corresponding verifier assertions; these five mutation executions were performed by the parent, not rerun by this auditor.

## Audited snapshot

These SHA-256 hashes identify the final source files read by this auditor. The audit report itself is intentionally not included in its own digest list.

| File | SHA-256 |
| --- | --- |
| `README.md` | `f42f5120173053324887df8fcf2d6d33e7514414d2927faa0fe38c467a907b20` |
| `README.ko.md` | `010b265c3f93f72415ebcf163f6a907ac3c29851d8f4b325e729ac377c477418` |
| `benchmarks/quill-renewal/REPORT.md` | `26529469d4a4e5279b61ebf87febe2c3d6213dd5bd4aa156ee058f325aa16289` |
| `benchmarks/quill-renewal/results.json` | `ffab4fb6e58165b02b6d5564f81a710c2577e69d42df5aea21b70a597dbc8000` |
| `benchmarks/quill-renewal/frozen-inputs.json` | `213de79345c07b2fe4cb8ae6e611c61ff4114b5ced7509f8f8f1e50d3b1819e2` |
| `benchmarks/verify_quill_renewal.py` | `df4b5c75db17813577bb71c31008ff90e27ecec10378432352d574ca73c22ae2` |
| `benchmarks/feature-trial/release-skill-hashes.json` | `710455d8adaa379a0d468dbc29dbd2cf9ab33488f7d076fce9b9e607f796fd05` |

The local `outputs/bilingual-humanizer-v1.6.0.zip` and `outputs/bilingual-humanizer.zip` both had SHA-256 `bc8304e69cdd419870eea0161ef40d08db703dcca1fac78e59bca3894a456084` and identical contents matching the release manifest. This independently establishes current package equality and retained release content; it does not reconstruct an earlier ZIP's byte identity without an earlier archived ZIP hash.
