# English reference review

Reviewed 2026-10-03 for version 1.9.0. The new [English composition guidance](english-composition.md) is an editorial hypothesis, not an empirically validated improvement in writing quality or detector scores. It adds no paid humanizer dependency and does not change the existing review budget.

The review covered 15 repositories and selected primary product, writing and research documentation. These are not 15 independent methods or validations: several share pattern inventories, and three implementation projects received narrower README-level inspection. No upstream code was installed or executed and no commercial rewrite service was called.

## Ideas adopted with constraints

| Source | Contribution to English composition | Boundary |
| --- | --- | --- |
| [apoapostolov/humanizer](https://github.com/apoapostolov/humanizer/blob/0a7633b0f71c9d29d454b4a7b90a78a72fad980a/skills/humanizer/references/required-checks.md) and [Google editing guidance](https://developers.google.com/tech-writing/two/editing) | Recompose related sentences; check continuity and the paragraph's organizing purpose | Do not force combination, a new outline, concrete detail or a numerical quality gate |
| [Google tone guidance](https://developers.google.com/style/tone) and [keez97 voice calibration](https://github.com/keez97/humanizer/blob/2d9a116fa9caee2c3466a7c7d419cbe02b35a470/references/VOICE-CALIBRATION.md) | Choose natural English for the audience; use supplied voice evidence | Contractions are contextual options, not quotas; thin samples do not establish permanent bans or an invented persona |
| [andreaskonopka/humanizer](https://github.com/andreaskonopka/humanizer/blob/862609a2caf3cadb63b9bef78576e6f5a1ed4e19/skills/humanizer/SKILL.md), [thevseprod English rules](https://github.com/thevseprod/humanizer-ru/blob/6ae6562cbf2cf97f298e94be2f2bf134da5ada6d/humanizer.en.md), [blader/humanizer](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/SKILL.md) | Inspect paragraph openings, dense noun groups, false ranges, generic reassurance, irrelevant rebuttals and shared-context replies | Preserve real distinctions, limitations, source facts and useful navigation; infer shared knowledge only from available context |
| [henmuc English academic style](https://github.com/henmuc/codex-academic-humanizer/blob/496d5d897d920d1c8f0d382e31406eeff0f29e45/references/english-academic-style.md) and [COMPASS English rules](https://github.com/dongshuyan/compass-skills/blob/1b2e556ce6f293ba12e95e18d51995d6a969d52f/skills/academic-humanizer/references/rules-en.md) | Calibrate methods, results and interpretation separately; retain functional academic syntax | Do not impose casualness, a new paper template, or unsupported mechanisms and future work |
| [amanmaqsood voice evidence](https://github.com/amanmaqsood/prose-humanizer/blob/8a7ec74c198ceaaed11fa3560e78bb94a6c1a7fe/references/voice.md) | Infer each voice feature separately and account for sample provenance/channel | Dictation can support cadence without establishing punctuation; do not transfer sample facts |
| [leoluyi workflow](https://github.com/leoluyi/skills/blob/8a85670f155490a413014065066ff46f3f37e103/skills/humanizer-zh/references/finished-prose-workflow.md) | Give requested audit findings exact spans, reasons and repair directions; deduplicate overlapping labels | A valid contextual exception cannot be defeated by renaming the same finding; default output remains the finished prose |

Existing fidelity, terminology, meaning-map and voice protections already covered most general advice. The revision therefore emphasizes concrete English compositional decisions rather than enlarging a word blacklist. The instructions and examples are newly written; upstream prescriptions are not adopted wholesale.

## Free access is not free local inference

Public pages for [Ahrefs](https://ahrefs.com/writing-tools/ai-humanizer), [Grammarly](https://www.grammarly.com/ai-humanizer), [QuillBot](https://quillbot.com/ai-humanizer), [Scribbr](https://www.scribbr.com/humanize-ai/), [Clever](https://cleverhumanizer.ai/), [Wordtune](https://support.wordtune.com/en/articles/9024394-wordtune-editor-writing-features), and [Naturalwrite](https://naturalwrite.com/humanizeai) describe free entry points, style options or paragraph-level editing. Their limits, paid features and availability differ. Documentation inspection did not verify an account's quota, unlimited access, output quality or a local backend. Scribbr's QuillBot links do not establish an independent rewriting backend. Proprietary-model claims reveal no reproducible algorithm.

Prompt files can be free to inspect while the host assistant still has costs. LeahLiang's MIT repository wraps a metered remote API; it is not a free local humanizer. TextHumanize's license restricts free use to specified noncommercial purposes and requires paid commercial licensing. Neither is integrated here. Missing root `LICENSE` files were recorded as gaps, not proof that no license exists: ZaynJarvis and xoxxel state MIT in their READMEs; mgannotti's inspected files leave licensing unresolved.

## Research and rejected shortcuts

[DIPPER](https://arxiv.org/abs/2303.13408) studies contextual paraphrasing with controllable lexical/order variation using a trained 11B model. Its reported results do not validate a prompt that merely names similar controls. [DAMAGE](https://aclanthology.org/2025.genaidetect-1.9/) evaluates 19 humanizers; its Pangram-affiliated authorship and tested setting should remain visible when interpreting results. Neither supports a universal ranking or a guarantee for this skill.

Reject detector-score chasing as a substitute for reader benefit and fidelity; arbitrary dash, hedge, sentence-length or vocabulary quotas; forced stances or autobiographical detail; typo/entropy injection; and silently dropping claims, attribution, obligations or exact material. A fluent rewrite can still change the subject or mechanism, as LeahLiang's published example demonstrates. Community success claims, bundled tests and free-tier labels were not treated as independently reproduced performance evidence.

Any later claim of improvement needs its own frozen candidates, meaning checks, independent reader assessment and exact-final detector receipts when detector testing is requested. At release drafting, that evidence has not yet been established for version 1.9.0.


## Focused drafting experiment, 2026-10-03

The English lab revisits composition rather than adding another pattern inventory. Its working diagnosis is that a flat proposition list can preserve facts while reproducing the source's allocation of one point per sentence. The revised guide makes a writer's speech act, stance and focal relationships the drafting brief; the full meaning map remains the fidelity constraint. A brief-only fresh-context alternative was also tested with the original retained by the fidelity reviewer. It changed context as well as instructions, introduced two narrow meaning shifts before repair, and scored below the earlier complete candidate. It was not adopted into the recommended drafting method.

Three public primary editorial sources informed the design:

- [Thomas and Turner, *Clear and Simple as the Truth*, author-hosted excerpt](https://classicprose.com/csx.html): treat style as a writer-reader relationship and a way of presenting a subject, rather than only a collection of verbal techniques. The skill does not import classic style's certainty or disinterested stance into a source expressing uncertainty or advocacy.
- [UW-Madison Writing Center, creating a reverse outline](https://writing.wisc.edu/handbook/processandstructure/reverseoutlines/): distinguish a paragraph's subject from what it does in the argument, then inspect the actual organization. The skill retains all substantive information rather than using restructuring as implicit permission to shorten it away.
- [UNC Writing Center, reading aloud](https://writingcenter.unc.edu/tips-and-tools/reading-aloud/): a sequential hearing can reveal awkwardness, tone and ordering problems missed on the page. The skill asks for an exact-word reader pass, without pretending a silent model review was an audible reading or forcing a conversational register.

These are free-to-read editorial methods, not local inference models, proprietary humanizer algorithms or evidence of detector acceptance. No source prose is copied into the guide. Development evidence and a later fresh transfer check must remain distinct; synthetic sources and score-guided revisions are not human controls or untouched evaluation data. Preserve failed alternatives as well as gains, with all four native classes and exact final-candidate receipts.


The two synthetic development sources do not establish superiority to the retained skill. Under the unchanged local English checkpoint, the selected planning note moved from Human 0.1958% to 0.6336%, while its evidence-first alternative scored 0.5178%. The selected personal review moved from 0.01636% to 25.0669%; the repaired brief-only fresh-context alternative scored 0.1896%. These are native, uncalibrated single-document class outputs, not word shares or authenticated authorship. All four classes, full texts, reviews and failed alternatives were retained in the development record. No commercial transfer or representative accuracy was measured. Fresh comparison against the retained skill is still required before a release-performance claim.
