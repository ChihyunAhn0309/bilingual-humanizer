# Renewal experiment and retained checkpoints

2026-10-03 KST. **The universal/all-selected-detector target is not achieved. Production remains v1.5.1.** The source-sensitive v1.5.2 prototype is archived as an experiment rather than replacing the retained release. Keeping a prior candidate is an actual selection decision, not a claim that the prior skill is optimal.

The latest user target is inclusive: GPTZero native Human document probability >=50%, and QuillBot native Human-written text share >=50%. Earlier reports used >50%; their original criteria remain unchanged. These two units are different and are not averaged. Sapling and ZeroGPT expose AI-side scores in this test; AI <=50% is a separate operational criterion, not a manufactured Human probability. A score cannot establish historical authorship.

## Complete new observations

All values are vendor readings on the linked exact input. A dash means no observation in this continuation, not a pass. Baseline GPTZero/ZeroGPT readings from the prior experiment are kept separately and matched by file hash in the checkpoint registry.

| Input | GPTZero Human probability ↑ | QuillBot Human-written share ↑ | Sapling AI probability ↓ | ZeroGPT AI GPT ↓ |
| --- | ---: | ---: | ---: | ---: |
| [candidates/en-museum.txt](candidates/en-museum.txt) | 0% | 100% | 95.2% | — |
| [d-candidates/en-museum.txt](d-candidates/en-museum.txt) | 0% | 100% | 94.3% | — |
| [v152-check/en-museum.txt](v152-check/en-museum.txt) | 0% | 100% | 91.3% | — |
| [candidates/en-support.txt](candidates/en-support.txt) | 0% | 70% | 100% | — |
| [v152-check/en-support.txt](v152-check/en-support.txt) | 0% | 78% | 100% | — |
| [candidates/ko-essay.txt](candidates/ko-essay.txt) | 9% | 100% | — | 100% |
| [sources/ko-essay.txt](sources/ko-essay.txt) | 6% | — | — | — |
| [v152-check/ko-essay.txt](v152-check/ko-essay.txt) | 3% | 100% | — | 100% |
| [candidates/ko-library.txt](candidates/ko-library.txt) | 93% | 15% | — | 100% |
| [d-candidates/ko-library.txt](d-candidates/ko-library.txt) | 16% | 15% | — | 100% |
| [v152-check/ko-library.txt](v152-check/ko-library.txt) | 31% | 15% | — | 100% |
| [baseline/en-support.txt](baseline/en-support.txt) | — | 83% | — | — |
| [baseline/ko-essay.txt](baseline/ko-essay.txt) | — | 100% | — | — |
| [baseline/ko-library-v151.txt](baseline/ko-library-v151.txt) | — | 12% | — | — |

There are **34 new completed observations** in [results.json](results.json), each with a submitted-text hash, source-file hash, raw receipt, timestamp, product/model where exposed, and original metric. No favourable readings from different drafts are combined. Failed/intermediate scans are described below and are not fabricated as completed records.

## What changed and what did not

C preserves effective prose and uses selective restructuring rather than always rebuilding from an abstract map. D uses a working decision-document form with purposeful headings. The [independent C-versus-baseline comparison](blind-review.md) preferred C slightly for the library and essay, preferred the retained English support email, and tied the museum memo. The candidates preserved substantive meaning in [the separate fidelity review](candidate-review.md); D also passed [its fidelity review](d-candidate-review.md). These are same-model independent-context reviews, not human ratings.

C library improved GPTZero Human from the exact v1.5.1 baseline's 50% to 93%, and QuillBot from 12% to 15%, but remained below the QuillBot floor and received ZeroGPT AI GPT 100%. The older essay baseline's GPTZero Human 42% and newly measured QuillBot 100% outperform C's 9%/100% and the independent v1.5.2 prototype output's 3%/100% on those two displayed criteria. The old support baseline received QuillBot 83%, versus C 70% and the prototype 78%; their GPTZero Human readings remained 0%. This is why the latest output is not automatically selected.

The v1.5.2 prototype incorporates source-sensitive routing, reader-task paragraph boundaries, explicit retained checkpoints, and a corrected example that keeps the review's “distinguish” duty separate from the notice's “explain” duty. Its exact instructions are in [experimental-skill](experimental-skill/). [The independent application audit](final-skill-audit.md) records actual drafts, repairs, reviewer passes, tests and limitations. The four inputs were previously used development sources; they are not new topic holdouts. The final validator incidentally saw brief summaries of earlier reviews via agent inventory and discloses that contamination. The earlier C preference comparison remained blinded to method identities and detector results.

The tested instruction changes did not establish a general improvement across required products, so the installed and published production skill stays at the exact 22-file v1.5.1 snapshot. [Checkpoint registry](checkpoint-registry.json) stores per-document selection, alternatives, file identities and supporting readings. It deliberately does not name one universal “best Human score.” A challenger needs preserved meaning, reader quality and a like-for-like comparison before replacing a checkpoint. Missing comparisons and service trade-offs remain visible.

## Local trained-model feasibility probe

One CPU inference was completed for each of two synthetic sources. Both outputs were rejected before detector submission by an independent fidelity reviewer: English changed authority, scope and evidence; Korean omitted operating days, changed the capacity referent, reversed a policy caveat and damaged syntax. No local-model output was sent to a detector or adopted by the skill.

The public [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base) and [HIP adapter](https://huggingface.co/YixuanEvenXu/Qwen3-0.6B-Base-HIP-adapter) were pinned to revisions in [the manifest](local-model/model-manifest.json). The model cards identify Apache-2.0 licensing. No weights, tokenizer assets, package dependencies, vendor implementation code or caches are redistributed here. The bounded [local runner](local_model_trial.py) is newly written; it uses safetensors, `trust_remote_code=False`, CPU inference and synthetic inputs. This probe is separate from the instruction-only skill and does not import a paper's reported performance as our result. The unchanged production reference note saying no adapter was run describes the earlier reference-review phase only; this later probe ran the pretrained adapter on two inputs, without training it.

## Access, errors and stopping

The first user-provided QuillBot allocation completed seven free scans. The user then supplied another usable free allocation and explicitly requested checkpoint retention; six further scans completed, leaving one at the end of this frozen experiment. The cumulative plan is in [PLAN.md](PLAN.md). Later account replenishment is not an additional observation. No agent-created accounts, purchases, paid trials or paid API calls occurred. The first attempt to open a document belonging to the prior account showed “Something went wrong”; opening the product's new-document flow resolved it. No attempt to bypass that access restriction was made.

Some editor inputs unexpectedly differed from the frozen file. Those attempts were stopped before submission or excluded, and the final recorded inputs were compared with the exact file before scanning and checked again against the completed result. This is why an apparently successful intermediate display was not sufficient evidence.

The unchanged Korean essay source comparator initially reached an unavailable Advanced Scan flow in GPTZero. The upsell was dismissed and the final recorded result is a completed Basic Scan with Text up-to-date. The intermediate display was excluded. The comparator remains AI-produced text, not a human control. One QuillBot quota parser initially missed singular “1 AI scan left”; the archived value was corrected to 1 against the receipt before publication, and singular/plural/explicit-zero cases are checked. No score changed in that correction.

Public model download attempts stalled under the initial hub transports. A bounded direct HTTPS retry completed the base weights, reached its time ceiling during the adapter, and a ranged continuation completed the adapter. No credentials or hosted inference were used. These operational retries are not detector rounds.

Further candidate sampling stops when no defensible gain remains or changes would damage fidelity. Remaining free quota is not a requirement to generate cosmetic variants. The unresolved goal is reported rather than presented as success.

## Reproduce local checks

```sh
python -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
python benchmarks/verify_evidence.py
```

These checks verify local consistency and helper behavior, not vendor authenticity, semantic quality or authorship. The receipts are unsigned agent observations. Scores can change with service models/settings, and this small adaptive sample cannot establish general acceptance rates. See [final evidence audit](final-evidence-audit.md) for the separate publication review.
