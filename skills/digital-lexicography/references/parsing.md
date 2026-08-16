# Parsing entries

A dictionary entry is a compressed notation. It is positional, it chains, and it was written by
someone who knew what they meant. Every trap below cost real data before it was found.

## Position is meaning

The same bracket means different things at different points in the entry. In one dictionary the
**first** bracket is the etymology, while brackets appearing **after the word class** are verb
conjugation patterns:

```
[rahat-la-t-mak] gçl. f. [-ır]
 └ etymology              └ inflection
```

So locate the word class first, then classify brackets by their position relative to it. Parsing
left to right without that anchor mixes two unrelated fields.

**Mask before you search.** An etymology bracket is full of parentheses that mean something else —
translations of the source word. Searching the raw string for "the parenthetical" finds the
translation instead of the pronunciation:

```
[Far. rānden (sürmek) > -rān -] (ra:n) {OsT} ek.
                └ translation      └ pronunciation
```

Blank the brackets to same-length spaces before looking for parentheses; offsets stay comparable and
the field stops stealing from its neighbour. Getting this wrong put the wrong value in 27,908 of
62,260 entries — silently, because both are plausible strings.

## Codes chain

A sense can carry several codes in a row, from different families:

```
öz. is. isl.   →  class, class, subject field
```

If your matcher only knows two families it stops at the first code it does not recognise and never
reaches the third. Recognise **all** families in one pass — word class, subject field, register,
grammar — and assign each match to its own slot. A version that knew only fields and registers left
7,590 senses with their word class still buried in the definition text.

Take the **first** code of each family; a repeat is the dictionary restating itself.

## Compound codes: do not split what names one thing

Some classes are written as two codes and name a single concept:

| Written | Is | Not |
|---|---|---|
| `öz. is.` | proper noun | proper-something + noun |
| `b. f.` | compound verb | compound + verb |
| `is. t.` | noun phrase | noun + t |
| `gök b.` | astronomy (a subject field) | astronomy + compound |

Order the alternation **longest first**, always. `is. t.` must be tried before `is.`, or the parser
takes the short match and leaves `t.` stranded.

Reading these apart is not a cosmetic loss. Splitting `öz. is.` filed every proper noun in the
dictionary as a plain noun, and the class "proper noun" appeared nowhere in the filter — 143 entries
whose most distinctive property vanished.

## The `X b.` trap

The second half of a compound field code can be spelled exactly like a standalone class code:

```
gök b.   yer b.   eğit. b.   dil. b.   ölç. b.     ← subject fields ("… science")
b. f.    b. is.   b. sf.                          ← compound + class
```

Both contain `b.`. Read apart, `eğit. b.` filed a definition under *education* **and** called it a
compound; `gök b.` fabricated the entire "compound" class — all 7 of its members were astronomy or
geology terms. Distinguish by what surrounds it, and guard the short code with a lookbehind for the
field's first half.

## Single-letter codes need corroboration

A single capital letter followed by a full stop is as likely to be a person's initial as a language:

```
[T. Tekin]                          → Talat Tekin, a researcher — not "Turkish"
[A. Temir]                          → Ahmet Temir
[W. Coleman (industrialist) > Fr.]  → the man colemanite is named after
[F. L. Nason (geologist) > …]       → initials
[A. ḥasren]                         → genuinely Arabic
[T. bey + Far. -zāde]               → genuinely Turkish, in a hybrid compound
```

Three rules together, and they cost nothing:

1. A single letter is a language **only if a printed key names it**. Letters no key lists are people.
2. Reject when the whole bracket is `letter + one capitalised word` — that is an attribution.
3. Reject when the next token is another single-letter initial.

Keep the guard narrow. `T. Kazak > İt. casacca` opens with a proper noun and is still a real
etymology; a rule that rejects "capital letter followed by a capitalised word" loses it.

## A code from another family is not a language

Whatever position it sits in, a code the key files as a word class or a subject field is not a
source language:

```
[Öz. is. Bāb-ī-lik]              → word class leaked into the etymology bracket
[Fiz. Einstein'ın adından]       → subject field, and an eponym
```

Compare case-blind, since the same code is capitalised here and lower-case in the key. Watch for
alphabet-specific folding: Turkish `İ` does **not** lower to plain `i`, which is the only reason
`İs.` (Spanish) is not mistaken for the class `is.`. When a guard holds by a property of the
alphabet rather than by anything you wrote, pin it with a test.

## Multi-word names: take the whole name

```
Amer. yerl. d.       = "American indigenous language"  — one name
Af. yerl. Bantu d.   = "African indigenous Bantu language"
```

The first token alone means something else entirely: `Amer.` on its own is American English, which
is not where *apaş*, *katalpa* and *totem* come from. Take the whole name, up to the word that
closes it — but only when the name **opens** the bracket. Where it appears in a later alternative,
the entry's language is still whatever it opened with.

## Spelling variants of one code

Sources drop spaces, lose diacritics, and shift case:

```
is.t..  → is. t.        yap.e.  → yap. e.
AR.     → Ar.           Mog.    → Moğ.
17.yy.  → 17. yy.       özl.    → öz.
```

Make the space optional inside two-part codes and file the result under the printed spelling, or the
filter grows a duplicate holding one entry. **Do not extend that latitude to codes separated by a
real space** (`son ek`, `ön ek`) — there the space is the only thing separating the code from
ordinary words.

For case and diacritic variants, merge only when the pair is lopsided enough to leave no doubt —
1 against 33,980, yes; 5 against 4, no. Record both decisions in the ledger, including the refusals.

## One field, two facts

The converse of compound codes. When the source writes `is. ve sf.` — "noun and adjective" — the
entry genuinely is both. Keeping one value made it findable among adjectives and not among nouns.

Store the printed form for reading, and a separate one-row-per-value table for filtering. Same shape
as senses: the display column reads as the dictionary prints it, the relation table answers queries.

## Leading parentheticals are notes, not content

```
(Kişi için) çok konuşan; geveze.
 └ usage note              └ the glosses start here
```

Strip a leading parenthetical before splitting a definition into parts, or the note becomes a sense.
