# Genre and voice

Use the actual purpose and source style. These defaults help only where the request leaves room for judgment.

| Genre | What naturalness means here | What must survive |
| --- | --- | --- |
| Email or workplace message | A clear purpose, appropriate courtesy, actionable details | Requests, deadlines, degree of urgency, separate gratitude/apology/commitment |
| Report or proposal | Readable reasoning, precise recommendations, useful hierarchy | Evidence, assumptions, alternatives, costs, ownership, planned versus approved work |
| Academic manuscript | Clear argument in the discipline's register | Citations, uncertainty, methods, statistical interpretation, negative results, venue constraints |
| Technical documentation | Unambiguous instructions and consistent terms | Commands, code, version constraints, preconditions, warnings, schemas, ordering dependencies |
| Blog or essay | A coherent line of thought and the writer's actual stance | Distinct examples, uncertainty, personality, attribution |
| Marketing or product copy | Specific, understandable benefits and a suitable voice | Approved claims, offer terms, disclaimers, pricing, feature availability |
| Speech or presentation | Sayable phrases, manageable breath groups, useful signposts | Timing constraints, sequence, speaker register, slide references, audience cues |
| Resume or application | Concrete contribution without generic self-praise | The writer's actual role, team versus individual ownership, evidence, dates and outcomes |
| Legal or policy prose | Clear sentence structure within exact obligations | Defined terms, negation, exceptions, normative force, approved clauses |
| Medical or financial explanation | Comprehensible qualifications and appropriate precision | Source-stated risks, probabilities, limits, conditions, advice scope |
| Dialogue or fiction | Distinct speaker voices and intentional narrative rhythm | Continuity, character knowledge, point of view, agreed plot and creative constraints |
| UI labels or brief captions | A concise, recognizable action or description | State, intent, accessibility, placeholders, interpolation variables, space constraints |

Do not insert a disclaimer merely because a document belongs to a specialized field. Editing fidelity is the task; fact-checking or professional advice is a separate operation unless requested.

## Voice matching

From supplied same-genre samples, infer a small set of usable traits: formality, Korean speech level or English spelling variety, point of view, typical paragraph shape, preferred vocabulary, punctuation, emotional directness, and tolerance for digression. Apply them without copying distinctive content or borrowing biographical facts. Do not invent a stable author profile from one unrelated example.

User instructions override the sample. Source meaning overrides generic style preferences. A real correction is not required just because it differs from a sample. If the writer's prose is already natural, keep it.

Optional preferences may be expressed in ordinary language or as `mode=light|rewrite|review`, `audience=...`, `register=...`, `keep=...`, `avoid=...`, and `length=...`. These are prompt conveniences, not a rigid command parser. Ask about a preference only when necessary to resolve a meaningful conflict.

## Bilingual documents

Identify the language of each prose span. Keep code, mathematical notation, names, and specialist abbreviations outside language conversion. Apply Korean sentence logic to Korean passages and English syntax to English passages; avoid translating through an intermediate language as a humanizing trick.

For parallel translations, align the same claims, scope, numbers, and attribution across both versions. If translation is not requested, edit each supplied language only. When they already disagree, flag the mismatch rather than silently deciding which version is true.
