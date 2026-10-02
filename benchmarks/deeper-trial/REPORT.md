# Expanded improvement trial and v1.5.1 maintenance release

Observed on 2026-10-03 KST (2026-10-02 UTC). **The requested target—each detector's native Human indicator strictly above 50—was not achieved.** The two experimental instruction methods are not promoted to the production default. Version 1.5.1 preserves the v1.5 rewriting approach while correcting a specific fidelity risk and report-threshold behavior.

한국어 요약: 실제 상용 검사와 독립 세션 검토를 진행했지만 모든 검사기의 Human 지표가 50%를 넘는 목표는 달성하지 못했습니다. 두 실험안은 기본값에 채택하지 않았습니다. v1.5.1에는 문서의 검토 목적·결정 단계를 빠뜨리지 않도록 하는 지침과 엄격한 `>50` 경계 처리를 반영했습니다. 아래 표는 같은 파일의 결과를 연결하며, 실패와 미검사도 그대로 공개합니다.

## Commercial observations

GPTZero's Human value is a document-class probability. QuillBot's Human-written value is a percentage of text; its UI describes the scores as percentages of words likely generated or refined using AI. These are not interchangeable probabilities of who wrote a document. Sapling and ZeroGPT expose AI scores here; the table does not invent Human probabilities by subtracting them from 100. Higher Human and lower AI are the respective directional preferences, not an authorship test.

| Exact candidate | GPTZero Human ↑ | QuillBot Human-written ↑ | Sapling AI ↓ | ZeroGPT AI GPT ↓ |
| --- | ---: | ---: | ---: | ---: |
| EN museum · v1.5 baseline | [0%](receipts/gptzero-en-museum-baseline-basic.txt) | [100%](receipts/quillbot-en-museum-baseline.txt) | [93.7%](receipts/sapling-en-museum-baseline.txt) | — |
| EN museum · A | [0%](receipts/gptzero-en-museum-a.txt) | [100%](receipts/quillbot-en-museum-a.txt) | [95.1%](receipts/sapling-en-museum-a.txt) | — |
| EN museum · B | [0%](receipts/gptzero-en-museum-b.txt) | [100%](receipts/quillbot-en-museum-b.txt) | [92.6%](receipts/sapling-en-museum-b.txt) | — |
| KO equipment · v1.5 baseline | [6%](receipts/gptzero-ko-equipment-baseline.txt) | [9%](receipts/quillbot-ko-equipment-baseline.txt) | — | — |
| KO equipment · A | [45%](receipts/gptzero-ko-equipment-a.txt) | [7%](receipts/quillbot-ko-equipment-a.txt) | — | [100%](receipts/zerogpt-ko-equipment-a.txt) |
| KO equipment · B | [8%](receipts/gptzero-ko-equipment-b.txt) | [9%](receipts/quillbot-ko-equipment-b.txt) | — | [100%](receipts/zerogpt-ko-equipment-b.txt) |
| KO library · A | [60%](receipts/gptzero-ko-library-a.txt) | [11%](receipts/quillbot-ko-library-a.txt) | — | [100%](receipts/zerogpt-ko-library-a.txt) |
| KO library · B | [72%](receipts/gptzero-ko-library-b.txt) | — | — | — |
| Fresh EN support · v1.5 baseline | [0%](receipts/gptzero-en-support-baseline.txt) | — | [100%](receipts/sapling-en-support-baseline.txt) | — |
| Fresh EN support · B | [0%](receipts/gptzero-en-support-b.txt) | — | [99.9%](receipts/sapling-en-support-b.txt) | — |
| Fresh KO essay · v1.5 baseline | [42%](receipts/gptzero-ko-essay-baseline.txt) | — | — | [100%](receipts/zerogpt-ko-essay-baseline.txt) |
| Fresh KO essay · B | [2%](receipts/gptzero-ko-essay-b.txt) | — | — | [100%](receipts/zerogpt-ko-essay-b.txt) |
| KO library · independent v1.5.1 output | [50%](receipts/gptzero-ko-library-v151.txt) | — | — | [100%](receipts/zerogpt-ko-library-v151.txt) |

There are **32 new completed observations**, including an initial Advanced-view GPTZero scan of the museum baseline (Human 0%). That baseline was also rescanned in Basic mode (Human 0%) for the table's matched comparison. `—` means not measured in this trial; it is never a pass. QuillBot's seven free scans were exhausted, leaving library B, both fresh-language pairs and the independent v1.5.1 output without QuillBot results. No subscription, trial or paid API was purchased.

Model versions observed: GPTZero 4o for English and 4.1m for Korean; QuillBot v7.1.0 for English and v6.2.1 for Korean. This is an observed language-specific difference, not evidence that a model changed during the trial. Sapling and ZeroGPT did not expose a model version. Their Korean/genre calibration was not established. Browser inputs were matched to the intended file before submission; stale results were not counted. Sapling's official page tool returned untruncated results whose sentence text matches the submitted text. An editor input-interference attempt was abandoned without submitting the altered text, then testing continued in a separate tab.

The Korean library A result (60/11) does not meet the joint >50 target. B's GPTZero 72% cannot establish a joint pass while QuillBot is missing. On fresh topics, B kept English GPTZero Human at 0 and reduced Korean GPTZero Human from 42 to 2. The Korean baseline's other classes were AI 18 and Mixed 40: `100 − AI = 82` would therefore misreport its actual Human 42. Sapling 100→99.9 on one English passage is not a meaningful demonstrated general gain.

Earlier library readings belong to different text files. The previous short-prompt candidate's GPTZero Human 85 and QuillBot Human-written 17 are documented in the [preceding trial](../additional-trial/REPORT.md), not obtained from this A/B run. The old v1.5 library baseline's 44/23 is historical and was not rerun here; blind review found a purpose omission in that baseline. Its historical score must not be reassigned to a corrected output.

## Design, reviews and concrete changes

- [Plan](PLAN.md): museum, equipment and library are development data. Writers saw source text and their method, not detector results. [A](method-a.md) emphasizes reader purpose and discourse composition; [B](method-b.md) uses original synthetic contrastive editing examples. These examples are not human training pairs or a replication of a trained paraphrasing model.
- [Development blind review](blind-review.md): candidates were relabeled before a fresh-context review. Differences were small: museum B approximately tied the baseline ahead of A, equipment candidates were near-tied, and library B/A were ahead of the baseline with its omission. Two A edits repaired a forward referent and obligation strength before scans. [Repair log](repair-log.json), [mapping](blind-mapping.json) and all initial/final candidates are retained.
- [Fresh genre review](fresh-review.md): support and essay sources were generated independently after the methods were fixed. B was selected for this transfer check on fidelity/near-tied reader review, not a detector win. The methods did not satisfy the plan's hoped-for broad development gain, so this extra check was exploratory. English candidates tied; Korean B was slightly preferred. The detector reversal shows why reader preference is not detector performance.
- [v1.5.1 forward check](v151-check/report.md): a new independent writer using the maintenance skill retained the library document's review purpose and pre-proposal stage. This is one behavioral check, not a representative regression benchmark.
- [Independent final skill audit](final-skill-audit.md): another fresh-context reviewer checked the source/output and score checker. It found no material issue within that scope; 45 unit tests and 10 additional synthetic boundary/metric checks passed. It did not itself call detectors. These are AI sessions using the same host model, not human or cross-model review.

The release adds an explicit rule to preserve the document's remit and decision stage when removing framing. It also implements strict `gt`/`lt` operators so exactly 50 does not satisfy “above 50.” Its tests cover boundary precision and separate service metrics. The default rewrite ceiling remains three. No compulsory typos, fabricated experiences, hidden characters, arbitrary sentence-length targets or universal detector-acceptance promise were added.

## Additional references and limits

Selected sections of 13 additional skill repositories and 3 research implementations were screened; the cumulative inventory is 32 skill repositories plus 3 method implementations. Related forks are not independent evidence. The [additional manifest](research/sources.json) records exact commits, entry hashes, licensing evidence and partial-read scope. The [research synthesis](../../skills/bilingual-humanizer/references/further-reference-review.md) distinguishes useful editorial hypotheses from unsupported claims. `im-not-ai` remains covered in the [specific review](../../skills/bilingual-humanizer/references/im-not-ai-review.md); a new Korean derivative was identified as such.

Research on SICO, HIP and MASH does not transfer its reported performance to this instruction-only skill. No upstream script, adapter training, downloaded model inference or paid model API was run. The local environment had CPU PyTorch and no CUDA; this is not proof that CPU inference is impossible.

All sources and rewrites here are synthetic AI-produced texts. There is no human-authored control, representative corpus, repeated-run estimate, human rating or cross-model trial. Small adaptive samples cannot establish a universal lower bound for any detector or genre. Free quotas leave a partial comparison matrix. Failure against the requested target remains explicit even if an individual vendor reading improves.

## Reproduction and integrity

[results.json](results.json) contains every observation with native metric, model, time, exact file SHA-256, trimmed submission SHA-256 and raw receipt SHA-256. The `observations/` files preserve the original capture records; `receipts/` preserve visible result text or official page-tool output. GPTZero/QuillBot input linkage was checked in the editor at capture; their panel receipts alone are not a provider-signed binding to that input. Local consistency checks cannot authenticate a service or prove an author.

[frozen-inputs.json](frozen-inputs.json) covers development and fresh files. The fresh manifest extension was archived after some scans, so it is not preregistration; the earlier blind mappings and each capture retain their own file hashes. The previous release's 20 files are preserved in `../additional-trial/retained-skill/` against the original hashes, while [release-skill-hashes.json](release-skill-hashes.json) identifies the new 22-file package. Failed outcomes are not removed or replaced by later candidates.

```sh
python -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
python benchmarks/verify_evidence.py
```

These offline checks validate script behavior and archive consistency. They do not make paid calls, rerun current commercial models, or automatically grade prose naturalness. [Final evidence audit](final-evidence-audit.md) records the separate publication review and its scope.
