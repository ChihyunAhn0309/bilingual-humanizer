# Offline feedback adapter review

Reviewed on 2026-10-03 against the installed `bilingual-ai-detector` v3.1.0. The review was performed in a separate agent context from the integration author. Scope: the staged `skill/scripts/local_feedback.py`, new `skill/evals/test_local_feedback.py`, and this report. No detector installation files, weights, calibration, publication files, or other skill content were changed.

## Result

**36 tests passed, zero failures, zero skips** with Python 3.13. The final run took 0.935 seconds. The suite includes one actual installed Korean index/model pipeline run and one contract check against the existing Korean baseline. English cases are explicitly synthetic fixtures; no English model inference, downloads, accounts, hosted inference, or detector service calls were performed for this review.

Command from the workspace root:

```text
py -3.13 -B -X utf8 -m unittest discover -s work/local-feedback/skill/evals -p test_local_feedback.py -v
```

## Contracts inspected

- Staged `references/local-detector-loop.md`.
- Installed detector `SKILL.md` and relevant result/model references.
- Actual `detector.py` UTF-8 byte reading and hashing; `evidence.py` paragraph indexing.
- Actual `korean_model.py` result fields and model release identity.
- Actual `run_english.py` supervised-result validation and execution guard, plus `local_model.py` native four-class/window output.
- Existing `development/ko-baseline.json` bound to the exact `development/ko-original.txt` bytes.

## Findings and fixes

1. **Unsupported output could become a completed receipt.** The previous adapter accepted arbitrary 64-character model hashes, weak model identity, `False` as the offline call count, and English results without the supervised execution guard. It now checks the supported model ID/hash/revision, English schema and experimental-status metadata, strict boolean/integer fields, and the successful serialized worker guard. Missing model caution, calibration-method, or measured-evidence metadata is rejected. Future detector releases need explicit contract review instead of silently gaining support.

2. **Some malformed JSON escaped the error path.** A non-object result or non-object English window could raise `AttributeError` without producing the intended failure receipt. Shape checks now produce `ValueError`, which is recorded with null probabilities. Error-bearing or explicitly unsuccessful results cannot normalize to completion. Probability validation rejects missing/extra classes, wrong sums, booleans, strings, negative/out-of-range numbers, NaN, infinity, and very large integers without overflowing during finiteness checks.

3. **English coverage needed an independent sanity check.** The adapter previously trusted the full-coverage flag alone. It now checks positive token totals, ordered overlapping/adjacent windows, complete token coverage, and the explicit document probability field. A single-window document must match its native window values; multiple windows must retain `null` document probabilities. AI-edited and Humanized remain separate from Human-only.

4. **Stale or missing output needed stronger binding.** Fresh output directories were already required. The adapter additionally refuses precreated stage results, rejects a zero-exit subprocess that creates no result, and requires the measurement timestamp to fall within that scoring invocation. A nonzero exit wins even if the subprocess leaves a valid-looking result file. The normalized payload and raw-result hash now derive from the same byte read. Source and snapshot mutation remain rejected.

5. **Process startup failure lacked a call record.** An `OSError` during subprocess startup is now retained with its stage, script hash, null return code, and error. Script hashes are captured before invocation. Captured nonzero exits and stderr remain available in `execution.json`.

6. **An empty/malformed index could imply no review was needed.** The adapter now requires a nonempty ordered paragraph-ID list before producing `paragraph_review_required`. It continues to leave `style_review_completed: false` and `semantic_review_required: true`.

## Preservation and failure evidence

- A UTF-8 input containing a BOM, CRLF paragraph breaks, Korean, decomposed `e` plus combining acute, precomposed `é`, and an emoji retains exactly the original bytes in both the source and snapshot. The actual Korean detector returns the matching hash and codepoint length. Its first indexed paragraph retains the BOM.
- Wrong source hashes and wrong model hashes are rejected. Invalid UTF-8 is refused before invoking a child process.
- English fixture values Human 5%, AI 15%, AI-edited 30%, and Humanized 50% produce Human-only 5%, preserving all four values. Multiwindow fixtures retain unavailable document/Human percentages.
- Fixtures cover index failure, native-style nonzero score exit with a result file, missing result despite exit zero, malformed/non-object JSON, startup failure, precreated result, old same-input result, source/snapshot mutation, missing script, wrong index hash, and empty review coverage. Recorded scoring failures contain null probabilities.
- An existing output directory is refused before invoking subprocesses; its stale contents remain untouched.

## Limits retained

The installed detector is a trusted local dependency. These checks bind supported metadata and exact candidate bytes; they do not authenticate arbitrary scripts, establish authorship, validate analyst interpretations, or prove English runtime stability. Detailed English span and occlusion consistency checks remain the supervised runner's responsibility, and exact analyst-ledger anchors remain the detector evidence validator's responsibility. No full detector validator was reimplemented.

Native Korean results are checked for the supported calibration method and retained intact, without recomputing or changing calibration. No inference-accuracy claim follows from the test count. The historical baseline test is a contract check, not a new measurement or holdout study. Receipt creation still requires a writable local filesystem; invalid input or a preexisting output directory is refused before creating a new run record.
