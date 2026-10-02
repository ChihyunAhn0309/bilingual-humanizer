# Commercial detector development test — 2026-10-02

**The multi-detector acceptance goal was not met.** The final v1.4 candidates retain mixed or high AI classifications. This release improves editing instructions and review, but this experiment does not demonstrate superior detector performance.

![Separate vendor observations](../../docs/assets/detector-observations.png)

All four source texts and all rewrites were AI-produced. Two fictional topics (library pilot and software cache) were written separately in English and Korean. They are not exact translations. There is no human-authored control, representative sample, or independent human assessment. These are real service observations on an adaptive development sample, not detector accuracy measurements.

## Final candidate observations

Values below are each provider's displayed AI metric. **Their meanings differ.** GPTZero: probability of the AI class for the entire document; QuillBot: share of words likely generated/refined by AI; Sapling: whole-text AI-generation estimate; ZeroGPT: vendor AI GPT percentage. Never average these values or interpret a low score as evidence of human authorship. N/A means no completed test, not zero.

| v1.4 input | GPTZero | QuillBot | Sapling | ZeroGPT |
| --- | ---: | ---: | ---: | ---: |
| en-library | 100% | 0% | 96.2% | N/A |
| ko-library | 11% | 86% | N/A | 100% |
| en-cache | 100% | 0% | 93% | N/A |
| ko-cache | 100% | 92% | N/A | 100% |

GPTZero classified the v1.4 Korean library memo as entirely human (Human 88%, AI 11%, Mixed 1%). The other three v1.4 files received AI 100%. QuillBot displayed AI 0% / Human 100% for both English v1.4 files, but high AI scores for both Korean files. Sapling returned high AI estimates for both English files; ZeroGPT labelled both Korean files AI/GPT-generated. These are different products evaluating the same frozen candidates, not proof of their actual authors.

The earlier Korean library v1.1 candidate received Human 94% / AI 5% in GPTZero, while v1.2 received Human 2% / AI 98%. The raw AI source itself received Human 76% / AI 22%. This illustrates both detector disagreement and non-monotonic scores; a newer editing instruction is not automatically a better detector outcome. Sapling's best cache score here was v1.2 (88.2), not v1.4 (93).

## All completed observations

The tables include every valid recorded completed scan used in the comparison. The v1.3 English library file was checked only in GPTZero; other v1.3 cells were not tested before the user requested the im-not-ai addition. Results are not cherry-picked across revisions to label v1.4 as passed.

### GPTZero

| Input | Source | v1.1 | v1.2 | v1.3 | v1.4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| en-library | [100](receipts/gptzero-en-library-source.txt) | [100](receipts/gptzero-en-library-rewrite.txt) | [100](receipts/gptzero-en-library-v12-auth.txt) | [100](receipts/gptzero-en-library-v13-auth.txt) | [100](receipts/gptzero-en-library-v14-auth.txt) |
| ko-library | [22](receipts/gptzero-ko-library-source.txt) | [5](receipts/gptzero-ko-library-rewrite-auth.txt) | [98](receipts/gptzero-ko-library-v12-auth.txt) | N/A | [11](receipts/gptzero-ko-library-v14-auth.txt) |
| en-cache | N/A | N/A | N/A | N/A | [100](receipts/gptzero-en-cache-v14-auth.txt) |
| ko-cache | N/A | N/A | N/A | N/A | [100](receipts/gptzero-ko-cache-v14-auth.txt) |

### QuillBot

| Input | Source | v1.1 | v1.2 | v1.3 | v1.4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| en-library | [0](receipts/quillbot-en-library-source.txt) | [0](receipts/quillbot-en-library-rewrite.txt) | N/A | N/A | [0](receipts/quillbot-en-library-v14.txt) |
| ko-library | [79](receipts/quillbot-ko-library-source.txt) | [75](receipts/quillbot-ko-library-rewrite.txt) | [90](receipts/quillbot-ko-library-v12.txt) | N/A | [86](receipts/quillbot-ko-library-v14.txt) |
| en-cache | N/A | N/A | N/A | N/A | [0](receipts/quillbot-en-cache-v14.txt) |
| ko-cache | N/A | N/A | N/A | N/A | [92](receipts/quillbot-ko-cache-v14.txt) |

### Sapling

| Input | Source | v1.1 | v1.2 | v1.3 | v1.4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| en-library | [98.6](receipts/sapling-en-library-source.txt) | [95.7](receipts/sapling-en-library-rewrite-webmcp.json) | [93.9](receipts/sapling-en-library-v12-webmcp.json) | N/A | [96.2](receipts/sapling-en-library-v14-webmcp.json) |
| ko-library | N/A | N/A | N/A | N/A | N/A |
| en-cache | [96.3](receipts/sapling-en-cache-source-webmcp.json) | [94.5](receipts/sapling-en-cache-rewrite-webmcp.json) | [88.2](receipts/sapling-en-cache-v12-webmcp.json) | N/A | [93](receipts/sapling-en-cache-v14-webmcp.json) |
| ko-cache | N/A | N/A | N/A | N/A | N/A |

### ZeroGPT

| Input | Source | v1.1 | v1.2 | v1.3 | v1.4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| en-library | N/A | N/A | N/A | N/A | N/A |
| ko-library | [100](receipts/zerogpt-ko-library-source.txt) | [100](receipts/zerogpt-ko-library-rewrite.txt) | [100](receipts/zerogpt-ko-library-v12.txt) | N/A | [100](receipts/zerogpt-ko-library-v14.txt) |
| en-cache | N/A | N/A | N/A | N/A | N/A |
| ko-cache | [100](receipts/zerogpt-ko-cache-source.txt) | [100](receipts/zerogpt-ko-cache-rewrite.txt) | [100](receipts/zerogpt-ko-cache-v12.txt) | N/A | [100](receipts/zerogpt-ko-cache-v14.txt) |

## Methods and access

- **Input integrity:** exact UTF-8 files and SHA-256 hashes are in [corpus-manifest.json](corpus-manifest.json). Each valid result links its input and receipt hashes in [results.json](results.json). UI editors may normalize whitespace; final v1.4 UI inputs were compared after whitespace normalization (ZeroGPT textarea values matched exactly). Sapling WebMCP received the file text directly and returned `truncated: false`. We did not inspect raw network payloads. Result-panel extracts, including all four final QuillBot receipts, omit the submitted input. Their association with a corpus file relies on the agent-observed comparisons in [input-verification-log.json](input-verification-log.json); the public bundle does not independently authenticate that binding. This retrospective log is an agent attestation, not a vendor receipt.
- **GPTZero:** Basic Scan; displayed English model 4o and Korean model 4.1m. Early scans were anonymous; later scans used the user-supplied authenticated account. Account settings are not perfectly controlled across phases. The final four candidates used the same authenticated Basic Scan access. Fresh results required matching input and “Text up-to-date.”
- **QuillBot:** displayed English model 7.1.0 and Korean model 6.2.1. Initial anonymous access reached its free quota. The user logged in; four final scans then ran through the free interface, leaving three daily scans. Paid offers were dismissed. No purchase was made.
- **Sapling:** English only in this test. Public UI/page-provided WebMCP, whole-document inputs below the observed 2,000-character free limit. Model version was not returned, so it is recorded as unknown rather than inferred from API defaults.
- **ZeroGPT:** Korean submitted under its advertised multilingual coverage. No Korean-specific accuracy was established. Model version unknown; scores are reported only as vendor output.
- **Timing:** `captured_at_utc` is the local receipt-file capture time, not a vendor-signed timestamp. Full model internals, training data and feature weights are undisclosed. Provider explanations and research are linked in [the detector reference](../../skills/bilingual-humanizer/references/detectors-and-authorship.md).

The [working protocol](protocol.md) was documented during execution, not preregistered. The skill author saw earlier scores while revising the instructions. Fresh writer contexts received only the current skill and original texts; this reduces direct score feedback to the writer but does not make the development corpus held out. Each candidate was frozen before its own scans. User follow-up requests authorized the additional functional versions; the distributed skill's default ceilings remain unchanged.

## Excluded attempts and missing tests

| Attempt | Status and reason |
| --- | --- |
| Anonymous GPTZero Korean v1.1 attempt | Quota blocked and concatenated input; stale displayed score excluded. Later authenticated exact-input scan is the valid observation. |
| Anonymous GPTZero v1.2 attempt | Free limit and contaminated input; no valid new result. |
| First ZeroGPT Korean source attempt | Input acquired extra characters; excluded and retested with verified exact input. |
| Authenticated GPTZero source recheck | An exploratory Advanced Scan displayed AI 100% and consumed 302 credits, then showed text-change/normalization state. Excluded from the Basic Scan comparison; no retained complete input-bound receipt. |
| UI timeouts, stale editor values, mobile result panels | Observed and resolved before counting a result. Failed submissions are not passes. No hidden API, CAPTCHA bypass or paid access used. |
| Other N/A cells | Not tested; they are not a language-support or product-quality conclusion. |

Excluded raw text receipts are preserved with their original filenames in `receipts/`; they are deliberately absent from `results.json`. Account profiles, OAuth URLs and unrelated browser history are not published.

## Independent review and local checks

[Pre-publication evidence audit](final-evidence-audit.md) checked all 36 observations and the final 12-service-result composition. Its initial input-binding disclosure finding was addressed; no unresolved actionable finding remained. The auditor did not independently authenticate remote scans.

- [v1.4 forward test](v14-review.md): four new rewrites, separate source/fidelity review, one fresh-context reviewer and one follow-up review. Two revision cycles repaired Korean directive strength and one English expression. Final files have no unresolved findings in those reviews. Three additional short Korean examples are author-generated self-tests, not independent evaluations.
- [Final skill audit](final-skill-audit.md): independent context found a conditional-to-factual example error. It was corrected and the auditor verified the repair. No unresolved actionable finding remained. The auditor ran 37 read-only unit tests; the main session ran all 42 including CLI tests.
- All 42 offline helper tests passed, and the skill-creator format validator passed. These checks do not measure naturalness or detector acceptance.
- Intermediate [v1.1](rewrite-review.md), [v1.2](v12-review.md), and [v1.3](v13-review.md) reviews are historical observations. The [v1.2 diagnosis](v12-quality-diagnosis.md) is a writer follow-up, not a new blind review. Model reviewers share the host model family; no human or cross-model review is claimed.

Run the evidence-integrity and helper checks from the repository root:

```sh
python benchmarks/verify_evidence.py
python -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
```

Recreate the observation chart with `python benchmarks/plot_results.py` after installing matplotlib and numpy. This script reads saved results and does not call a service. The editable workflow diagram follows [paper-figure](../../docs/figure-evidence/render-review.md); the statistical chart uses standard plotting tools.

The useful release is the faithful bilingual editing workflow and transparent evidence. Universal human classification, human authorship certification and a guaranteed detector bypass remain unachieved and are not advertised.
