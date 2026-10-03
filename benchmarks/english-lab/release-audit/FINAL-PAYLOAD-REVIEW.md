# Independent final payload review

**Release-ready for publishing the evidence archive while retaining production v1.10.0.** No blocking finding remains. The frozen v1.11.0-dev guide remains experimental; this review does not recommend adopting it as a detector-performance upgrade.

Audit time: 2026-10-03 11:07:34 UTC.

## Exact payload

The independently computed canonical payload SHA-256 is:

`c9ac0ed1cde852f3089369c7eb85d57923e8ab196592dcb4f6ae1c79ca07b523`

It matches the parent’s value and covers **1,858 files** in `outputs/github-repo`. The calculation hashes each file’s bytes, maps its repository-relative POSIX path to that SHA-256, serializes the mapping with `json.dumps(..., sort_keys=True, separators=(',', ':'))`, encodes UTF-8, and hashes the serialized bytes.

Only `__pycache__` directories, `.pyc` files, and these three exact paths are excluded:

- `benchmarks/english-lab/frozen-files.json`
- `benchmarks/english-lab/release-audit/FINAL-PAYLOAD-REVIEW.md`
- `benchmarks/english-lab/release-audit/final-payload-review.json`

The existing staged evidence manifest passed verification. After these two audit files are inserted, the parent must regenerate that manifest to include them. Those packaging changes do not alter this audited payload hash. This review verifies the local stage; it does not claim remote publication.

## Receipt and process verification

The full repository command `py -3.13 -B -X utf8 outputs/github-repo/benchmarks/verify_evidence.py` passed all old and new evidence checks. A separate read-only audit passed **249 of 249** final checks. The [machine-readable review](final-payload-review.json) retains every one of the 17 native result hashes, exact input hashes, Human values and timestamps.

There are exactly **17 distinct new document submissions**: six development, nine first transfer and two continuations. Every checked run has a matching original/input/native/adapter/execution binding, successful serialized worker receipt, full single-window coverage and the same pinned scorer revision and weight hash. Four native classes remain distinct. The published report correctly says that paragraph-deletion rescoring adds internal forward evaluations beyond those 17 submissions.

The first comparison, its blind review, method freeze, complete candidate-feedback records and earlier independent audit remain byte-identical to the working frozen evidence. Both complete continuations preserve source meaning on my direct reading. Their seven paragraphs have complete independent review and 14 retained findings, with no required repair concealed. The feedback-package objects match the full validated reviews, and the writer’s final acknowledgement binds the actual evidence through 57 checked file references.

| Case | Parent pre-score review | Native result | Full feedback integration | Writer acknowledgement | Correct final selection |
| --- | --- | --- | --- | --- | --- |
| T01 | 10:53:36 UTC | 10:54:15 UTC | 10:58:39 UTC | 11:02:46 UTC | draft-1, 0.962205% Human |
| T02 | 10:54:55 UTC | 10:55:36 UTC | 10:58:39 UTC | 11:02:46 UTC | original, 0.671584% Human |

All times are on 2026-10-03; exact fractions are retained in the JSON. T01 continuation Human is **0.32673710957169533%**, below its prior draft. T02 continuation Human is **0.6310708820819855%**, above its first rewrite but below its original. Each continuation consumes one revision. The final cycle selections correctly preserve the strongest eligible checkpoint, and T02’s original fallback is explicitly not a successful rewrite gain. T03 remains at its closed first prototype draft, **0.1346115255728364%**.

## Production preservation

The installed skill, staged production skill and archived baseline contain the same **33 substantive files**, exactly matching the baseline manifest. Production remains v1.10.0.

Both `outputs/bilingual-humanizer-v1.10.0.zip` and `outputs/bilingual-humanizer.zip` have SHA-256:

`e37c403d3d781e98e4682e7c602adab364ae2aeb34cfec993efa2c6212de4db9`

Each ZIP contains the exact same 33 baseline files. The prototype still changes only the three previously frozen instruction/reference files.

## Claims and decision

The root report, results, English and Korean README experiment sections, final writer closure and cycle selections agree with the measured evidence. They keep the small first-comparison values, both failed-to-replace continuations and the larger uncontrolled development result separate. They do not claim Human >=50%, authenticated authorship, commercial transfer, human ratings, a cross-model assessment or general superiority.

The extra parallel exhibition repair remains disclosed as five distinct artifacts against a planned four; main-path cycle validation is not presented as compliance with the total artifact ceiling. Both writers’ post-freeze counterpart-excerpt exposure remains explicit. Continuations are described as feedback-driven and not untouched transfer. T01’s independent continuation reader knew the new score; T02’s new score was not available to that reader during qualitative preparation, although it already existed elsewhere. Neither is represented as a new fully blind method comparison.

My recommendation is unchanged: **publish the complete negative/mixed evidence and retain v1.10.0**. The new guide is plausible editorial guidance, but the user’s high-Human objective was not met and these results do not justify replacing production.

This auditor is a separate AI context and knew method identities and scores. No inference, payment, external upload, installed-skill edit or staged-repository edit was performed. Receipt and hash checks establish internal consistency; they do not independently authenticate historical execution or prove every semantic judgment.

