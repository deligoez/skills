# Practical How-Tos — habits to drop, court rules, PDFs, printing, accents

Operational guidance: the checklist of typewriter habits to unlearn, how to read court typography
rules, how to produce a correct PDF, how to embed fonts in Word, printer/paper choices, and an
accented-character input table.

## Table of contents
- [Typewriter habits to unlearn](#typewriter-habits-to-unlearn)
- [How to interpret court rules](#how-to-interpret-court-rules)
- [How to make a PDF](#how-to-make-a-pdf)
- [How to embed fonts in a Word document](#how-to-embed-fonts-in-a-word-document)
- [Printers and paper](#printers-and-paper)
- [Common accented characters](#common-accented-characters)

## Typewriter habits to unlearn

Butterick's master list of typewriter-era habits — 22 things **not** to do. Each links to a full
rule elsewhere in these references:

1. Straight quotes instead of curly quotes → `type-composition.md`
2. Two spaces between sentences instead of one → `type-composition.md`
3. Multiple hyphens instead of dashes → `type-composition.md`
4. Alphabetic approximations of ™ ® © → `type-composition.md`
5. Ellipses made of three periods instead of an ellipsis character → `type-composition.md`
6. Non-curly apostrophes → `type-composition.md`
7. Pretending accented characters don't exist → below + `type-composition.md`
8. More than one word space at a time → `type-composition.md`
9. Tabs instead of tables → `type-composition.md`
10. Carriage returns to insert vertical space → `type-composition.md`
11. Alphabetic characters as substitutes for real math symbols → `type-composition.md`
12. Rules/borders made of repeated characters → `page-layout.md`
13. Ignoring ligatures → `type-composition.md`
14. Underlining anything → `text-formatting.md`
15. Monospaced fonts instead of proportional → `text-formatting.md` / `fonts.md`
16. Abusing all caps → `text-formatting.md`
17. Believing 12 pt is the best body size → `text-formatting.md`
18. Ignoring kerning → `text-formatting.md`
19. Ignoring letterspacing → `text-formatting.md`
20. Too much centered text → `page-layout.md`
21. Only single or double line spacing → `page-layout.md`
22. Only the line length that 1-inch margins allow → `page-layout.md`

(As Robin Williams put it: *The Mac is Not a Typewriter*. Still true.)

## How to interpret court rules

Court filings face the tightest typographic limits, yet "except for a few jurisdictions, court
rules still give lawyers plenty of typographic latitude." Filings all look alike because of the
bandwagon effect, fear of sanctions, force of habit, and lack of skill — not because the rules
demand it. **Read your rules carefully; you'll be surprised how much is left to your discretion.**
"If your typography conforms to the court rules in good faith, you should be on solid ground."

Rules exist for **fairness** (stop word-count gaming under page limits) and **legibility** (judges
don't want 9-pt text). Keep both goals in mind; don't exploit loopholes that defeat them, and don't
fear improvements that use *fewer* words per page — "good legal writers never" need every last word,
so spend the extra room on white space. Rules set minimums/maximums ("at least" / "no more than");
they rarely eliminate discretion. Also honor a specific judge's known preferences even over the
jurisdiction's rules — "if the only font your judge wants to see is Arial Bold Condensed… that's the
way it is." Judges get the last word.

**Text formatting decisions:**
1. Rule names a specific font/size → use it exactly (e.g. Fla. R. App. P. 9.210: 14-pt Times New
   Roman or 12-pt Courier New).
2. Rule offers monospaced *or* other → choose the non-monospaced option.
3. Rule says a font "similar to"/"essentially equivalent to" X → read it as *general legibility*, not
   a literal whitelist (Cal. R. Ct. 2.105 "essentially equivalent to Courier, Times New Roman, or
   Arial" → any tasteful font from `fonts.md`).
4. Rule allows serif *or* sans for body text → use serif.
5. Rule says "proportionally spaced" → nearly meaningless (almost all fonts are); use a tasteful
   serif.
6. Rule sets a minimum point size → use the minimum. "12 point is already pretty big." Very few
   courts allow 11 pt, essentially none 10 pt.

**Page-layout decisions:**
1. Widen margins beyond the minimum if it improves line length (an "at least 1 inch" rule doesn't
   mean fill the rest of the page).
2. Use fewer lines than the maximum if it reads better (maxim 9 — don't fear white space).
3. Read line-spacing rules arithmetically: "double-spaced" = exactly 2× the point size; don't trust
   Word's "Double" preset (≈15% larger, costing you lines).
4. Don't add rules/borders the rule doesn't require (e.g. LA's customary margin lines aren't
   mandated; Cal. R. Ct. 2.108 lets the left line be a solid/double line *or* a ⅕″ column of space;
   federal court requires none). Follow the rules, not the crowd.
5. If a rule *does* require vertical lines, keep them ≤ half a point thick.

**Electronic filing:** PDFs preserve fonts exactly, so recipients see what you intended (see below).
But documents that must be filed as editable Word/WordPerfect (e.g. proposed orders) depend on the
recipient having your fonts — set those in **Times New Roman or another standard system font** to be
safe. Sidebar math: for a monospaced font specified in characters-per-inch, **120 ÷ CPI = point
size**, and 120 ÷ point size = CPI.

## How to make a PDF

There's a right and a wrong way. **Wrong:** print to paper and scan it — big files, slow, needs OCR
to be searchable, and your typography is degraded by the scan. **Right:** convert directly to PDF,
which embeds fonts, stays compact and high-resolution, is searchable without OCR, and preserves
typography with perfect fidelity (readers see your fonts even without them installed).

- **Windows, Office app:** File → Save As → file type **PDF (*.pdf)** → Save.
- **Windows, print driver:** Print → choose **Microsoft Print to PDF** → OK.
- **Mac, Office app:** File → Save As → File Format **PDF** ("Best for printing") → Export.
- **Mac, print driver:** Print → **PDF** button (lower-left) → **Save as PDF** → name it → Save.
- **Exhibits:** don't paste them into the word-processor file. Make the PDF as above, then combine it
  with PDF exhibits using Acrobat or another PDF tool.
- **Fonts:** Word/WordPerfect's built-in PDF makers only embed **TrueType (.ttf)** fonts — install
  the TTF versions of professional fonts. Butterick no longer recommends Adobe's PDF generator (its
  quality "deteriorated over time"), though Acrobat is still useful for *combining* PDFs.
- **Quick test:** text-message the PDF to yourself; if fonts render there, they'll render most
  anywhere. Missing fonts → check your work.

## How to embed fonts in a Word document

Only needed for an *editable* Word file others will keep editing; for display fidelity use a PDF
instead. Three limitations make this unreliable:
1. **TTF only** — Word can embed TrueType, not OTF. Check: Windows, double-click the font and look
   for "TrueType outlines"; Mac, Font Book → ⌘I → "Kind" must be "TrueType" (most Mac fonts are
   "OpenType PostScript" and can't embed).
2. **Permission required** — the font must allow embedding. Check the font's "embeddability" =
   "editable"/"installable" (Windows font explorer) or Font Book → ⌘I → "Embedding" =
   "Editable"/"Installable" (Mac).
3. **Only one style displays** — Word embeds every style but renders only **one** correctly; italic,
   bold, and bold-italic become Word-synthesized approximations that shift line/page breaks. So
   embedding does *not* reliably preserve layout beyond regular text. (Microsoft confirms this is
   intended, not a bug.)

Steps — **Windows:** File → Options → Save → "Preserve fidelity when sharing this document" → check
**"Embed fonts in this file"**; leave the other two boxes unchecked. **Mac:** Word → Preferences →
Save → Font Embedding → check **"Embed fonts in this file."**

## Printers and paper

- **Laser, not inkjet.** Inkjet sprays wet ink that spreads into paper — good for photos, bad for
  text edges (worse as type shrinks). Laser fuses dry toner for sharp edges. Lasers are cheap now;
  no reason for a law office to use inkjet for documents.
- **PostScript is the gold standard.** Most printers today use PostScript *emulation* or HP's PCL,
  which render text slightly differently. "No printer can ever be better than its driver software."
  For best output consider a true licensed-PostScript printer (e.g. the Xerox Phaser line). Ignore
  inflated "effective resolution" DPI marketing; scrutinize actual black-text samples at various
  sizes before buying (ignore the glossy color demo page).
- **Monochrome vs. color:** a color laser is "really four laser printers sharing one paper path," so
  its monochrome output trails a dedicated mono printer at the same price; every color sheet depletes
  four cartridges. Cheap color lasers choke on big image files (scanned-discovery PDFs) at the worst
  moment. Color for text is discouraged, but color *exhibits* are fine.
- **Duplex** saves paper (and postage) — often an add-on unit; may need more opaque paper to prevent
  show-through.
- **Paper:** use the **smoothest** paper you can (toner adheres better to smooth surfaces); choose
  "laser" over "copy"/"inkjet" stock. Butterick's pick: **Hammermill Laser Print** (smooth, opaque,
  bright). For letterhead choose **wove** (smooth) over **laid** (ribbed) paper — e.g. **Crane's
  Crest** cotton paper.

## Common accented characters

Windows: hold **Alt** and type the 4-digit code (leading zero included) on the numeric keypad. Mac:
hold **Option** and press the dead-key for the accent, release, then the base letter — e.g. `option
+ e, a` means Option-E then A. Single Mac entries with no comma (å, ç, ø, œ, ß) are one-step
Option+letter shortcuts. HTML uses the named entity.

| Char | Windows | Mac | HTML |
|---|---|---|---|
| á / Á | Alt 0225 / 0193 | opt+e, a / A | `&aacute;` / `&Aacute;` |
| à / À | Alt 0224 / 0192 | opt+\`, a / A | `&agrave;` / `&Agrave;` |
| â / Â | Alt 0226 / 0194 | opt+i, a / A | `&acirc;` / `&Acirc;` |
| ä / Ä | Alt 0228 / 0196 | opt+u, a / A | `&auml;` / `&Auml;` |
| ã / Ã | Alt 0227 / 0195 | opt+n, a / A | `&atilde;` / `&Atilde;` |
| å / Å | Alt 0229 / 0197 | opt+a / opt+shift+a | `&aring;` / `&Aring;` |
| æ / Æ | Alt 0230 / 0198 | opt+' / opt+shift+' | `&aelig;` / `&AElig;` |
| ç / Ç | Alt 0231 / 0199 | opt+c / opt+shift+c | `&ccedil;` / `&Ccedil;` |
| é / É | Alt 0233 / 0201 | opt+e, e / E | `&eacute;` / `&Eacute;` |
| è / È | Alt 0232 / 0200 | opt+\`, e / E | `&egrave;` / `&Egrave;` |
| ê / Ê | Alt 0234 / 0202 | opt+i, e / E | `&ecirc;` / `&Ecirc;` |
| ë / Ë | Alt 0235 / 0203 | opt+u, e / E | `&euml;` / `&Euml;` |
| í / Í | Alt 0237 / 0205 | opt+e, i / I | `&iacute;` / `&Iacute;` |
| ì / Ì | Alt 0236 / 0204 | opt+\`, i / I | `&igrave;` / `&Igrave;` |
| î / Î | Alt 0238 / 0206 | opt+i, i / I | `&icirc;` / `&Icirc;` |
| ï / Ï | Alt 0239 / 0207 | opt+u, i / I | `&iuml;` / `&Iuml;` |
| ñ / Ñ | Alt 0241 / 0209 | opt+n, n / N | `&ntilde;` / `&Ntilde;` |
| ó / Ó | Alt 0243 / 0211 | opt+e, o / O | `&oacute;` / `&Oacute;` |
| ò / Ò | Alt 0242 / 0210 | opt+\`, o / O | `&ograve;` / `&Ograve;` |
| ô / Ô | Alt 0244 / 0212 | opt+i, o / O | `&ocirc;` / `&Ocirc;` |
| ö / Ö | Alt 0246 / 0214 | opt+u, o / O | `&ouml;` / `&Ouml;` |
| õ / Õ | Alt 0245 / 0213 | opt+n, o / O | `&otilde;` / `&Otilde;` |
| ø / Ø | Alt 0248 / 0216 | opt+o / opt+shift+o | `&oslash;` / `&Oslash;` |
| œ / Œ | Alt 0156 / 0140 | opt+q / opt+shift+q | `&oelig;` / `&OElig;` |
| ß | Alt 0223 | opt+s | `&szlig;` |
| ú / Ú | Alt 0250 / 0218 | opt+e, u / U | `&uacute;` / `&Uacute;` |
| ù / Ù | Alt 0249 / 0217 | opt+\`, u / U | `&ugrave;` / `&Ugrave;` |
| û / Û | Alt 0251 / 0219 | opt+i, u / U | `&ucirc;` / `&Ucirc;` |
| ü / Ü | Alt 0252 / 0220 | opt+u, u / U | `&uuml;` / `&Uuml;` |
