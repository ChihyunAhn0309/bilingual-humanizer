# Bilingual Humanizer

[한국어](README.ko.md) · [Skill](skills/bilingual-humanizer/SKILL.md) · [Test evidence](benchmarks/2026-10-02/) · [Reference research](skills/bilingual-humanizer/references/research-sources.md)

A Korean–English editing skill that rebuilds AI drafts around their meaning and intended reader. It supports ordinary content, work documents, technical writing, research, and creative prose, including mixed-language documents.

The default is active rewriting: reorganize paragraphs, recast sentences, preserve the source's information, then review the completed draft. It also supports light edits, review-only requests, and matching a supplied voice sample.

![Editorial workflow with an optional detector evidence stage](docs/assets/workflow.png)

[Editable PowerPoint](docs/assets/workflow.pptx) · [Design draft](docs/assets/composition-draft.png) · [Figure validation](docs/figure-evidence/render-review.md). The diagram was created using [JYS1025/paper-figure](https://github.com/JYS1025/paper-figure). External findings can inform another editorial review; that optional return path is described in the skill rather than drawn in this overview.

## Current release: v1.9.0

English is the focus of this update: recompose clauses from meaning, connect information naturally, choose register without forced casualness, and preserve academic section roles. Reviewed 15 repositories and seven product documentation surfaces; no paid humanizer integration. Korean guidance and the revision ceiling are unchanged.

Three synthetic sources received paired v1.8/v1.9 rewrites and nine successful local measurements. The new candidate had a higher native Human score in 3/3 comparisons; independent reader preferences were mixed (old email, new technical note, tied reflection). These experimental class scores do not certify authorship or commercial-detector success. [Full measured results and limitations](benchmarks/english-focus/REPORT.md), [research](benchmarks/english-focus/research/REVIEW.md), and [retained v1.8](benchmarks/english-focus/retained-skill/).

## Previous release: v1.8.0

The repaired local detector **v3.1.2** is working. The skill now compares a bounded number of source-grounded complete compositions when stronger detector-oriented rewriting is explicitly requested, with source-fidelity and reader review before scoring. The revision ceiling is unchanged; the best faithful checkpoint is retained separately from editorial preference.

Five new local measurements: Korean library Human **80.12% → 91.46%**; English archive previous-best **0.323% → 0.666%**; fresh English source/candidate **0.0074% → 0.0230%**. These native local class values do not establish human authorship; English remains below 50%. No new commercial transfer is claimed. [Full results, independent reviews and retained choices](benchmarks/composition-feedback/REPORT.md). The prior [v1.7.0 skill](benchmarks/composition-feedback/retained-skill/) and 179 commercial observations remain available.

## Previous release: v1.7.0

The user-authorized detector repair is now published as **v3.1.2**. Both English texts and the installed humanizer adapter ran successfully with unchanged model weights and score semantics. Native Human was **0.083% → 0.323%**, still below 50%. The 27 humanizer skill files are unchanged; the original failure receipts remain archived. [Successful runtime follow-up and actual scores](benchmarks/local-runtime-followup/REPORT.md).

For substantial rewrites, the skill now starts with a trusted installed **bilingual-ai-detector** by default, unless editing without detection is requested. Light edits and review-only tasks remain opt-in for detection. The adapter supports the inspected v3.1 runtime contract; the detector documentation was subsequently updated to v3.1.1 without a runtime change. It preserves an exact input snapshot, local model output and execution record; reviews every paragraph; turns anchored feedback into revise/retain/unresolved decisions; checks meaning against the original; then measures the completed candidate again. Character contributions and paragraph-deletion effects guide inspection, never automatic word bans or deletions. [Workflow and commands](skills/bilingual-humanizer/references/local-detector-loop.md).

This release adds an optional offline adapter and a tested feedback workflow. It does not bundle detector weights, change the detector, or establish universal detection performance. Real trials include rejected higher-scoring edits, fidelity repairs, a separate fresh-source application, and an English runtime failure kept as unavailable. [Complete results and independent reviews](benchmarks/local-feedback/REPORT.md). Prior commercial checkpoints and all 179 external observations remain separate; this phase makes no new commercial transfer claim. The exact [v1.6.0 skill archive](benchmarks/local-feedback/retained-skill/) remains recoverable.

Example: “Use bilingual-humanizer and my installed bilingual-ai-detector alternately. Review every paragraph, apply only justified feedback, preserve the source, and retain the best faithful version.” Ordinary rewriting does not require the detector or Python. Offline detector use has no vendor quota, but still requires local compute and an assistant session.

## Previous release: v1.6.0

Public commercial features informed audience/register/scope controls, source-backed voice cues, and choosing local versus structural edits. An existing consolidation example now preserves both the review's duty to distinguish and the notice's duty to explain. No added review turns, paid service dependency, invented imperfections or detector guarantee. [Research and actual free trials](benchmarks/feature-trial/REPORT.md).

Independent writing and review sessions found no actionable fidelity issue on two new cases. GPTZero Human was **16% → 98%** for a Korean notice and **0% → 0%** for an English memo. The Korean final was 98 words and triggered GPTZero's under-100-word accuracy warning; its source was 101 words, so the comparison crosses that warning boundary. [Renewed free QuillBot checks](benchmarks/quill-renewal/REPORT.md) now show **100% → 100% for both source/final pairs**. The notice final meets both selected >=50 targets on its exact text; the English memo does not. This is not evidence of universal improvement or a QuillBot gain.

The same follow-up tested two faithful new library rewrites. Their GPTZero / QuillBot Human readings were **47% / 14%** and **61% / 17%**, below retained library E at **97% / 30%** (QuillBot rechecked). With another user-provided login, a free commercial output with fidelity repairs reached **68% / 24%**; this also failed to replace E. All three candidates received independent source reviews. At that stage the skill remained v1.6.0 and previous exact checkpoints were retained; worse candidates were not promoted. Nine QuillBot scans completed across the two access periods without payment, with five scans remaining at the last observation. [Results, input hashes, commercial limits and review records](benchmarks/quill-renewal/REPORT.md).

The completed [Cloud experiment and eight desktop checks](benchmarks/continuation-g/REPORT.md) scored GPTZero **0%, 0%, 1%, 6%** and QuillBot **100% on all four**. Korean inputs received a short-text warning. The metrics have different meanings and none of those four candidates met both >=50 targets. All **179 external observations** are archived, including the thirteen renewed-access observations; vendor rewrite self-scores are excluded. [Independent release review](benchmarks/feature-trial/independent-final-review.md) · [Latest publication audit](benchmarks/quill-renewal/publication-audit.md).

## Earlier continuation: v1.5.1 and exact checkpoints

At that stage production remained **v1.5.1**, with all 22 skill files unchanged. [34 new commercial observations](benchmarks/renewal-trial/REPORT.md) tested source-sensitive editing, decision-document structure, and an independently applied v1.5.2 prototype. The requested **each-detector native Human >=50** target remains unmet. The prototype was not promoted. Two local HIP-model outputs were also generated on CPU and rejected for meaning changes before any detector submission.

The [prior checkpoint registry](benchmarks/renewal-trial/checkpoint-registry.json) and [latest overrides](benchmarks/continuation-e/checkpoint-registry.json) retain exact candidates and their own evidence: Korean library **97% GPTZero Human / 30% QuillBot Human-written**; Korean essay **42% / 100%**; English support **0% / 83%**; English museum **0% / 100%**. These are different native metrics on four specific texts, not one authorship probability or a representative success rate. The museum's Sapling AI score is 91.3%; Korean ZeroGPT readings remain 100% AI. Some retained readings were observed earlier; the registries link their original timestamp and matching input hash. No cross-draft score merging occurs.

[Seven further observations](benchmarks/continuation-e/REPORT.md) on refreshed free access raised the library checkpoint from 93% / 15% to 97% / 30%. Another Korean candidate reached 91% / 33% and remains a trade-off alternative; its 33% is not combined with the other candidate's 97%. The new English support candidate fell to 0% / 72%, so the previous text was kept. Independent source/final reviews are included, and no universal skill improvement is claimed.

The prior release is recoverable from [its exact archived files](benchmarks/deeper-trial/retained-skill/). New challengers must preserve meaning and reader quality before replacing a checkpoint; missing checks and regressions do not overwrite it. [Prototype audit](benchmarks/renewal-trial/final-skill-audit.md) and [evidence audit](benchmarks/renewal-trial/final-evidence-audit.md) record the independent-context checks and their limitations.

## Previous release: v1.5.1

This is a narrow fidelity and reporting fix, **not a demonstrated detector-performance breakthrough**. It explicitly preserves a document's review purpose and decision stage when rewriting an opening. The offline checker now supports strict `gt`/`lt`: exactly 50 does not pass a target of Human >50.

Two additional rewriting prototypes were tested after screening 13 more skill repositories and 3 research implementations. They are not adopted as defaults. In the [32-observation follow-up](benchmarks/deeper-trial/REPORT.md), the same English museum candidate received GPTZero Human 0% and QuillBot Human-written 100%; Korean library A received 60% and 11%. Fresh Korean prose dropped from GPTZero Human 42% to 2% under prototype B. The independent v1.5.1 library output received GPTZero Human 50% and ZeroGPT AI GPT 100%, with QuillBot unavailable after its free quota at that time; the continuation above later measured Human-written 12% on that exact text. **The requested each-detector Human >50 target remains unmet.** The two Human columns have different native units and are not authorship certificates.

[Independent skill audit](benchmarks/deeper-trial/final-skill-audit.md): the library output preserved facts and purpose; 45 regression tests plus 10 additional boundary/metric checks passed. [Final archive audit](benchmarks/deeper-trial/final-evidence-audit.md) checks publication evidence separately. These are fresh-context AI reviews, not human ratings. [Expanded reference review](skills/bilingual-humanizer/references/further-reference-review.md) records what was examined and why unsupported rules were rejected.

## Rewriting approach introduced in v1.5

- Establish a positive editorial brief before cleanup; consolidate repeated functions without preserving each staging sentence.
- Compare repeated instructions by actor, action, object, occasion and force; recompose abstract predicates in each language.
- Compose paragraphs from a map of facts, qualifications, opinions and reader actions, instead of following the original sentence skeleton.
- Keep dependent claims together: a measured median stays near its missing-distribution limitation; a proposal stays near its approval status.
- Combine repeated framing while preserving distinct review, notice and approval instructions.
- Apply Korean particles, predicates, honorifics and sentence boundaries directly; apply English information flow and register without forced slang or punctuation bans.
- Add contextual Korean discourse checks informed by [im-not-ai](skills/bilingual-humanizer/references/im-not-ai-review.md): preserve useful contrast and modality, clarify referents, and catch new formulaic phrasing introduced by editing.
- Review fidelity and naturalness separately. Use a fresh-context reviewer when explicitly requested or permitted. Keep actual review counts and evidence honest.

The improvement is a drafting-method change. The default revision ceiling remains three; increasing the number of turns is not the feature.

## Use

Install `skills/bilingual-humanizer` as a skill directory in your agent's skills location. For Codex, ask the built-in skill installer:

> Install the skill from https://github.com/ChihyunAhn0309/bilingual-humanizer at skills/bilingual-humanizer.

Or copy that directory into `$CODEX_HOME/skills/bilingual-humanizer` (typically `~/.codex/skills/bilingual-humanizer`). Review an existing installation before replacing it. Start a new session if the host does not refresh its skill catalog automatically.

Example requests:

```text
Use bilingual-humanizer to actively rewrite this memo.
Keep all facts, qualifications, numbers and requests; rebuild the structure if useful.

이 글을 bilingual-humanizer로 자연스럽게 다시 써줘.
사실·조건·말투는 유지하고 문장과 문단 구조는 적극적으로 바꿔줘.

Match the style of the supplied sample, using only the draft as the source of facts.

Review this text without rewriting it. Point to specific awkward passages.
```

For requested commercial detector checks, supply usable service access or existing reports. The local detector requires a separate trusted installation and its supported Python environment. The skill does not bundle vendor accounts, API clients, or a paid subscription. It records settings, input hashes, scope and receipts. Missing, stale, unsupported or blocked results are never counted as passed.

## v1.5 measured outcome

**Historical v1.5 decision:** a shorter reader-led instruction produced some development gains, but 17 further observations did not show an improvement on fresh topics; blind reader review also slightly preferred v1.5 on both fresh texts. The [additional experiment and retention decision](benchmarks/additional-trial/REPORT.md) disclose all outcomes. At that point production files were unchanged; that exact 20-file v1.5 snapshot is now archived with the experiment. The v1.5.1 maintenance changes are described above.

The Korean technical development memo improved from 92% to 0% AI in QuillBot and from 100% to 79% AI in GPTZero. Other results worsened: the Korean library memo rose from 11% to 32% AI in GPTZero; the final English technical memo rose from 93% to 94.6% in Sapling and from 0% to 24% in QuillBot. **Broad detector acceptance has not been achieved.**

Two fresh paired texts did not demonstrate a detector improvement, and blind model review slightly preferred v1.4 in five of six cases. Read the [complete v1.5 experiment](benchmarks/2026-10-02-v15/REPORT.md), including final-text hashes, all regressions and the unsuccessful detached-composition trial. The earlier 88.2% Sapling result belongs to a candidate before a fidelity repair, not the final text.

## Evidence and limits

The repository includes synthetic source texts, frozen rewrites, real commercial detector observations, review records and reproducible local checks. The small development smoke test is **not an accuracy benchmark or a guarantee of detector acceptance**. All trial texts—including the rewrites—were AI-produced. There is no human-authored control, representative sampling, or human/cross-model validation.

Detector results disagree, and some revised texts still receive high AI scores. Scores are reported in their original units; they are not averaged across products or treated as proof of who wrote a text. See the [commercial test report](benchmarks/2026-10-02/REPORT.md) for complete outcomes and access limitations.

Editing without detection runs entirely as instructions. Python is needed for the optional offline audit helpers and installed-local-detector adapter:

```sh
python skills/bilingual-humanizer/scripts/audit_preservation.py source.txt rewrite.txt
python -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
```

The preservation helper finds surface changes, not semantic truth. `check_detector_report.py` checks report consistency and hashes; it makes no external calls and cannot authenticate a receipt. See its [report format](skills/bilingual-humanizer/references/detector-report-format.md).

![Observed v1.5 development comparisons](docs/assets/detector-v15-comparison.png)

[Earlier v1.4 chart](docs/assets/detector-observations.png)

## Sources and license

The inventory covers 32 skill repositories and 3 research implementations at recorded commits, including related forks and a Russian comparison reference. It is not 35 independent methods or validations, and some large entrypoints were only partially inspected. The [original manifest](skills/bilingual-humanizer/references/skill-sources.json), [additional manifest](skills/bilingual-humanizer/references/further-sources.json) and [research notes](skills/bilingual-humanizer/references/research-sources.md) identify scopes and distinguish adopted ideas from rejected assumptions. Newly written instructions and examples are licensed under MIT. Referenced third-party skill sources are not redistributed. Vendor screenshots and outputs are test evidence and retain their respective rights. See [THIRD_PARTY.md](THIRD_PARTY.md).
