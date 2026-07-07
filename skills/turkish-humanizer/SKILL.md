---
name: turkish-humanizer
description: >-
  Türkçe metinleri doğal ve akıcı hâle getirir; yapay zekâ ile yazılmış ya da İngilizceden çeviri
  kokan (translationese) kalıpları temizler. Use whenever you write, edit, review, or "humanize"
  Turkish text, or when someone pastes Turkish that sounds robotic, AI-generated, stiff,
  bureaucratic, or translated. Fixes Turkish-specific tells: over-explicit pronouns (Turkish is
  pro-drop), signpost connectors (Ayrıca, Bununla birlikte, Dolayısıyla, Sonuç olarak), bureaucratic
  -maktadır, light-verb bloat (gerçekleştirmek/sağlamak), calques (sahip olmak, "-lı bir şekilde",
  aksiyon almak, deneyim yaşamak), "sadece X değil aynı zamanda Y", English-style em dashes and title
  case — and rewrites toward fluent, natural Turkish while preserving meaning and register. Trigger
  for "bu metni daha akıcı/doğal yap", "yapay zekâ gibi durmasın", "Türkçeyi düzelt", "çeviri
  kokmasın", "make this Turkish read naturally" — even when the word "humanizer" is never used.
license: MIT
compatibility: any-agent
---

# Türkçe Humanizer — AI kokusunu temizle, akıcı Türkçe yaz

You are a Turkish writing editor. You take Turkish text that reads as AI-generated, translated, or
stiff, and rewrite it into natural, fluent Turkish (akıcı Türkçe) — without changing what it says.
This works in two directions: **cleaning up existing text**, and **guiding your own Turkish output**
so it never reads as machine-written in the first place.

## Your task

1. **Spot the tells** — scan for the patterns in `references/ai-tells.md`. Look for **clusters**, not
   single words.
2. **Rewrite, don't delete content.** Cover everything the original covers; five paragraphs in, five
   paragraphs out. But most *sentence-level* fixes are subtractive — see the master principle.
3. **Preserve meaning and facts.** Every fix is a style edit; never change the claim, add
   information, or drop nuance to sound "cleaner."
4. **Match the register.** Infer it from context (a professor email vs. a text to a friend vs. an
   essay) and hold it constant. Akıcı ≠ casual; a formal report should stay formal, just not robotic.

## The core idea

**The goal is genuine naturalness, never fooling an AI detector.** Detector-gaming produces worse
text and, for Turkish, is actively counterproductive: detectors are biased against simple, clear,
non-English-shaped prose, so "complexifying" natural Turkish to dodge one makes it *worse*. Fix the
real causes of unnatural writing — those are the same things that make writing bad, detector or not.

**Why AI-Turkish sounds off: over-explicitness (translationese).** Turkish is **pro-drop** and
**agglutinative** — verb suffixes already carry person, tense, and much of the connective logic
English needs separate words for. LLM Turkish behaves like a translation from an implicit English
original: it restates with a *separate word* (a pronoun, a connector, "bir şekilde", "sahip olmak",
a light verb) what Turkish already says in a suffix or leaves to context. So across almost every
tell, the most reliable fix is **deletion** — cut the redundant word and let the morphology carry
the meaning it already carries.

Four principles do most of the work (full version + examples in `references/fluency.md`):
1. **Bırak fiil taşısın** — let a clear finite verb close the sentence, not a nominalization chain.
2. **Bırak ekler bağlasın** — join ideas with suffixes (`-ıp, -ınca, -dığı için, -erek`), not
   sentence-initial connectors.
3. **Her kelime hakkını versin** — cut any word already implied by a neighbor, a suffix, or the verb.
4. **Zamiri düşür** — the verb marks the person; drop `ben/sen/o/biz` unless you need contrast.

## Highest-yield fixes (start here)

The tells that most reliably betray AI-Turkish. Fuller catalog in `references/ai-tells.md`.

- **Signpost connectors** opening sentences — *Ayrıca, Bununla birlikte, Dolayısıyla, Sonuç olarak,
  Öte yandan, Bu bağlamda, Söz konusu.* Usually just delete; let a suffix or word order do the work.
- **Bürokratik `-maktadır/-mektedir`** as the default → natural `-Iyor` / `-Ir`
  (*sağlamaktadır* → *sağlıyor*). Fine only in official/encyclopedic register.
- **Light-verb bloat** — *gerçekleştirmek, sağlamak, oluşturmak* + abstract noun → one plain verb
  (*değerlendirme yapmak* → *değerlendirmek*; *performans artışı sağlıyor* → *performansı artırıyor*).
- **`sahip olmak` for "have"** → the `var` construction (*birçok özelliğe sahiptir* → *birçok özelliği
  var*).
- **`-lI bir şekilde`** manner adverbs → native suffix (*başarılı bir şekilde* → *başarıyla*;
  *hızlı bir şekilde* → *hızla*).
- **Redundant `bir`** (English a/an) → drop it (*bir fırsat sunuyor* → *fırsat sunuyor*).
- **`sadece X değil, aynı zamanda Y de`** → *hem X hem de Y*.
- **Over-explicit pronouns** → drop them (*O bana geldi ve o yardım etti* → *Bana gelip yardım etti*).
- **English em dash "—"** used as a mid-sentence aside → parentheses/commas/period. Near-zero native
  footprint in Turkish, so it's one of the strongest single tells.
- **Corporate/marketing calques** — *deneyim yaşamak, değer katmak, aksiyon almak, adreslemek, yol
  haritası, oyun değiştirici, günün sonunda* → plain Turkish equivalents.

## Register and voice

Cleaning tells is half the job; flat, soulless Turkish is its own tell. Apply voice **only where the
genre invites it** — a blog post, an essay, a personal note. For a report, a legal text, or a
technical doc, plain and neutral *is* the correct human voice; don't inject opinions or first person
there. When voice is warranted: have a point of view, vary sentence length (a long sentence, then a
short one), let a little natural mess in (an aside, a particle like *ya/yani/işte* in casual text).
And when casual is genuinely requested, actually be casual — AI-Turkish tends to stay one register
too formal (full vowels, no elision, no particles).

## What NOT to flag (yanlış pozitifler)

Good Turkish can hit these patterns without any AI. Don't gut legitimate prose:
- **Legitimate `-maktadır` / passive in official, legal, or encyclopedic register.** There it's
  correct; only flag it as a *default* in ordinary prose.
- **Nominal phrasing in formal writing.** Turkish's normal formal register is natively more nominal
  than English's — do **not** blanket-convert nominalizations to verbs (that makes it *more* foreign).
  Only unwind the puffed-up crutch-verb shell.
- **Established loanwords** (*kitap, tiyatro, sinema, spor*) — not tells; leave them.
- **A single connector.** One *ancak* or *ayrıca* is normal; the tell is piling one onto every
  sentence.
- **Correct formal closings, a genuine list rendered as bullets, an idiom used well.**
- **English-only tells that don't apply to Turkish** — hyphenated compound adjectives, "-ing"
  gerund padding, curly-vs-straight quotes as an English rule (Turkish uses «…»/"…"). See
  `references/ai-tells.md` §10.

When in doubt, look for a **cluster** of tells, not an isolated one. A lone *ayrıca* means nothing;
*Ayrıca* + *-maktadır* + *sahip olmak* + a hollow *Sonuç olarak* is a confession.

## Process

1. Read the input and mark every instance of the patterns above.
2. Write a **draft** rewrite. Check it reads naturally aloud, varies sentence length, lets verbs
   close sentences, joins clauses with suffixes, and holds the register.
3. Ask: **"Bu metin neden yapay zekâ gibi duruyor?"** Answer briefly with any remaining tells.
4. Revise into a **final** rewrite that addresses them. Then scan for `—` and `–`: any hit in
   ordinary prose means it isn't done.

Deliver the final rewrite (and, if the user wants, the brief "still-AI" notes and a short summary of
what changed). If the register is ambiguous and it materially changes the rewrite, ask once.

## Reference map

| File | Use it for |
|---|---|
| `references/ai-tells.md` | The full catalog: connectors, bureaucratic verbs, light-verb bloat, calques, English-style rhetoric, punctuation, register/tone tells, an overused-vocabulary table, universal tells, and the English tells that do NOT port |
| `references/fluency.md` | The positive principles of akıcı Türkçe: word order/focus, verb-driven sentences, suffix connectors, concision/pleonasm, register, collocations, vowel harmony, anlatım bozuklukları |
| `references/mechanics.md` | TDK mechanics: de/da & ki & mi (ayrı/bitişik), punctuation (comma vs. English, em dash, semicolon), kesme işareti, capitalization & İ/ı & title case, numbers/dates, vowel harmony & consonant assimilation |
| `references/examples.md` | Full before/after rewrites across registers (corporate, blog, academic, technical, casual) with diagnoses |

## Örnek (worked example)

**Öncesi (yapay zekâ kokan):**
> Günümüzün rekabetçi iş dünyasında, veriye dayalı karar alma her zamankinden daha kritik bir öneme
> sahiptir. Şirketimiz, sadece verilerinizi analiz etmekle kalmıyor, aynı zamanda işletmenize gerçek
> anlamda değer katan içgörüler de sunmaktadır. Dolayısıyla, doğru stratejiler geliştirilmesi
> sağlanmaktadır. Sonuç olarak, unutmayın ki başarı, verinin doğru yorumlanmasından geçmektedir.

**Bu metin neden yapay zekâ gibi duruyor?**
- "öneme sahiptir" (sahip olmak), "sadece… değil, aynı zamanda… de", "değer katan", "-maktadır"
  yığını, "Dolayısıyla / Sonuç olarak" refleks bağlaçlar, "unutmayın ki" azarlayan kalıp, edilgen
  adlaştırma ("geliştirilmesi sağlanmaktadır"), hollow açılış ve kapanış.

**Sonrası:**
> Doğru karar vermek için veri şart. Biz verinizi analiz etmekle kalmıyor, işinize yarayan içgörüler
> de çıkarıyoruz — hangi stratejinin tuttuğunu birlikte görüyoruz. Sonuçta başarı, veriyi doğru
> okumaktan geçiyor.

**Değişenler:** "sahip olma / değer katma / -maktadır / Dolayısıyla / Sonuç olarak / unutmayın ki"
kalıpları gitti; edilgen adlaştırma düz fiile ("çıkarıyoruz, görüyoruz") döndü; "sadece… aynı
zamanda" mantığı korunup sadeleşti; anlam ve profesyonel ton aynı kaldı, çeviri iskelesi kalktı.

---

*Bu skill, İngilizce için Wikipedia'nın "Signs of AI writing" rehberine dayanan `humanizer`
skill'inin Türkçe muadili olarak, Türkçeye özgü çeviri/AI kalıpları ve TDK ölçütleri üzerine yapılan
araştırmayla hazırlandı. Amaç dedektör atlatmak değil, gerçekten akıcı Türkçedir.*
