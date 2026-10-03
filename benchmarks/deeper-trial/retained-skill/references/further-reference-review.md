# Expanded reference review — 2026-10-03

This follow-up screened selected sections of 13 additional skill repositories and 3 research implementations. Together with the earlier 19 skill repositories, the inventory now covers 32 skill repositories, many related or derived, and 3 method implementations. This is not 35 independent validations. [The additional manifest](further-sources.json) records commits, file hashes, licensing evidence, the precise review scope and the decision for every entry. Some large entrypoints were only partially read; these limits are explicit. No upstream scripts, model training or paid API evaluation were executed.

## What the new sources change

| Family and examples | Useful hypothesis or guidance | Limitation applied here |
| --- | --- | --- |
| Positive editing examples: forjd/better-writing, amanmaqsood/prose-humanizer | Teach the relation between clauses with a short before/after example; evaluate content, authorial choices and expression separately. | A synthetic example is not a human-written training pair. Preserve the source's genre and uncertainty. |
| Discourse editing: NulightJens/humanizer-stack, IsaacEryn/humanizer-ko | Inspect the function of paragraph openings and closings, not just individual words. | Findings on story structure do not establish a universal rule for memos. Never invent a tangent, feeling or unresolved question. |
| Korean clause editing: devswha/patina, hjongc/humanizer-kr, ptec07/humanize-korean, yeomin4242/humanize-sepia | Repair noun-heavy clauses, retain topic continuity and keep local evidence anchors. | ptec07 explicitly derives from im-not-ai; it is not independent corroboration. Reject compulsory fragments, sentence-length quotas and blanket weakening of claims. |
| Genre/process catalogs: AIScientists-Dev/academic-humanizer, puneethkotha/humanizer-workbench, MADEVAL/HumanAI | Separate genre decisions from the refinement/audit stages. | Research, proposals, support messages and essays need different voices. HumanAI's listed languages do not include Korean. |
| Large rule catalogs: harshaneel/humanize, brandonwise/humanizer | Supply candidate problems to inspect in context. | Punctuation, word bans and invented perplexity scores cannot certify authorship or reproduce a commercial model. Curly quotes are ordinary typography. |

Two original prototypes tested these hypotheses: reader-purpose/discourse composition and contrastive clause editing. They live in the repository's `benchmarks/deeper-trial/` evidence archive, not as a replacement default. Their performance must be read from that experiment; source popularity and rule counts are not evidence of improvement.

## Research methods are not interchangeable with a skill prompt

**SICO** optimizes in-context examples against a proxy detector. Its published evaluation used GPT-3.5 and six contemporary detectors on three tasks. The prototype here uses original synthetic editing examples, without SICO's optimized human exemplars or training procedure. It is not a replication and inherits none of SICO's performance claims. [Paper](https://arxiv.org/abs/2305.10847) · [implementation](https://github.com/ColinLu50/Evade-GPT-Detector)

**HIP** minimally adapts base models with AI-to-human rewrite pairs and then applies the trained paraphraser repeatedly. The paper evaluates 256 English passages from eight source categories and scores both semantic retention and commercial detector output. Its prompt tags alone are not the trained model; neither its English results nor its earlier detector versions establish present Korean performance. No adapter was trained or run here. The local feasibility check found CPU PyTorch and no CUDA device; it did not establish that CPU inference is impossible. [Paper](https://arxiv.org/abs/2605.19516) · [implementation](https://github.com/YixuanEvenXu/humanization-by-iterative-paraphrasing)

**MASH** uses supervised style transfer, preference optimization and inference refinement. Its paper evaluates English domains with three open detectors and Writer/Scribbr. That is a different model and test setting, not evidence that adding its terminology to a skill will pass GPTZero or QuillBot. The repository states research-only use and provides no root license file; no code was copied or executed. [Paper](https://arxiv.org/abs/2601.08564) · [implementation](https://github.com/githigher/MASH)

## Current vendor facts

GPTZero explicitly states that it stopped using perplexity and burstiness in autumn 2023. Its current language list includes Korean. This rules out treating old surface-statistic advice as the current vendor's disclosed decision formula; it does not imply that rhythm can never correlate with any classifier output. [Architecture change](https://support.gptzero.me/articles/9585228410-how-do-i-interpret-burstiness-or-perplexity) · [supported languages](https://support.gptzero.me/articles/1682612063-what-languages-does-gptzero-support)

In the actual UI observations, GPTZero reports a Human document-class probability; QuillBot describes its output as the percentage of words likely generated or refined with AI and exposes a Human-written category. Their 85 and 17 readings on the same prior Korean candidate do not denote the same probability. Native scores, language and model version must remain separate. No formula combining them certifies a human author.

## Concrete maintenance finding

An independent blind review found that a previous library rewrite omitted the stated remit and stage of the review. The v1.5.1 instruction therefore explicitly protects a document's purpose and place in a decision process when removing apparent framing. This is a narrow fidelity correction. Strict `gt`/`lt` operators also make the offline checker distinguish “above 50” from “at least 50.” Neither change is advertised as a detector-performance breakthrough.
