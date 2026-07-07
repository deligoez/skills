# Akıcı Türkçe — natural, fluent Turkish (the positive principles)

Removing AI tells is only half the job. This file describes what fluent Turkish *does*, so a
rewrite is pushed toward genuine naturalness — not just scrubbed of bad patterns. Drawn from TDK
guidance and the tradition of Nurullah Ataç, Feyza Hepçilingirler (*Türkçe Off*), and Ömer Asım
Aksoy (*Dil Yanlışları*). Each principle pairs a **çeviri kokan/bozuk → doğal** example.

## The four master principles

Almost every fix below is one of these. Internalize them and most rewrites become obvious.

1. **Bırak fiil taşısın** — let a clear finite verb carry the sentence, not a nominalization chain.
2. **Bırak ekler bağlasın** — join ideas with verb suffixes (`-ıp, -ınca, -dığı için, -erek`),
   not heavy sentence-initial connectors.
3. **Her kelime hakkını versin** — cut any word whose meaning is already carried by a neighbor, a
   suffix, or the verb.
4. **Fiil ekine güven, zamiri düşür** — Turkish is pro-drop; the verb already marks person, so drop
   `ben/sen/o/biz` unless you need contrast.

Turkish is agglutinative and pro-drop: suffixes already encode person, tense, and much of the
connective logic English needs separate words for. The single thing that most makes Turkish read as
translated is **over-explicitness** — saying with a separate word (a connector, a pronoun,
"bir şekilde," "sahip olmak," a light verb) what the language already says through a suffix. The
most reliable rewrite is usually **deletion**.

## 1. Word order and focus (vurgu)

Turkish is SOV: the predicate normally closes the sentence, and **the element immediately before
the verb carries the focus.** Word order is flexible *because* focus is positional — which is
exactly why word-for-word English SVO calques read wrong. Keep subject and predicate from drifting
apart; put the emphasized element right before the verb.

- Focus moves with the pre-verbal slot:
  - "Okula **Ali** gitti." (who went → Ali) vs. "Ali **okula** gitti." (where → okula)
- Don't spray subject pronouns or chop every idea into its own sentence (English shape) — chain:
  - ✗ *O, sabah erken kalktı. O, kahvaltısını yaptı. O, işe gitti.*
  - ✓ *Sabah erken kalkıp kahvaltısını yaptı, işe gitti.*
- Don't strand the predicate far from its subject with a giant embedded clause:
  - ✗ *Şirketin geçtiğimiz yıl, ekonomik belirsizliklere ve artan maliyetlere rağmen, yeni pazarlara
    açılma stratejisi kapsamında gerçekleştirdiği yatırımlar başarıyla sonuçlandı.*
  - ✓ *Şirket geçen yıl, ekonomik belirsizliklere ve artan maliyetlere rağmen, yeni pazarlara açıldı.
    Yatırımlar başarıyla sonuçlandı.*

**Devrik cümle (inverted order).** Natural and expressive in speech, literary/emotional prose, and
deliberate emphasis (Nurullah Ataç built a style on it): *"Gitmek istemiyordu. Ama gitti."* But in
formal, informational, or academic writing, inversion reads as stiff — there, keep predicate-final
(kurallı) order. Match inversion to register; don't sprinkle it into a technical explainer.

## 2. Verb-driven, not noun-heavy

Turkish's verb carries tense, aspect, person, and voice in one word. Fluent Turkish lets a clear
verb drive the sentence instead of stacking nominalizations behind a crutch verb (`yapmak, etmek,
gerçekleştirmek, sağlamak, bulunmak`). Noun-heavy chains creep in from bureaucratic language and
English translation.

- ✗ *Sporcular koşuyu gerçekleştirdi.* → ✓ *Sporcular koştu.*
- ✗ *Karar verme işlemini gerçekleştirdi.* → ✓ *Karar verdi.*
- ✗ *Projenin zamanında tamamlanmasının sağlanması için ekstra personel görevlendirilmesi
  gerekmektedir.* → ✓ *Projeyi zamanında tamamlamak için ekstra personel görevlendirmek gerekiyor.*

**Important caveat (do not overcorrect).** Turkish's normal formal/academic register is *natively*
more nominal than English's. So the goal is **not** "verbs instead of all nominalizations" — that
would make Turkish sound *more* foreign. The target is only the *puffed-up bureaucratic* form when a
plain one exists: unwind the crutch-verb-plus-abstract-noun shell (`değerlendirme yapmak` →
`değerlendirmek`), but leave legitimate nominal phrasing alone (*"Okumanın faydaları saymakla
bitmez"* is perfect Turkish). See `ai-tells.md` §3.

## 3. Connect with suffixes, not signpost words

Fluent Turkish folds "and then / because / by doing / when" into the verb. Reach for suffixes before
reaching for a sentence-initial connector.

| Meaning | Suffix (not connector) | Example |
|---|---|---|
| and then (sequence) | `-ıp` | *Kapıyı açıp içeri girdi.* (not *açtı ve girdi*) |
| because | `-dığı için` | *Kar yağdığı için hava soğuktu.* (not *Çünkü kar…* as a new sentence) |
| by means of | `-erek/-arak` | *Kitabı okuyarak öğrendi.* (not *okudu ve bu şekilde öğrendi*) |
| when | `-ınca / -dığında` | *Eve gelince telefon çaldı.* (not *geldi ve tam o sırada…*) |
| while | `-ken` | *Yürürken düşündü.* |
| as / the more | `-dıkça` | *Okudukça anladı.* |
| without | `-madan` | *Sormadan girdi.* |

- Trade heavy academic connectors for light native links:
  - ✗ *Şirket kâr elde etmiştir. Bununla birlikte, maliyetler de artmıştır. Ayrıca bu durum
    çalışanları etkilemiştir.*
  - ✓ *Şirket kâr etti ama maliyetler de arttı; bu da çalışanları etkiledi.*
- Placement: the traditional rule is not to *open* a sentence with **ve** (a bağlaç links, so it
  shouldn't start a clause), but **ama / ancak / çünkü / oysa** at the head of a sentence is natural
  and idiomatic for emphasis.

## 4. Concision — cut gereksiz sözcük

Agglutination lets one word do a phrase's work. Cut any word whose meaning is already carried by a
neighbor, a suffix, or the verb. **Test:** remove the suspect word; if the meaning is unchanged, it
was redundant.

- **Synonym doubling:** ✗ *Sene 2010 yılıydı* → ✓ *2010 yılıydı*; ✗ *ana, temel konu* → ✓ *temel konu*.
- **Pleonasm (meaning already inside another word):**
  - ✗ *geri iade etmek* → ✓ *iade etmek* (iade = giving back)
  - ✗ *gizlice çalmak* → ✓ *çalmak* · ✗ *ilk kez tanışmak* → ✓ *tanışmak* · ✗ *gizli sır* → ✓ *sır*
  - ✗ *en optimal* → ✓ *en iyi / optimal* · ✗ *ilk önce* → ✓ *önce* · ✗ *beklenmedik sürpriz* → ✓ *sürpriz*
- **Suffix already carries it:** ✗ *karşılıklı mesajlaştılar* → ✓ *mesajlaştılar* (-laş- is already
  mutual); ✗ *hemen yiyiverdi* → ✓ *yiyiverdi* (-iver- already means suddenly).
- **Yardımcı fiil padding:** ✗ *yapmakta olduğumuz iş* → ✓ *yaptığımız iş*.

## 5. Register (üslup) — hold it constant

Turkish separates **resmi** (formal/official), **samimi** (intimate), and **edebi** (literary).
Fluent writing stays inside the one the context calls for; *mixing* registers mid-passage is itself
a fluency failure. Infer the target from context (email to a professor vs. text to a friend vs. an
essay) and rewrite consistently toward it.

- Avoid needless bureaucratic weight (ağdalı/bürokratik dil) in non-official contexts:
  - ✗ *Gereğinin yapılmasını arz ederim.* → ✓ *Gereğini rica ederim.* / *Bilgilerinize sunarım.*
- But don't force casualness where it doesn't belong either: don't drop spoken contractions
  (*geliyom, napıyosun*) or filler (*yani, işte*) into considered prose. Register-matching is
  bidirectional.
- (Note: in official correspondence, a subordinate → superior closes with *"Arz ederim,"* a
  superior → subordinate with *"Rica ederim"* — reversing them is an error. For ordinary use,
  *"Saygılarımla"* fits.)

## 6. Collocations and idiom (kulağa doğru gelmek)

A grammatical sentence can still be "off" if the pairing isn't the one natives use. When a rewrite is
correct but sounds wrong, check the collocation:

- ✓ *karar almak* (not *karar yapmak*), *önem taşımak / arz etmek* (not *önem tutmak*),
  *dikkat çekmek* (not *dikkat almak*).
- Idiom (deyim) is a fluency signal, not decoration: a flat, idiom-free rewrite of originally
  colorful text often reads as flattened/translated even when every sentence is correct. Keep the
  color where the register invites it — but don't manufacture idioms that weren't there.

## 7. Vowel harmony and native feel

- **Büyük ünlü uyumu:** back vowels (a, ı, o, u) follow back; front (e, i, ö, ü) follow front.
- **Küçük ünlü uyumu:** unrounded → unrounded; rounded → narrow-rounded (u, ü) or wide-unrounded.
- Established **loanwords are exempt** and don't sound wrong (*kitap, model, tiyatro, dükkân*), but
  suffixes still harmonize to the word's final vowel (*kavun-u, saat-i*). Apply harmony-checking to
  native-feeling coinages, not to established loans.
- Memorized native exceptions (not errors): *anne, elma, hangi, kardeş, şişman*. Fixed
  non-harmonizing suffixes: *-yor, -ken, -ki, -daş, -gil, -leyin, -mtırak*.

## 8. Common anlatım bozuklukları to fix

Turkish pedagogy groups expression errors into semantic and structural families. Flag both when they
appear (fuller list with examples in `mechanics.md` and `ai-tells.md`):

- **Özne–yüklem uyumsuzluğu:** *Herkes aynı fikirdeydi* (not *…fikirdeydiler*); inanimate plurals
  take a singular verb: *Çiçekler kurumuş* (not *kurumuşlar*).
- **Öge eksikliği** (missing shared object/complement): ✗ *Öğrencilerini sever ve sürekli yardımcı
  olurdu* → ✓ *…ve onlara sürekli yardımcı olurdu.*
- **Tamlama yanlışı:** ✗ *tıbbi ve gıda yardımı* → ✓ *tıbbi yardım ve gıda yardımı*.
- **Mantık/sıralama:** escalate weak→strong: ✗ *ölebilir hatta yaralanabilirsin* → ✓ *yaralanabilir
  hatta ölebilirsin.*
- **Yanlış anlamda sözcük:** *şans* vs *risk*, *öğrenim* vs *öğretim*, *kaplamak* vs *kapsamak*.

## Net heuristic

A Turkish sentence "sounds right" when (a) native-feeling words obey vowel harmony, (b) pairings
match established collocations, (c) idiom appears where register invites it, and (d) pronouns and
clause-joining lean on Turkish's own suffixes rather than importing an obligatory-pronoun,
conjunction-joined English shape. When a sentence is grammatical but reads translated, the fix is
almost always one of the four master principles above — usually **deletion**.
