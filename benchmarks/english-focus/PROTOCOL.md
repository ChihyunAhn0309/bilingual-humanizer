# English-focused development comparison

Predeclared before candidate drafting on 2026-10-03. All three sources are newly AI-authored synthetic fixtures, not records of real customers, experiments or personal experiences. Sources were frozen before their first detector run.

Compare the retained v1.8.0 skill with the English-focused v1.9.0 instruction candidate on a support email, a reading reflection and a technical update. A fresh-context writer for each arm receives its assigned skill, the same original sources and the same source evidence review. One complete candidate per arm and source; at most one necessary fidelity repair before scoring. No score-led best-of-N sampling. The detector model and weights stay fixed.

Independent review receives source and randomly labeled candidate pairs, without arm labels or candidate scores. Review fidelity and reader quality separately. A failed candidate is ineligible until its material error is repaired and rechecked. Editorial preference can be a tie or the original; a higher detector score does not settle it. Record blinding limits honestly.

Run the installed local detector serially on frozen inputs. The English native Human class is reported alone; AI-edited and Humanized are not counted as Human. Preserve failures and retry at most once for a transient execution failure, never to seek a favourable value. If runtime remains unavailable, continue editorial review and report missing measurements rather than manufacturing a probability. This is the separately installed experimental four-class model, not GPTZero or QuillBot, and its outputs are not verified authorship probabilities.

Full-document reviews before and after rewriting record exact evidence and retain/revise decisions. Preserve original, baseline and experimental candidates. Select a faithful native-score checkpoint separately from the editorial choice. Promote instruction refinements only if independent review supports useful behaviour and the final release audit finds no material regression in scope or fidelity; do not promise universal detector gains from three development samples. Preserve v1.8.0 byte-for-byte regardless of outcome.

No additional payments, paid APIs, commercial detector calls or upstream code execution. References are source/document inspections; vendor performance is not reproduced by reading marketing pages. Both writers and the independent reviewer are AI agents, not human evaluators; this is not a multi-model or statistically powered evaluation.

## Execution deviations recorded before candidate scoring

- The subagent thread limit prevented a new experimental writer. The experimental arm uses the source-review agent in its existing separate context; the baseline writer has a fresh context. Both receive the same saved source triage and are instructed not to read the other arm. The experimental writer's prior source analysis is a confound: any preference cannot be causally attributed to the instruction version alone.
- The technical source and its first retry failed with Windows error 1455. The user then freed memory; the read-only OS check showed available virtual memory increasing from about 2.1 GiB to 5.9 GiB. A distinct `source-score-recovered` invocation was started after that external resource change. Original failure receipts are retained. This is a resource-recovery attempt, not score selection; no model setting changed.
