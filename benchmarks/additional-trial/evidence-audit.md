# Independent additional-trial evidence audit

Audit date: 2026-10-03 (Asia/Seoul). Verdict: **PASS for local evidence consistency; no blocking finding.** Retaining v1.5.0 is supported by the archived comparisons and review mapping. No detector requests were made and no public files were changed.

## Scope and method

Read the public `benchmarks/additional-trial` package, `verify_additional_trial.py`, `verify_evidence.py`, both public READMEs, the prior `2026-10-02-v15` records needed for cited baselines, and the public production skill. Executed `python outputs/github-repo/benchmarks/verify_additional_trial.py`: **PASS: 17 additional observations, frozen inputs and 20 unchanged production files.** The umbrella verifier was inspected but not executed because it also reads the earlier `2026-10-02` corpus outside this audit's scope.

Additional independent checks compared every observation to its receipt, rebuilt Sapling input from sentence receipts, matched blinded source/A/B copies to mappings, replayed all declared repairs, checked historical baseline identity, and compared the retained production manifest directly with the earlier v1.5 manifest and current public files.

## Verified observations

Scores below remain in each vendor's own units. GPTZero entries are AI/Mixed/Human classification percentages. QuillBot entries are AI-generated / Human-written & AI-refined / Human-written text percentages. Sapling and ZeroGPT entries use their respective AI-side metrics.

| Observation | Archived score | Archived model |
| --- | --- | --- |
| GPTZero English cache baseline | 100 / 0 / 0 | 4o, Basic Scan |
| GPTZero English cache trial | 100 / 0 / 0 | 4o, Basic Scan |
| GPTZero Korean library baseline | 32 / 24 / 44 | 4.1m, Basic Scan |
| GPTZero Korean library trial | 14 / 1 / 85 | 4.1m, Basic Scan |
| QuillBot English cache trial | 21 / 0 / 79 | 7.1.0 |
| QuillBot Korean library trial | 83 / 0 / 17 | 6.2.1 |
| Sapling English cache baseline | 94.6 | Not exposed |
| Sapling English cache trial | 90 | Not exposed |
| ZeroGPT Korean library trial | 100 | Not exposed |
| GPTZero English holdout baseline | 100 / 0 / 0 | 4o, Basic Scan |
| GPTZero English holdout trial | 100 / 0 / 0 | 4o, Basic Scan |
| GPTZero Korean holdout baseline | 94 / 0 / 6 | 4.1m, Basic Scan |
| GPTZero Korean holdout trial | 99 / 0 / 1 | 4.1m, Basic Scan |
| Sapling English holdout baseline | 93.7 | Not exposed |
| Sapling English holdout trial | 95.1 | Not exposed |
| ZeroGPT Korean holdout baseline | 100 | Not exposed |
| ZeroGPT Korean holdout trial | 100 | Not exposed |

- All 17 IDs are unique; there are nine development observations and eight fresh-source observations. All completed statuses, capture times, declared input checks, scores, metric labels, models, settings and other result fields agree between the index and per-observation receipts.
- All 17 input and receipt SHA-256 values match bytes on disk. All submission hashes match UTF-8 input after the declared trim-only transformation. All 13 frozen-input entries match.
- All eight GPTZero receipts contain Basic Scan and Text up-to-date markers, the recorded AI/Mixed/Human values and the recorded language-specific model. Displayed word and character counts match whitespace-normalized submitted inputs.
- Both QuillBot receipts contain the recorded model and all three class percentages, which sum to 100; neither contains Outdated score. The Korean receipt confirms one free scan remaining.
- All four Sapling receipts have `truncated=false`; their sentence text reconstructs the complete submitted input after whitespace normalization.
- All three ZeroGPT receipts contain the complete submitted text after whitespace normalization and the recorded 100% AI GPT result.

## Comparisons, reviews and retention

The two development baseline files are byte-identical to the prior final v1.5 candidates. Six relevant earlier observations and their receipt hashes were checked: GPTZero English final and Korean library, Sapling English final, QuillBot English final and Korean library, and ZeroGPT Korean library. They confirm the report's historical baselines and consistent exposed model labels. In particular, QuillBot Human 76% and 23%, and ZeroGPT 100%, are historical results and are correctly excluded from the 17 new observations. The repeated GPTZero and Sapling baselines equal the previous values.

Both report tables and the additional-trial notices in both READMEs agree with the records. English development changes are GPTZero Human 0 to 0, QuillBot Human 76 to 79, and Sapling AI 94.6 to 90. Korean development changes are GPTZero Human 44 to 85, QuillBot Human 23 to 17, and ZeroGPT 100 to 100. Fresh-source results show no beneficial change: English GPTZero Human 0 to 0 and Sapling AI 93.7 to 95.1; Korean GPTZero Human 6 to 1 and ZeroGPT 100 to 100. No cross-vendor average or common authorship probability is asserted.

All 12 blinded source/A/B files match their intended originals and mapped versions. Development A is the trial in both languages and is preferred in both reviews; holdout A is v1.5 in both languages and is slightly preferred in both reviews. Thus the published preference interpretation is correct. The four declared development repairs replay exactly from initial to reviewed files; the final recheck confirms the preference survives those repairs. The detector inputs are the repaired development files and the frozen holdout files. No material fidelity defect is reported by the archived reviews.

All 20 non-cache files in the public production skill exactly match both the retained manifest and the prior v1.5 frozen manifest, after normalizing path separators. The production entrypoint still declares version 1.5.0. The trial skill has a separate frozen identity under the benchmark directory. The public unchanged-production claim is supported. The plan's fresh-source promotion conditions were not met, so non-promotion is consistent with the recorded decision rule.

## Nonblocking recommendations

1. **Clarify GPTZero input linkage alongside QuillBot.** `additional-trial/REPORT.md:47` explicitly identifies QuillBot's reliance on the operator's input observation. The eight GPTZero raw receipts also omit the complete input; they preserve scores, model, freshness and counts. Those counts match, but they do not independently establish exact text identity. Extend the disclosure to GPTZero. This does not contradict the general local-consistency/authenticity caveat or change the comparison outcome.
2. **Optionally extend the reusable verifier to cover the extra checks above.** `verify_additional_trial.py:49-51` hashes the candidate paths in the mappings but does not compare the actual blinded copies; it also does not replay repairs, reconstruct Sapling inputs, or compare the retained manifest with the prior v1.5 manifest. All these checks passed in this audit. Encoding them would prevent future review-copy or provenance drift from escaping the standard command. This is hardening, not a current evidence mismatch.

## Limits

This audit verifies archived local consistency, not vendor authenticity, detector accuracy, human authorship, or a guaranteed future score. No vendor authentication is claimed. GPTZero and QuillBot exact UI input/result linkage ultimately relies on agent observations; receipt hashes authenticate neither the vendor nor the capture time. Capture ordering, pre-submission freezing, session isolation, and the absence of post-score edits are documented process claims rather than independently timestamped proofs.

The earlier report documents 36 original plus 28 v1.5 observations; 28 v1.5 and 17 additional records were counted here. The original 36 were outside scope, so the total 81 is arithmetically consistent but not fully recounted by this audit. The original package, live installed skill, account/payment history, and final GPTZero 6,242-credit balance were also outside scope. This audit therefore confirms public production files only, not the report's broader three-location or billing assertions. Synthetic-data provenance, same-host-model review limitations and the small, exploratory nature of the comparison are appropriately disclosed.
