# Type Composition — character-level rules

The small marks that separate professional typesetting from typewriter output. Each rule
below states the **right** form, the **common mistake**, and how to produce the correct
character. Keyboard shortcuts: Windows uses **Alt + numeric code** (type the digits on the
numeric keypad with Num Lock on); Mac uses **Option** combinations.

## Table of contents
- [Quotation marks and apostrophes](#quotation-marks-and-apostrophes)
- [Spaces between sentences and words](#spaces)
- [Dashes and hyphens](#dashes-and-hyphens)
- [Symbols: ¶ § & ™ ® © and math](#symbols)
- [Ellipses](#ellipses)
- [Accented characters](#accented-characters)
- [Foot and inch marks](#foot-and-inch-marks)
- [White-space characters](#white-space-characters)
- [Ligatures and optional hyphens](#ligatures-and-optional-hyphens)

## Quotation marks and apostrophes

**Use curly ("smart") quotes, never straight ("dumb"/typewriter) quotes.** Curly quotes match
the design of the rest of the typeface; straight quotes are a typewriter relic. Straight quotes
are only tolerable in plain-text email.

| Character | Windows | Mac | HTML |
|---|---|---|---|
| Opening single ' | Alt 0145 | Option + ] | `&lsquo;` |
| Closing single ' / apostrophe | Alt 0146 | Option + Shift + ] | `&rsquo;` |
| Opening double " | Alt 0147 | Option + [ | `&ldquo;` |
| Closing double " | Alt 0148 | Option + Shift + [ | `&rdquo;` |

- Turn on smart quotes: Word → AutoCorrect → *AutoFormat As You Type* → check "Straight quotes"
  with "Smart quotes". To convert an existing document, search-and-replace `'` with `'` and `"`
  with `"` — the replace forces conversion.
- **Apostrophes always curl downward** (like a closing single quote: ’), never upward. Two uses:
  possession (*Jessica's*) and omission (*isn't*, *'211* for a patent number).
- **The leading-apostrophe trap:** at the start of a word (*'70s*, *rock 'n' roll*) the smart-quote
  logic guesses wrong and inserts an *opening* quote (‘) that curls up. Fix: type two marks, then
  delete the wrong (upward) one, leaving the downward apostrophe.
- Fix curly quotes *before* apostrophes: in `Patent '211`, the leading mark is an apostrophe, not
  an opening quote.
- Hawaiian ʻokina is a *letter* that points upward — use an opening single quote for it, not an
  apostrophe.

## Spaces

**One space between sentences, one space after any punctuation.** Two spaces is a monospaced-
typewriter convention with no place in proportional fonts. Backed by Bringhurst, Bryan Garner,
the Chicago Manual of Style, and the Seventh Circuit's typography guide. (Follow an employer's
two-space mandate if imposed, but one is the standard.)

**The word space (space bar) has exactly one job: one gap between two words.** Never hold the
space bar to fake alignment or indents — it reflows chaotically when the document is edited. For
other spacing use tabs, indents, nonbreaking spaces, or a table.

## Dashes and hyphens

Three different characters — never interchange them, and never fake a dash with `--` or `---`.

| Character | Windows | Mac | HTML |
|---|---|---|---|
| Hyphen `-` | keyboard `-` | keyboard `-` | `-` |
| En dash `–` | Alt 0150 | Option + Hyphen | `&ndash;` |
| Em dash `—` | Alt 0151 | Option + Shift + Hyphen | `&mdash;` |

**Hyphen** — line-end hyphenation (auto); compound words (*cost-effective*, *topsy-turvy*; but
prefixes don't take one — *nonprofit*, not *non-profit*); and phrasal adjectives before a noun
(*commercial-speech restriction*, *five-dollar bills* vs. the ambiguous "five dollar bills").
Exceptions: no hyphen after "-ly" adverbs (*closely held company*) or in foreign/proper-name
adjectives.

**En dash** — ranges (`1880–1912`, `Exhibits A–E`; but write "from 1880 to 1912", never
"from 1880–1912"); and connection/contrast between separate things (*conservative–liberal split*,
*Sarbanes–Oxley Act* — two people take an en dash; one person's hyphenated surname takes a hyphen).

**Em dash** — a break in a sentence "when a comma is too weak but a colon, semicolon, or
parentheses is too strong." Set flush against surrounding text (spaces allowed if the line looks
cramped).

For subtraction/negatives use the minus sign (en dash `–` or true minus `−`), not a hyphen.

## Symbols

Always use the real symbol, never an alphabetic substitute like `(c)`, `(TM)`, or `x`.

| Symbol | Name | Windows | Mac | HTML |
|---|---|---|---|---|
| ¶ | pilcrow / paragraph | Alt 0182 | Option + 7 | `&para;` |
| § | section | Alt 0167 | Option + 6 | `&sect;` |
| ™ | trademark | Alt 0153 | Option + 2 | `&trade;` |
| ® | registered | Alt 0174 | Option + R | `&reg;` |
| © | copyright | Alt 0169 | Option + G | `&copy;` |

- **¶ and § must be followed by a nonbreaking space** so the mark never splits from its number
  across a line. Double them for multiples: **¶¶**, **§§**. Spell the word out at the start of a
  sentence ("Section 17200 applied…", not "§ 17200 applied…"). Don't sprinkle ¶ inside body text
  to number internal paragraphs — archaic.
- ™ and ® are superscript, set tight against the mark with no space: *Roxy's Tacos*™. © sits on
  the baseline (not superscript) and takes a nonbreaking space before the year: `© 2026`.
- **Autocorrect collision:** Word silently turns `(c)`, `(r)`, `(tm)` into symbols — this mangles
  citations like "Fed. R. Civ. P. 12(c)" into "12©". Watch for it in citations.
- **Ampersand (&)** is a stylized ligature of Latin *et*. Reserve it for proper names
  (*Fromage & Cracotte LLP*) and citation forms (*Bus. & Prof. Code § 17200*). Rule of thumb:
  the more formal the document, the less you use it.
- **Math:** `+` and `=` are fine for simple arithmetic; use the true multiplication sign `×`
  (not the letter x) and true minus `−`. Right: `8.5″ × 14″`, `12 × 34 − 56 = 352`. Insert via
  Word's Symbol dialog.

## Ellipses

A three-dot mark for omitted text. Use the single ellipsis glyph `…` — not three tight periods
(`...`) and not three spaced periods (`. . .`) in general prose.

| Platform | Method |
|---|---|
| Windows | Alt 0133 |
| Mac | Option + Semicolon |
| HTML | `&hellip;` |

- One regular word space before and after (omit if it looks odd). If text sits on only one side,
  use a nonbreaking space there to keep the ellipsis attached.
- **Bluebook (Rule 5.3)** is the exception: it requires **three separate periods with word spaces**
  between and around them (`imperative to . . . courts`), *not* the single glyph. To stop bad
  breaks, join the periods with nonbreaking spaces.

## Accented characters

Reproduce accents faithfully — dropping them misspells the word. **Proper names** always keep
their accents (*Albrecht Dürer*, *François Truffaut*, *Plácido Domingo*) and are never italicized
for them. **Loanwords** vary: some have naturalized and lost accents (*naive*, *melee*, *coupe*),
others keep them (*cause célèbre*, *piña colada*); check a dictionary. The German Eszett (ß,
Alt 0223 / Option + S) is best skipped in English — follow the Swiss "ss" convention, since ß
reads as a "B" or β to most readers. See `practical-howtos.md` for a common-accents input table.

## Foot and inch marks

These are the one place you use **straight** quotes, not curly: foot mark = straight `'`, inch
mark = straight `"` (also prime/double-prime for minutes/seconds). In Word, type the mark and
immediately press **Undo** to defeat the auto-curl; WordPerfect inserts straight marks after
numbers automatically. *Italic* straight quotes approximate the ideal 118° slope better than
roman ones. Use a nonbreaking space between feet and inches: `6' 10"`.

## White-space characters

Invisible characters that control spacing. Using the *right* one keeps layout stable when the
document is edited; faking it (stacked spaces or returns) breaks on the next edit. Toggle
formatting marks to see them: Word ¶ button (Win **Ctrl+Shift+8**, Mac **⌘+8**).

- **Nonbreaking space** — same width as a word space, but glues its neighbors together across
  line/page breaks. Shortcuts: Word Win **Ctrl+Shift+Space**, Word Mac **Option+Space**,
  WordPerfect **Ctrl+Space**. Use before reference numbers (`§ 1782`, `¶ 49`, `Ex. A`, `Fig. 23`),
  after ©, and inside Bluebook ellipses. Judgment call on citations: gluing every space in
  `116 Cal. App. 4th 602` makes one giant unbreakable chunk — glue selectively.
- **Tab / tab stops** — horizontal positioning *within* a line (not for first-line paragraph
  indents — use paragraph settings). Left / center / right / decimal stops set on the ruler
  (Word: View → Ruler). Use a **tab leader** for dotted lines in a table of contents — never type
  rows of periods. For true tabular data, **use a real table, not tabs.**
- **Hard line break** (Word **Shift+Return**, WordPerfect **Ctrl+Shift+L**) — new line *without*
  a new paragraph. Use for address lines and to rebreak a heading without incrementing its number
  (a carriage return there would renumber it).
- **Carriage return** (Enter) — use *only* to start a new paragraph. Never press Enter repeatedly
  to add vertical space (use paragraph space-before/after) or to push text to the next page.
  To clean up: search-and-replace two paragraph marks with one.
- **Hard page break** (Word Win **Ctrl+Enter**; Word Mac 2016 **⌘+Enter**, 2011 **Shift+Enter**;
  WordPerfect **Ctrl+Enter**) — one break forces the next page. Never fake it with carriage
  returns; the layout collapses on any edit above the break. Can be baked into a paragraph style
  ("page break before") so section headings always start a new page.

## Ligatures and optional hyphens

- **Ligatures** merge colliding letters into one glyph. **Mandatory only for an actual f-i
  overlap** (the "fi" ligature) — and check the bold and italic weights, which can collide even
  when roman doesn't. Everything beyond that is stylistic and can look old-fashioned; Butterick
  avoids it except for real collisions. Enable in Word: Font → Advanced → Ligatures → "Standard
  Only". WordPerfect has no automatic ligatures. Don't paste ligature glyphs manually — it breaks
  spell-check and hyphenation. Avoid intrusive decorative ligatures (the "Th" ligature in Minion;
  a spreading italic "gy").
- **Optional (soft) hyphen** marks where an unusual word *may* break if it lands at a line end —
  invisible otherwise. Use it to stop the hyphenation engine from mis-breaking jargon, trade
  names, and odd spellings (e.g. forcing `True-Type` instead of `Tru-eType`). Insert via
  Word → Symbol → Special Characters → Optional Hyphen; WordPerfect → Format → Line → Other Codes
  → Soft hyphen. You can place several in one long word.
