# QuillBot access renewal and v1.6.0 follow-up

Observed on 2026-10-03, including a second access renewal requested during the work. Production remains **v1.6.0**, with all 24 skill files unchanged. The new Korean notice and English memo each received **QuillBot Human-written 100%**, but their sources also received 100%. Two new local library rewrites and a repaired commercial derivative failed to improve the retained library checkpoint. There is no basis here for a detector-performance upgrade or a universal acceptance claim.

## Same-text results

GPTZero reports **Human document probability**; QuillBot reports **Human-written text percentage**. These columns have different meanings and are not averaged. An earlier GPTZero result is linked only to the identical file hash and retains its original observation time.

| Exact input | GPTZero Human | QuillBot Human-written | Both selected native metrics >=50? |
| --- | ---: | ---: | --- |
| [Korean notice source](inputs/korean-original.txt) | 16% (earlier) | 100% (new) | No |
| [Korean notice v1.6.0](inputs/korean-final.txt) | 98% (earlier; short-text warning) | 100% (new) | Yes, for this particular text and these two services |
| [English memo source](inputs/english-original.txt) | 0% (earlier) | 100% (new) | No |
| [English memo v1.6.0](inputs/english-final.txt) | 0% (earlier) | 100% (new) | No |
| [Retained library E](inputs/ko-library-retained.txt) | 97% (earlier) | 30% (rechecked) | No |
| [Independent v1.6.0 library rewrite](inputs/ko-library-v160.txt) | 47% (new) | 14% (new) | No |
| [Second library alternative](inputs/ko-library-alternative.txt) | 61% (new) | 17% (new) | No |
| [Library source](inputs/ko-library-source.txt) | 76% (second access period) | 21% (second access period) | No |
| [Commercial output with fidelity repairs](inputs/ko-library-vendor-repaired.txt) | 68% (second access period) | 24% (second access period) | No |

The notice source was 101 words and its rewrite 98 words in GPTZero. The rewrite triggered “This text is under 100 words” and the accuracy warning; the source did not. Thus its earlier 16%→98% change crosses a warning boundary. QuillBot was 100%→100% for both languages, so these new comparisons do **not** demonstrate a QuillBot gain. Neither the high readings nor the two-service threshold establishes historical human authorship.

The library baseline was rechecked before its challengers in the same free-access session. QuillBot reproduced its earlier 30%. All three library observations used QuillBot v6.2.1; their GPTZero results used model 4.1m. The new library candidates were 249 and 252 words respectively in GPTZero and did not receive the short-text warning. The English QuillBot source/final pair used v7.1.0; the Korean pair used v6.2.1. Earlier English GPTZero scores used model 4o. Full timestamps, hashes, native categories and model labels are in [results.json](results.json).

## What was actually changed and reviewed

The independent writer received only the current skill and the original library source, without detector results or earlier candidate texts. It completed one draft and two revisions, with a source comparison and reader review for each candidate. It rearranged the response limitations, volunteer condition, capacity and guidance duties. Its [writing record](writer-review.md) records the actual repairs; a separate session then [reviewed the final against the source](independent-fidelity-review.md) and found no actionable fidelity issue.

After seeing that result, the parent session drafted a second local alternative using the existing editorial controls. It simplified some count interpretation and clause connections, followed by one repair pass and source/reader checks. The [writing record](alternative-writing-review.md) identifies this as a development follow-up. The same independent reviewer performed a [follow-up source comparison](alternative-fidelity-review.md), again without detector scores. That was not a new blind session or a human review. Both candidates retained the source's formal register, quantitative referents, decision stage and distinct review/guidance obligations.

The second alternative improved over the first new attempt on both services, but both were below retained library E on both native Human metrics. Neither replaces that checkpoint. The earlier library F trade-off (91% / 33%) remains archived separately; its QuillBot 33% is not combined with E's GPTZero 97%. Existing essay, support and museum checkpoints are unchanged. [Prior exact checkpoint registry](../continuation-e/checkpoint-registry.json).

No skill rule was promoted merely to create a new version. The v1.6.0 release and ZIP remain unchanged. These results test current instructions on a known difficult development document, not an unseen representative sample. The fresh notice and memo are two forward-test documents from the preceding phase, not additional new holdouts generated during this phase. Earlier reports remain historical snapshots; their QuillBot-pending status at the time is resolved by the records here.

## Second access renewal: commercial comparison

The user then supplied another QuillBot login and asked to continue. The full English archive input hit QuillBot Humanizer's **125-word free limit** (input: 134 words), and Korean was absent from that humanizer's visible language selector. Restricted output was not extracted or accepted. No upgrade or trial was started.

Undetectable Basic / General Writing processed the full Korean library source for free. Its raw output dropped requirements/recommendations and changed an unresolved condition to an unverified one, so it was rejected before independent detector submission. The parent repaired those changes against the source and normalised duplicated spaces. The same separate reviewer completed a [follow-up fidelity review](vendor-repaired-fidelity-review.md) without detector results. The repaired derivative received **GPTZero 68% / QuillBot 24%**; the source received **76% / 21%**. Thus QuillBot rose by 3 points against the source, GPTZero fell by 8, and both were below retained E. This mixed outcome does not justify replacing the checkpoint or claiming a portable-skill improvement. It is commercial output plus editing, not output of this skill alone. All these Korean checks used GPTZero 4.1m and QuillBot v6.2.1 without a GPTZero short-text warning. [Vendor inputs, limits, raw output and repair rationale](vendor/REVIEW.md).

## Access, exact inputs and reproducibility

Across the two access periods, nine QuillBot scans and four GPTZero scans completed: **13 new external observations**, bringing the archived total from **166 to 179**. The earlier five GPTZero readings linked in the table are not counted again. Vendor humanizer self-scores are excluded. The user supplied renewed free access; no purchase, paid trial, subscription change, paid API or agent-created account was used. QuillBot displayed **No free AI scans left** after the first seven scans. Work resumed only after the user supplied another login; two more scans completed and the last result displayed **5 free scans remaining**. No quota exhaustion is claimed for that second access period.

Two preparations of the first library candidate contained extraneous Korean input and failed the local DOM comparison. They were not submitted or counted. After the user paused typing, the clean full input was verified. Each QuillBot observation includes a saved before/after input DOM receipt, the result panel text, file and submitted-text hashes, model and quota. Visible result freshness was checked and an outdated result was not accepted. GPTZero input text was compared with the file and its completed panel showed `Text up-to-date`.

The saved UI observations are locally recorded evidence, not vendor-signed certificates. Whitespace-normalized DOM equality is used for input comparison; the exact submitted text and original file hashes are also recorded separately. The GPTZero receipts contain result panels rather than full input DOM snapshots. Its `input_verified_in_dom` flag records the agent's observed comparison, but a third party cannot reconstruct or independently reverify the full submitted GPTZero input from those saved panels. QuillBot's before/after input snapshots provide a stronger local trail. Neither trail independently authenticates vendor calculations. No naturalness score or authorship probability is inferred from the offline validator.

```sh
python benchmarks/verify_quill_renewal.py
python benchmarks/verify_evidence.py
python -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
```

The verifier links every table pair to the same input hash, checks native metrics/model/timestamp, result freshness, QuillBot before/after input receipts, quota, vendor source/output hashes and self-score separation, and unchanged v1.6.0 files. It recomputes the earlier total from the eight completed-observation result files, excluding alternative summary snapshots and vendor self-scores. Independent publication validation is recorded in [publication-audit.md](publication-audit.md).
