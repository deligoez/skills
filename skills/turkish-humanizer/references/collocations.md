# Eşdizim ve fiil değerliği — the biggest residual gap

The catalog in `ai-tells.md` catches *phrases*. This file catches something harder: **kelimeler tek
tek doğru, birliktelikleri yanlış.** These are not grammar errors — they're collocation and valency
errors, and they are exactly where an LLM fails, because nothing looks broken locally.

## The governing principle: diller kavramları farklı böler

Two directions, and you must handle both — they are the same insight seen from two sides.

**A. İngilizce birleştirir, Türkçe ayırır → doğru fiili seçmek zorundasın.**
English has one verb where Turkish has five. Picking the wrong one produces a sentence that parses
but no Turkish speaker would write. This is the source of almost every error below.

**B. İngilizce ayırır, Türkçe birleştirir → ayırmaya çalışma.**
Where Turkish uses one word for what English splits, that is a *resource*, not a defect. **Doğallaştırmak,
İngilizceye benzetmek değildir.** Don't manufacture a distinction Turkish doesn't make:
- **tık** — the tap on a wall and the tick of a clock are the same word. English splits (tap/knock
  vs. tick). A text whose ending rests on that unity would be destroyed by "fixing" it.
- **halka** — closed-circuit loop, feedback loop, ring oscillator: all *halka*. English splits
  loop/ring.

Before you "correct" a repeated word, ask whether Turkish is merging on purpose.

## 1. Fiil değerliği — which case does the verb govern?

Turkish verbs govern a specific case. English governs a direct object where Turkish often demands
dative/ablative/instrumental. Getting this wrong is the single most common calque error.

| Fiil | İster | ✓ Doğru | ✗ İngilizce kalkı |
|---|---|---|---|
| güvenmek | -e | sana güveniyorum | seni güveniyorum (trust you) |
| inanmak | -e | sana inanıyorum | seni inanıyorum |
| yardım etmek | -e | sana yardım et | seni yardım et (help you) |
| katılmak | -e | toplantıya katıldı | toplantıyı katıldı (attend/join) |
| girmek | -e | odaya girdi | odayı girdi (enter the room) |
| başlamak | -e | işe başladı | işi başladı |
| ulaşmak / yaklaşmak | -e | sonuca ulaştı | sonucu ulaştı (reach) |
| uymak | -e | kurala uy | kuralı uy (obey) |
| karar vermek | -e | gitmeye karar verdi | gitmeyi karar verdi |
| ihtiyaç duymak | -e | yardıma ihtiyaç duyar | yardımı ihtiyaç duyar |
| dokunmak | -e | tele dokundu | teli dokundu (touch) |
| cevap vermek | -e | soruya cevap ver | soruyu cevap ver (answer) |
| korkmak | -den | akımdan korkar | akımı korkar |
| oluşmak | -den | üç parçadan oluşur | üç parçayı oluşur |
| vazgeçmek / bahsetmek / yararlanmak | -den | bundan vazgeçti | bunu vazgeçti |
| ilgilenmek | -le | bununla ilgileniyor | bunu ilgileniyor |

**Ters yön — Turkish takes the accusative where English uses a preposition:**
- **dinlemek** (-i): ✓ *seni dinliyorum* ✗ *sana dinliyorum* ("listen **to**")
- **beklemek** (-i): ✓ *seni bekliyorum* ✗ *senin için bekliyorum* ("wait **for**")
- **aramak** (-i): ✓ *seni aradım* ✗ *senin için aradım* ("search **for**", "call")
- But **bakmak** (-a): ✓ *bana bak* — a useful contrast with *dinlemek*. Don't generalize either way;
  check the verb.

**Geçişsiz fiile nesne takma.** A verb that can't take an object won't grow one.
- ✗ *bir tanesini bile **şaşırmadan** sayacak* → **şaşırmak** is "to be confused," not "to miss."
  ✓ *bir tanesini bile **atlamadan** sayacak* (or *şaşmadan* — *şaşmaz bir doğrulukla*).
  (The idiom *yolunu şaşırmak* exists, but that's a fixed expression, not a general valency.)

## 2. Işık fiil seçimi — hangi ad hangi fiili çeker?

The noun chooses its verb. There is no rule; there is only usage. Getting it wrong is instantly
audible.

- **ses çıkarmak**, *not* **ses etmek**. *Ses etmek* means to **speak / to object** (*Ses etme!* =
  don't say a word). An inanimate thing makes a noise: ✗ *kapı ses eder* → ✓ **kapı ses çıkarır**
  (better still: *kapı gıcırdar / tıkırdar*).
- **karar vermek** (decide) vs. **karar almak** (a body adopts a decision) — not *karar yapmak*.
- **hata yapmak** (not *hata etmek* in modern usage), **kaza yapmak**, **fark etmek**,
  **dikkat etmek** (pay attention) vs. **dikkat çekmek** (attract attention).
- **nefes almak**, **duş almak** but **banyo yapmak**.
- **yol açmak / neden olmak** for a *negative or neutral* result; **sağlamak** implies a *positive*
  one: ✗ *tembelliğim geç kalmamı sağladı* → ✓ *…geç kalmama neden oldu.*

## 3. Bir İngilizce fiil → çok Türkçe fiil

The split table. Pick by what is actually happening, not by the English verb.

| EN | TR seçenekleri |
|---|---|
| make | yapmak · etmek · **çıkarmak** (ses) · **vermek** (karar) · **kurmak** (cümle, plan) · oluşturmak |
| run | koşmak · **çalışmak** (program çalışır) · çalıştırmak · yürütmek · işletmek |
| set | ayarlamak · kurmak · belirlemek · koymak · (bit) **1 yapmak / kurmak** |
| clear / reset | temizlemek · **sıfırlamak** |
| drive | sürmek (**hattı sürmek**) · beslemek · kumanda etmek |
| hold | tutmak · saklamak · barındırmak |
| carry | taşımak · iletmek · (aritmetikte) **elde** |
| store | saklamak · depolamak · yazmak |
| toggle | **evirmek** · çevirmek · değiştirmek |
| latch | **mandallamak** · tutmak |
| feed | beslemek |

**Domain trap — open/closed (bir gözlem, belgelenmiş bir yanılgı değil):**
Devre kuramında **açık devre** = *akım geçmez*, **kapalı devre** = *akım geçer* — bu **doğrulanmıştır**
(MEB *Basit Elektrik Devreleri* modülü bunu birebir böyle tanımlar). Ama günlük Türkçede **"aç" =
çalıştır** (*ışığı aç*). Dolayısıyla çıplak *"anahtar açık"* iki yöne birden çekilebilir.

Dürüst ol: bunun Türkçe fizik eğitiminde **belgelenmiş bir kavram yanılgısı olduğuna dair kaynak
bulunamadı** — literatür başka yanılgıları (akımın "tükenmesi" vb.) sayar, bunu saymaz. Yani bu, bir
*kural* değil, dikkat edilecek bir **gerilim**. (Yine de gerçek: tr.wikipedia'nın "Anahtar (elektrik)"
taslağı bu eşleştirmeyi **tersten** yazmış durumda — demek ki insanları ısırabiliyor.)

Pratik: çıplak bırakma. Ya açımla (*anahtar açık, yani akım geçmiyor*) ya da tartışmasız bir söyleyiş
seç (*anahtar iletimde / kesimde*). Kararı terim defterine kilitle (`terminology.md`).

## 4. "gibi" isteyen yapılar — evidential calques

English "appears/seems to VERB" does not map onto a bare Turkish verb chain.
- ✗ *tutuyor **görünüyor*** → ✓ *tutuyor **gibi** görünüyor* / *tuttuğu anlaşılıyor* / *tutuyor
  olmalı.*
- "tends to X" → *genelde X-er*; "is likely to X" → *büyük ihtimalle X-er* — not a literal chain.

## 5. Tamlama mantığı — nesne gerçekten o fiilin nesnesi olabilir mi?

A possessive phrase must name something the verb can actually act on.
- ✗ *duvarın **ardını** açıyorsun* — a thing's "ardı" is not openable.
  ✓ *duvarı açıyorsun* / *duvarın ardına geçiyorsun* / *duvarın arkasını görüyorsun.*

Test: strip the modifiers and read the bare pair. *"Ardını açmak"* — does that phrase exist? No.

## 6. Kendini sınama (the self-test that catches all of the above)

Run this on every verb you write, especially in a rewrite:

1. **"Bu fiil bu nesneyi/tümleci gerçekten alır mı? Hangi hâli ister?"**
2. **"Bu ikiliyi Türkçe yazan biri kurar mı? Tanığım var mı?"** Look for the pair in real usage (TDK
   Sözlük'ün örnek cümleleri, gerçek metinler). If you cannot attest the pairing, **you invented it.**
3. **Tanık bulamıyorsan icat etme** — tanıklı bir fiil seç, ya da olayı betimle.
4. Before "fixing" a word that repeats, ask direction **B**: is Turkish merging on purpose?

The failure mode is confident invention. When in doubt, choose the plainer verb you can attest over
the more elegant one you cannot.
