---
name: digital-lexicography
version: 1.0.0
description: >-
  Turn an existing dictionary into structured data, audit it, then grow it — for reading, for search,
  and as an NLP resource. Use whenever you retrodigitise or restructure a dictionary, lexicon,
  glossary, thesaurus, terminology base or word list: parsing entries into headword/sense/etymology
  fields, decoding abbreviation codes and damaged character encodings, merging or cross-verifying
  against another dictionary, adding new entries without corrupting the source, designing dictionary
  search (headword vs definition vs meaning-to-word), or exporting to DMLex / TEI Lex-0 /
  OntoLex-Lemon. Also for the judgement calls: when to leave a field NULL, why merging on a derived
  key destroys homographs, why coverage measured against your own table proves nothing, and where a
  language model helps versus where it silently modernises historical spellings. Trigger on
  "dictionary", "lexicon", "sözlük", "headword", "madde başı", "lemma", "gloss", "etymology",
  "retrodigitise", "scanned dictionary", "wordnet merge" — even when "lexicography" is never said.
license: MIT
compatibility: any-agent
---

# Digital lexicography — a dictionary into data, then further

A dictionary is not a document to convert. It is a dataset that a human being wrote by hand, over
decades, in a private notation that is mostly consistent and occasionally not. Your job is to
recover that notation faithfully, prove you recovered it, and only then extend it.

Two failure modes bracket the work. **Losing** what the source said — collapsing homographs,
dropping a code, modernising a spelling. And **inventing** what it did not say — filling a gap with
the most likely value. The second is worse: lost data is visibly missing, invented data reads as
fact and propagates into everything downstream.

## The contract

Six rules. They are not style preferences; every one of them exists because breaking it destroyed
real data in a real project.

1. **The source layer is immutable.** Scraped or OCR'd files are read-only. Nothing overwrites them
   — new material is appended to new files. Rebuild the database from them; never edit in place.
2. **Every cleaned field keeps its raw twin.** `headword`/`headword_raw`, `definition`/
   `definition_raw`. Any cleaning decision must remain auditable against what arrived.
3. **When it is ambiguous, write NULL.** A field you guessed is indistinguishable from a field you
   knew. Leaving it empty is a claim you can defend; filling it is one you cannot.
4. **Every departure from the source goes in a ledger.** One file, every merge, every blanked field,
   every dropped row, with its count and its reason. Reading the source, "is this ours or theirs?"
   must always have an answer. See `references/source-fidelity.md`.
5. **Every deviation is pinned by a test that names a real entry.** Not "single-letter codes are
   rejected" but "`Babilik` has no etymology language". A rule can be loosened by accident; an entry
   argues back.
6. **Every record knows its layer.** The moment you add or merge anything, per-record provenance
   stops being optional. See "Growing" below.

## The workflow

### 1. Find the source's own key before inventing rules

Printed dictionaries document themselves: an abbreviations list, a symbols page, a "how to use this
dictionary" section. Read them **before** writing a parser, and read them as page images rather than
OCR text — OCR mangles exactly the short tokens that matter (`bot.` → `bol.`, `tic.` → `tie.`).

This routinely pays for itself. In one project the symbols page defined `;` as *"separator between
synonymous and near-synonymous words"* — which turned 126,431 definitions into a 300,243-edge
thesaurus that nobody had noticed was there. The key also settles arguments: when a code was
ambiguous, the author's *other* dictionary listed it.

Expect the key to be incomplete. Codes the dictionary uses but never lists are normal. That fact
drives the auditing rule below.

### 2. Model it as a dataset, not a document

Use DMLex (OASIS standard) as the target shape even if you never export to it: `entry` →
`sense` → `definition`/`example`, plus a general `relation`/`member` table for synonymy, antonymy,
variants and cross-references. Two fields are easy to omit and painful to add later:
`homographNumber` and `listingOrder`. See `references/standards.md`.

### 3. Parse without guessing

Codes chain, compound, and collide. `öz. is.` is one class (proper noun), not two. `gök b.` is a
subject field whose second half is spelled like a word-class code. A single capital letter followed
by a name is a person, not a language. Details and the full trap list: `references/parsing.md`.

### 4. Audit non-circularly

Measuring parsed codes against your own table proves nothing — a code added because you saw it is
covered by construction. Measure against the source's printed key, report the two numbers
separately, and floor each one. See `references/auditing.md`.

### 5. Grow it

Adding entries, merging another dictionary, cross-verifying against a third — this is where a
carefully built resource usually dies, because merging looks like data cleaning and is actually
data destruction. The rules, and the layered provenance model that makes growth safe:
`references/growing.md`.

### 6. Design the access

A dictionary has more than one question. "Which entry is spelled X", "which definitions mention X",
and "which entries *mean* X" are three different searches, and the third is the one print could
never do. `references/access.md`.

### 7. Export

DMLex, TEI Lex-0 (built specifically for retrodigitised dictionaries), OntoLex-Lemon for linked
data. `references/standards.md`.

## Where a language model belongs

Measured, not assumed. A 2025 study on 17th–18th-century dictionaries at the Institute of the
Estonian Language gives the numbers, and the field's own assessment gives the rest.

**Good at — with review:** *enrichment*. Adding modern equivalents, glosses, or commentary to
entries that already exist. Measured at **81% correct**, 11% needing minor edits, **8% needing full
revision**. Usable, and a real time saving, if every suggestion lands in a separate layer that a
human approves.

**Bad at — do not automate:** *structure extraction from images*. Zero-shot recognition of a Fraktur
dictionary produced **41% of entries perfectly**, at a character error rate of **42%** where the
field considers **below 5%** a success.

**The failure that matters most:** *modernisation*. The Estonian team's "most persistent" error was
the model updating historical spellings **despite explicit instructions not to** — `körts` → `kõrts`.
If your source carries historical orthography or transliteration diacritics, this is the exact
damage you spent months preventing.

**Bad at — and it is the one you need:** *word sense disambiguation*. The field's own verdict is
that LLM definition-writing is "often as good as most humans" while sense disambiguation is
"embarrassingly bad". If you already have a dictionary you do not need definitions written; you need
senses told apart.

**The rule:** a model may propose into a layer. It may never write the source layer, transform
existing text, or normalise orthography. Its output carries provenance like any other added layer,
and is reproducible only if you pin the model version — which most lexicographic workflows require
and most model APIs do not guarantee.

## References

| File | Read it when |
|---|---|
| `source-fidelity.md` | Starting a project; writing the deviation ledger; deciding NULL vs guess |
| `parsing.md` | Writing or debugging the entry parser; codes behave oddly |
| `auditing.md` | Building the regression suite; a coverage number looks too good |
| `growing.md` | Adding entries, merging a second dictionary, cross-verifying |
| `characters.md` | The text arrives damaged — PUA, mojibake, tofu, wrong diacritics |
| `access.md` | Designing search; deciding what a "search mode" means |
| `standards.md` | Modelling the schema; exporting; making the data reusable |

## Decision card

```
before writing any parser        → find the printed key; read it as images, not OCR
a field is ambiguous             → NULL, and a line in the ledger
a code appears once              → look for a variant of a code you already know
two records look like duplicates → do NOT merge on a derived key (see growing.md)
coverage looks great             → check what you measured it against (auditing.md)
a character will not decode      → font metrics > printed page > context > never guess
adding a second dictionary       → per-record provenance FIRST, merge second
"the LLM can just clean this up" → not the source layer; propose into a layer, human approves
search returns nothing           → count it; empty results are the design signal
```
