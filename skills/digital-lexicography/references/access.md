# Access design

A printed dictionary has one access path: alphabetical, by spelling. Everything a digital edition
adds beyond that is the actual product. Design the paths deliberately, and measure the ones that
fail.

## More than one question

"Which entry is spelled X" is one question. These are others, and they need different machinery:

| Mode | Matches | Answers |
|---|---|---|
| **Headword** | prefix on a folded spelling column | "how is X spelled / what is X" |
| **Definition** | full-text over definition text | "which entries mention X" |
| **Meaning** | whole gloss segment equality | "which entries **mean** X" |
| **Semantic** | vector nearest-neighbour | "which entries are *like* this description" |

The third is the one print could never do, and it is usually already in the data — see below. The
fourth is expensive and mostly redundant once the third exists; measure demand before building it.

Name them for what they answer, not for how they work. A mode called "synonym" promises symmetry the
data may not have; "near meaning" promises less and delivers it.

## The thesaurus already in the definitions

Many dictionaries separate near-synonyms inside a definition with a fixed punctuation mark, and say
so in their symbols page:

```
ra'de   Titreme; titreyiş; raşe.        → three glosses of the headword, not one sentence
```

Splitting on that separator across one dictionary produced **300,243 gloss segments over 100,835
entries**, half of them naming an entry that exists. That is a thesaurus the author wrote by hand and
nobody had extracted.

**Measure the reciprocity before naming the feature.** In that corpus only **6%** of the edges ran
both ways — the rarer word is glossed by the commoner one, not the reverse. So it is not a synonym
ring; it is a one-way relation from rare to common. Read backwards it becomes a way into the
dictionary *by meaning*, which is far more useful than the symmetric reading would have been:

```
"cesur"  →  acar · ahves · alp · atak · bagatur · bahadır …   (96 entries)
```

The definition search returns 162 entries for the same word — every definition that *mentions* it.
The gloss search returns only the ones that *are* it.

Two design rules follow:

- **Match the whole segment, not a prefix.** The segment is an assertion that the entry means this;
  half a word is not that assertion. A prefix match here drags back the same haystack the definition
  search already returns.
- **Only count a list.** A definition with no separator is a definition, not a one-item gloss list.
  Reading it as one makes every entry a synonym of its own definition.

## Show the sense that matched

A hit list normally shows an entry's first sense. In a meaning-based mode the match often comes from
a *later* sense, and showing the first makes a correct result look wrong:

```
query "cesur" → ala göz   "Hafif açık, mavimsi göz; ela."     ← reads as a bad match
                          (the match is sense 2: "Cesur; yiğit.")
```

Order the displayed sense by whether it matched. Same principle anywhere a result has parts: show
the part that answered the query.

## Every offered filter must filter

A facet value that returns everything is worse than one that returns nothing — it silently lies
about the size of the answer. This happens when a filter understands some values and drops the rest:
a period filter that knew four layers and let the other four fall through returned the **entire
dictionary** for a value whose sidebar count said 2.

Two guards:

- Any value the sidebar offers must be reachable by the query that the sidebar links to. Test the
  round trip, not the count.
- Counts and results come from the same table. If the count is computed from one place and the
  filter runs against another, they will diverge and only one of them will be right.

And where a value belongs to a different category than the facet's name suggests, drop it from that
facet rather than redefining the facet — but keep it in the data, and record the removal.

## Counts must not over-promise

If results are capped, cap the count too. Reporting "39,902 entries" while serving 500 is a false
statement about what is reachable. Cap both, or say plainly that the count is a total and the view
is a page.

## Measure the failures, not the traffic

Dictionary user research has a long tradition of log analysis, and its central finding is that
**lookup failures** are what teach you the design. Online dictionaries have a floor of failed
lookups they cannot go below; understanding that floor is the work.

The useful measurements, none of which require storing query text:

- per mode: number of searches, and **share returning zero**
- what a user did immediately after an empty result — retry in another mode, edit the query, leave
- which mode users choose first, and whether they switch

This is also how to decide whether an expensive feature is worth building. "Does semantic search
help?" is unanswerable from a standing start; "what fraction of searches return nothing, and do
those queries describe rather than name?" is a number you can have in three weeks.

## Onomasiological access has a literature

Searching by meaning rather than by form is a named tradition — onomasiological dictionaries — and
its computational form is the **reverse dictionary** task: take a description, return the words that
fit. Approaches range from information retrieval and graph methods to embedding models that encode
descriptions and entries into one space and search by nearest neighbour.

The advantage a real dictionary has over those systems is worth understanding: neural reverse
dictionaries *learn* the description-to-word relation from definitions. A dictionary that separates
its near-synonyms explicitly has a large part of that relation **already written down**, by a human,
with no training and no inference. Extract that first; reach for embeddings for the residue — the
queries that describe a concept in words no gloss contains.
