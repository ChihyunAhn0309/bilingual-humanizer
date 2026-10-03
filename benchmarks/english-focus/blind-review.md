# Independent score-blind paired review

Review date: 2026-10-03. Pre-score gate: all six candidates pass source fidelity and are eligible for scoring without required repairs. Eligibility is a content/readability gate, not authorship certification or detector validation.

The reviewer is an AI, independent of candidate writing but with prior English-humanizer reference-audit context. Only the nine specified source/A/B files were read for this review. Assignment files, method labels, writer reviews, scores and other experiment artifacts were not opened; no candidate method was guessed. The task described the sources as AI-authored synthetic prose. No inference or text edits were performed.

The JSON report contains every source/candidate SHA-256, 30 grouped source constraints, exact supporting spans from each text, and per-candidate findings. Every quoted span was checked as an exact substring of its named source or candidate. Source truth beyond the provided text was not fact-checked.

| Case | A fidelity / scoring | B fidelity / scoring | Editorial result |
| --- | --- | --- | --- |
| support-email | Pass / eligible | Pass / eligible | B (slight preference) |
| reading-reflection | Pass / eligible | Pass / eligible | tie |
| technical-update | Pass / eligible | Pass / eligible | B (slight preference) |

## support-email

Reader: Professional customer email. B groups status and scope, keeps the apology before the timing explanation, and gives the next contact commitment a clear final position. A remains acceptable; the source is also already serviceable. This is a narrow reader-order preference, not a factual or fluency failure.

**A:** Professional and comprehensible; contractions fit the relationship. Required repairs: none.

> The request covers only the duplicate £36 payment.
> I understand why seeing two charges would be frustrating, and I'm sorry for the extra work this has caused you.

The separate scope paragraph repeats wording from the opening, and the empathy/apology arrives after the process explanation. All speech acts survive, but the sequence feels more procedural before acknowledging the customer's inconvenience.

**B:** Clear, restrained professional English; full forms are acceptable. Required repairs: none.

> The payment team has not approved it yet, and the request covers only the duplicate £36 payment.
> I will email you by 3 p.m. on Friday even if I am still waiting for a decision.

The first paragraph gathers status and scope; the follow-up promise has its own final paragraph. This is easier to scan as an action/status email than A, although the initial paragraph is denser and the source places empathy earlier.

Source constraint coverage:

- **S01:** Thank recipient for patience while reviewing the duplicate charge on order R-214. Preserved in both candidates.
- **S02:** Sender confirmed the second payment was taken on 18 September. Preserved in both candidates.
- **S03:** Sender submitted a £36 refund request this morning; payment team has not approved it. Preserved in both candidates.
- **S04:** Recognize frustration about two charges and apologize for the extra work caused. Preserved in both candidates.
- **S05:** Only if approved, money should reach original card within five working days; timing is an estimate, not a guarantee. Preserved in both candidates.
- **S06:** No additional form is needed while the request remains pending. Preserved in both candidates.
- **S07:** Sender promises an email by 3 p.m. Friday even if no decision has arrived. Preserved in both candidates.
- **S08:** If that update is not received, request a reply to this email including the order number. Preserved in both candidates.
- **S09:** Sender cannot cancel the first payment because order already shipped; refund request covers only duplicate £36. Preserved in both candidates.
- **S10:** Preserve sender Alex, customer Morgan, professional courtesy and British payment/time wording. A's contractions remain suitable for professional customer correspondence; neither introduces a different dialect or relationship.

Hashes:

- Source: `8eaac80ec6d96595dc7da3b9138d253e653c9d412bb22c4d3895074649e4340e`
- A: `25068e764bf8485cb8bb335bb8b31baf2b08daf56fdd885ac387d3bfab108091`
- B: `c03768d09bbed072a30d8e24c27f08fde9711e2e799a62bcb3912c26c2125031`

## reading-reflection

Reader: First-person reading reflection. The source is already natural and fully qualified. A offers a warmer, more conversational cadence; B preserves the restrained cadence and makes the recommendation's grounds explicit. These benefits do not establish a clear overall winner over each other or the source. A's optional connective polish is minor, not a gate failure.

**A:** Natural conversational reflection with suitable contractions and varied clause structure. Required repairs: none.

> I didn't keep to the routine every morning, either: on two mornings, I skipped reading altogether.

The 'either' has a loose connection to the preceding phone-checking sentence, because checking after finishing complied with the routine. Dropping 'either' would make that transition cleaner, but the explicit two skipped mornings and every-morning qualification prevent a material misstatement.

> The change I noticed was in how I read: I stopped interrupting a chapter to check messages.

This states the behavioral difference plainly; the source's modest evaluative word 'simpler' is less explicit. The underlying contrast and personal approval remain.

**B:** Restrained, idiomatic first-person English; short sentences fit reflection rather than causing fragmentation. Required repairs: none.

> My mornings were quiet during those weeks, and I did not try the routine when I was travelling, so I am reluctant to recommend it to everyone.
> I did not follow the routine consistently: on two mornings I skipped reading altogether.

The reasons sit beside the qualified recommendation, and non-adherence is direct. Compared with the source, the reflective routine-versus-rule phrasing becomes a more literal description; neither is clearly superior for this voice.

Source constraint coverage:

- **R01:** For eight weeks the first-person writer tried reading a chapter in the morning before looking at their phone. Preserved in both candidates.
- **R02:** Writer expected this change to improve memory of reading, not that an improvement was established. Preserved in both candidates.
- **R03:** At end, could recall plots of three novels, but no pre-experiment memory test means improvement cannot be determined. Preserved in both candidates.
- **R04:** A simpler observed benefit concerned stopping message checks mid-chapter; writer liked that change. A replaces the explicit 'simpler' characterization with a description of reading behavior. The modest contrast with unestablished memory benefit and the positive personal stance survive; this is a small expressive tradeoff, not a material factual loss.
- **R05:** Writer still checked phone immediately after finishing; skipped reading entirely on two mornings; routine was a trial, not consistent adherence. Both retain the two omissions and trial/non-adherence distinction. Neither claims after-chapter phone checking broke the routine; A's 'either' makes the connection slightly less clean.
- **R06:** Reluctance to recommend the routine universally; mornings were quiet during the period; no trial while travelling. B's 'so' expresses the explanatory relation already supplied by the adjacent source sentences. It does not turn the limited experience into a general claim about other readers.
- **R07:** Reading was worthwhile to the writer without evidence of a memory benefit. Preserved in both candidates.
- **R08:** Next month writer wants to try after-dinner reading instead; no start date chosen. Preserved in both candidates.
- **R09:** Keep first-person reflective voice, qualified recommendation, British spelling and no invented experience. A is more conversational through contractions; B stays closer to the source's restrained register. Both are natural choices for the stated reader.

Hashes:

- Source: `c6dc5c0f6a7383078f26d00b708a4843b251aec4010da962c89e12833c878498`
- A: `a23b258bca774db7d6074c123e99451b14efb249ee7c6d23ac1790bc79c503b8`
- B: `23a2fb1d02e1c05417f6b6fe995c2a98477d118643b0736d47f5bbe8bc9675aa`

## technical-update

Reader: Internal technical note. B improves local traceability between measurements, excluded jobs and the review-note requirement while preserving the memory warning, unscheduled repeat and approval status. A and the source are still valid; the preference is organizational rather than a claim of stronger evidence or greater factual completeness.

**A:** Precise and readable internal reporting; the separate instruction paragraph is easy to locate. Required repairs: none.

> The review note must state both the ten-job denominator for the timing comparison and the two excluded failures.

The reporting obligation remains exact but is placed in the final paragraph, away from the timing evidence. Grouping all next-step instructions is defensible, though it requires the reader to reconnect this instruction to the opening numbers.

**B:** Direct internal English with justified clause connections and clear numerical referents. Required repairs: none.

> For those ten jobs, median processing time fell from 75 ms with the existing worker to 52 ms with the proposed worker.
> The review note must state both the ten-job denominator for the timing comparison and the two excluded failures.

The two medians have explicit worker referents, and the reporting obligation is adjacent to the data it governs. The opening paragraph carries more functions, but the remaining memory and rollout paragraphs retain clear boundaries.

Source constraint coverage:

- **T01:** Queue test covered 12 jobs using the existing and proposed workers; ten completed in both configurations. Preserved in both candidates.
- **T02:** For only those ten jobs, median processing time fell from 75 ms to 52 ms with proposed worker. B makes the baseline referent explicit; it is established by the source comparison, not an added measurement. No mean, significance, total-job speedup or production benefit is invented.
- **T03:** Other two jobs failed before producing timing; excluded from timing comparison; causes not established. B's exclusion rationale follows from absence of timing results. Neither assigns the failures to a particular configuration or invents a cause.
- **T04:** Proposed worker retains the same retry limit of 3. Preserved in both candidates.
- **T05:** Proposed worker used more memory in this test, but peak memory was not recorded. Preserved in both candidates.
- **T06:** Cannot quantify largest memory increase or predict production peak usage from these results. Preserved in both candidates.
- **T07:** No concurrent clients were included. Preserved in both candidates.
- **T08:** Writer wants repeat with concurrent clients before recommending rollout; repeat unscheduled; no production change approved. Preserved in both candidates.
- **T09:** Review note must state both ten-job denominator and two excluded failures. Preserved in both candidates.
- **T10:** Before approving rollout, service owner should review memory measurements from repeat test; recommendation is not a new mandatory approval condition. Preserved in both candidates.
- **T11:** Keep team knowledge ('we') distinct from writer preference ('I') and service-owner responsibility; technical register remains suitable. Both preserve agency, status and normative force. B's contractions are suitable for an internal note and do not change uncertainty.

Hashes:

- Source: `c56efc051e8caf76cd7e504be0dabb6c7e2f4c362c8a250877ffff886318fcce`
- A: `b56c44d0fc8082a0f0fd3073e6927b02a6db969782f24a56db93c6bf97b9121c`
- B: `60adf8cb98580d1c5507054e9ea0576bf22d9a5fb724958056221b798f299b47`

## Limits

This is one AI review of three small synthetic cases. It establishes no general improvement, commercial-detector result, or human-reader preference. Full forms, contractions and different valid paragraph orders were treated as contextual choices rather than automatic defects. Optional polish is separate from a required fidelity or comprehension repair.
