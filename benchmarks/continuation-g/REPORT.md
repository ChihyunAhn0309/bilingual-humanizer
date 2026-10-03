# Continuation G: desktop commercial checks

Cloud task `task_e_6ac06a71ed9c83319e7a6e2f08f501eb` completed commit `1644484`. Its original [report](REPORT-cloud.md), [pending results](results-cloud.json), review and 17 frozen text files are preserved. Desktop checks below were performed on 2026-10-03 using existing free accounts; no money was spent.

| Exact final | GPTZero Human document probability | QuillBot Human-written text percentage |
| --- | ---: | ---: |
| English incident | 0% | 100% |
| English letter | 0% | 100% |
| Korean neighborhood notice | 1% | 100% |
| Korean exhibition review | 6% | 100% |

**None meets both native metrics >=50%.** QuillBot's text share is not GPTZero's document-class probability. The Korean GPTZero scans displayed an under-100-word accuracy warning. QuillBot displayed v6.2.1 for the incident and both Korean texts, and v7.1.0 for the letter; these are UI labels as observed, not inferred from language. GPTZero displayed 4o for English and 4.1m for Korean.

The four finals have no same-session QuillBot comparator measurements: the account's four remaining scans were used for these finals. Therefore this table is an absolute observation, not a controlled gain over v1.5.1. The previous best checkpoints remain unchanged. The account ended with zero free scans. Scores did not guide these already-frozen drafts.

[results.json](results.json) binds all eight agent-observed results to exact input and receipt hashes. Editors were checked before submission and after completion, whitespace normalized, against the frozen local inputs. GPTZero results had Text up-to-date; QuillBot results had no Outdated score. The saved receipt text and agent input checks are not signed vendor attestations. The document editor was reused, so its title may refer to an older sample rather than the input.

The original Cloud method and review supported a voice-preservation hypothesis but found fidelity errors that required repair. These detector observations do not justify promoting G as a detector improvement. Current release maintenance and optional editing controls are evaluated separately in [feature-trial](../feature-trial/REPORT.md).

Run `python -B benchmarks/verify_evidence.py` for old and new evidence checks. The new observation verifier checks metrics, hashes, sums, quota and freshness; it does not certify authorship or semantic equivalence.
