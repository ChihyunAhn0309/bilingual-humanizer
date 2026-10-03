# English instruction and release-verifier audit

Scope: compared the new SKILL.md and english.md with the retained v1.8.0 copies; read english-composition.md and english-reference-review.md; inspected verify_english_focus.py and the existing helper code it imports. I previously wrote the baseline candidates, so this is not a fully independent candidate-quality assessment. I did not read experimental candidates, blind-review data or assignment data for this audit. No inference, upstream calls or hosted calls were made, and no audited files were edited.

No actionable semantic, register, overconstraint or unsupported-performance-claim issue was identified in the new instructions. The following findings concern the release verifier.

## 1. Require one selection for every case before evaluating the aggregate target

Priority: P1. Location: verify_english_focus.py, lines 104-111.

The selections list has neither an expected length nor an exact case-set check. With `selections: []` and `all_selected_human_ge_50_targets_met: true`, the loop performs no checks and the final assertion succeeds because `all([])` is true. A list containing only a successful case can likewise conceal unselected cases. This lets the gate report the requested target as met without verifying a selected checkpoint for every case.

Repair: require exactly three selection records with the exact case set already used for assignment validation, reject duplicate cases, then evaluate the aggregate flag. Validate the flag as a Boolean as well. A focused in-memory AST probe of the actual selection section confirmed that the empty-list input passes; no experiment data was read.

## 2. Bind each measurement and review to the expected case and arm

Priority: P1. Location: verify_english_focus.py, lines 69-95 and 105-107.

The expected set validates only directory names. The gate never requires an item under `cases/{case}/experimental-score` to measure `cases/{case}/experimental.txt`, nor does it require its `case` field to match that directory. A correctly normalized receipt for a different candidate can therefore be assigned to that directory and pass the current raw-input/hash checks. The review count does not repair this: `measured` collapses repeated candidate hashes, while nine duplicated review records can satisfy both `len(reviews) == 9` and the set-of-hashes comparison. The selection stage then trusts the unchecked case labels.

Concrete failure mode: valid matching receipts for one candidate could be copied into all nine expected score directories, every measurement row could name that same candidate, and nine copies of its valid review could satisfy the measurement/review coverage checks. The separately checked blind candidate files would not establish that each was actually scored.

Repair: construct an explicit expected mapping from each score directory to its case and exact candidate path, including the recovered technical source directory; check all three fields. Require the reviews to cover exactly those candidate paths once each, rather than relying on a hash set and total count. If byte-identical texts are legitimately possible, retain their separate case/arm identities instead of using distinct hash count as the substitute.

## 3. Reject empty or incomplete execution-call records

Priority: P2. Location: verify_english_focus.py, line 83.

`all(c['returncode'] == 0 for c in execution['calls'])` accepts an empty list. A completed record containing only a successful indexing call also passes. Thus the receipt and its normalization can be internally consistent while the recorded execution no longer includes the scoring invocation that the verifier claims to check.

Repair: require the documented adapter stages in order (`index`, `score`), exactly once, with successful return codes and nonempty script hashes. Retain any supported execution variant explicitly rather than silently accepting absent calls. A direct in-memory probe confirmed that the empty list satisfies the existing assertion.

## 4. Fail explicitly when Python assertions are disabled

Priority: P2. Location: verify_english_focus.py, lines 20-22 and 31-112.

The verifier's 41 assertions include the path-containment, manifest, input-binding, eligibility and target checks. Running Python with `-O`, or with `PYTHONOPTIMIZE` set, removes these checks while leaving the final PASS message reachable for files that parse and normalize. This is a false-success mode for a release gate, not just a loss of diagnostic detail.

Repair: either replace the validation assertions with explicit checks that raise an exception or reject optimized execution at module startup with an explicit `if not __debug__` branch. A Python compile probe with `optimize=1` confirmed assertion removal; no release run was claimed.

## Assembly boundary

The path calculation is consistent with the intended final location `<public-repo>/benchmarks/verify_english_focus.py`: `parents[1]` then resolves the repository root, and the imported helper is its sibling under `benchmarks`. The current staging location is not the assembled layout, so this audit did not treat missing release artifacts as defects or attempt a full gate run. The findings above concern missing structural checks even when all files are assembled and manifests match.

Audited verifier SHA256: 3f070acbd2052a839b0b9f028fca142e9f7fb9266ce4ebfcf4191609a18e2c22

Audited instruction SHA256 values:

- SKILL.md: 7e3f2219201d546dfdf14a588fdd5a64f36e31c1180cae0502d52b1a423bc994
- references/english.md: a3753190970b1baa9b025663a25147145464c53ebecbf6e2079c105337f2a5c4
- references/english-composition.md: 636b8bb411e44166b150f303e5d8c5524a313b69a91a15eb8b475f265685c7f7
- references/english-reference-review.md: 08fdfb3fa6df6bd1dfd10b917830662172f076ad8f9956b18220a2ea212207ae
