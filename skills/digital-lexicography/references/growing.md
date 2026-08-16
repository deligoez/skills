# Growing a dictionary

Adding entries, merging a second source, cross-verifying against a third. This is where carefully
built resources die, because merging *looks* like tidying and is actually deletion.

## Merging is where dictionaries die

The canonical accident. A project derived a `stable_key = sha1(headword + etymology_note)` and used
it to group records: "same key means the same real entry, keep the newest, archive the rest."

It ran cleanly. It also destroyed nine of the ten senses of one word — ten genuinely different
dialect meanings that happened to share a short, generic etymology note. Nothing errored, nothing
was flagged, and the loss was invisible in every count except the one nobody looked at.

**The rule: never merge on a key you derived from fields you chose.** A derived key measures
*your* notion of sameness, and homographs are precisely the case where that notion is wrong.

Merge only on **independent evidence** — an identifier that comes from outside your own processing:
the source system's own record id, a stable URL, an explicit cross-reference the author wrote. If
you have no such evidence, keep the rows apart. A duplicate row is a cosmetic problem; a swallowed
homograph is data loss you will not detect.

Corollary, for identifiers: once an external id is assigned to one row, it may **never** be assigned
to a second. Enforce that with a claimed-set in code, not with care. Two separate id-collision bugs
in one project were caught only by that guard.

And accept a ceiling. When the source's own index does not distinguish every sense, some records
simply cannot be matched. Pushing past that means guessing, and the guess is unfalsifiable.

## Provenance before growth, not after

The moment a second source enters, per-record provenance stops being a nicety. Minimum per row:

- **which layer** it belongs to (original / addition / merged-in / correction)
- **which source** it came from, at a granularity you can cite
- **what evidence** justified a merge, if it was merged
- **who or what** proposed it, and whether a human approved

Without this, six months later nobody can answer "is this the author's definition or one we
imported?" — and at that point the corpus is no longer citeable as an edition of anything.

Keep the original layer queryable **alone**. Any statistic, audit, or export must be able to say
"the dictionary as published" versus "the dictionary as we have extended it". A reader comparing to
the printed book needs the first; a researcher training a model may want the second.

## Merging a second dictionary

### Measure the overlap first

Before designing anything, answer one question with a number: **how many of our headwords exist in
the other resource at all?**

This is cheap and it usually decides the project. A modern wordnet is modern; a historical
dictionary is mostly not. If 5% of your entries overlap, the merge is a footnote. If 40% do, it is a
new feature. Do not build the pipeline before you know which.

Match on a folded form, and report the overlap **by layer** — modern entries will overlap far more
than historical or dialectal ones, and the average hides that completely.

### Headword agreement is not sense agreement

Two dictionaries listing the same spelling are not thereby talking about the same thing. Aligning
*senses* across resources is a genuine research problem — the field calls it dictionary linking, and
it is hard enough that a whole infrastructure exists for it.

The practical consequence: **what is safe to import differs by field type.**

| Safe | Unsafe without sense alignment |
|---|---|
| Relations attached to a spelling (antonym pairs, variant spellings) | Definitions |
| Inventories (attested forms, inflections) | Sense-level labels: register, domain |
| Frequency and attestation data | Examples attached to a sense |
| Script variants, transliterations | Anything that assumes "sense 1 = sense 1" |

Import into a **separate relation or annotation layer**, never into the original fields. A borrowed
antonym pair is a claim by another resource; store it as such, with its source.

### Licence contaminates

A resource's licence travels with its data. Merging a share-alike or non-commercial resource into
your tables can constrain the whole product, and there is no way to un-merge it later without the
provenance you did not record. Check the licence **before** the technical work, and keep imported
material separable by construction.

## Cross-verification: disagreement is a signal, not an error

The most valuable use of a second dictionary is not filling gaps — it is **disagreeing**.

Run the comparison as a report, not a patch:

- Where do the two resources give different etymological languages for the same headword?
- Where does one mark a sense the other lacks entirely?
- Where does a spelling exist in ours and nowhere else?

Each class tells you something different. A systematic disagreement usually means one of the two has
a parsing bug — often yours. A scattered disagreement is usually genuine scholarly difference, and
is *content*, not noise: "these two dictionaries disagree about this word" is a fact worth exposing
to a reader, not a conflict to resolve silently.

**Never let a cross-check overwrite the source layer.** The other dictionary is not more correct by
virtue of being second.

## Adding new entries

A new entry is held to the same standard as a parsed one, plus provenance:

- Same fields, same codes, same controlled vocabularies. An addition that invents a new label
  fragments every filter it touches.
- An explicit source: attestation, citation, corpus evidence. "It seemed to be missing" is not one.
- A layer marker, so it can be excluded from any comparison with the printed work.
- An entry in the ledger, aggregated by batch rather than per row.

Where additions come from a model, they are **proposals** until a human approves them. Measured
enrichment quality on historical dictionaries is around 81% correct — good enough to save real time,
nowhere near good enough to write unattended. Keep the proposal, the approval, and the approver.

## The audit follows the layers

Once there is more than one layer, every audit needs to know which one it is measuring.

- Coverage against the **printed key** applies to the original layer only. Added entries were never
  in that key; including them makes the number meaningless in both directions.
- Invariants apply everywhere — a dangling reference is a bug whatever layer created it.
- Shape checks should be reported **per layer**. A distribution that shifts after an import is
  exactly what you want to see, and an aggregate hides it.
