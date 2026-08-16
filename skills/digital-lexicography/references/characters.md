# Damaged characters

Dictionary text arrives broken more often than not, and in ways that look like your bug. Private-use
codepoints, C1 control bytes, mojibake from a re-encoded font, transliteration diacritics that
survived typesetting but not the web export. Before decoding anything, establish **whose damage it
is**: yours, the delivery channel's, or the published work's.

## Evidence, strongest first

1. **Render the font the text was served with.** If the data came from a site that ships its own
   web font, that font *is* the specification. What a reader saw on screen is what the data means,
   whatever the codepoint claims.
2. **The printed page, as an image.** Not the OCR layer.
3. **Independent external facts.** An etymology whose correct spelling is documented elsewhere.
4. **Contextual inference across many words.** Only with several independent attestations.
5. **Never a single example.**

## Fonts lie in their names, not in their outlines

The most useful trick in this work. A publisher who cannot type a character often **redraws an
unrelated codepoint** and leaves the glyph name alone. The font's `cmap` says `Ocircumflex`; the
outline it draws is a `t` with a dot underneath.

You can prove this without rendering anything. A redrawn glyph keeps the **advance width and
horizontal metrics of the letter it was derived from**, and differs only below the baseline:

```
U+00D4  named "Ocircumflex"   advance 569  = the width of "t", not of "O" (1479)
```

And the bounding box separates mark types:

```
bbox bottom -441 = a dot below       -444 = a bar or cedilla below
```

Two consequences worth building into the pipeline:

- A character-mapping audit can assert **metric identity** — every claimed mapping must share an
  advance width with the base letter it claims. That is a pure measurement, needs no rendering, and
  fails loudly if the font is ever swapped or a mapping is invented.
- When the font and the printed book disagree, **the font wins for web-sourced data**. The corpus
  came from the site; the site's font is what its readers saw. Record the choice in the ledger — the
  raw twins make it reversible.

## When the font does not help

Some characters are data-entry errors rather than font hacks, so the font never redrew them. Two
methods work:

**Wildcard matching inside the corpus.** Dictionaries repeat the same word across entries. Treat the
broken character as a wildcard and look for the same shape spelled cleanly elsewhere:

```
[Ar. ðįb]     ↔  [Ar. ðĊb]
[Far. tįmār]  ↔  [Far. tĊmār]
```

**Measure on long words only.** In short words every vowel matches something — a three-letter
pattern will "confirm" six different readings, all of them real words. A minimum length of six
letters turned an unusable 14.9% signal into a decisive 40.4% one.

**Align with the headword.** The entry's own headword is usually the modern form of the word its
etymology describes, so it supplies the missing character directly.

## Look for the encoding, not just the character

Before mapping a codepoint by hand, check whether it belongs to a *scheme*. One project's entire
`0xF0xx` block turned out to be `0xF000 + ASCII` — symbol-style font encoding. `0xF072` = `r`,
`0xF062` = `b`. One observation replaced dozens of individual investigations.

When a new code appears, look at the low byte before looking at the glyph.

## Finding an entry in a scanned original

Searching a scan for a headword usually fails: OCR merges two-column layouts and mangles exactly the
short strings you are searching for. Two things work instead:

1. **Search by definition text.** Definitions are long and distinctive; normalise aggressively and
   search page by page. The headword may be unreadable while its definition is fine.
2. **Build an index from the running heads.** The first letters of the page's entries are printed in
   the corner of nearly every page. Collect them and you have an alphabetical index straight to the
   page you want.

Once you have the page, **read it visually at high resolution** — render at 400 dpi and crop. A
character read as a dot at 150 dpi turned out to be an acute accent at 400.

## Refuse to resolve, and say so

Some codes map to different letters in different words. That is a genuine contradiction in the
source, not a puzzle to solve by picking the more frequent one. Flag the affected rows
(`has_unmapped_glyph`) and leave them.

Sometimes the gap is the work's own. One dictionary prints a hollow box mid-definition — the
original edition is missing the character too. No amount of processing recovers what was never
published; the honest record is a flag and a ledger line.

## Re-verify mappings on every build

A mapping justified once by an argument in a commit message is a mapping that will quietly stop
being true. Make the audit **re-measure** instead of remember:

- Every mapping anchored to real words whose correct spelling is known independently.
- Nothing you claim to have fixed survives decoding.
- Support for each mapping recomputed against a second signal in the corpus, with a failure
  threshold that stops the build.
- An **unknowns** report: every character present in the source that is neither expected, mapped,
  nor deliberately flagged. A fresh scrape that introduces a new broken glyph shows up here instead
  of silently entering the database.

That last check is what turns a one-off cleanup into something that survives the next re-scrape.
