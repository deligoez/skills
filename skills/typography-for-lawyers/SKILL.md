---
name: typography-for-lawyers
description: >-
  Professional typography rules for legal and professional documents, distilled from Matthew
  Butterick's "Typography for Lawyers." Use this whenever you draft, format, review, or advise on
  the appearance of a brief, motion, memo, contract, pleading, caption page, court filing,
  letterhead, business card, résumé, or any document a lawyer produces — and whenever someone asks
  which font, point size, line spacing, margins, or line length to use, how to comply with a court's
  typography rules, how to fix "typewriter habits" (straight quotes, two spaces after a period,
  underlining, all-caps, faux dashes), how to combine or pair fonts, or how to make a proper PDF.
  Trigger it for questions like "what font should this brief use", "format this contract", "is my
  motion's formatting professional", "alternatives to Times New Roman / Arial", or "make this
  document look like it was professionally typeset" — even when the word "typography" is never said.
---

# Typography for Lawyers

A working reference distilled from Matthew Butterick's *Typography for Lawyers*
(<https://typographyforlawyers.com>). It turns a document from typewriter output into professional
typesetting. Use it to advise on, review, or apply typography to any legal or professional document.

## The core idea

**"Typography is the visual component of the written word"** — and it exists **for the reader, not
the writer.** Good typography makes text *more effective*: it conserves the reader's attention (a
lawyer's scarcest resource) so more of it lands on the argument. It is not more important than good
writing, but it makes good writing better — and bad typography quietly undercuts it. There's no
separate "legal typography"; legal documents are held to the same standard as any professional
publishing, because **lawyers are, functionally, publishers.** When a judgment call isn't covered
below, favor *more* consistency with professional typography, not less. (The full reasoning,
including the two "Laws of Typography," the em, and how far to push formatting in court, is in
`references/foundations.md`.)

## Start here: the highest-impact fixes

If you change nothing else, change these — they do the most work, in rough priority order. Most are
**page layout**, because layout outranks font choice.

1. **Fix the line length.** Aim for **45–90 characters per line** (~2–3 alphabets). Default 1″
   margins give ~6.5″ lines that are too long. At 12 pt use **1.5″–2.0″** side margins. Control line
   length with margins, not indents.
2. **Fix line spacing.** Use **120–145% of point size**, set with Word's **"Exactly"** option (a
   fixed point value) — not the "Single/1.5/Double" presets, which miss the range. If a court
   requires "double," that means exactly 2× the point size, *not* Word's "Double" preset (~15% too
   loose).
3. **Body text 10–12 pt** (11 pt is often ideal); experiment in **half-point** steps if unrestricted.
   12 pt is not magic — it's a typewriter habit.
4. **One space between sentences**, never two. **Curly quotes**, never straight. Real **en/em dashes**,
   never `--`. These are the most visible tells of amateur work.
5. **Never underline** for emphasis (a typewriter relic) — use *italic* or **bold** (never both,
   always sparingly). Don't set paragraphs in ALL CAPS; it reads *slower*, so readers skip exactly
   what you meant to stress.
6. **Separate paragraphs one way, not two** — a first-line indent (1×–4× the point size) *or* space
   between paragraphs (4–10 pt), never both.
7. **Turn on kerning** (off by default; enable for 8 pt and up) and **letterspace caps/small-caps**
   by 5–12% (never lowercase).
8. **Upgrade the font.** Replace Times New Roman / Arial with a professional face; if you can't
   install one, at least move off the C- and F-list system fonts. See the font guidance below.

## Reviewing or formatting a document — workflow

1. **Identify the document type and its constraints.** A court filing has rules (point-size minimum,
   margins, line spacing, sometimes a required font); a contract, memo, letterhead, or résumé does
   not. Read any governing court rule *carefully* — it usually leaves far more discretion than lawyers
   assume, and it sets minimums/maximums ("at least", "no more than"), not a fixed look. See
   `references/practical-howtos.md` → *How to interpret court rules*.
2. **Design the body text first** — font, point size, line spacing, line length. It's the bulk of the
   page and determines most of the appearance.
3. **Apply the character-level fixes** — quotes, spaces, dashes, symbols (§/¶ + nonbreaking space),
   ellipses. See `references/type-composition.md`.
4. **Handle emphasis and headings** — bold/italic sparingly, ≤3 heading levels, space above/below as
   the main emphasis, small caps for cross-references. See `references/text-formatting.md`.
5. **Refine layout** — margins, paragraph separation, lists, tables, rules, footnotes, page-break
   controls, line numbers. See `references/page-layout.md`.
6. **Apply the type-specific recipe** for that document. See `references/sample-documents.md`.
7. **Deliver as a PDF** (convert directly, never scan) so your fonts and layout survive. See
   `references/practical-howtos.md` → *How to make a PDF*.

## Font choice — the quick answer

- **Body text: use a serif** — the traditional and still-best choice for body text.
- **The clichés to replace:** Times New Roman (no court actually requires it; it survives by habit)
  and Arial. Professional replacements cost under $200 and instantly upgrade every document. Two
  genuinely good **free** fonts: **Charter** and **Cooper Hewitt**.
- **Butterick's own families** (built for this): **Equity** (serif, made for lawyers), Valkyrie,
  Century Supra, Heliotrope (body serifs); **Concourse** (sans); Triplicate (a nice monospace);
  Hermes Maia and **Advocate** (display/headline).
- **Combining fonts (the pairing question):** most documents want **one** font; a second is the most
  you usually need; almost none tolerate a third. Serif+sans is *not* required — any two *identifiably
  different* fonts work. The reliable trick: **pick two fonts by the same designer.** Butterick's one
  named pairing is **Equity (body) + Concourse (headings/labels)**. Give each font a fixed role;
  never switch fonts mid-paragraph.
- Full alternatives table for every overused system font, the A/B/C/F system-font tiers, licensing,
  and formats are in `references/fonts.md`.

## Reference map

Load the file that matches the task; each is self-contained.

| File | Use it for |
|---|---|
| `references/foundations.md` | The *why* — principles, the two Laws, the em, screen vs. print, judgment calls, how far to push it in court |
| `references/type-composition.md` | Character-level marks: curly quotes, one space, dashes/hyphens, § ¶ ™ ® © and math, ellipses, accents, foot/inch marks, white-space characters (nonbreaking space, tabs, line/page breaks), ligatures — with Windows/Mac keyboard shortcuts |
| `references/text-formatting.md` | Emphasis (no underlining; bold *or* italic), all-caps & small caps, point size, headings & tiered numbering, letterspacing & kerning, color, figures/ordinals/OpenType, fonts to avoid, **mixing fonts**, web/email addresses |
| `references/page-layout.md` | The high-impact numbers: margins, line spacing, line length, indents, paragraph spacing, block quotes, lists, tables, rules/borders, widow/orphan & keep-together controls, columns, footnotes, line numbers, Bates numbering, styles, the nine maxims |
| `references/fonts.md` | Professional vs. system fonts, Butterick's families, **font combinations/pairings**, alternatives to Arial/Times/Palatino/etc., A–F tiers, buying & licensing, font copyright |
| `references/sample-documents.md` | Concrete recipes: caption pages, motions, research memos, letterhead, business cards, résumés, grids of numbers, presentations, contracts, court opinions |
| `references/practical-howtos.md` | The 22 typewriter habits to drop, interpreting court rules, making a correct PDF, embedding fonts in Word, printers & paper, and a common-accented-character input table |

## A few rules worth stating up front

- **Design for the real reader** — busy, skeptical, looking for a reason to stop reading — not the
  patient, fascinated reader you imagine.
- **Use the smallest visible increment.** Headings go 12 → 12.5/13 pt, not 14–15. Typography lives in
  fine differences; the gap between "not enough" and "too much" is small.
- **Test visually.** Print options side by side rather than deciding in the abstract.
- **Embrace white space.** "Work outward from the text, not inward from the page edges. If the text
  looks good, the white space will take care of itself."
- **Judges get the last word** on how a filing is formatted. Comply in good faith; never try to
  "correct" a judge's reading of the rules in a high-stakes matter.

---

*This skill distills the freely available web edition of Matthew Butterick's* Typography for Lawyers
*(<https://typographyforlawyers.com>). All credit for the underlying rules and examples belongs to
Butterick; buy the book to support the work. The typefaces named as "Butterick's own" are his
commercial MB Type fonts.*
