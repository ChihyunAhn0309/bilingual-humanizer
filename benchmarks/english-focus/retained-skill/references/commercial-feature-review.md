# Public commercial features — 2026-10-03

Scope: official public product pages and one primary research paper. No proprietary code, weights, training corpus or private detector formula was obtained. Marketing percentages below are not reproduced as measured performance. Existing public-skill snapshots, including im-not-ai, remain in the source manifests; this review adds product evidence rather than counting derived skills again.

| Source | What its public page describes | Decision for this skill |
| --- | --- | --- |
| [QuillBot Humanizer](https://quillbot.com/ai-humanizer) | Genre modes, sentence-level refinement, editorial rules and fine-tuned models trained on curated writing. Its listed humanizer languages are English, Spanish, French, German and Portuguese. | Separate reading knowledge, register and rewrite scope; evaluate wording in context. Korean detector support does not imply Korean humanizer support. Prompt instructions do not reproduce its trained model. |
| [Undetectable AI](https://undetectable.ai/ai-humanizer) | Readability and purpose controls. Its FAQ distinguishes a free basic model from the promoted detector-oriented model. | Infer audience and purpose explicitly. Do not use paid-model claims as evidence for a free product or for our skill. No paid trial activated. |
| [WriteHuman](https://writehuman.ai/) | Prose restructuring, voice retention, sentence-level detection and an updated model. The landing page shows platform scores without a reproducible test corpus in the inspected material. | Preserve source-supported voice and evaluate exact candidates. Displayed promotional scores do not establish a comparative benchmark. No proprietary algorithm is inferred. |
| [StealthWriter](https://stealthwriter.ai/humanizer) · [changelog](https://beta.stealthwriter.ai/changelog) | Compare-and-review workflow; model variants emphasizing coherence/readability. Its FAQ explicitly rejects a guaranteed detector score and asks writers to check facts and citations. | Review semantic fidelity separately from fluency; retain effective passages. Model names do not reveal implementable training methods. |
| [HIX Bypass](https://hixbypass.com/humanize-ai) | Context-sensitive rewriting, multiple modes, language support, and adding emotional nuance; broad performance guarantees. | Use genre and context controls. Reject invented emotion, unsupported guarantees and claims that grammatical quality proves authorship. |

## What research adds

[DAMAGE](https://arxiv.org/html/2501.03437v1) audits 19 humanizers and studies detection of their output. Its fluency/faithfulness categories are separate from evasion performance. Some tools changed meaning or degraded readability, and its detector was trained to recognize humanized text. The authors are affiliated with Pangram Labs, a detector vendor; this is primary research, not a neutral certification of commercial products. Its 2025 results do not measure today's versions or establish Korean performance.

Earlier reviewed SICO, HIP and MASH likewise involve optimized examples, trained paraphrasers or preference training; see [the expanded review](further-reference-review.md). Renaming instructions after those methods is not replication. The earlier local HIP-style base-model probe failed fidelity and was not promoted.

## Implementable without new service charges

The adopted changes are explicit editorial controls, evidence-backed voice cues, choosing an appropriate edit unit, comparing local alternatives when useful, and preserving exact expressions. They use the existing language model and ordinary review; no new API dependency is introduced. Existing account usage limits still apply.

These are quality and controllability changes. Their detector impact must be evaluated separately on exact final files and fresh genres. A vendor's own detector is not an independent check of its humanizer. Any direct vendor trial belongs in the benchmark archive with access limits, input identity, output and fidelity findings; it is not proof that this skill implements the vendor.
