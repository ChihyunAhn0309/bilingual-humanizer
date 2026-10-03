# Publication package and evidence audit

Date: 2026-10-03. This is a **follow-up to my earlier text and instruction review**, not a new blind evaluation. I inspected the current publication files under `outputs/github-repo`, read the saved observations and receipts, and ran offline consistency checks. I used no network, browser or publication tools and changed no existing package files. This report is the only file I wrote.

## Outcome

The inspected current scores, input identities, retained versions and observation totals are consistent. One material reporting omission was found and repaired during this audit: the Korean final's GPTZero short-text warning was initially absent beside its highlighted improvement. I verified the correction in the current English README, Korean README and feature-trial report and reran the integrated evidence check successfully.

One small verifier coverage gap was reproduced, repaired by the author and verified: the continuation-G document summaries were not fully compared with their underlying records. The actual metadata already agreed; the finding concerned what a later inconsistent edit could escape, not a false measurement in this archive. **Both findings are closed; no remaining actionable inconsistency was found within this audit's scope.**

## Scope and executed checks

Read: both READMEs; continuation-G current and preserved Cloud reports/results; feature-trial report, results, observation JSON, receipt text, frozen manifest and release manifest; the three new or modified verifier files (`verify_evidence.py`, `verify_continuation_g.py`, `verify_current_observations.py`); relevant retained-version/checkpoint verifiers; and the current skill identity against the candidate I reviewed earlier.

I ran `python -B benchmarks/verify_evidence.py` from the package root before and after the reporting correction. Both executions passed every invoked verifier. After the verifier correction I reran `verify_current_observations.py` and three in-memory mutation checks; the valid package passed and all three inconsistent summaries were rejected. I separately recomputed the observation counts, compared the current and previously reviewed skill inventories, checked the complete v1.5.1 retained inventory, compared Cloud/current final identities and all duplicated continuation-G summary fields, and matched vendor text paragraphs against their UI receipts. These were read-only checks. I did not rerun the 45-test unit suite, whose tests create temporary files, and do not present its earlier result as a fresh test performed in this audit.

| Archive | Completed records |
| --- | ---: |
| 2026-10-02 | 36 |
| 2026-10-02-v15 | 28 |
| additional-trial | 17 |
| deeper-trial | 32 |
| renewal-trial | 34 |
| continuation-e | 7 |
| Earlier subtotal | **154** |
| continuation-g | 8 |
| feature-trial | 4 |
| Total | **166** |

The two commercial rewrite trials and their vendor self-scores are correctly excluded. The aggregate is a count of archived observations, not distinct documents, human-authored controls or independent services.

## Findings and repair history

### A1 — Medium; repaired and verified: short-text warning omitted from the featured comparison

Initial paths: `README.md`, `README.ko.md`, and `benchmarks/feature-trial/REPORT.md` highlighted Korean GPTZero Human **16% → 98%** without mentioning that the final crossed the product's warning boundary. The nearby short-text caveat originally described only continuation G.

Evidence:

- `benchmarks/feature-trial/receipts/feature-korean-final-g.txt` contains `This text is under 100 words`, `Your result may be less accurate`, and `Text up-to-date 386 characters • 98 words`.
- `benchmarks/feature-trial/receipts/feature-korean-original-g.txt` contains `Text up-to-date 407 characters • 101 words` and does not contain the short-text warning.

The scores themselves were transcribed correctly, but omitting this difference next to the main improvement could encourage an overconfident comparison. The author added the 101/98 displayed word counts and final-only warning immediately beside the result in both READMEs and in the feature report. I read the updated text and confirmed that the refreshed frozen manifest passed. This finding is closed. The different warning conditions do not prove that length caused the score change; the corrected text appropriately treats them as a limit on interpretation.

### A2 — Low; repaired and verified: duplicated summary metadata was not reconciled

Path: `benchmarks/verify_current_observations.py`, the `if directory == 'continuation-g'` document-summary loop, originally lines 56–64.

The loop compared vendor, input path/hash, score and target status, but did not compare the summary's `status`, `metric`, `model`, `observed_at` or `receipt` against the selected `records` row. I reproduced this without touching disk: I loaded the module with `runpy`, patched `Path.read_text` only in memory to give the first document summary an incorrect `model`, and called `verify('continuation-g', 8)`. It still printed PASS. This is a narrow consistency-check gap, not a vendor-authentication claim.

My separate current-data comparison found **no actual mismatch** in `status`, `metric`, `score`, `model`, `observed_at` or `receipt`, and confirmed four unique document summaries with eight unique vendor/input pairs. The author then added comparisons for all six duplicated fields and an explicit `threshold == '>=50%'` check. I inspected the updated loop, reran the current-observation verifier successfully, and repeated the in-memory test for three separate corruptions: model, receipt and threshold. All three were rejected with an assertion. No disk data was changed by these tests. This finding is closed.

## Confirmed identities, versions and interpretations

- The current skill has **24 substantive files**, excluding ignored Python caches. Every byte hash matched both the current release manifest and the candidate skill reviewed in my preceding assessment. Its version is **1.6.0**. There is no unreviewed skill change hidden behind the current detector results.
- The retained v1.5.1 directory has exactly **22 substantive files** and its complete inventory matches the archived manifest. The integrated prior verifiers also passed the old evidence and checkpoint links. The READMEs distinguish the current v1.6.0 release from the earlier v1.5.1 decisions; the current continuation-G results label the prior release as `production_release_at_cloud_trial`.
- All four continuation-G final path/hash pairs equal the preserved Cloud result pairs. The 17-file frozen manifest passes byte-length and hash verification. Current measurements are separate from `results-cloud.json`'s historical pending state; the latter must be read as the preserved Cloud snapshot, not current access status.
- Continuation G's GPTZero Human values are **0, 0, 1, 6**, while QuillBot Human-written is **100** on each exact same final. No final meets both native >=50 criteria. The saved model labels and Korean warnings support the current report. QuillBot's displayed remaining quota descends **3, 2, 1, 0** across the four measurements.
- Feature-trial GPTZero values are **16 → 98** for Korean and **0 → 0** for English. Timestamp order confirms finals were checked before originals. The expected language-specific model labels match within each pair. Missing QuillBot checks are explicitly pending, not passed; there is no paired v1.5.1 release comparison or supported universal improvement claim.
- The published independent text review is byte-identical to my preceding report. HIX and Undetectable inputs and outputs match their recorded hashes. Their receipt paragraphs support the saved outputs and vendor self-assessments. The HIX seven findings and Undetectable two low-severity findings are represented consistently. Neither vendor result is counted as an independent detector test or promoted into a retained checkpoint.

## Evidence limits retained in this audit

The new GPTZero/QuillBot receipt excerpts contain result panels, not a full independent reconstruction of the editor's input. Input identity is bound by local hashes and the agent's recorded DOM-verification assertion. I confirmed those local links, but cannot independently replay the original browser check from these excerpts. The continuation-G report already distinguishes agent-observed checks from signed vendor attestations. The vendor rewrite receipts expose their input/output text, so those paragraphs can additionally be compared offline.

The scripts establish the documented local consistency properties; they do not authenticate vendor servers, prove semantic equivalence, establish human authorship or prove general detector performance. No new detector estimate or external measurement was generated in this audit.
