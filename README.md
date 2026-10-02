# Bilingual Humanizer

[한국어](README.ko.md) · [Skill](skills/bilingual-humanizer/SKILL.md) · [Test evidence](benchmarks/2026-10-02/) · [Reference research](skills/bilingual-humanizer/references/research-sources.md)

A Korean–English editing skill that rebuilds AI drafts around their meaning and intended reader. It supports ordinary content, work documents, technical writing, research, and creative prose, including mixed-language documents.

The default is active rewriting: reorganize paragraphs, recast sentences, preserve the source's information, then review the completed draft. It also supports light edits, review-only requests, and matching a supplied voice sample.

![Editorial workflow with an optional detector evidence stage](docs/assets/workflow.png)

[Editable PowerPoint](docs/assets/workflow.pptx) · [Design draft](docs/assets/composition-draft.png) · [Figure validation](docs/figure-evidence/render-review.md). The diagram was created using [JYS1025/paper-figure](https://github.com/JYS1025/paper-figure). External findings can inform another editorial review; that optional return path is described in the skill rather than drawn in this overview.

## What changed in v1.4

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

For requested detector checks, supply usable service access or existing reports. The skill does not bundle vendor accounts, API clients, or a paid subscription. It records per-service settings, input hashes, scope and receipts. Missing, stale, unsupported or blocked results are never counted as passed.

## Evidence and limits

The repository includes synthetic source texts, frozen rewrites, real commercial detector observations, review records and reproducible local checks. The small development smoke test is **not an accuracy benchmark or a guarantee of detector acceptance**. All trial texts—including the rewrites—were AI-produced. There is no human-authored control, representative sampling, or human/cross-model validation.

Detector results disagree, and some revised texts still receive high AI scores. Scores are reported in their original units; they are not averaged across products or treated as proof of who wrote a text. See the [commercial test report](benchmarks/2026-10-02/REPORT.md) for complete outcomes and access limitations.

Ordinary editing runs entirely as instructions. Python is optional for the two offline audit helpers:

```sh
python skills/bilingual-humanizer/scripts/audit_preservation.py source.txt rewrite.txt
python -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
```

The preservation helper finds surface changes, not semantic truth. `check_detector_report.py` checks report consistency and hashes; it makes no external calls and cannot authenticate a receipt. See its [report format](skills/bilingual-humanizer/references/detector-report-format.md).

![Observed commercial results](docs/assets/detector-observations.png)

## Sources and license

Eleven upstream English/Korean humanizer skills were inspected at recorded commits. The [source manifest](skills/bilingual-humanizer/references/skill-sources.json) and [research notes](skills/bilingual-humanizer/references/research-sources.md) distinguish adopted ideas from rejected assumptions. Newly written instructions and examples are licensed under MIT. Referenced third-party skills are not redistributed. Vendor screenshots and outputs are test evidence and retain their respective rights. See [THIRD_PARTY.md](THIRD_PARTY.md).
