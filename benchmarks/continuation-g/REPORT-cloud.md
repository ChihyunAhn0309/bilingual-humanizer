# Continuation G: voice anchors on four new holdouts

Date: 2026-10-03 UTC. Production remains **v1.5.1**. This bounded experiment tested an explicit voice-anchor ledger on four new AI-produced synthetic sources: a Korean neighborhood notice, a Korean exhibition review, an English incident notice, and an English withdrawal letter. They are not human controls.

## Decision

G is a defensible editorial direction, but this trial does **not** establish general improvement and does not change production or any retained per-document checkpoint. In the first independent review, G was preferred on three of four pairs, with the retained-skill comparator narrowly preferred for the English letter as frozen. However, that same review found required fidelity repairs in three G candidates and in three comparator candidates. G therefore did not eliminate the core risk it was meant to control. After the recorded G repairs, the reviewer cleared all four exact `final/` files for optional detector submission; no second comparative preference was solicited after seeing the repairs.

No commercial detector result was obtained. This Cloud environment provided no transferable authenticated free GPTZero or QuillBot session, and the laptop's cookies were neither available nor sought. No account, trial, purchase, billing method, API inference, compute, model download, or recurring job was created. The requested **GPTZero Basic native Human document probability >=50% and QuillBot native Human-written text share >=50% on the same final document remains pending for every holdout**. No AI-side metric has been converted into a human probability.

## Method and like-for-like comparator

[Challenger G](METHOD.md) adds an explicit ledger of three or four source-evidenced voice anchors—such as distance, connective habits, directness, and characteristic lexical choices—to the ordinary proposition-and-constraint check. It is not the archived source-sensitive method, a heading route, a fixed surface rule, or a detector-feedback loop. The hypothesis arose from the upstream review's unresolved voice-preservation problem; SICO, HIP, and MASH require optimization or trained models and do not justify copying their claims into a prompt method. The rejected Qwen3-0.6B HIP probe was not repeated.

The comparator applied the unchanged retained v1.5.1 skill. Both arms used the same frozen source, one drafting pass, one self-review opportunity, no detector result, and the same task/session writer. This controls context better than comparing against an old document checkpoint, but it is still an unblinded, single-writer experiment.

## Actual draft and review history

The [authoring log](drafts/authoring-log.md) records the ledgers and each actual repair. Before independent review, self-review caught one omission in the G incident draft: the CSV restoration time, 16:35. The rejected pre-repair bytes remain in `drafts/en-incident-g-v1.txt`. The initial baseline and G candidates were then frozen without silent replacement.

A separate fresh-context Codex reviewer was instructed to read only the method, manifest, and source/candidate files—not the authoring log or earlier benchmarks. Its [full review](review/fresh-review.md) preserves negative findings. Initial preferences were:

| Holdout | Initial preference | Required fidelity findings |
| --- | --- | --- |
| English incident update | G, modestly | None for either; one optional baseline precision note |
| English withdrawal letter | Comparator, narrowly | Comparator narrowed “prevent” to “disqualify”; G changed comment-retention speech act and weakened intended resubmission |
| Korean neighborhood notice | G, clearly | Comparator changed directive/modality and lost an accommodating concession; G assumed first-person association authority and blurred the counting actor |
| Korean exhibition review | G, with repairs | Both shifted evaluations; G also invented a cognitive process and changed the line/person contrast |

The writer repaired only G, retaining all first candidates. In a follow-up against the original sources, the same independent reviewer confirmed that the required repairs were implemented without a new regression and cleared all four frozen finals for detector submission. This is an independent-context AI review, not a human rating, cross-model validation, or blinded study. The reviewer knew arm labels; there is one text per language–genre combination.

## Frozen identity and pending commercial validation

[`frozen-inputs.json`](frozen-inputs.json) fixes 17 source, comparator, initial-candidate, final, and rejected-draft files by byte length and SHA-256. [`results.json`](results.json) lists each exact final hash and records both target fields as `pending_no_authenticated_free_access`; it contains no invented model label, time, receipt, or score.

For a user with existing free authenticated access:

1. Do not edit the files. From the repository root run `sha256sum benchmarks/continuation-g/final/*.txt` and compare all four values with `results.json`.
2. Submit one exact final document at a time to **GPTZero Basic** and **QuillBot**, without applying vendor rewriting. Verify the editor content against the local bytes before reading the result.
3. For each service, preserve the displayed native model label, UTC timestamp, complete unmodified receipt, exact submitted-input SHA-256, and native metric. Record GPTZero's **Human document probability** and QuillBot's **Human-written text share** separately for the same hash.
4. A document meets the requested target only when both native Human metrics are at least 50% on that exact final. Preserve errors, quota blocks, and mixed/negative results. Do not merge scores across drafts or convert another product's AI score into a Human score.

## Reproducible checks and limits

Run:

```sh
python -B benchmarks/verify_continuation_g.py
python -B -m unittest discover -s skills/bilingual-humanizer/evals -p 'test_*.py'
python -B benchmarks/verify_evidence.py
```

The G verifier checks all 17 frozen byte lengths and hashes, paired-arm presence, distinct identities, and protected numeric/name surfaces. It cannot prove semantic equivalence; that required source-to-candidate reading. Existing evidence verification confirms that this addition did not mutate the published evidence or release checkpoints.

Four adaptive examples cannot support a release claim, an authorship claim, a detector guarantee, or statistical generalization. The result is mixed: explicit voice anchors helped the reviewer recognize the original voice more often, while the first G drafts still introduced agency, speech-act, and inference errors. Production and all earlier checkpoints therefore remain unchanged.
