# Alternate rewriting with the local detector

Use by default for substantial rewriting when the trusted local `bilingual-ai-detector` is installed, or when the user explicitly requests local feedback. Respect an editing-only request; light editing and review-only tasks do not automatically trigger a scan. Read the installed detector's actual skill and relevant language/model/evidence references. If it is absent, continue editing and mark scoring unavailable; do not install or replace its models as part of rewriting. Commercial scanning still requires user authorization and usable access.

## Distinguish the roles and evidence

The humanizer owns the source, editorial decisions, fidelity and final prose. The detector measures an unchanged candidate and reviews the whole document. Give a separate reviewer the exact candidate, its result and known creation history when a separate context is available and authorized. Do not supply a desired verdict. A same-context review must be identified as self-review when reporting independence.

| Detector evidence | Useful editorial response | Invalid shortcut |
| --- | --- | --- |
| Korean learned character contributions | Inspect the surrounding clause in context | Ban positive fragments or insert negative-weight fragments |
| Paragraph-deletion sensitivity | Prioritise that paragraph while reviewing the full argument | Delete it or call the delta its AI probability |
| Exact-span style finding and human counterexplanation | Decide whether a reader problem exists in this genre | Treat every flagged formal sentence as defective |
| Documented drafting history | Keep attribution and reporting honest | Claim that a favourable score changed the history |

Overlapping Korean n-grams are not independent evidence. English Humanized is not Human-only: preserve all four classes. Long English input may have window scores but no document probability. Use the actual Korean genre or `unknown`, preserving length/genre/coverage cautions. Neither model is validated as a universal judge of naturalness or previously unseen humanizers.

## Complete the feedback cycle

1. Freeze the original and current candidate, plus protected propositions and register. On the first cycle the candidate is the unchanged source: obtain detector evidence **before** the first rewrite. Retain an explicit user threshold with its metric and scope if one was requested; do not invent a 100% target for “natural writing.”
2. Score the exact candidate with the adapter below. It preserves input bytes, paragraph index, native result and execution record. It does **not** perform the detector's interpretive review.
3. Apply the detector skill's whole-document review and evidence protocol, including neutral paragraphs and human counterexplanations. Validate ledger excerpts and coverage using its `evidence.py`. Anchor validation checks coordinates, not the truth of an explanation.
4. Triage each consequential finding as `revise`, `retain`, or `unresolved`. Record its ID, exact candidate hash/span, evidence basis, human alternative, decision and reason. Use `revise` for a concrete reader problem. Retain effective/protected/genre-appropriate wording; a model contribution alone is insufficient reason to change it. Do not fabricate findings to populate a table.
5. Before revising, state the intended reader improvement and source constraint. Edit the needed clause, sentence or connected paragraph. When consolidating repetition, compare actor, action, object, occasion and force: a review duty and a notice duty cannot be merged simply because their topic is the same. Do not use fragment substitution lists, padding, truncation, invented experiences or deliberate errors.
6. Compare the full revision against the immutable source, then perform a reader review. Link applied decisions to the resulting passages and record any repairs or rejected edits. Freeze the text before rescoring. Any text change invalidates its previous whole-document result.
7. Compare native values without relabelling or averaging incompatible metrics. Preserve gains and regressions. An acceptable repair must preserve meaning and voice and provide a defensible editorial improvement; a higher model score alone is not sufficient. In explicitly requested complete-composition comparison, a useful stated reader route and retained quality qualify an alternative even when an overall readability win is not established. Retain the best faithful complete candidate, which need not be the newest.

When readability and a detector value disagree, preserve both the editorial selection and the highest-scoring faithful checkpoint with separate names and hashes. Explain the trade-off instead of silently replacing a user's preferred checkpoint. If a proposed consolidation removes a distinct later check, notice or approval duty, restore it even when the detector favours the shortened version. The repetition may be functional, so do not keep trying synonyms for that same finding.

Continue alternating while justified findings remain, within [the existing revision budget](iterative-review.md). Before each repair cycle, identify the unresolved reader problem and the meaning that must survive its repair. A lower Human value alone is not that problem. If the user explicitly requests stronger detector-oriented rewriting after this plateau, [complete-composition comparison](composition-variants.md) permits a bounded alternative route with a declared reader benefit within that same budget; it does not require inventing a defect. Local scoring has no commercial quota, but computation and the surrounding assistant session still use resources. Stop at completed review, two consecutive cycles without defensible improvement, repeated runtime failure, or the requested budget. Do not increase the turn ceiling instead of improving the editing method. Resume from recorded source/candidate/decision state when asked; never restart from a weaker candidate merely because it is newer.

## Offline adapter

Requires a local `bilingual-ai-detector` installation. The default is `$CODEX_HOME/skills/bilingual-ai-detector`, or `~/.codex/skills/bilingual-ai-detector`; an explicit path overrides it. Read the detector skill first and use its supported Python environment, for example `py -3.13 -B -X utf8` on Windows.

```text
python scripts/local_feedback.py candidate.txt --language ko --genre unknown --detector-skill /path/to/bilingual-ai-detector --out-dir work/round-0-ko
python scripts/local_feedback.py candidate.txt --language en --detector-skill /path/to/bilingual-ai-detector --out-dir work/round-0-en
```

Choose a **new output directory for every invocation**. The adapter calls only the local indexer and Korean model or supervised English runner, with argument arrays and offline settings. It does not download, train, call hosted inference or start a trial. The installed detector is a user-supplied trusted local dependency; an arbitrary downloaded folder is not equivalent. Do not change detector weights, calibration, genre or thresholds to obtain a desired score.

`feedback.json` keeps native classes, a document Human percentage when available, model identity, input hash, cautions and measured evidence. `style_review_completed: false` means analyst review is still required. `execution.json` retains subprocess exits and errors. Failure yields null probabilities; stale files are never reused. An English native crash can be retried once in a fresh directory after the worker exits. Repeated failure leaves its score unavailable; continue the evidence review without silently switching runtime, hosted model or language. Run English workers serially.

The adapter supports the inspected v3.1 runtime contract, including successfully tested v3.1.2, and pins its Korean model identity/hash and English model revision/hash. It also checks native coverage, English supervisor success and measurement freshness. A later incompatible detector release needs an explicit adapter review; do not loosen these checks to turn an unsupported result into a success.

Use the detector's evidence tools to validate a completed analyst ledger:

```text
python /path/to/bilingual-ai-detector/scripts/evidence.py validate work/round-0-ko/input.txt ledger.json --model-result work/round-0-ko/model-result.json --out checked.json --html review.html
```

Without a completed score, omit `--model-result` and keep numeric results unavailable. Store ledgers, decisions, reports and candidates in the task workspace, not the installed skill. If a future detector changes its contract, inspect the documented schema and report incompatibility rather than inventing an adapter result.

## Verify reusable improvements

A useful skill change explains how feedback alters an editorial decision. Add a general rule only when actual use reveals a missing decision; a high-scoring draft is not a universal template. After development, apply the proposed skill to a different source, then review fidelity and score the complete result. Describe these as fresh development checks, not representative accuracy or formal statistical cross-validation. Score-driven revisions are not untouched holdouts.

Report language-specific before/after values, actual cycles, applied and retained findings, model cautions and failures. Commercial transfer stays unmeasured unless separately tested on the same final text. A high local Human value cannot certify historical human authorship or universal detector acceptance.
