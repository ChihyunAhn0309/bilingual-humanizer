# Detector-first composition comparison — 2026-10-03

The released skill is **v1.8.0**, with 28 files. This adds an explicitly requested, bounded comparison of complete compositions after ordinary feedback-led editing plateaus. It does not raise the revision ceiling. The repaired **bilingual-ai-detector v3.1.2** completed all five new local runs with unchanged model identities, weights and class meanings. No commercial calls, hosted inference or payments were made.

**The all-detectors Human ≥50% objective remains unmet.** These are local model outputs on three synthetic sources, not probabilities that a verified person wrote the text. There was no new commercial test. The previous 179 commercial observations and their selected texts remain intact.

## Native Human outputs

| Case | Original source | Previous accepted local checkpoint | New complete alternatives | Retained native-score checkpoint |
| --- | ---: | ---: | --- | ---: |
| Korean library review | 80.115126% | 80.115126% | A: 91.462756% | 91.462756% |
| English archive memo | 0.083031% | 0.323491% | A: 0.641659%; B: 0.666012% | 0.666012% |
| Fresh English walking-guide reflection | 0.007394% | New source | A: 0.023042% | 0.023042% |

Korean increased by 11.347631 percentage points. The English archive best value increased by 0.342521 percentage points over its previous accepted local checkpoint; it is still far below 50%. A/B differ by only 0.024354 percentage points, with no demonstrated practical significance. Retain the candidate as the native-score checkpoint.

Full precision, timestamps, all four English classes, input/model hashes and native receipts are in `results.json` and each `*-score` directory. English Humanized and AI-edited were never counted as Human. The English model is experimental and uncalibrated, with high-confidence false positives in its recorded human-text pilot. Korean calibration covers a limited reference population: this business genre is outside the evaluated essay/abstract/poetry scope, and both library versions exceed the central training length range. Cautions are preserved beside the saved values.

## What changed in the skill

The editor declares a reader route and maps protected propositions before composing from the source. At most two meaningful whole-document alternatives may be compared within the remaining existing revision budget when the user explicitly requests stronger detector-oriented rewriting. Each alternative undergoes source-fidelity and reader review before scoring. No defect is invented just because Human is low. No character fragments, random synonyms, deliberate errors, fabricated experiences, translation or shortened-away facts are used as a scoring trick.

Native scores may rank eligible alternatives for the requested objective. The editorial selection and highest-scoring faithful checkpoint remain separate, and a worse or invalid candidate never silently replaces the retained text. The adapter itself is unchanged; its documentation now records successful v3.1.2 compatibility.

The Korean conditions-first route produced a meaningful local gain and a defensible reading benefit. The archive examples produced small gains. The fresh-source check and its tradeoffs are preserved; three synthetic sources do not establish broad effectiveness across genres, generators or detectors. The option is promoted as a tested workflow improvement, not as a proven universal detector bypass.

## Feedback and independent checks

- Detector-first source review preceded writing. The library and archive source reviews are preserved in the prior local-feedback/runtime-followup benchmarks; the new walking-guide source has its own full review here.
- The two archive alternatives and the library alternative passed a separate writer-independent review before their scores were requested. That reviewer had audited historical source evidence earlier; it was blind to new candidate scores, not history-naive about the original sources. See `independent-candidate-review.md`.
- A fresh-context writer applied the method to the new English source. Another fresh-context reviewer received only its original and final candidate plus fidelity guidance. It found no material loss but recorded a denser opening and a less distinct closing reflection. See `fresh-independent-review.md`.
- Every newly measured text has a whole-document detector review with exact anchored evidence, native class context and full paragraph coverage. Model deletion deltas are sensitivities, not paragraph authorship probabilities.
- The humanizer retained the Korean initial/later checking duties and separate notice/document duties despite weak repetition suggestions. The source-based decisions are in `ko-library/feedback-decisions.md`.
- These are AI-agent reviews in separate contexts, not human ratings or cross-model validation. No external fact-check or authorship certification was performed.

## Selection and reproducibility

[Independent final audit](release-review.md) found and prompted a consistency-check repair: the verifier now binds every normalized feedback field and the validated report's model identity, calibration, limitations and semantics to the native receipt. The corrected verifier accepted the valid fixture and rejected all 12 corrupted fixtures. [Negative checks](audit-work/negative-checks.json) and [release integrity checks](audit-work/integrity-checks.json) preserve the outcomes. The skill suite ran 81 tests: 80 passed and one optional development-baseline test was skipped. Skill metadata validation and the full historical evidence verifier passed. These checks establish artifact consistency, not authorship or universal prose quality.

`selection.json` records the cumulative budget and separates the native-score and editorial choices. Archive A remains the editorial choice for quickly finding extension conditions; the selected score checkpoint is candidate-b. The original fresh English reflection remains an editorial option because the independent reader found the reorganization a tradeoff, not an unequivocal improvement. No favourable values from different texts are combined.

The prior v1.7.0 skill is archived byte-for-byte in `retained-skill/`; historical release verification uses its original 27-file manifest. Current installation and packaging are checked against the new 28-file manifest. The full offline suite verifies historical evidence as well as this experiment. Re-running inference requires the separately installed trusted detector and its pinned local weights; the repository does not bundle those weights or invoke paid services.
