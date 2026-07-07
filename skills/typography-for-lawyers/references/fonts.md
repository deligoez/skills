# Fonts — professional families, combinations, and alternatives

What to use instead of the fonts every legal document already uses, how Butterick's own families
fit together, and how to combine two fonts. For the general emphasis/size rules see
`text-formatting.md`; the mixing rules live in both places because they belong to both.

## Table of contents
- [Why professional fonts](#why-professional-fonts)
- [Butterick's MB Type families](#butterick-mb-type-families)
- [The recommended combinations](#the-recommended-combinations)
- [Alternatives to overused system fonts](#alternatives-to-overused-system-fonts)
- [System font tiers](#system-font-tiers)
- [Buying, licensing, and formats](#buying-licensing-and-formats)
- [The copyright status of fonts](#the-copyright-status-of-fonts)

## Why professional fonts

Lawyers are professional writers, so they should use professional fonts — "the quickest and easiest
way to upgrade your typography." A top-quality family costs under $200 and, unlike a layout skill,
you "put them to work without learning anything new": they improve every document, are distinctive,
won't break, and won't be obsolete in three years. System fonts fall short in print for three
reasons — many are simply low quality; screen-era fonts (Georgia, Verdana, Calibri) had detail
"sanded off" to survive 1990s screens and look clunky on paper; and all of them are overexposed
("please don't adopt the slogan 'A Law Firm Unlike Any Other' and then set it in Helvetica").

Two genuinely good **free** options exist: **Charter** and **Cooper Hewitt**.

## Butterick's MB Type families

Matthew Butterick designed these; Equity was made specifically for legal writers. All ship in
OTF/TTF/WOFF2 with real small caps (as separate caps fonts with recommended letterspacing built in)
and oldstyle + tabular figures. The serif text faces include **two weight grades (A/B)** so you can
pick the one that prints best on your specific printer.

**Six interchangeable body-text families** — each is "one of the fonts available for body text";
they're alternatives to each other and to specific system fonts, not meant to be combined with one
another:

| Family | Type | Character / best use | Replaces |
|---|---|---|---|
| **Equity** | serif | Fits as much text as Times New Roman, legible small; designed for legal writers | Times New Roman |
| **Valkyrie** | serif | Contemporary, calligraphic serif inspired by Palatino | Palatino |
| **Century Supra** | serif | Century Schoolbook style, darker and narrower (fits more) | Century Schoolbook / Georgia |
| **Heliotrope** | serif/sans hybrid | Sans skeleton with serif stroke contrast; blackletter-inspired italic | Helvetica |
| **Concourse** | sans | 1930s geometric sans with warmth; 6 weights | Arial / Helvetica |
| **Triplicate** | monospaced | A *nice* monospace for when one is required; real italics + small caps; Code variant; no programming ligatures ever | Courier |

**Two display / heading families** — meant to sit *above* a body-text family for titles:

| Family | Type | Best use |
|---|---|---|
| **Hermes Maia** | serif display | 1920s German display type inspiration; headings/display |
| **Advocate** | all-caps display (sans + slab, 3 widths × 3 weights) | Business cards, letterhead, logos, titles, headlines |

## The recommended combinations

This is the part about pairings. Butterick is generally reluctant to give a rote pairing method,
but endorses exactly one reliable rule and one named pairing among his own fonts:

- **The rule: combine two fonts by the same designer.** They're built to harmonize. His examples:
  Harriet + Alright Sans (both by Jackson Cavanaugh), and — his one explicit named pairing —
  **Concourse (sans) + Equity (serif), both by Butterick.** That is the canonical
  Typography-for-Lawyers font combination: Equity for body text, Concourse for headings, sidebars,
  labels, and technical callouts (exactly how his own book is set).
- **Advocate + a body serif.** Advocate is the all-caps headline face throughout his book, so
  Advocate (headlines) over Equity/Valkyrie/Century Supra (body) is the natural title pairing.

Combination doctrine (full version in `text-formatting.md`):
- At most **two fonts** per document; rarely three; never four+. One font is fine.
- **Serif + sans is not required** — any two *identifiably different* fonts work, and lower contrast
  often reads better than high. Two different serifs can pair (Lyon + Harriet); two near-identical
  fonts cannot (Palatino + Palatino Nova).
- Give each font a **fixed role.** In a research memo: one for body, one for headings. In a motion:
  one for the center (body + headings), one for the edges (line numbers, footer, miscellany).
- **One font per paragraph** — change fonts only at paragraph breaks.

## Alternatives to overused system fonts

Butterick's chapter pairs each tired system font with better replacements. Bold entries are his own
MB Type families; ★ marks free fonts.

| Instead of… | Because… | Use |
|---|---|---|
| **Arial** | Clunky and painfully overexposed | Neutral, Bernini Sans, Cooper Hewitt ★ |
| **Helvetica** | Neutral needn't be dull | Neue Haas Grotesk, Atlas, **Concourse** |
| **Times New Roman** | "You can and should do better" | **Equity**, Tiempos, Verdigris |
| **Courier New** | "Spindly, lumpy, and just plain ugly" | **Triplicate**, Pitch |
| **Palatino** | Harsh version of Zapf's original | **Valkyrie**, Palatino Nova, Iowan Old Style, Lyon |
| **Baskerville** | "Brittle and excessively quaint" | Baskerville 10, Ingeborg, Kingfisher |
| **Georgia** | Screen-era compromises now obsolete in print | Miller, Harriet, Chronicle, **Century Supra** |
| **Verdana** | Built for 1990s screens | Alright Sans, Sweet Sans, Breuer, **Concourse**, **Hermes Maia** |
| **Gill Sans** | Overexposed | Ideal Sans, Brandon Text, Verlag, **Concourse** |
| **Cambria** | "Too much consistency can be numbing to read" | Guardian Egyptian, Elena, Skolar, Charter ★, Source Serif ★ |
| **Calibri** | Rounded corners make print body text look soft | **Concourse**, Guardian Sans, Seravek, Fort |

Note the myth to retire: **no court actually requires 12-pt Times New Roman.** Times New Roman was
drawn narrow for 1929 newspaper columns (Stanley Morison / Victor Lardent), "the italic is
mediocre," and it survives in law by habit, not any rule. (The one place a Century-family font *is*
mandated is the U.S. Supreme Court, which under Rule 33 forbids Times New Roman — see
`sample-documents.md`.)

## System font tiers

When you can't install a professional font, Butterick grades the bundled ones as a harm-reduction
chart. Rule: **print → A list only; screen/drafts → A and B; avoid C; never F.**

- **A (tolerable):** Athelas, Avenir, Bell MT, Book Antiqua, Californian FB, Calisto MT, Century
  Schoolbook, Charter, Franklin Gothic, Garamond, Gill Sans, Hoefler Text, Iowan Old Style, Optima,
  Palatino…
- **B (limited, screen ok):** Calibri, Candara, Constantia, Corbel, Futura, High Tower Text,
  Perpetua, Segoe UI, Tw Cen MT.
- **C (questionable):** Baskerville, Cambria, Courier New, Didot, **Georgia**, **Times New Roman**.
- **F (fatal to credibility):** **Arial**, Comic Sans MS, Tahoma, Trebuchet MS, Verdana, plus
  novelty/script fonts.

If a PDF might be printed, embed a print-quality font rather than relying on a screen-optimized one
(Acrobat renders its own way, and print is the more demanding medium).

## Buying, licensing, and formats

- **Where/how much:** sold online by designers or retailers, ~$20–50 per style. For body text buy
  the core styles: **roman, italic, bold, bold italic, and roman small caps.** MB Type families run
  $119 (1–2 people) / $239 (3–5) / $359 (6–10); the 8-family library is $499/$999/$1499.
- **Licensing:** fonts are software, licensed per user. The most common violation is buying one
  license and sharing it across an organization. Buy the number of seats you need.
- **Names aren't protected:** "Baskerville," "Garamond," "Caslon" are unprotected, so wildly
  different fonts share a name ("Stempel Garamond and ITC Garamond are as similar as Bart Simpson and
  Lisa Simpson"). Trademarked names (Myriad, Minion) are more reliable.
- **Format:** most professional fonts are OpenType (.otf); some TrueType (.ttf). Both work
  cross-platform, but **Microsoft Office on Windows does better with TrueType** — and Word's PDF
  generator and font-embedding only work with TTF — so install the .ttf versions for Office. See
  `practical-howtos.md` for PDF and embedding.
- **Install:** Windows → Control Panel → Fonts folder (drag in/out). Mac → Font Book (drag into the
  list).

## The copyright status of fonts

- **Typeface *designs* (the letterforms) are not copyrightable** under U.S. law — historically
  classified as "useful articles," and the 1992 Copyright Office change didn't alter that.
- **Font *software* (the .otf/.ttf file) may be protectable** as software (registrable since 1992),
  but the scope was left to the courts. *Adobe v. Southern Software* (1997) suggested glyph shapes
  as expressed in software could be protectable expression, but it settled before appeal — so the
  question remains unresolved.
- **Practical takeaway:** font copyright is weak and uncertain; the industry runs largely on an
  honor system. Don't assume strong copyright protection for a typeface design — at most for the
  specific software file. This is a *licensing* matter (respect the license you bought), not a
  robust copyright regime.
