# Frozen holdout corpus provenance

These are newly generated AI-synthetic prose drafts. They are not human-authored control samples and must not be described as such. All named people, events, observations, numerical details, and attributed statements in the articles are invented for evaluation; no factual research was performed.

Prepared by the independent holdout-corpus subagent on 2026-10-02T07:48:46Z. The subagent did not inspect skill files, previous corpus files, detector scores, or the web. English genre: practical community newsletter about repair intake. Korean genre: personal-voice everyday informative essay about storing umbrellas. The topics differ, and neither concerns libraries, caches, or memos.

The sources were drafted and length-checked in memory. An alternative Korean draft was considered only while attempting the original combined length constraints and was discarded without saving. After the parent's clarification prioritized natural Korean over the character floor, the original natural Korean draft was selected. No detector feedback or rewriting-skill output informed selection. No source rewrite or ideal answer was created.

## Frozen file manifest

Counting method: all nonempty whitespace-delimited tokens, including the title. Characters include spaces, LF newlines, and the final LF. Files use UTF-8 without BOM and LF newlines. SHA-256 covers the exact file bytes.

| File | Words / eojeol | Characters | SHA-256 |
| --- | ---: | ---: | --- |
| en-source.txt | 195 | 1194 | 8fd9af644cb36d9d210f5caf3d2ffc275d04287cb7719f623b64565b25923052 |
| ko-source.txt | 193 | 732 | 54ac7cc91ffd4704c1d7ada924024a511a75b67b9694737cca620c0ee2001e6f |

Both files are frozen after their initial write. Preserve these bytes for every baseline and improved paired test. The Korean character count below 1,000 is expressly permitted by the recorded clarification.

## Exact generation instruction

Independent evaluation corpus preparation authorized by user. Cwd [workspace]. Write ONLY work/v15/holdout/en-source.txt, ko-source.txt, provenance.md. Do not inspect any skill, old corpus, detector scores, or web. Create two fresh synthetic prose drafts in different realistic non-academic genres: English practical explanation/newsletter and Korean personal-voice everyday informative essay, different topics, not library/cache/memos. Each 170-200 whitespace words/eojeol; >=1000 characters; Korean may need 150-180eojeol if length. Each self-contained with concrete fictional facts, 2-3 numbers, a qualification, an attribution, and a genuine original viewpoint. Natural intent but generic LLM structure/canned transitions possible; don't deliberately exaggerate defects. No rewrite or ideal answer. Mark in provenance that AI synthetic, not human control; source texts themselves should read like complete articles without 'fictional' boilerplate. Record exact generation instruction, word counts, hashes. Freeze sources once written; report paths/hashes. These will be used for honest paired baseline vs improved tests.

## Exact follow-up clarification

Korean naturalness priority: use 170-200eojeol and allow <1000characters. Don't distort morphology to reach char floor. Detector minimum relevant only100words orcharacters. Freeze natural source within wordbounds.
