# Experimental writer record: support email

Applied `work/english-focus/skill/SKILL.md` v1.9.0, including English composition, English editing, structural rewrite, editing controls, genre/voice, iterative review, local detector loop, and fidelity references. The task's explicit no-inference instruction governed this writer phase.

**Context limitation:** This writer previously produced this case's source review and therefore was not fresh to the source or its assessment. It used the frozen `source-review/triage-feedback.txt` supplied to both writers. It had seen the existing source model results. It did not access the baseline skill or any rival candidate. Drafting and the checks below were same-context self-review, not independent validation. Known source origin is an AI-authored synthetic fixture.

## Reader brief and decisions

Morgan needs the request's status and scope, the conditions for receiving money, and the next contact. Keep Alex's professional warmth, gratitude, apology and firm update commitment. Preserve the supplied currency and date conventions; contractions are appropriate to this correspondence without adding slang or a new persona.

- Applied triage R1: moved the duplicate-only scope and inability to cancel the shipped order's first payment into the paragraph immediately after request status. The email now progresses from current state to scope, conditional timing and next contact.
- Applied R2 only selectively: shortened clause structure and used ordinary contractions. Kept gratitude, acknowledgement of frustration and the apology, since they have separate interpersonal functions. The apology now introduces the final follow-up paragraph.
- Retained the clear conditional timing sentence and the explicit non-guarantee; the five-day estimate must remain recognizable as an estimate. Kept the greeting, sender identity and specific fallback instruction.
- Combined payment confirmation and request submission under Alex's subject. Kept the payment team's approval in its own sentence so submitted and approved do not blur together.

## Source-to-candidate fidelity check

Candidate paragraph numbers count the greeting as P1 and `Best, / Alex` as P6.

| Source constraint | Candidate location and finding |
| --- | --- |
| F1 recipient/sender | P1/P6 retain Morgan and Alex. |
| F2 review, order R-214, second payment, 18 September | P2 contains all; no new transaction or approval is asserted. |
| F3 £36 request submitted this morning; team approval pending | P2 keeps amount, time, actor and pending state. |
| F4 gratitude, frustration acknowledgement, apology for extra work | Gratitude remains P2; acknowledgement/apology remain P5. |
| F5 approval condition, original card, five working days, no guaranteed date | All remain together in P4. |
| F6 no further form while pending | P4 preserves the pending-request scope. |
| F7 email by 3 p.m. Friday even without decision; reply with order number if absent | P5 preserves the firm promise, condition, channel and required reference. |
| F8 first payment cannot be cancelled because shipped; duplicate £36 only | P3 preserves cause and scope. |

No new dates, references, approval, refund completion or delivery promise were added. The source and frozen evidence reviews were not edited.

## Completed checks and freeze

One initial complete candidate; no post-draft revision cycle. A distinct semantic comparison and final reader self-review found no remaining issue requiring change. The reader review checked paragraph progression, references to the request, polite register and the ending's next action. Keeping effective original sentences was deliberate, not a missed change quota.

The offline surface checker exited 0 and returned `no_surface_change_found`; its report is `experimental-surface-audit.json`. This checks recognized protected features, not semantic truth or authorship. No inference, hosted service or external call was made in this writer phase; no score improvement is claimed.

Frozen candidate SHA256: `25068e764bf8485cb8bb335bb8b31baf2b08daf56fdd885ac387d3bfab108091`.

Source SHA256: `8eaac80ec6d96595dc7da3b9138d253e653c9d412bb22c4d3895074649e4340e`.
