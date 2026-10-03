# Continuation E/F — independent publication evidence audit

Date: 2026-10-03. Scope: the seven observations and supporting files in `benchmarks/continuation-e/`, `verify_continuation_e.py`, the latest portions of both repository READMEs, and retained production-file identity. This is a separate-context AI audit using the fact-check workflow. The previous renewal audit remains a separate, fixed 34-observation review; it was not edited during this audit.

**Result:** no score, input-hash, source-identity, checkpoint-selection, or production-file mismatch was found. One receipt-provenance clarification was recommended, added by the parent, and checked. E's Korean checkpoint is **97% GPTZero Human / 30% QuillBot Human-written / 100% ZeroGPT AI GPT**. F remains a separate **91% / 33%** alternative with no ZeroGPT observation. English E's **0% / 72%** does not replace the prior **0% / 83%** checkpoint. The all-selected-detector target remains unmet.

No browser, detector, external upload, inference, account action, or publication action was performed. Production files and experimental texts were not edited. This report does not authorize publication or certify human authorship. Login screens, private account screenshots, and Cloud execution preparation are outside its scope.

## Checks executed

From the proposed public repository root:

```text
python -B benchmarks/verify_evidence.py
PASS: 36 original observations.
PASS: 28 v1.5/development observations.
PASS: 17 additional-trial observations.
PASS: 32 deeper-trial observations.
PASS: 34 renewal observations.
PASS: 7 continuation E/F observations.
Exit 0; 154 observations in total.

python -B -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
45 tests; OK; exit 0.
```

These runs check archive consistency and helper behavior. They are not additional detector trials or automatic semantic evaluations. The new verifier checks all seven original observation records against the consolidated results; file, submitted-text, receipt and source hashes; freeze/result chronology; native score fields and category totals; model labels; quotas; and retained/alternative checkpoint references. The top-level verifier invokes it.

Additional independent checks reconstructed all three report-table rows, compared both sources byte-for-byte to the renewal sources, resolved prior comparator model settings, compared complete production file sets, searched the proposed public tree for credential patterns and unwanted artifacts, and inspected the actual originals, drafts, final candidates and review follow-ups.

## All new observations and units

| Exact candidate | GPTZero Human document probability | QuillBot Human-written text percentage | ZeroGPT AI GPT percentage |
| --- | ---: | ---: | ---: |
| [English support E](candidates/en-support.txt) | 0% | 72% | Not measured |
| [Korean library E](candidates/ko-library.txt) | 97% | 30% | 100% |
| [Korean library F](candidates/ko-library-f.txt) | 91% | 33% | Not measured |

The seven records comprise three GPTZero, three QuillBot, and one ZeroGPT reading. Every displayed value agrees with its receipt and [results.json](results.json). GPTZero's F receipt contains AI 7%, Mixed 2%, and Human 91%: Human is correctly read directly, not manufactured as `100 - AI`. QuillBot's Human-written category is a text-share measure and is not conflated with GPTZero's document-class probability. ZeroGPT's AI-side score is not converted to a purported Human probability.

English observations use GPTZero Basic model 4o and QuillBot v7.1.0. Korean observations use GPTZero Basic model 4.1m and QuillBot v6.2.1. The corresponding prior comparator records expose the same settings. ZeroGPT exposes no model identifier. Different dates/accounts and undisclosed backend changes remain limits; this is not a controlled estimate of general improvement.

## Input identity and chronology

The original English and Korean sources match their renewal counterparts exactly. Every recorded input hash matches the actual file; every submitted-text hash matches the UTF-8 text after the recorded trimming convention. All receipt hashes match. No result is attached to either repaired Korean draft.

| Final candidate | SHA-256 |
| --- | --- |
| English E | `1c67717b28837f8fc240915a80cecface583057abb6e4f27bfdda287bd0967df` |
| Korean E | `24ccfbae46622c5c5db7266f496dd478484a6b8963b9f2bc5c5f9f5ff7fa362c` |
| Korean F | `17bbd0b09fe818d3daf2982deaef2613622fc23012147a17f22f0654e73c658c` |

The first two candidates' recorded freeze is `2026-10-03T02:25:24.323725+00:00`; their first recorded result follows by about 40.58 seconds. F's recorded freeze is `2026-10-03T02:29:06.907786+00:00`; its first result follows by about 39.17 seconds. Every result is later than its applicable freeze. These are internally consistent agent-recorded timestamps, not externally attested creation/submission times. The archive alone cannot independently authenticate the clock or prove the start time of a submission or review.

QuillBot receipts show six, five, and four scans remaining after English E, Korean E, and Korean F respectively. This supports three completed scans from the stated seven-scan allocation, with four remaining. The stated initial GPTZero 10,000-credit balance and account/access history are experiment narrative, not independently reauthenticated by this offline audit. The recorded GPTZero results are Basic panels containing “Text up-to-date”; no unavailable Advanced result is counted.

## Fidelity reviews and selection

The E [review](fidelity-review.md) distinguishes the initial Korean draft's two required repairs from the final reread. The final text restores the distinction between expressed preference and evidence of actual visits, restores the scope of the notice obligation, and explicitly states the review's condition-organizing purpose. The optional wording refinement also appears. Direct source/final inspection found those repairs present and no remaining substantive mismatch in the reviewed quantities, conditions, evidence limits, or obligations.

English E preserves the event and diagnostic details, uncertainty about cause, immediate customer actions, both conditional replacement paths, delivery-charge scope, reporting deadline and local time, and the distinction between storage diagnostics and the unchecked recording. Its action/reporting paragraph is reordered, not omitted.

The F [review](fidelity-review-f.md) records no required repair, an optional representativeness clarification, and a source/final follow-up. Its stated final hash matches the current F file. The draft-to-final difference is the recorded one-sentence clarification. These are same-model separate-context AI reviews with follow-ups in their respective review contexts, not human ratings or new independent reviewers for every pass. This evidence audit itself has seen scores and is not a blind reader-preference test.

The [registry](checkpoint-registry.json) correctly retains E for the Korean document: its two Human readings rise from the previous C checkpoint's 93%/15% to 97%/30%, while the measured ZeroGPT reading stays AI 100%. F raises QuillBot to 33% but lowers GPTZero to 91%, so it is kept as a trade-off alternative. Its evidence map contains only its own GPTZero and QuillBot observations; E's ZeroGPT result is not attached to it.

The prior English support text remains selected because E lowers QuillBot from 83% to 72% while GPTZero stays 0%. Its earlier Sapling AI 100% is linked to the original baseline file and timestamp; it is not presented as a new E reading. All registry links resolve to the same vendor, native metric, score, timestamp and exact input hash as their source bundle. The essay and museum selections are inherited from the prior registry rather than retested here.

Both READMEs match these decisions, explicitly keep 97%/30% separate from 91%/33%, retain the English 0%/83%, state that production is unchanged, and avoid claiming general skill improvement. Their relative links and the report's relative links resolved at inspection. Both the stored target flags and the actual selected scores support non-attainment: retained Korean QuillBot is below 50%, English GPTZero is below 50%, and Korean ZeroGPT AI is above the separate 50% ceiling.

## Resolved receipt-provenance finding

All three QuillBot receipts retain the same document URL and the English title “Foldlight Desk Panel Diagnostic Report,” including the Korean scans. The auditor reported this potential source of confusion. The parent added an explanation to [REPORT.md](REPORT.md), which this auditor then checked: the editor documents were reused, the old title can remain, and identity is established by the recorded submitted-text comparison/hash rather than by the title.

The same clarification correctly states the main evidentiary limit: GPTZero/QuillBot receipts capture score panels without a complete submitted-text echo. Their actual input binding relies on `input_verified_in_dom` and the experiment's recorded agent comparison. The local verifier can verify the hash and score consistency but cannot authenticate that DOM assertion. ZeroGPT's receipt does echo the entire E Korean input; normalized text comparison succeeds. These are unsigned observations, not signed vendor reports. No score was changed to resolve this documentation issue.

## Production and publication hygiene

The complete non-cache 22-file production set still matches the retained v1.5.1 hash manifest in the proposed public folder, rollback folder, local master, and installed skill. The earlier renewal bundle still contains 34 records. This audit did not alter the renewal report or audit; the public and working copies of its audit matched at inspection.

The new continuation folder contained only Markdown, JSON, and text files before this report was added: no screenshots, model weights, tokenizer assets, dependency code, or binary account artifacts. A scan of the proposed public text files found no common API token, private-key, bearer-credential or quoted password/token patterns. No model/dependency artifacts were found in the public tree. This is a practical scan, not a guarantee against every possible secret format.

The same eight pre-existing production `.pyc` files remain in the local assembly tree. They are excluded by `.gitignore` and the previously inspected publication-manifest filter; they are not part of the 22 production files. Final uploaded-tree/ZIP filtering and remote publication status are the publisher's remaining assembly checks, outside this offline snapshot. Account login screens and screenshots outside the public tree were neither examined nor included.

Overall confidence is **high for the local score/file/comparison consistency checked here**. Service authenticity, account history, human authorship, detector accuracy, and general editing effectiveness are not established. This remains adaptive development on two reused synthetic sources, with no human-authored control, representative sampling, randomized comparison, or human reader study.
