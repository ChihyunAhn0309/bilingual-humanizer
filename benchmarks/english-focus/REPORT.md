# English-focused release — v1.9.0

The English editing method now includes clause-level recomposition, information continuity, contextual register/contractions, noun-attachment checks, discourse review, academic section roles and feature-specific voice evidence. These are additions to the existing bilingual skill; Korean instructions and the three-revision ceiling are unchanged. The 30-file release retains every v1.8.0 file in its 28-file archive.

Research covered **15 public repositories and seven product documentation surfaces**, with different inspection depths recorded in [the research review](research/REVIEW.md). This is not 15 independent methods, nor a performance contest between those services. No third-party code was executed or new paid dependency added.

## Exact local measurements

| Synthetic English source | Unchanged source | v1.8 candidate | v1.9 candidate |
| --- | ---: | ---: | ---: |
| support-email | 0.012120% | 0.008422% | 0.314060% |
| reading-reflection | 0.009758% | 0.010690% | 0.014873% |
| technical-update | 0.025962% | 0.039713% | 0.127413% |

These are the native **Human-only class outputs** of local `bilingual-ai-detector` v3.1.2's pinned English model, not validated probabilities of a person having written the text. AI-edited and Humanized are not counted as Human. All inputs fit a single scoring window. Model revision/weight hashes, four-class values, dates, execution records and exact inputs are saved per case. Full precision is retained in `results.json`.

The experimental candidate is higher than the baseline candidate in **3/3** cases. This small development comparison does not establish a causal skill improvement, stable detector gain, or commercial transfer. **The retained-checkpoint Human ≥50% target across these three local cases is not met.** There were **zero new commercial detector calls**; the 179 historical commercial observations remain unchanged. No additional payment, hosted inference or humanizer service call was made.

## Independent reader results and retained choices

The [score-blind paired review](blind-review.md) accepted all six candidates as faithful, checking 30 grouped source constraints with exact quotations. It slightly preferred v1.8 for the support email, slightly preferred v1.9 for the technical note, and found the reflection a tie; the original reflection was already strong. This is mixed evidence, not an overall naturalness win for v1.9.

The technical version keeps medians explicitly attached to their workers and places the reporting duty near the evidence. The email's older version has a better apology/status/follow-up order for this reviewer. The new reflection's `either` has a loose connection to compliant after-reading phone use; it remains an optional local issue, not a material change of facts. The tied reflection retains the older candidate as its editorial choice, while every original and variant remains available. No manuscript was changed after scoring to hide a weakness.

`results.json` records the **highest-scoring faithful complete text** separately from the **editorial choice**, including their exact hashes. A score improvement never silently replaces the reader-preferred option. The new English guidance is released as a richer set of contextual editing decisions with a demonstrated use in one technical case, not a universally superior rewriting recipe. The [previous skill](retained-skill/) is retained byte-for-byte.

## What actually ran

- Sources were newly generated synthetic fixtures and frozen before inference. They are not real customer transactions, personal memories or production tests.
- An independent source review covered every paragraph before writing. Both arms received the same saved triage. One writer used v1.8; another used v1.9. Both performed fidelity and reader self-review.
- The baseline writer had a fresh context. The experimental writer retained its earlier source-review context after the subagent thread limit prevented another fresh writer. This asymmetry is a confound, recorded in [the protocol](PROTOCOL.md).
- The paired reviewer was independent of writing and blind to method labels and candidate scores, but had prior reference-audit context. These are separate AI-agent reviews, not human evaluations or a cross-model study.
- All six final candidates were frozen and passed the independent gate **before** native scoring. No score-driven best-of-N search occurred.
- Nine successful local runs measure three originals and six candidates. The technical original initially failed twice with Windows memory error 1455; after the user freed memory, a distinct run succeeded. Both failure receipts and the original no-score review are preserved. Failures were never treated as Human scores, and detector settings/weights were unchanged.
- Each successful measurement has a complete anchored document review. Independent editorial ledgers were written without candidate scores; the parent attached native output and reviewed deletion sensitivities after measurement. Such sensitivity is not a paragraph authorship probability or a reason to delete content.

## Reproduce the evidence checks

From the repository root run `python -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'` and `python benchmarks/verify_evidence.py`. The offline suite checks preserved historical records and this experiment's inputs, results, exact spans, review coverage, blinded mappings, selections and skill hashes. It does not reproduce subjective judgments or establish detector accuracy. Re-running inference requires the separately installed trusted detector and pinned weights; no model weights are bundled here.

The final [release audit](release-review.md) records checks and limitations. No claim of universal detector acceptance or human authorship is made.
