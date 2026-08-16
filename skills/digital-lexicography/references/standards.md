# Standards and export

Three standards matter, they are deliberately interoperable, and the reason to care is not
compliance — it is that a dictionary nobody can consume is a dictionary nobody will cite.

## DMLex — the one to model against

**Data Model for Lexicography**, an OASIS standard developed by the LEXIDMA technical committee.
It is a *data model*, not a markup language, and it publishes recommended serialisations in XML,
JSON, NVH, **relational database (SQL)** and RDF. That last-but-one is why it is the right target
even for a project that never exports: it was designed to be implemented as tables.

Its stated premise is the one this whole skill assumes: a dictionary is not a document but a dataset
of objects — entries, senses, examples — connected by relations.

### Core

```
lexicographicResource  title, uri, langCode
  entry                headword, homographNumber, partOfSpeech*, label*,
                       pronunciation*, inflectedForm*, sense*
    sense              listingOrder, indicator, label*, definition*, example*
      definition       text, definitionType, listingOrder
      example          text, sourceIdentity, sourceElaboration, label*, listingOrder
```

Two fields are routinely skipped and expensive to retrofit:

- **`homographNumber`** — the thing that distinguishes two entries with the same spelling. Projects
  that instead distinguish homographs by a content hash have no stable, citeable identifier for a
  sense, which matters the moment anyone links to an entry or merges another resource into it.
- **`listingOrder`** — the order the source printed things in, kept separately from any sort order
  you compute. Alphabetical order is a view; listing order is data.

DMLex also defines controlled value lists (for part-of-speech tags, usage labels) with mappings to
external ontologies — the machine-readable version of your abbreviation key.

### Linking module

The general relation model, and the answer to "where do synonymy and antonymy go":

```
relation      type, description, member (2..*)
  member      memberID, role, listingOrder, obverseListingOrder
relationType  type, scopeRestriction, memberType (role, type, min, max, hint)
```

Everything relational uses it: synonymy, antonymy, variant spellings, subsenses, subentries,
cross-references. `role` carries direction — which is exactly what a one-way gloss relation needs,
where the rarer word points at the commoner one.

If you have separate special-purpose tables for each relation kind (a synonyms table, a
cross-reference table, an idiom-link table), you have DMLex's linking module in denormalised form.
That is a reasonable starting point and a bad ending point: the fourth relation kind is the moment
to generalise, because each new special table multiplies the query surface.

## TEI Lex-0 — for retrodigitised dictionaries specifically

A baseline TEI customisation for lexicographic data, with an explicit focus on **retrodigitised**
dictionaries. Of the lexicographic resources collected for the ELEXIS infrastructure, every single
one encoded in TEI Lex-0 was a retrodigitised dictionary.

If your project is a digital edition of a printed work — as opposed to a born-digital lexicon — this
is the format your data will be asked for, and the community that maintains it is the one that cares
about the problems you have.

## OntoLex-Lemon — for linked data

The de facto standard for lexical information as RDF, with modules that matter here:

- **lexicography module** — extensions for traditional dictionary structures.
- **FrAC** (Frequency, Attestation and Corpus) — connects entries to corpus evidence, and includes
  representations for **word embeddings**. If you plan to publish vectors alongside the dictionary,
  there is a defined way to do it; you do not need to invent a format.
- **morphology module** — records the decomposition of forms into morphs, descriptively and
  generatively, aimed explicitly at morphologically rich languages.

## Export as a checklist

What makes an exported dictionary actually reusable, in rough order of how often it is missed:

1. **Stable identifiers.** Per entry and per sense, stable across rebuilds. Derived from source
   provenance, not from row order.
2. **The abbreviation key, machine-readable.** Codes are meaningless without it, and it is the
   cheapest thing to ship.
3. **Provenance per record.** Which layer, which source. Without it, an extended dictionary cannot
   be cited as an edition of the original.
4. **The deviation ledger**, as documentation alongside the data.
5. **Raw twins**, or at least a statement of what cleaning was applied.
6. **Licence and access terms** stated per artefact, not per project.

## Tiering derived data

Where the underlying dictionary is not yours to redistribute, the difference between *the work* and
*facts about the work* is the difference between an impossible negotiation and a workable one.

A tiering that has proved legible to rights holders:

| Tier | Contents | Reconstructs the dictionary? |
|---|---|---|
| **0 — open** | Parsing code, abbreviation key, statistics, deviation ledger | No |
| **1 — open, attributed** | Morphological segmentations, headword list with word class, affix and root inventories, relation graph **without definition text**, frequency data | No |
| **2 — on application** | Full database including definitions | Yes |

The argument that makes tier 1 acceptable is empirical, not rhetorical: fifty thousand morphological
segmentations do not let anyone rebuild three hundred thousand definitions. And tier 1 is usually
where most of the NLP value sits, which means a rights holder can say yes to the useful part without
giving away the asset.

Design the schema so that tier boundaries are a query, not a manual extraction. If separating
definitions from relations requires hand-editing, the tiering will not survive its second release.
