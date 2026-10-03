# Independent English-humanizer reference audit

Reviewed 2026-10-03 against installed `bilingual-humanizer` version 1.8.0. This is a source-code/document audit, not a rewrite-performance experiment. No upstream instructions were followed, code installed or executed, accounts created, payment made, text submitted to services, or model inference run.

Scope: nine of the original twelve repositories; `apoapostolov/humanizer`, `keez97/humanizer`, and `dongshuyan/compass-skills` were reserved for the parent review. The parent subsequently added other repositories, which are outside this audit. All 30 saved files for these nine repositories match the SHA-256 values in [repositories.json](repositories.json); 28 were content-read, while the Russian combined `SKILL.md` and LeahLiang's Chinese `README.md` were hash-checked only. Nine additional pinned reference files were content-read and saved under [independent-extra](independent-extra/manifest.json), with URL, commit, timestamp, size and SHA-256.

The installed baseline is already unusually complete on proposition preservation, meaning maps, claim/qualification dependencies, reader routes, genre, voice evidence, term consistency, and bounded review. Most generic advice in these repositories duplicates it. The useful next changes are specific diagnostic operations and English examples, not more global prohibitions.

## Cost and licensing evidence

“Prompt-only” means the inspected editing instructions do not require a dedicated paid humanizer API. It does not mean the host assistant is free, offline, or private. A local Markdown file does not establish where the host model processes text.

| Repository and pinned commit | Dependency established by inspected material | License evidence |
| --- | --- | --- |
| andreaskonopka/humanizer `862609a2` | Prompt/reference files; no required humanizer API in inspected instructions | Full root MIT grant, Andreas Konopka, 2026 |
| ZaynJarvis/ai-writing-humanizer `7e9a8096` | README explicitly describes a static prompt with no external API key | README says MIT; root `LICENSE` request returned 404. License assertion present, full grant not captured; do not call this confirmed unlicensed |
| mgannotti/humanizer `dcd29ecb` | Prompt for Scout; README asserts local runtime/no third-party transmission, without inspected runtime implementation | Root `LICENSE` request returned 404; neither inspected file supplies a grant. Licensing unresolved, not a proof that no license exists anywhere |
| thevseprod/humanizer-ru `6ae6562c` | Standalone Markdown rules; chosen host LLM still required | Full root MIT grant, thevseprod, 2026 |
| henmuc/codex-academic-humanizer `496d5d89` | Prompt/reference files; no required dedicated API in inspected workflow | Full root MIT grant, contributors, 2026 |
| LeahLiang/humanizer `2b186179` | Remote service wrapper requiring an account/key and metered quota; submit/poll HTTP client, no local rewrite model | Full root MIT grant for repository code, ReduceAIGC Skill Contributors, 2026; that does not make service usage free |
| blader/humanizer `225a6f39` | Prompt-only workflow for a host assistant | Full root MIT grant, Siqi Chen, 2025 |
| amanmaqsood/prose-humanizer `8a7ec74c` | Prompt needs no dedicated API; README describes optional local Node CLI. CLI implementation not inspected or executed | Full root MIT grant, Aman Maqsood, 2026 |
| leoluyi/skills `8a85670f` | Humanizer instructions explicitly require no external tools/API | Full root MIT grant, Lu Yi, 2026; pinned per-skill `NOTICE` confirms this skill's MIT status and records upstream attribution |

## What each source actually contributes

### andreaskonopka/humanizer

The workflow edits structure before language: repeated triads, punctuation pivots, interpretive tails, concession followed by reassurance, tidy endings, false ranges, and repeated parallel rhythm. Its English catalog treats punctuation and word choice contextually and follows publication typography. Useful additions are the **concession-reset arc** and **false range** as explicit review leads: preserve a limitation instead of automatically neutralizing it, and distinguish a meaningful scale from unrelated examples linked by “from/to.” These sharpen existing generic contrast/transition guidance.

Cautions: do not adopt the instruction to change list count merely to avoid three. Do not reassign vague attribution to the author or delete a claim solely because its source is not named. Its English artifact-cleaning suggestions also include changing URL parameters, which conflicts with the installed exact-material policy unless authorized.

Content read: [SKILL.md](https://github.com/andreaskonopka/humanizer/blob/862609a2caf3cadb63b9bef78576e6f5a1ed4e19/skills/humanizer/SKILL.md), [README.md](https://github.com/andreaskonopka/humanizer/blob/862609a2caf3cadb63b9bef78576e6f5a1ed4e19/README.md), [LICENSE](https://github.com/andreaskonopka/humanizer/blob/862609a2caf3cadb63b9bef78576e6f5a1ed4e19/LICENSE), and extra [patterns-en.md](https://github.com/andreaskonopka/humanizer/blob/862609a2caf3cadb63b9bef78576e6f5a1ed4e19/skills/humanizer/references/patterns-en.md). [Pinned English catalog](https://github.com/andreaskonopka/humanizer/blob/862609a2caf3cadb63b9bef78576e6f5a1ed4e19/skills/humanizer/references/patterns-en.md).

### ZaynJarvis/ai-writing-humanizer

Actual method: diagnose a 27-item inventory, subtract mechanical patterns, restore suitable delivery, then audit. The English catalog adds useful granularity around adjective/appositive accumulation, reader-moralizing, emotion labels, generic address and over-explaining. Most of these are already covered by the installed actor/predicate and genre controls; use new examples rather than adding another long inventory.

Cautions: its 0/0.5/1 scoring is an uncalibrated editing count, not an authorship probability. English has 25 entries while the top-level denominator includes two Chinese-specific entries. Requiring fewer list items, prescribing vocabulary substitutions, converting imperatives into observations, or making dates “timeless” can lose content, force, or scope. “Add a scene/detail” must remain conditional on source evidence. README success language supplies no independent performance evidence.

Content read: [SKILL.md](https://github.com/ZaynJarvis/ai-writing-humanizer/blob/7e9a8096b8cb2dadbca7ffde41dc0efc4c8a4b60/SKILL.md), [README.md](https://github.com/ZaynJarvis/ai-writing-humanizer/blob/7e9a8096b8cb2dadbca7ffde41dc0efc4c8a4b60/README.md), extra [ai-tells-en.md](https://github.com/ZaynJarvis/ai-writing-humanizer/blob/7e9a8096b8cb2dadbca7ffde41dc0efc4c8a4b60/patterns/ai-tells-en.md). [Pinned English catalog](https://github.com/ZaynJarvis/ai-writing-humanizer/blob/7e9a8096b8cb2dadbca7ffde41dc0efc4c8a4b60/patterns/ai-tells-en.md).

### mgannotti/humanizer

A short prompt inventory covers filler, symmetrical prose, punctuation, corporate vocabulary, unsupported universals and recap endings, followed by audience calibration and a clean rewrite. No distinct method beyond the installed skill was established. Its explicit instruction to preserve asserted claims and flag missing support is sound and already present locally.

Cautions: mechanically cutting some sentences to three words, deleting every transition-only sentence, or replacing generic claims with numbers/examples would create artificial cadence or inventions unless constrained. README's runtime/privacy statement is a project assertion; it was not verified against Scout implementation. Do not extrapolate it to any assistant that loads the prompt.

Content read: [SKILL.md](https://github.com/mgannotti/humanizer/blob/dcd29ecbd788037bb3b1875864472e7f2326a672/SKILL.md), [README.md](https://github.com/mgannotti/humanizer/blob/dcd29ecbd788037bb3b1875864472e7f2326a672/README.md).

### thevseprod/humanizer-ru

The English rules use a rewrite followed by a naturalness/fact/voice review. They explicitly protect superlatives or temporal words that carry actual claims, calls to action, deadlines, warnings and an author's peculiarities. The strongest distinct operation is to **read all paragraph-opening sentences in sequence**: if they merely announce upcoming topics, replace redundant staging with actual content. Another useful English diagnostic is unpacking dense noun compounds; use ambiguity/readability, not a fixed noun count, as the trigger.

Cautions: reject its em-dash ban, forced first person/stance, rigid paragraph sizes, hedge-count threshold, and five-rule authorship verdict. Claimed sample-count limits and “nothing uploaded” assurances are unsupported for arbitrary host LLMs. Its suggested objections and strong endings can invent reactions or conclusions. The preservation rules and these prescriptions are internally in tension.

Content read: [humanizer.en.md](https://github.com/thevseprod/humanizer-ru/blob/6ae6562cbf2cf97f298e94be2f2bf134da5ada6d/humanizer.en.md), [README.md](https://github.com/thevseprod/humanizer-ru/blob/6ae6562cbf2cf97f298e94be2f2bf134da5ada6d/README.md), [LICENSE](https://github.com/thevseprod/humanizer-ru/blob/6ae6562cbf2cf97f298e94be2f2bf134da5ada6d/LICENSE). Combined Russian/English `SKILL.md` was not content-read.

### henmuc/codex-academic-humanizer

Actual method: calibrate language, intensity, sample and paper section; revise with stable terminology; compare factual content; return clean prose and comparison notes. Useful specificity lies in section functions: abstracts compact the problem/approach/result; introductions connect gap to response; related work separates prior findings from contribution; methods preserve reproducible sequence; results preserve values/baselines; discussion distinguishes observation from interpretation; conclusions do not invent future work.

This is a worthwhile compact English-academic subsection, since the installed genre table is broader. Terminology maps, protected LaTeX/citations and cautious claim language duplicate existing protections.

Cautions: do not transplant mandatory dual output, default paragraph immutability, or a mechanical “aims to” → “examines” replacement: purpose, completion and authorship still require checking. Detailed academic pattern catalogs referenced by this project were not inspected, so its advertised 36-pattern coverage is not independently evaluated here.

Content read: [SKILL.md](https://github.com/henmuc/codex-academic-humanizer/blob/496d5d897d920d1c8f0d382e31406eeff0f29e45/SKILL.md), [english-academic-style.md](https://github.com/henmuc/codex-academic-humanizer/blob/496d5d897d920d1c8f0d382e31406eeff0f29e45/references/english-academic-style.md), [style-control.md](https://github.com/henmuc/codex-academic-humanizer/blob/496d5d897d920d1c8f0d382e31406eeff0f29e45/references/style-control.md), [README.md](https://github.com/henmuc/codex-academic-humanizer/blob/496d5d897d920d1c8f0d382e31406eeff0f29e45/README.md), [LICENSE](https://github.com/henmuc/codex-academic-humanizer/blob/496d5d897d920d1c8f0d382e31406eeff0f29e45/LICENSE).

### LeahLiang/humanizer

This is an external inference client, not a disclosed free editorial method. The Python client requires a key, sends input to an English/Chinese job endpoint, and polls for the server result. English has a single mode charged against word quota. No account, call or payment was attempted.

Its English README example fails a direct source comparison: the original discusses gliomas arising from glial cells; the rewrite introduces patients developing lymphomas and an immune-cell mechanism. This is observable subject/mechanism substitution, without needing to decide which medical assertions are true. The Chinese example also introduces interviews, incentives and named company details absent from the source. Detector-success claims cannot override those fidelity failures.

Adopt no editorial method from this wrapper. It is useful negative evidence for distinguishing free source code from metered inference and fluency from semantic preservation.

Content read: [SKILL.md](https://github.com/LeahLiang/humanizer/blob/2b186179184f3f1c2956312348faef80f03b7ea2/SKILL.md), [README.en.md](https://github.com/LeahLiang/humanizer/blob/2b186179184f3f1c2956312348faef80f03b7ea2/README.en.md), [humanizer_api.py](https://github.com/LeahLiang/humanizer/blob/2b186179184f3f1c2956312348faef80f03b7ea2/scripts/humanizer_api.py), [LICENSE](https://github.com/LeahLiang/humanizer/blob/2b186179184f3f1c2956312348faef80f03b7ea2/LICENSE). Chinese `README.md` was not content-read.

### blader/humanizer

The pinned version leads with staging and discourse patterns, drafts, self-critiques, then rewrites. Its newer **wrong-reader** check is useful: where surrounding correspondence actually establishes shared knowledge, bring the decision forward and avoid reconstructing the recipient's own background. Apply this only within the requested rewrite scope; known context is not blanket permission to drop source facts. A related useful check catches an argument against an alternative nobody raised, while preserving real trade-offs.

Cautions: no-dash rules, unconditional word flags, adding reactions, deleting unsupported-looking claims, and priority rankings are editorial prescriptions rather than validated detector facts. The pre-November-2022 authorship exemption is not a valid general boundary. README's 16/16 preference claim was not reproduced or independently verified. Several illustrative rewrites add or remove substantive claims; do not use them as fidelity exemplars.

Content read: [SKILL.md](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/SKILL.md), [README.md](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/README.md), [LICENSE](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/LICENSE).

### amanmaqsood/prose-humanizer

The source separates semantics, authorial decisions and expression, uses a source ledger, and reviews fidelity separately from voice/naturalness. Most of this already exists locally. Distinct refinements: test whether a generic sentence could migrate to an unrelated topic unchanged; test whether topical nouns conceal no plainly expressible claim; and assess each voice feature independently. Its voice reference differentiates typed, dictated, translated, collaborative and AI-edited samples: evidence for cadence need not establish punctuation, humor or stance. Conflicting samples can imply channel-specific variation rather than an averaged persona.

Cautions: some reference vocabulary defaults remain too broad; removing attribution, placeholders or URL parameters automatically can conflict with preservation. The optional CLI and benchmark were described, not code-audited or run. Their claimed checks are not proof of general quality or detector performance.

Content read: [SKILL.md](https://github.com/amanmaqsood/prose-humanizer/blob/8a7ec74c198ceaaed11fa3560e78bb94a6c1a7fe/SKILL.md), [README.md](https://github.com/amanmaqsood/prose-humanizer/blob/8a7ec74c198ceaaed11fa3560e78bb94a6c1a7fe/README.md), [LICENSE](https://github.com/amanmaqsood/prose-humanizer/blob/8a7ec74c198ceaaed11fa3560e78bb94a6c1a7fe/LICENSE), extra [voice.md](https://github.com/amanmaqsood/prose-humanizer/blob/8a7ec74c198ceaaed11fa3560e78bb94a6c1a7fe/references/voice.md) and [patterns.md](https://github.com/amanmaqsood/prose-humanizer/blob/8a7ec74c198ceaaed11fa3560e78bb94a6c1a7fe/references/patterns.md). [Pinned voice reference](https://github.com/amanmaqsood/prose-humanizer/blob/8a7ec74c198ceaaed11fa3560e78bb94a6c1a7fe/references/voice.md).

### leoluyi/skills / humanizer-zh

The workflow distinguishes audit/rewrite/file modes, protects exact material, chooses edit scope, rewrites, checks source traceability, and reviews the completed output. The English layer is explicitly present; the repository name should not make it disappear from English research. Particularly useful review mechanics: one defect gets one finding even if several pattern labels overlap; a contextual exception remains effective under synonymous labels; and an empty paragraph receives a concrete repair direction rather than invented content. These improve audit quality more than a pattern count does.

The English catalog covers announcement scaffolding, hollow lists/tables, vague relationships, artificial emotion, artifact self-description and merge seams, mostly already represented in the local structural guidance. Reject numerical dash/format/TTR quotas, automatic authorship expectations, forced first-person or near-zero-hedging voice profiles, and silent URL/placeholder edits. Do not infer that every unreferenced factual claim is fabricated. Its language-of-request rule would also conflict with preserving source language unless translation is requested.

Content read: [SKILL.md](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/skills/humanizer-zh/SKILL.md), [README.md](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/README.md), [LICENSE](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/LICENSE), extra [routing](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/skills/humanizer-zh/references/finished-prose-routing.md), [review criteria](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/skills/humanizer-zh/references/review-criteria.md), [workflow](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/skills/humanizer-zh/references/finished-prose-workflow.md), [English rules](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/skills/humanizer-zh/references/en-rules.md), and [NOTICE](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/skills/humanizer-zh/NOTICE). [Pinned English rules](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/skills/humanizer-zh/references/en-rules.md).

## Recommended changes relative to the installed skill

1. **Add a short English discourse checklist with positive fixes and keep conditions.** Cover concession-reset reassurance, false ranges, irrelevant rebuttals and shared-context replies. Each must test whether real claims, recipient needs or useful uncertainty survive. This is more useful than enlarging the word list.
2. **Add two concrete structural probes.** Read paragraph openings together to find repeated announcements; then ask whether a “specific-looking” sentence states an actual proposition. Retain navigation, summaries, deliberate recurring form and ordinary generalizations when they serve the document. Do not turn either probe into a deletion quota.
3. **Expand English syntax examples around dense nominal groups.** Recover relationships/verbs already in the source and check the noun attachment. The installed reference explains nominalization, but not ambiguous stacked noun modifiers. This is a limited editorial extension, not a claim about authorship.
4. **Add compact academic section calibration.** Methods, results and discussion need different editing checks. Preserve required structure and the distinction between intended work, completed procedure, observed outcome and interpretation.
5. **Refine voice evidence handling.** Keep confidence separate by feature, note sample provenance where available, and allow channel variation. Do not demand more samples by fixed count or turn one correction into a permanent profile. Existing voice matching remains the default framework.
6. **Improve requested audit reports without expanding routine output.** Report exact spans with a contextual reason and an actionable edit direction; combine duplicate pattern findings. An allowed usage should not become a defect merely because another label names the same stylistic move. The existing default of delivering only the finished prose should remain.

No additional detector-first mandate, iteration ceiling, randomization target, typo insertion, punctuation blacklist, fixed pattern threshold, external API integration, or inference installation is warranted by this audit. The sources are related community editing heuristics, not nine independent validations of quality or detector behavior.

Baseline content-read: installed `SKILL.md`, `references/english.md`, `references/structural-rewrite.md` (full file recovered across reads), `references/editing-controls.md`, and `references/genres-and-voice.md`. Targeted `rg` checks across other installed references tested whether candidate ideas were already documented; those files were not all read end to end. Incidental root-license reads for newly added `kitfoxs/humanize-mcp` and `vvandriichuk/texthumanize` are not full source reviews; the latter's restrictive noncommercial/commercial split was separately flagged to the parent.
