# v1.6.0 editorial controls and free commercial feature trial

Date: 2026-10-03. This release adds audience/register/scope controls, source-backed voice cues, selecting the unit that needs editing, and contextual comparison of local alternatives. It also repairs an existing example that lost a notice's duty to explain a distinction. The default revision budget remains unchanged. These are editorial and fidelity improvements, not a proven generic detector-performance upgrade.

## Independent behavioral checks

A fresh-context agent applied the candidate skill to two new synthetic sources: a Korean book-exchange notice and an English archive trial memo. It received the source and realistic user request, without expected answers, detector scores or earlier experiment conclusions. The actual originals and finals are in [forward/](forward/). One candidate per language was written, self-reviewed and frozen; no rewriting followed the detector results. A second fresh-context agent independently reviewed fidelity, readability and instruction quality. It found no actionable defect in either final or the candidate instructions. [Full independent review](independent-final-review.md). Both are AI sessions; there was no human or cross-model rating.

| Exact document | GPTZero Human before | GPTZero Human after | QuillBot |
| --- | ---: | ---: | --- |
| Korean book-exchange notice | 16% | 98% | Not tested: free quota exhausted |
| English archive memo | 0% | 0% | Not tested: free quota exhausted |

The Korean source was 101 words in GPTZero and its final was 98 words. The final scan explicitly warned that texts under 100 words may be less accurate; the source scan did not show that warning. This confounds the score comparison further, so the 16% to 98% shift should be interpreted cautiously. No padding was added to change eligibility.

The final was scanned first and its source afterward; timestamps disclose the order. Both Korean scans used displayed model 4.1m; both English scans used 4o, Basic mode. This is a source-versus-rewrite comparison on two selected synthetic examples, not a controlled release comparison, a representative success rate or a probability that a human wrote the text. The before/after difference is a one-case observed improvement, not proof of which instruction caused it. The joint GPTZero/QuillBot >=50 target remains unverified for the Korean final and unmet for English.

## Public commercial references and direct free trials

[Feature research](../../skills/bilingual-humanizer/references/commercial-feature-review.md) examines QuillBot, Undetectable AI, WriteHuman, StealthWriter and HIX Bypass, and the primary DAMAGE paper. It supplements the existing public-skill manifests, including im-not-ai. No proprietary model or training corpus was available. The adopted controls are original instructions; no vendor code was copied.

Two signed-out free trials were actually run, with original inputs, exact outputs and browser observations retained under [vendor/](vendor/). No account, purchase, trial subscription or paid API call was created.

- **HIX Bypass, Latest, English:** the 148-word incident source produced a displayed 169-word output. It invented `(Oct 2023)`, narrowed PDF availability, changed unresolved investigation status and reporting responsibility, and introduced awkward grammar. Independent review records seven findings, including low-severity wording issues. It was rejected before independent detector submission. The vendor's own “human-written” assessment is not a verified GPTZero result.
- **Undetectable AI, Basic / General Writing, Korean, Undetectable toggle off:** its free output retained the main notice, with small losses in timing and honorific/obligation wording. The independent reviewer found two low-severity issues. Its own UI reported **40% AI / GPT** and **Your text is written by AI**. That is a vendor self-check, not a Human probability or an independent commercial scan. No external detector result is claimed for this output.

Neither one sample nor a free model tests the vendor's entire paid product. The comparison supports preserving claims and register while editing; it does not support adding invented emotion, random errors or unconditional detector guarantees. Neither vendor output replaces a retained checkpoint.

## Release and evidence integrity

[Publication evidence audit](publication-audit.md) records the separate follow-up verification, including the short-text caveat and metadata-validator repairs.

The exact v1.5.1 release remains under [the retained archive](../deeper-trial/retained-skill/); all prior per-document checkpoints and 154 observations remain intact. The four Cloud G finals received [eight new observations](../continuation-g/REPORT.md). The four observations here bring the actual external GPTZero/QuillBot/Sapling/ZeroGPT archive total to **166**. The two vendor rewrite trials and vendor self-scores are excluded from that count.

`release-skill-hashes.json` binds the 24 v1.6.0 files. `frozen-inputs.json` binds all source/final texts, vendor outputs, raw receipts and review records. Run `python -B benchmarks/verify_evidence.py` and the existing 45 regression tests. These checks establish local consistency, not vendor authenticity or authorship. QuillBot's exhausted free quota remains the only missing service for the new two-case release check; it was not counted as passed. No old favorable score was transferred to a new text.
