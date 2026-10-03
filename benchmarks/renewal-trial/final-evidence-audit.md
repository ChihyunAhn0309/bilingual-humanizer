# Renewal publication evidence audit

Date: 2026-10-03. This is a separate-context AI audit of the proposed public repository, especially `benchmarks/renewal-trial/`, `README.md`, `README.ko.md`, and `THIRD_PARTY.md`. It used the fact-check workflow after content generation. No browser, detector, hosted inference, account action, publication action, or production-file edit was performed. This audit does not grant publication approval. Its renewal scope is the frozen 34-observation bundle; the later `continuation-e` phase is outside this audit.

**Finding:** the recorded scores, comparisons, checkpoint identities, and retained release are locally consistent. The requested all-selected-detector target remains unmet. The missing runner and historical HIP scope clarification were resolved and checked. Final publication-artifact hygiene remains the assembly qualification recorded below. No score correction or production-skill change was required by this audit.

## Checks actually run

From the proposed repository root:

```text
python -B -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
45 tests; OK; exit 0.

python -B benchmarks/verify_evidence.py
PASS: 36 original observations.
PASS: 28 v1.5/development observations.
PASS: 17 additional-trial observations.
PASS: 32 deeper-trial observations.
PASS: 34 renewal observations.
Exit 0.
```

The five evidence groups total 147 observations. Rechecking them does not add observations or independent detector trials. Tests exercise helper behavior and archive consistency, not rewriting quality, service authenticity, or authorship.

Additional read-only checks independently reconstructed the 14-row renewal report table, resolved every selected and alternative checkpoint reference, compared full release file sets and ZIP contents, checked prototype application manifests, inspected source/model attribution, searched for credential patterns, and inspected unwanted artifact paths. The `-B` flag prevented these audit test runs from creating bytecode caches.

## Claims checked against the local evidence

| Claim | Local source and result | Confidence and limit |
| --- | --- | --- |
| There are 34 new completed observations. | [results.json](results.json), 34 individual observation JSON files and 34 receipts agree: GPTZero 11, QuillBot 13, Sapling 5, ZeroGPT 5. IDs are unique; all timestamps parse. | High for archive consistency; receipts are unsigned observations. |
| Scores belong to the exact frozen texts. | Every input-file hash, stripped submitted-text hash, receipt hash, and corresponding [frozen-inputs.json](frozen-inputs.json) value matches. The report table reproduces every new reading, including dashes for absent readings. | High for local identity. A hash does not independently prove the service received that text. |
| Native metrics are kept separate. | GPTZero receipts say “Chance this entire text is...” and expose AI/Mixed/Human classes. QuillBot exposes AI-generated, Human-written & AI-refined, and Human-written text shares. Sapling reports AI probability percent; ZeroGPT reports AI GPT percentage. | High for the displayed definitions. These are not one calibrated authorship probability. |
| The inclusive continuation target is unmet. | GPTZero and QuillBot targets use `gte` 50 in the current result bundle; Sapling/ZeroGPT use separate `lte` 50 AI-side criteria. Each selected checkpoint fails at least one applicable recorded criterion. | High. Historical strict `>50` criteria are preserved separately. |
| No cross-draft score combination was used. | All retained and alternative evidence entries in [checkpoint-registry.json](checkpoint-registry.json) resolve to an original result ID with the same vendor, metric, score, timestamp, and input hash. | High for the listed candidates; the registry explicitly is not an exhaustive historical ranking. |
| Production remains v1.5.1. | The complete 22-file release manifest matches the public production folder, local master, installed skill, deeper-trial rollback files, and local Git objects at `cf1af74baa5fac59f7fcf4bc20c5dc1e349054d9`. | High for inspected bytes, excluding generated cache files. No remote branch state was queried. |
| v1.5.2 is a separate archived prototype. | All 22 [experimental hashes](experimental-skill-hashes.json) match the archive. After resolving their original workspace paths, all 22 entries in `v152-check/skill-snapshot.json` and all 11 entries in its application manifest match the archived prototype or associated texts. | High. Prototype results are not mislabeled as tests of retained production. |
| Two local model outputs were rejected. | [inference metadata](local-model/inference-metadata.json), raw/final outputs, runner, and [fidelity review](local-model-review.md) are mutually consistent. No renewal detector record uses either model output hash. | High for the recorded evidence and rejection grounds; inference was not rerun or independently authenticated. |
| Source inventory is 32 skill repositories plus 3 research implementations. | The original manifest contains 19 entries; the additional manifest has 13 skill and 3 method entries. All 35 recorded entry hashes match locally retained source files. The 16 additional local repository HEADs and recorded license-file hashes match their manifest. | High for local attribution and counts. This does not establish 35 independent methods or validate all paper claims. |

The full parser checked every new receipt's native score. GPTZero category totals and QuillBot category totals each sum to 100. GPTZero receipts contain the recorded Basic Scan/model and “Text up-to-date.” QuillBot receipts contain the recorded model and no “Outdated score.” Sapling's sentence sequence reconstructs the submitted text after whitespace normalization and marks it untruncated; ZeroGPT receipts contain the submitted text and matching score. GPTZero/QuillBot input matching additionally relies on the experiment's recorded DOM-verification assertion: their trimmed receipts do not themselves retain a complete input echo. This is a provenance limit, not a discovered score mismatch.

QuillBot's 13 successful readings form a seven-scan allocation followed by six scans in the next allocation. Recorded remaining counts are `6,5,4,3,2,1,0` and `6,5,4,3,2,1`; the singular “1 AI scan left” and zero-scan receipts agree. No unobserved scan was counted as a pass.

## Checkpoint comparisons

| Retained text | GPTZero Human | QuillBot Human-written | Additional reading |
| --- | ---: | ---: | --- |
| Korean library C | 93% | 15% | ZeroGPT AI GPT 100% |
| Korean essay baseline | 42% | 100% | ZeroGPT AI GPT 100% |
| English support baseline | 0% | 83% | Sapling AI 100% |
| English museum prototype | 0% | 100% | Sapling AI 91.3% |

These values match both READMEs and the registry. Prior observations remain tied to their earlier timestamp and exact input. Comparisons within each case use the same exposed models: GPTZero Basic 4o and QuillBot v7.1.0 for English; GPTZero Basic 4.1m and QuillBot v6.2.1 for Korean. Sapling/ZeroGPT do not expose a model version in these records, so stability of their underlying models cannot be guaranteed.

The C library comparison is 50% to 93% GPTZero Human and 12% to 15% QuillBot Human-written against the exact v1.5.1 library baseline. The essay baseline's 42% exceeds C's 9% and the prototype's 3% in GPTZero, with QuillBot at 100% for all three. Support baseline 83% exceeds C 70% and prototype 78% in QuillBot, while their GPTZero readings are all 0%. Museum prototype 91.3% Sapling AI is lower than baseline 93.7%, while the other two readings match. These are observed differences on specific texts, not general superiority or statistical significance.

The blind mapping and all source/X/Y copies match their hashes. Its stated preferences resolve to C for library and essay, baseline for support, and a museum tie. The prototype audit explicitly discloses that development sources were previously used and that its writer incidentally saw brief earlier-review summaries. The reports correctly distinguish same-model separate-context reviews from human or cross-model validation.

## Release and local model provenance

The two inspected release ZIPs each contain exactly the 22 release files with matching hashes. Both have SHA-256 `2f005800d6c86bee6c2c82fcac61ce0b48e988b0746c2afb89713799a4d4142f`, matching the registry. The experimental snapshot differs from production in exactly three files: `SKILL.md`, `references/iterative-review.md`, and `references/structural-rewrite.md`.

All 16 entries in the model download-hash manifest match actual local files retained outside the public repository, including both safetensors files. Existing local file sizes agree with the pinned model manifest. Both stored model cards identify Apache-2.0 licensing. The base revision is `da87bfb608c14b7cf20ba1ce41287e8de496c0cd`; the adapter revision is `98a907f41440e10aafedd10364b41c32bb5fbf6a`. No network provenance was reauthenticated.

The runner uses local-only loading during inference, disables remote custom code, specifies a 1,200-token/240-second generation ceiling, and records CPU/float32 settings. Both raw generations include the closing target tag; each clean output is exactly the runner's extraction from its raw output. EOS completion is recorded in metadata rather than independently recoverable from decoded text. The museum output changes exception authorizers into applicants and drops the disputed-object restriction. The Korean output omits the operating weekdays, attaches 12-person capacity to an incoherent volunteer phrase, and reverses the permanent-policy caveat. Those concrete source/output differences support rejection without relying on a detector score.

No weights, tokenizer assets, downloaded dependency code, virtual environment, or model cache were found in the proposed public tree. Text scanning found no common API-token/private-key credential patterns. Vendor document URLs/IDs are receipt provenance, not authentication credentials. This is a practical inspection, not a guarantee that arbitrary secrets could never evade a pattern search.

## Assembly findings sent to the parent

1. **Resolved missing runner.** Initially, the report and attribution file said the repository contained a bounded runner, but `local_model_trial.py` was missing. The parent was notified; the runner subsequently appeared in the renewal archive and matched the inspected local implementation. This auditor did not copy or edit it.
2. **Publication hygiene.** Eight pre-existing `.pyc` files were present in production `__pycache__` folders in the assembly directory. `.gitignore` excludes these files, and the inspected publication script explicitly filters them from its upload manifest and constructs the final repository ZIP from that manifest. They are not among the 22 release files. Final publication verification must use that filtered artifact rather than an indiscriminate directory ZIP; the final uploaded tree/ZIP was outside this audit's snapshot.
3. **Resolved historical scope clarification.** The byte-preserved production reference `further-reference-review.md` says that no HIP adapter was run “here.” The parent added explicit explanations in `REPORT.md` and the repository's `THIRD_PARTY.md`, and this auditor checked both changes: the statement describes only the earlier reference-review phase, while the separate renewal probe ran an existing pretrained adapter on two synthetic inputs without training it. The apparent conflict is resolved without requiring a production-skill edit. This follow-up checked those documentation changes only; it did not repeat detector or inference work or extend the audit to `continuation-e`.

At initial inspection, the only broken relative documentation links in the two READMEs and renewal report were links to this not-yet-written audit. Publication assembly needs to place this file at `benchmarks/renewal-trial/final-evidence-audit.md`.

## Limits of this audit

Overall confidence is **high for local evidence consistency and retained-file identity**, with the stated assembly qualifications. Commercial receipts, inference metadata, review independence, access errors, user account allocations, and claims of no purchases/account creation are contemporaneous experiment records, not independently authenticated service/account histories. No live service or remote publication status was checked. Existing scientific-paper claims and current vendor documentation were not reverified online; the audit checked their attribution inventory and locally stored sources without importing research performance into this experiment's results.

Nothing in this report establishes actual human authorship, a detector's accuracy, or general acceptance of the skill. The evidence remains a small adaptive experiment on AI-produced development texts, with no human-authored control, representative sample, or human rating study.
