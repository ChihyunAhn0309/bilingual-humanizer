# Independent audit of the frozen English composition comparison

Recommendation: retain v1.10.0 as the production skill and preserve the v1.11.0-dev prototype as an experimental alternative. The prototype is a reasonable concise editorial method, but the frozen evidence does not establish the stronger English detector performance the user prioritizes. Nothing in this recommendation requires discarding the faithful development texts or negative results.

This audit was conducted independently after the first comparison was complete. It is not blind: the auditor read the method identities, scores and earlier judgments, then directly compared all three transfer sources and all six first candidates, plus both development sources and their measured alternatives. The auditor did not write those texts, run inference, change a model, edit production, or rewrite a candidate. This is a separate AI-agent review, not an independent human or cross-model validation. Later optional candidate continuations are excluded from the verdict below, whether or not their files already exist.

## What the frozen evidence establishes

| Transfer case | Source Human | v1.10 Human | Prototype Human | Prototype minus v1.10 | Frozen reader judgment |
| --- | ---: | ---: | ---: | ---: | --- |
| T01, public explanation | 0.307263% | 0.187967% | 0.962205% | +0.774238 pp | Slight prototype preference |
| T02, operational memo | 0.671584% | 0.558569% | 0.453104% | -0.105465 pp | Tie |
| T03, personal reflection | 0.023340% | 0.133516% | 0.134612% | +0.001095 pp | Slight prototype preference |

The values are the exact submitted documents' native Human-class outputs from the same pinned, experimental English checkpoint, rounded only for this table. They are not Humanized scores, word shares, a commercial detector result, or authenticated authorship probabilities. No prototype first candidate reached Human 1%, much less the user's Human >=50% objective. Describing this as two wins out of three without the absolute values would exaggerate its practical significance. T03's difference is negligible for this decision. T02 is lower than both the baseline and its unchanged source.

Development produced a much larger single-case response for the exhibition review: 0.016360% to 25.066924%. The selected policy note rose from 0.195801% to 0.633648%. Neither is a retained-skill comparison; both are synthetic texts created and revised within development. The evidence-first policy alternative scored 0.517771%, and the repaired fresh-context exhibition alternative scored 0.189623%. Retaining those regressions is appropriate. The best exhibition result is worth preserving as an exact faithful checkpoint, but does not demonstrate that the proposed skill caused a general improvement.

## Fidelity and reader judgment

My source-to-candidate review agrees that all six frozen first candidates are eligible. The repair-queue versions preserve the fictional setting, staffing schedule, partly work-dependent ordering, required owner agreement, qualified inference about neglect, suggested labels, limited benefit and lack of a completion guarantee. The memo versions retain both desks, timing, entry order, inspection/availability rules, safety exception, Nia's duties, the no-duplicate-entry instruction and the undecided trial outcome. The reflections retain the inherited chair, understood warning, expected resistance, uncertain repair history, possible patch explanations, imperfect practical outcome and unresolved emotional ending. I found no material addition, omission or strengthened claim that requires withdrawing a reported score.

The prototype's repair-queue wording links the benches and capacity limitation more directly; its personal reflection gives the practical result and unresolved ending clear space. These are defensible local preferences. Both baseline alternatives also read naturally. The memo differences are principally contraction and phrasing choices, not a meaningful improvement in usefulness. No candidate is a credible demonstration of a large editorial advantage.

The selected development texts also preserve their source meaning. Development did introduce real semantic errors in rejected drafts: the basis of a recommendation became a claim about survey conduct; uncertain causality became uncertainty about whether movement occurred; expectation became hope; present uncertainty became past inability. Those errors were caught and repaired before the affected version was scored. They support retaining a distinct source-fidelity pass and rejecting brief-only drafting as a demonstrated improvement. They do not invalidate the exact corrected candidates' measurements.

## Was real, full detector feedback used?

Yes, the saved process contains materially more than a numerical scan. The frozen development and transfer evidence includes native results, subprocess receipts, exact text bindings, paragraph deletion measurements, complete paragraph review, six document dimensions, anchored findings, plausible human alternatives, and explicit editorial decisions. Development records show source feedback before drafting, accepted organization changes, before/after resolution links, rejected drafts, post-score review and selection of an earlier faithful candidate. This is documented feedback-driven development.

For the first transfer comparison, both writers received the common source feedback. The score-blind review was frozen before candidate measurements. The later full candidate ledgers add actual measured output and deletion sensitivity to the prior editorial observations; the final reviewer read the supplied native feedback without changing the frozen reader preference. All 44 candidate findings were retained, with no accepted repair outstanding. I agree that the retained content and genre choices do not become defective because their deletion changes a model score. A review that finds no repair is legitimate closure, not a fabricated rewriting cycle.

The adapter deliberately says `style_review_completed: false`; the separate ledgers supply that review. Reporting the adapter alone as full feedback would have been incorrect, but that is not what the audited package does. The baseline writer's closure and prototype follow-up records explicitly acknowledge the new native output and full findings. The baseline closure also discloses that comparative excerpts were encountered after its draft was frozen. That exposure cannot retroactively change the first text, but it prevents claiming continued cross-arm blindness during closure. Prototype follow-up records disclose analogous exposure; any continuation is score-guided and partly exposed to the other arm.

“Six development measurements” and “nine transfer measurements” should be called document submissions or detector runs, not the total number of model forward evaluations. Their explanation mode also rescored paragraph-deleted inputs. The audit did not independently re-execute those runs; receipts and hashes establish internal consistency, not cryptographic authentication of historical execution.

## Integrity and design limits

The read-only checker in [check_frozen_evidence.py](check_frozen_evidence.py) passed **703 of 703** checks, saved in [frozen-integrity-checks.json](frozen-integrity-checks.json). It checked:

- Both complete 33-file skill manifests and the method freeze. Exactly `SKILL.md`, `references/english-composition.md` and `references/english-reference-review.md` differ; scripts remain unchanged.
- Every pointer in the frozen transfer comparison, the complete candidate-feedback manifest, and both development sessions.
- All 15 frozen document submissions' original/input/native/adapter/execution hashes, successful serialized worker exits, one-window full coverage, unchanged four classes, correct Human percentages and absence of external detector calls in the recorded outputs.
- All nine transfer and six measured-development ledgers' input hashes, paragraph coverage, six dimensions, exact evidence spans and native class binding; all candidate findings have matching triage records.
- The recorded blind review predates every candidate score, and all reported prototype-versus-baseline deltas are arithmetically correct.

These checks do not turn a synthetic, three-case probe into a representative experiment. There is one draw per arm, no repeated generation, no human ratings and no commercial detector measurement. The baseline writer had fresh context; the prototype writer also developed the method. The blind evaluator authored the sources and knew their constraints and source scores. Development and transfer overlap in repair-workshop subject matter. These are material limits on attributing a difference to the skill alone.

The development artifact ceiling was exceeded: the exhibition sequence has its planned initial draft plus three main revisions, and one additional parallel repair created during a coordination race. The corrected provenance note preserves both versions and identifies the scored version. This is a real process deviation, appropriately disclosed. A passing cycle validator only certifies the represented main sequence, not compliance with a total artifact ceiling. It should stay visible in any release record.

The frozen prototype is restrained as skill design: it focuses on writer stance, paragraph function and source-supported relationships, retains fidelity and budget boundaries, and makes no claim to implement a proprietary humanizer. The shorter guide is plausible editorial guidance. Those merits alone do not justify promoting it as a performance upgrade given the user's stated priority and the available fallback.

## Release recommendation and permissible claims

Keep v1.10.0 installed. Preserve the prototype, source texts, all first candidates, rejected alternatives, native outputs, full reports and provenance correction. A negative-results publication is justified; production adoption as a stronger detector-oriented humanizer is not justified by this frozen comparison.

Supported wording: “A concise experimental composition method produced two slight reader preferences and one tie on three synthetic comparisons. Native Human changes against the retained skill were +0.774238, -0.105465 and +0.001095 percentage points; all first prototype values were below 1%. A larger response occurred on one development text, without a baseline-method control. The retained skill remains the production version.”

Unsupported wording includes general English superiority, robust detector acceptance, a >=50% success, commercial transfer, a human-authorship transformation, statistically meaningful improvement, independent human validation, or isolated proof of the skill's causal effect. Calling any score-guided continuation untouched transfer evidence would also be inaccurate.

Later completed continuations may justify choosing a different exact candidate for that source, provided independent eligibility review, actual measurement and returned full feedback are complete. They must appear in a separate section with their real budget, exposure and selection history. They do not replace this first comparison or provide a symmetric method comparison unless both arms were run under the same continuation opportunity. A later high value on one such candidate alone would not erase the need for restrained adoption claims.

Final release payload, installed-state comparison and publication claims remain to be checked when the parent supplies the completed release. This report is the independent first-comparison recommendation, not that final verification.
