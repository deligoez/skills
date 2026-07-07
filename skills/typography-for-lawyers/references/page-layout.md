# Page Layout — the highest-impact rules

Layout changes do more for a document than any font swap. Design the **body text first** — it's
the most common element and most determines how the document looks. Four decisions carry the body
text: **font, point size, line spacing, line length** (see also `text-formatting.md` for point
size and `fonts.md` for font choice).

## Quick reference — the key numbers

| Element | Value |
|---|---|
| Line spacing | **120–145%** of point size |
| — Word "Multiple" setting to hit that | enter **1.03–1.24** (not 1.20–1.45) |
| — Word presets to avoid | Single ≈117%, 1.5 ≈175%, Double ≈233% |
| Line length | **45–90 characters** per line (rule of thumb: 2–3 alphabets) |
| Page margins at 12 pt | **1.5″–2.0″** left/right on 8.5×11 |
| First-line indent | **1×–4× point size** (12–48 pt / 0.17–0.67″ at 12 pt) |
| Space between paragraphs | **4–10 points** (0.06–0.14″) |
| Block-quote indent | **0.5″–1.0″** left (optional matching right) |
| Rule / border thickness | **0.5–1 pt** |
| Table cell margins | start **~0.03″**, add in **0.01″** steps |
| Columns on 8.5×11 | **2–3** good; 4 is too many |
| Bates number size | **≥ 12 pt** |
| Asymmetric L/R margins | need **≥ 1″** difference to look intentional |
| Vertical centering | bottom margin **~0.25″** larger than top |

## Body text

Serif is the default and best choice for body text — "most books, newspapers, and magazines use
serif fonts for body text." Configure body text before anything else; the four decisions above
determine most of the page's appearance.

## Line spacing

Optimal is **120–145% of point size**. Typewriter-era "double spacing" meant exactly 2× the size;
word-processor presets miss the target badly (Word's "Double" is ~15% looser than true double).
- **Word:** use the **"Exactly"** setting with a fixed point value (best). If you must use
  "Multiple," enter **1.03–1.24** (Word's math makes 1.5/2.0 land far off). Never use "At least."
- **WordPerfect:** Format → Line → Height and Spacing; leave Spacing at 1.0, set Height to
  **"Fixed"** within 120–145%.
- Line spacing changes document length more than point size does — it's your main lever for hitting
  a page target. (Conversion: points ÷ 72 = inches.)

## Line length

**45–90 characters per line** (including spaces); ~2–3 alphabets is a no-tools heuristic. Short
lines read more comfortably; long lines tire the reader tracking back to the start. **Control line
length with margins, not indentation.** Check character count with the word processor's word-count
tool.

## Page margins

Default 1″ margins are a typewriter holdover — on 8.5×11 they give a 6.5″ line that's too long for
proportional fonts. At 12 pt, use **1.5″–2.0″** left/right; smaller type needs larger margins.
Target the character count, not a fixed measurement. Margins needn't be equal on all sides: trim
top/bottom to fit more lines while preserving line length; for vertical centering make the bottom
margin ~0.25″ larger than the top; asymmetric left/right margins need ≥1″ difference to read as
deliberate. (Worked comparison: 2″ margins + 11 pt + 15 pt line spacing reads like a typeset book
and fits comparable words-per-page to the traditional 1″/12 pt/double-spaced setup.)

## Alignment, indents, and paragraph separation

- **Centered text — sparingly.** Fine for short titles (business-card name, letterhead) and major
  section headings; bad for body blocks (both edges go ragged, and it's hard to align with other
  elements). If you center, use hard line breaks to break lines sensibly.
- **Justified text — your choice, but hyphenation is then required** to avoid "gruesomely large"
  word gaps. Word-processor justification is coarse compared to page-layout software; left-alignment
  is the safer default in a word processor.
- **First-line indent OR space between paragraphs — not both** ("belts and suspenders; you only need
  one"). Indent = 1×–4× point size (narrower columns ≤3″ take smaller indents). The first paragraph
  of a section needs no indent. Never indent with tabs or spaces; never use drop caps in legal
  documents. Space between paragraphs = 4–10 pt (the gap between two paragraphs is the *larger* of
  one's space-after and the next's space-before, not the sum — drive it with space-after).

## Hyphenation

Automated breaking for evenness. **Mandatory with justified text.** Optional with left-aligned text
(cuts raggedness but doesn't aid readability). More useful as lines get shorter. **Suppress it in
headings** — auto-breaks there cause more harm than good ("utterly use-less"). Word (Win): Layout →
Hyphenation → Automatic; Word (Mac): Tools → Hyphenation; WordPerfect: Tools → Language →
Hyphenation.

## Block quotations

Set slightly smaller point size and slightly tighter line spacing than body text; indent the left
side **0.5″–1.0″** (matching right optional); **omit quotation marks** (the indent already signals
it). Keep the indent noticeable without making the line too short. Don't overuse block quotes for
emphasis — readers treat a long block as "something long and dull" to skip. Prefer editing the quote
and weaving it into the narrative.

## Lists

Use the **automated** bulleted/numbered list features — manual bullets/numbers waste time and break.
Bullets may use a different font or smaller size; hollow bullets are subtler than solid; asterisks
make poor bullets (too small, too high); dingbat geometric shapes work better than pictorial ones
at small sizes (and beware symbols with cultural/religious meaning).

## Tables

Use tables for data grids and for positioning text side-by-side (letterhead, caption pages) where
white-space characters fall short. Two fixes that make tables look professional:
1. **Turn off all cell borders first,** re-enabling only the few needed for readability — the text's
   arrangement already implies structure.
2. **Increase cell margins** — defaults (especially Word's) are too tight. Start ~0.03″ and raise in
   0.01″ steps; top/bottom may exceed side margins.

## Rules and borders

Use sparingly — often extra space above/below does the separating job without a line at all
(Tufte's "chartjunk"). Thickness **0.5–1 pt**: thinner won't reproduce on office printers, thicker
adds noise. Standalone rules allow a bit more latitude than box borders. **Never** make rules/borders
from repeated characters (hyphens, underscores, section marks) or use patterned/dotted/double
borders. When a rule accompanies a heading, put it **above** the heading (separating it from the
prior section, not from its own text).

## Keeping things together across page breaks

- **Widow/orphan control** — prevents a lone last line at a page top (widow) or lone first line at a
  page bottom (orphan). Test it, though: the blank gaps it leaves can annoy more than the widows it
  fixes. Word: Paragraph → Line and Page Breaks → Widow/Orphan control.
- **Keep with next paragraph** — binds a heading to the text it introduces so they never split.
  **Always use it on headings.** Word: same panel → "Keep with next."
- **Keep lines together** — forces a whole paragraph onto one page; use selectively for headings,
  signature blocks, jury-instruction groups (it's blunt — long paragraphs leave big gaps).
- **Page break before** — starts a paragraph on a new page; built into a heading *style* it beats
  inserting manual page breaks everywhere. Word: "Page break before" (WordPerfect: manual breaks
  only).
- Space above/below a heading is emphasis (a "dramatic pause"): make space **below** a heading
  *smaller* than space above (headings relate to what follows), and larger than normal paragraph
  spacing so it stands out.

## Columns

Good for long documents (contracts, settlements) to get short lines without huge margins. **2–3
columns** on 8.5×11; four is too many. Align rows across columns like a newspaper: note the line
spacing, then set space-between-paragraphs to a whole multiple of it — simplest is either **zero**
or **equal to the line spacing**.

## Footnotes

Four fixes: (1) delete the default separator line, using white space instead — but keep it when a
footnote continues across a page; (2) make the in-text reference numbers *more* prominent (bold or a
sans face), not less; (3) set the reference number *inside* the footnote at the same size as the
footnote text, not shrunken superscript; (4) use a **negative first-line indent** so the number sits
flush at the block edge and the wrapped lines align.

## Line numbers (court filings)

Lock everything to **exact** line spacing so numbers align with text baselines. California example
(adapt per jurisdiction): 1″ margins, 12 pt, 28 lines/page, **exactly 24 pt** line spacing (twice
the size — do *not* use the "Double" preset), **zero** space between paragraphs everywhere including
headings. Put the numbers in a tall borderless text box in the left margin, typed with **hard line
breaks** between numbers, also set to exactly 24 pt, then nudge with arrow keys to align. Numbers may
use a different size/font as long as the 24 pt spacing holds.

## Bates numbering

Size **≥ 12 pt**. Font: Franklin Gothic Medium/Demi; avoid condensed or very heavy faces (Arial
Black) that scan/photocopy poorly. Color: a medium-dark **orange** stands out in discovery yet
survives black-and-white copying. Ensure numbers don't overlap content (Acrobat can shrink pages to
free margin space). Add via Acrobat's Bates Numbering tool with "Shrink document to avoid
overwriting" enabled.

## Watermarks

**Avoid them.** ("Draft"/"Confidential" in six-inch red diagonal letters.) They add visual noise,
darken when photocopied, and are hard to make look good. Put the status notice in the header or
footer instead.

## Styles are the DNA of layout

Use **paragraph and character styles** for anything that should look the same. Benefits: apply a
whole set of attributes at once; edit the style once to update everywhere; parent styles cascade to
substyles. Character styles cover font/size/letterspacing/bold/italic/caps/small caps; paragraph
styles add line spacing, indents, rules. Name styles by *role* ("Block Quotation"), not appearance
("Caslon Bold 11.5 pt"); prefer modifying built-in styles to inventing new ones.

## The nine maxims of page layout

1. **Prioritize body text** — font, size, line length, line spacing decide the look.
2. **Distinguish foreground from background** — keep secondary elements subordinate in position,
   size, font, color.
3. **Use the smallest visible increments** — the gap between too little and too much is small.
4. **Test options visually** — print and compare side by side; don't decide in the abstract.
5. **Maintain consistency** — same things look the same; different things are actually different.
6. **Relate new elements to existing ones** — each addition constrains the next, like a puzzle.
7. **Keep it simple** — resist extra colors and fonts.
8. **Learn from good examples** — emulate typography you admire in print.
9. **Embrace white space** — "Work outward from the text, not inward from the page edges. If the
   text looks good, the white space will take care of itself."
