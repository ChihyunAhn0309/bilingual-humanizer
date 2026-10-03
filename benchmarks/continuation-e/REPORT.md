# Continuation E/F: plain professional prose

2026-10-03 KST. Production stays at the exact v1.5.1 snapshot. This experiment improves one retained Korean document; it does not establish a generally better skill or meet the all-detector target.

## All new observations

| Exact input | GPTZero Human probability ↑ | QuillBot Human-written text share ↑ | ZeroGPT AI GPT ↓ |
| --- | ---: | ---: | ---: |
| [candidates/en-support.txt](candidates/en-support.txt) | 0% | 72% | — |
| [candidates/ko-library.txt](candidates/ko-library.txt) | 97% | 30% | 100% |
| [candidates/ko-library-f.txt](candidates/ko-library-f.txt) | 91% | 33% | — |

GPTZero used Basic Scan, model 4o for English and 4.1m for Korean. QuillBot displayed v7.1.0 for English and v6.2.1 for Korean. ZeroGPT did not expose a model identifier. These match the displayed comparator settings where applicable; observations occurred at different times and accounts. The native Human columns have different definitions and are never averaged. ZeroGPT's AI score is not converted into a claimed human-authorship probability.

## What was tested

E recasts institutional wording into ordinary professional prose while preserving the genre and the recipient's practical needs. A [separate reviewer](fidelity-review.md) found an overbroad evidence assertion and a narrowed notice obligation in the first Korean draft; both were repaired, and the explicit review purpose was restored. The reviewer reread both source/final pairs and found no remaining required changes. The English draft needed no repair. These were independent-context AI reviews, not human ratings.

The E library text improved from the prior checkpoint's GPTZero Human 93% / QuillBot Human-written 15% to 97% / 30%. Its ZeroGPT reading remained AI 100%. It replaces only this document's checkpoint. E support regressed from 0% / 83% to 0% / 72%, so the earlier support text stays selected.

After those four primary readings, the [plan](PLAN.md) was explicitly extended for the ZeroGPT comparison and one further Korean candidate, F, that groups procedural statements more tightly. Its separate [fidelity review](fidelity-review-f.md), original draft and one optional clarity repair are retained. F reached GPTZero 91% / QuillBot 33%: a trade-off against E's 97% / 30%, not an unambiguous improvement. F is retained as an alternative, without attaching E's ZeroGPT reading to it. This was adaptive development on reused sources, not a new-topic holdout, randomized trial or preregistered success estimate. No extra English variants were sampled after its regression.

The [checkpoint registry](checkpoint-registry.json) records exact retained files, alternatives and the original evidence for each. No scores from different documents are combined. The all-selected-detector target remains unmet: QuillBot 30% is below the inclusive 50% target for the retained Korean candidate; English GPTZero remains 0%; Korean ZeroGPT remains AI 100%.

## Access and evidence

The user supplied refreshed free detector access. GPTZero displayed 10,000 remaining credits at the beginning. QuillBot began with seven free scans; three completed scans consumed three and left four. GPTZero initially opened its Advanced results tab; the recorded observations are explicitly the completed Basic panel, and the premium offer was declined. No payment, paid trial, paid API or agent-created account was used.

Each candidate was fixed before its first submission. [Frozen inputs](frozen-inputs.json), the original draft, raw displayed receipts and [results](results.json) are preserved. The exact text was checked in the editor before submission and again when the completed result was read. The same editor documents were reused, so a QuillBot receipt can retain the old English document title while showing the Korean result; identity is the verified submitted text hash, not the auto-generated title. GPTZero/QuillBot receipts capture the displayed score panel rather than the complete submitted text; their input binding therefore relies on the recorded agent DOM comparison, not a signed vendor report. ZeroGPT echoed the entire input. A first ZeroGPT extraction attempted to parse a DOM outline; it failed because outline markers interrupt the text. Reading the visible page text confirmed the exact echoed input and score; no repeat scan or score change was involved.

Run `python benchmarks/verify_evidence.py` from the repository root. The checks establish internal consistency of dates, hashes, native metrics, source identity, receipts and checkpoint links, not vendor authenticity, actual authorship or general editing quality. Receipts are unsigned agent observations. The separate final evidence audit covers this continuation independently of the earlier 34-observation renewal audit.
