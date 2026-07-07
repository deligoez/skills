# Text Formatting — emphasis, size, headings, and combining fonts

How to make type do work: emphasis, capitalization, point size, headings, and mixing typefaces.
The through-line: emphasis is a budget. Spend it sparingly, because "if everything is emphasized,
then nothing is emphasized."

## Table of contents
- [Never underline](#never-underline)
- [Bold or italic (not both)](#bold-or-italic)
- [All caps and small caps](#all-caps-and-small-caps)
- [Point size](#point-size)
- [Headings](#headings)
- [Letterspacing and kerning](#letterspacing-and-kerning)
- [Color](#color)
- [Figures, ordinals, and OpenType features](#figures-ordinals-and-opentype)
- [Fonts: goofy, monospaced, and system fonts](#fonts-to-avoid)
- [Mixing fonts](#mixing-fonts)
- [Web/email addresses and email formatting](#addresses-and-email)

## Never underline

**Don't underline text — ever, for emphasis.** It's a typewriter workaround (typewriters had no
bold or italic), it's ugly, it cuts through descenders, and it's confused with hyperlinks and
track-changes marks. Use bold, italic, small caps, a point-size change, or a heading instead.
The Bluebook (20th ed.) actually prefers italics *over* underlining for case names. The one place
underlining belongs is a clickable web hyperlink.

## Bold or italic

**Treat bold and italic as mutually exclusive — never combine them — and use both sparingly.**
Plain text is called *roman*. Long stretches of bold or italic are harder to read and burn your
ability to emphasize anything later.

- **Serif fonts:** italic = gentle emphasis, bold = stronger emphasis.
- **Sans-serif fonts:** skip italic (a sans italic is often just a faint slant that doesn't read
  as emphasis, a real problem for citations) — use bold instead.
- Italicize foreign words by how naturalized they are (*bête noire* yes; *croissant* no).
- Weights heavier than bold (black/heavy) belong in headlines, not body text. Small caps are a
  further emphasis option.

## All caps and small caps

**Use caps sparingly, and never set whole paragraphs in caps.** All caps flattens the varied
contours of lowercase (ascenders/descenders) that the eye uses to recognize word-shapes, so it
reads slower — capitalizing an "important" contract paragraph is self-defeating, because readers
skip what's hard to read.

- Fine for short items: headings under a line, headers/footers, captions, labels, letterhead,
  business cards, small sizes.
- **Always add letterspacing (5–12%) and enable kerning on caps and small caps.**
- Apply caps as a *formatting toggle* (Word: **Ctrl/⌘+Shift+A**) over mixed-case text, so it can
  be reverted; don't retype in caps.
- For defined terms, capitalize only the first letter — not the whole word.
- Court specifics: California requires defined terms in discovery in all caps
  (Cal. Civ. Proc. Code § 2030.060(e)); New York bans all caps except in headings
  (22 N.Y.C.R.R. 500.1(j)).

**Small caps** are capitals redesigned to the height of lowercase — ideal for cross-references.
**Never use the small-caps toggle button:** it just shrinks regular caps into thin, too-tall
counterfeits. Real small caps are separate font files with calibrated weight and height; buy them
and apply via a character style. (Word/WordPerfect can't reach OpenType small caps, so separate
font files are the practical route.)

## Point size

**Body text: 10–12 point in print.** Courts often mandate a 12-pt minimum, but 10–11 pt is often
more comfortable — experiment downward in **half-point** increments if unrestricted. Business
cards and other professionally-set small items run 6–8 pt; avoid below 7 pt or above 30 pt in
legal documents. On screen, body text wants **15–25 pixels** (screens are read from farther away).

Point size is *not* absolute: the same point size looks different across fonts (it sets the em,
not any glyph — see the em concept in `foundations.md`). To match two fonts' apparent size, set
them equal and nudge until line breaks fall in about the same place. Counterintuitively, when you
bold or cap something, *reduce* its point size slightly — bold/caps already look bigger. Never
shrink a font's effective size to sneak a larger face under a court's stated minimum.

## Headings

Two failure modes: too many heading levels, and too much visual contrast between them. Headings
are signposts for the *argument's* structure, not a transcript of your outline.

**Structure:** at most three levels; two is better. Simplify the outline rather than promoting
every sub-sub-topic to a heading.

**Nine rules:**
1. Avoid all caps and title case (a full-sentence heading is too long for caps).
2. Don't underline.
3. Avoid centering (with narrow exceptions).
4. Use space above/below as the primary emphasis — subtlest and most effective.
5. Prefer bold over italic; never bold-italic.
6. Increase point size by the smallest useful increment (12 → 12.5 or 13, not 14–15).
7. Use at most two indent levels even with more heading levels.
8. Suppress hyphenation in headings; use "keep lines together" and "keep with next paragraph" so a
   heading never strands at a page bottom.
9. For numbering, prefer tiered decimals (see below).

**Hierarchical numbering:** the traditional I / A / 1 / a / i scheme is hard to read (roman
numerals and romanettes are easy to confuse, letter-to-number mapping breaks down past F/G/H) and
ambiguous (does "i" mean first or ninth?). Prefer a **tiered decimal scheme** (1, 1.1, 1.2,
1.2.1) borrowed from technical writing: all numbers, every reference unique, reader always knows
their position, and word processors auto-generate it.

## Letterspacing and kerning

**Letterspacing** (tracking) adds uniform space between every letter pair. Rule: **add 5–12% to
all-caps and small-caps text — never to lowercase.** Caps are designed to sit beside lowercase,
so cap-to-cap looks too tight without it (especially small footers).
- Word: right-click → Font → Advanced → Spacing → **0.6–1.4 pt per 12 pt** of size.
- WordPerfect: Format → Typesetting → Word/Letter Spacing → **105–112% of optimal**.
- Don't overdo it: if a gap could fit another letter, it's too wide.

**Kerning** adjusts specific problem pairs (the font ships hundreds of pairs). **Always turn it
on** — it's off by default. Word: Font → Advanced → "Kerning for fonts ___ Points and above" →
enter **8**. WordPerfect: Format → Typesetting → Automatic Kerning. Build both into your paragraph
and character styles so they apply consistently.

## Color

**Body text must be black in print — no exceptions** (résumés, memos, letters). At body sizes
there's too little letter area for color to register as emphasis anyway. Principles: light/dark
contrast is the strongest pull (so bold beats colored type for emphasis); thin/small type can
carry more intense color than heavy/large type; avoid colored type on colored backgrounds. Avoid
white-on-dark ("knockout") type in laser printing — it uses ~20× the toner. When color is
warranted, prefer several *shades of one color* over contrasting hues. On screen, consider dark
gray rather than pure black to cut eye strain (but keep PDFs black if they may be printed — gray
prints "gritty"). Color suits Bates numbering, which is meant to stand out.

## Figures, ordinals, and OpenType

- **Figure styles:** *Lining* figures align at cap height and are the default — **always use
  lining figures with all-caps text** ("TOP 40 IN 1987"). *Oldstyle* figures vary in height like
  lowercase and suit lowercase body text. *Tabular* figures share one width for aligning number
  columns; *proportional* figures vary in width for even body text. (Test: type "00000" over
  "11111" — matching widths = tabular.)
- **Ordinals:** the Bluebook (Rule 6.2(b)(i)) **forbids superscripted ordinals** (1st, 2nd), and
  they read poorly. Set them on the baseline: disable Word's AutoFormat → "Ordinals (1st) with
  superscript" (WordPerfect: QuickCorrect → Format-As-You-Go → QuickOrdinals).
- **OpenType features** (alternate figures, small caps, ligatures, ordinals, fractions) require
  *both* the font and the app to support them. Word 2010+ supports ligatures/alternate
  figures/stylistic sets; **Excel and PowerPoint support none.** Adobe InDesign has the fullest
  support. Foundries publish specimen sheets listing each font's features.

## Fonts to avoid

- **Goofy fonts:** "Distinctive is fine. Goofy is not." No novelty, script, handwriting, or circus
  fonts in any lawyer's document.
- **Monospaced fonts:** every character is the same width (Courier, Consolas, Menlo). They read
  worse and waste horizontal space; there's no reason to use one in body text. If a court *mandates*
  monospacing, pick a good one (see `fonts.md`, Courier alternatives).
- **System fonts:** the fonts bundled with Windows/Mac. Three problems in print: many are simply
  low quality; screen-era fonts (Georgia, Verdana) look clunky on paper; and they're overexposed.
  Butterick grades them — **A-list** acceptable in print, **B-list** ok for screen/drafts,
  **C-list** questionable (Times New Roman, Cambria, Georgia, Courier New, Baskerville), **F-list**
  fatal to credibility (Arial, Comic Sans, Tahoma, Trebuchet MS, Verdana). If a PDF may be printed,
  embed print-quality fonts. See `fonts.md` for professional replacements.

## Mixing fonts

You asked about combinations — here is the core guidance:

- **How many:** "Most documents can tolerate a second font. Few can tolerate a third. Almost none
  can tolerate four or more." One well-chosen font is completely valid.
- **Serif + sans is not required.** You can mix *any two fonts that are identifiably different* —
  even two serifs (e.g. Lyon + Harriet; American papers pair a serif body with a different serif
  headline). *Lower* contrast can read better than maximal contrast; the fonts just need to be
  clearly distinct. Counter-example: don't pair Palatino with Palatino Nova — too similar to
  register as intentional.
- **Rules:** give each font a fixed role (one for body, one for headings); never switch fonts
  *within* a paragraph — only at paragraph/section boundaries.
- **Reliable pairings come from a single designer.** Named examples:
  **Concourse + Equity** (both by Matthew Butterick) and **Harriet + Alright Sans** (both by
  Jackson Cavanaugh). See `fonts.md` for Butterick's font system, which is built to combine.
- **Alternative to mixing families:** get differentiation *within* one family via point size,
  bold/italic, and small caps.

## Addresses and email

- **Never hyphenate a web or email address to wrap it** — a reader may think the hyphen is part
  of the address. Control wrapping with a **hard line break**. Shorten long URLs (TinyURL, Bitly);
  in footnotes you can show both the full and shortened forms.
- Turn off Word's auto-hyperlinking of addresses (AutoFormat → "Internet and network paths with
  hyperlinks") so printed URLs aren't blue and underlined.
- **Email:** fonts aren't transmitted with an email, so recipients only see a font they already
  have. Either stick to common system fonts with simple formatting, or (Butterick's preference)
  treat email as a **typography-free zone**. Don't fake alignment with multiple word spaces, and
  don't send contact info as an image — use text so it can be copied.
