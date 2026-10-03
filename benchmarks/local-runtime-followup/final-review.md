# Independent audit of the English runtime follow-up

2026-10-03. **No actionable findings remain within this bounded audit.** This is a separate-context AI evidence review, not a human evaluation, authorship certificate, accuracy study, or guarantee of runtime stability.

Scope: `benchmarks/local-runtime-followup`, `benchmarks/verify_local_runtime_followup.py`, and the newly inserted English/Korean README summaries in `outputs/github-repo`. The reviewer ran no inference, edited no model or repository file, and did not repeat the earlier prose-fidelity review. The prior fidelity result remains applicable because the original and EN1 bytes match their earlier archived hashes.

## Validation performed

`py -3.13 -B -X utf8 benchmarks/verify_local_runtime_followup.py` passed with:

> PASS: 3 English successful measurements on 2 texts, 2 complete reviews, adapter compatibility and unchanged earlier failure.

The verifier checks frozen evidence hashes, the existing adapter's native English contract, all four class values, exact inputs, successful execution records, whole-document scope, final ledger/index/quote/coverage consistency, and equality between the imported EN1 and separately executed adapter results. It uses `validated-final.json` for the current ledger. Earlier `validated.json` and `analysis.html` remain preserved history; their presence is not treated as final validation.

Additional direct checks confirmed native, normalized-feedback and result-registry timestamps agree for all three runs; imported execution-record hashes match; each native output has one window covering all 153 model tokens; both current reviews cover 4/4 paragraphs with none excluded; and their measured timestamps match the native results. The input hashes are:

- Original: `a15af3a012825dd0ff18c1fc9eb67e58e0e4a53a9f05963c186f053bc295d184`.
- EN1 and the adapter rerun: `728fe7cabb22fea96dadb4678e7e6b52b361299b9c5f65f5a2f9c96aea05abff`.

All 27 released humanizer skill files match the existing release hash manifest. The earlier English failure input, feedback and execution receipt still match their frozen hashes. The later successful measurements have not replaced those failures.

## Results, units and provenance

| Text | Human % | AI % | AI-edited % | Humanized % |
| --- | ---: | ---: | ---: | ---: |
| Original | 0.083031 | 99.643207 | 0.011131 | 0.262634 |
| EN1 | 0.323491 | 98.873353 | 0.045136 | 0.758016 |

These displayed percentages equal the native 0–1 class outputs multiplied by 100. Humanized remains separate from Human. The exact Human values are 0.08303148206323385% and 0.3234913805499673%, a change of **0.24045989848673344 percentage points**. The report and README rounding is correct. Both are below 50%; the registry marks the selected Human >=50 targets unmet. No accuracy gain, universal detector acceptance, or historical human authorship is claimed.

The two imported runs are labelled `detector_repair_session`, preserve their original measurement times and distinct execution proofs, and explicitly say normalization was not a new adapter invocation. The third is labelled `humanizer_adapter`, has a completed index/score execution receipt, and returns exactly the same four class values as imported EN1. Thus the reported **three successful runs on two exact texts** is accurate and is not presented as three independent accuracy samples.

All three receipts identify the unchanged model revision and pinned weight hash, supervised success, and the `pread` loading backend. The report appropriately limits the Windows workaround to the reproduced failure and distinguishes runtime repair from calibration or model-quality improvement. This audit assesses saved receipts and their consistency; it does not independently certify the upstream repair or every execution environment.

## Review and stopping decision

Both final ledgers preserve the supplied synthetic provenance and the uncalibrated, experimental scope of the four-class outputs. The report accurately describes the reviewer as a follow-up reviewer rather than a new blind review. The source's denominator wording was already clarified by EN1; the final review records no additional concrete reader defect.

The deletion-effect arithmetic also agrees with the native records: EN1's P2 and P4 changes are approximately 8.477244 and 14.071854 percentage points. Those paragraphs are unchanged text, and the report describes context sensitivity instead of assigning a paragraph authorship probability or recommending deletion. Retaining the faithful EN1 while reporting an unmet detector threshold is coherent with the stated stopping rules.

Reviewed verifier SHA256: `9711e83ea96accc58216b27a46440b1b4ed02e4d7ca828206fd0f094108164cb`.

Reviewed result registry SHA256: `e45c8b83e6b15b9a6af53b7ecf6bbca2b18492a134827729c9cd1a4445c98a0f`.
