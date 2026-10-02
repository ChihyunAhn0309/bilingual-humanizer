# Figure contract — bilingual-humanizer

Publication width: 177.8 mm (672 CSS px); aspect 672 × 360. White background. English labels keep this overview legible across both README versions; Korean explanation goes in the caption.

Required native objects: Original source, Rewrite candidate, Fidelity + reader review, Best faithful text, Optional detector checks, Evidence record. The source is immutable. Candidate → review; review → candidate is a revision loop driven by concrete findings, at most three revisions by default. Review → best text means editorial selection, not detector acceptance. Best text → checks → evidence identifies the exact submitted candidate. Optional feedback returns to review, never declares authorship.

Relationship plan: each arrow transfers one candidate or its findings, not a batch. Rectangular boundaries are connector endpoints. Solid edges are editorial progression; dashed edges are optional external checking/feedback. Original source remains factual authority for all reviews. Evidence refers to an exact SHA-256 and keeps failures and missing checks visible. No all-pass outcome is implied. Draw no additional operators.

Reference inspected: CLIP original overview https://arxiv.org/html/2103.00020v1/main-diagrams.png (local visual inspection). Borrow explicit stream identity and dark, visibly attached arrows; do not reuse CLIP mechanism, shapes, matrix, or content.

Color book: sage-lavender from paper-figure. Sage identifies editorial transformations; lavender identifies optional external evidence. Neutral gray source and output. Labels and lane captions preserve identity in grayscale. Ink #24272B; connectors #363C42; sage fill #E3EFEB / stroke #557E73; lavender fill #E6E3F2 / stroke #7B70A0. Smallest intended native text 12 px (9 pt). Arial.

Full image draft required before reconstruction. Save prompt, draft, transfer decisions, final render, and comparison. The draft is design guidance only; all final diagram labels, boxes, and arrows will be native editable PPTX objects.
