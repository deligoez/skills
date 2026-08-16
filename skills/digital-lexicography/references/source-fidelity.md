# Source fidelity

The discipline that lets you answer, at any point and for any record, **"is this the dictionary's or
ours?"** Without it a corpus becomes unciteable within months, because nobody can tell which of its
oddities are the source's and which are yours.

## The layer model

Three layers, and the boundary between them is enforced by the pipeline, not by discipline.

| Layer | What it holds | Mutable? |
|---|---|---|
| **Source** | Exactly what arrived: scraped JSONL, OCR output, publisher files | Never |
| **Derived** | The parsed database, indexes, statistics, embeddings | Rebuilt from scratch |
| **Added** | New entries, merged material, corrections, model suggestions | Append-only, provenanced |

The derived layer is disposable by construction: a full rebuild from source must be a routine
command, deterministic, and fast enough that nobody avoids it. If rebuilding is frightening, you no
longer have a source layer — you have a database with a backup.

Two properties make this real:

- **Deterministic**: the same source produces a byte-identical database. Measure it once with a
  checksum and keep measuring it; the day it stops being true, something is reading the clock, a
  hash seed, or a file listing order.
- **Offline**: the build makes no network calls. A build that fetches is a build you cannot
  reproduce next year.

Record `source_file` and `source_line` on every row. When something looks wrong, the question
"where did this come from" should cost one query, not an afternoon.

## Raw twins

Every field that cleaning touches keeps the arrival version beside it: `headword`/`headword_raw`,
`grammar_note`/`grammar_note_raw`, `definition`/`definition_raw`.

This is what makes a cleaning decision reversible without re-scraping. It is also what lets you
answer a reviewer who disagrees with a decision: the evidence is in the table, not in a commit
message from two years ago.

## NULL is a result

The rule that saves the corpus: **a field you guessed is indistinguishable from a field you knew.**

Concretely, prefer NULL when:

- Two readings both fit and the counts are close. Merging spelling variants is fine when one side has
  33,980 occurrences and the other has 1; it is not fine at 5 against 4.
- The notation is in the right position but the content is the wrong kind of thing — a person's name
  where a language code belongs, a region where a language belongs.
- The source itself is damaged in a way the printed original shares. If the book prints an empty box
  there too, the gap is the work's, and flagging it beats inventing a reading.

Corollary: **a row asserting nothing is worse than no row.** An "Arabic spelling" row whose value is
`""` claims the dictionary gave an empty spelling. It did not; it gave nothing. Drop the row.

## The deviation ledger

One document, versioned with the code, listing every point where the data differs from the source.
Sections that earn their place:

1. **Spelling merges** — source form, written form, counts, and the pairs you deliberately did *not*
   merge, with the reason.
2. **Deliberately blank** — what was in the field, why it is not a value of that kind, how many.
3. **Not split** — where the source writes two tokens that name one thing (`öz. is.` = proper noun)
   and splitting would lose the name.
4. **Split** — where the source writes one field that carries two facts (`is. ve sf.` = both noun
   and adjective) and keeping one silently loses the other.
5. **Hidden from a filter** — values kept in the data but withheld from a particular facet, and why.
6. **Dropped rows** — with counts.
7. **Repaired typos** — only where the repair needs no judgement about that entry. A closing paren
   inside a brace-delimited tag can only be a typo; a misspelt headword cannot be "fixed".
8. **Namings** — expansions you supplied for codes the source never explained, separated from the
   ones it did. And the list you refused to name, with reasons.
9. **Not a deviation** — the things that look wrong and are the source's own. This section stops the
   same investigation from being repeated every six months, and it is usually the most-read part.

Section 9 deserves emphasis. "Why does this dictionary of Turkish list only 38 words as being of
Turkish origin?" is a question that will be asked again and again. Writing down that native words
simply are not marked, and the code appears only in hybrid derivations, retires it permanently.

## Every deviation gets a test

Two kinds, and you want both:

- **Evidence** — named entries with expected values. `kazak → T.`, `Babilik → NULL`. These are
  arguments, not assertions: loosening a rule means explaining why `kazak` should change.
- **Invariants** — shapes that must hold whatever the source says. "No entry is glossed as itself."
  "No gloss still contains the separator it was split on." "The parsed word class must have left the
  definition text." That last one caught 7,590 wrong senses in one project.

Include *negative* evidence — entries that must **not** change. A guard that over-fires is as bad as
one that never fires, and only a pinned counter-example catches it.
