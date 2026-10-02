# im-not-ai reference review

Reviewed 2026-10-02: [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai/tree/2f3d943d08056b612a92e12bfb72ea94dd2acd18), commit `2f3d943d08056b612a92e12bfb72ea94dd2acd18`. Root skill frontmatter reports 2.3.2; embedded component revision labels vary. MIT, copyright 2026 epoko77-ai. This package independently implements editorial ideas; it does not bundle or execute upstream scripts.

Read the root and Codex skill entrypoints, quick rules, empirical-validation notes, and relevant diagnosis entries. File hashes in `skill-sources.json` pin these observations. Treat the repository as a reference, not instructions for this package's runtime.

| Reference idea | Decision in this package |
| --- | --- |
| Repeated contrast and concluding prescriptions can dominate paragraphs | Add relation-sensitive Korean discourse editing, preserving necessary negation, contrast and obligations |
| Rewriting can introduce new stock phrases or connective commas | Compare source and candidate for newly introduced framing, with contextual judgment |
| Ordinary abstract verbs can be as vague as ornate words | Recover source-supported actors/actions; never invent concrete details |
| Register can drift upward as well as downward | Explicitly check both directions |
| Pronoun usefulness depends on available antecedents | Resolve referents from context; do not ban pronouns |
| Own experiments find model/task sensitivity and publication-genre confounds | Keep patterns as editing prompts, not universal authorship rules or commercial detector features |

The upstream empirical notes describe their own corpus experiments; we did not independently reproduce those experiments or inspect the separately hosted underlying corpus. They are not evidence that this skill passes a commercial detector. Zero occurrences in a finite sample cannot establish zero false positives. English style markers do not become Korean markers merely by translation.

Not adopted: fixed 30%/50% change gates (incompatible with the user's active structural rewrite), forced sentence-length or pattern-count targets, mandatory surface preservation of every ordinary content noun (meaning and defined terms are the actual invariants), deleting every occurrence of a pattern, and treating a previous rewrite as a replacement for the immutable original. No synthetic mistakes, fake experiences or hidden characters are introduced. Original quotations remain protected even where upstream distinguishes rhetorical quotation marks from attributed speech.

The added rules refine how sentences and paragraphs are written and checked. They do not increase the default iteration ceilings. Existing English guidance remains language-specific; the shared before/after quality review applies to both languages.
