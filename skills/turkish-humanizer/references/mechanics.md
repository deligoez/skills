# Türkçe mekanik — TDK yazım, noktalama, sayı kuralları

The mechanics that betray non-native / machine output, with the correct TDK rule. Each pairs a
✓ correct and ✗ wrong example, chosen to match the errors AI and translation produce. Items marked
*(yumuşak)* are style guidance, not hard errors — don't over-correct them.

## Table of contents
1. [de/da, ki, mi — ayrı mı bitişik mi](#1-dedaki-mi)
2. [Noktalama (comma, dash, quotes, apostrophe)](#2-noktalama)
3. [Büyük harf, İ/ı, title case](#3-buyuk-harf)
4. [Kalıp fiiller, "bir", edilgen çatı](#4-kalip)
5. [Ünlü/ünsüz mekaniği](#5-ses)
6. [Sayı, tarih, saat, birim](#6-sayi)
7. [**Otomasyon ve araç tuzakları**](#7-otomasyon)
8. [Hızlı başvuru tablosu](#8-tablo)

## 1. de/da, ki, mi {#1-dedaki-mi}

### de/da — bağlaç (ayrı) vs. ek (bitişik)
- **Test:** the separate conjunction *never* devoices to *te/ta*; the locative suffix does after a
  voiceless consonant. If it can become *-te/-ta*, it's the suffix (bitişik). It's also the
  conjunction if you can swap in *dahi* or delete it.
- ✓ **Evde** kaldım (ek) · **Ben de** geliyorum (bağlaç = dahi) · **Kitapta** yazıyor (ek → kitap+ta)
- ✗ **Bende** geliyorum · Gidip **te** gelmemek (bağlaç asla "te" olmaz) · **Ev de** kaldım
- Özel ad: suffix takes an apostrophe, conjunction never does. ✓ *Ankara'da* (ek) vs. *Ankara da bu
  soruna çözüm arıyor* (bağlaç). ✗ *Ayşe'de geldi* (should be *Ayşe de geldi*).
- *ya da* is always two words (✗ *yada*).

### ki — bağlaç (ayrı) vs. ek (bitişik)
- Bağlaç ayrı: ✓ *Biliyorum ki gelecek.* ✗ *Biliyorumki.*
- **Bitişik yazılan kalıplaşmışlar:** belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki.
- Ek *-ki* bitişik ve genelde uyuma girmez: ✓ *masadaki, yoldaki, yarınki, seninki, onunki.*
  - Sadece üç uyumlu istisna: **bugünkü, dünkü, öbürkü** (✗ bugünki, dünki).

### mi/mı/mu/mü — soru eki (her zaman ayrı)
- Ayrı yazılır, 4'lü uyuma girer, sonraki ekler soru ekine bitişir. "m" ile başladığı için asla
  sertleşmez (ti/tı yok).
- ✓ *Aldın mı? · Gelecek misin? · Okuyor musun? · Gördü mü?* ✗ *Aldınmı, gelecekmisin, okuyormusun.*
- Soru dışı kullanımda da ayrı: ✓ *Güzel mi güzel!* · *değil mi?* (✗ dimi).

## 2. Noktalama {#2-noktalama}

### Virgül — where English adds one and Turkish doesn't
- **No Oxford comma before ve/veya/yahut:** ✓ *elmalar, armutlar ve muzlar* ✗ *…armutlar, ve muzlar.*
- **No comma before "ve" joining two clauses:** ✓ *Toplantı bitti ve herkes ayrıldı.*
- **No comma after a fronted subordinate/adverbial clause** (unlike English "Because X, Y"):
  ✓ *Hava soğuk olduğu için dışarı çıkmadık.* ✗ *…olduğu için, dışarı çıkmadık.*
- **No comma between subject and predicate** in a short sentence: ✓ *Ali dün eve geç geldi.*
  ✗ *Ali, dün eve geç geldi.* (only justified when a long clause separates them)
- Keep legitimate TDK uses: eş görevli sözcükler (*soğuktan, karanlıktan ve korkudan*), ara söz,
  hitap (*Efendiler,*), *evet/hayır/peki* sonrası, ondalık ayırıcı.

### Çizgi — the em-dash trap
Turkish has **two** dashes, and **no** English-style em-dash-as-parenthesis.
- **Kısa çizgi (-):** ara söz (flush, no spaces), aralık/range: ✓ *Küçük bir sürü -dört inekle
  birkaç koyun- yola çıktı.* · *1919-1923* · *Aydın-İzmir yolu.*
- **Uzun çizgi (—) = konuşma çizgisi:** dialogue only, at line start.
- The classic AI habit — a spaced em dash for a mid-sentence aside — is **wrong**. Use flush kısa
  çizgi, a comma pair, or parentheses:
  - ✗ *Proje ekibi — özellikle yeni üyeler — çok şey öğrendi.*
  - ✓ *Proje ekibi (özellikle yeni üyeler) çok şey öğrendi.* / *…, özellikle yeni üyeler, …*
  - ✗ *1919 – 1923* (spaced) → ✓ *1919-1923.*

### Tırnak
- Çift tırnak **"…"** for quotes and titles; single **'…'** only for a quote inside a quote.
- Quoted sentence's own punctuation stays inside: ✓ *Öğretmen "Kim anlamadı?" diye sordu.*
- Mark work/title names: ✓ *"Kendi Gök Kubbemiz" adlı şiir* ✗ *Kendi Gök Kubbemiz adlı şiir.*
- **Never emit guillemets « »** — convert to "…". ✗ *«büyüme»* → ✓ *"büyüme".*

### Kesme işareti (apostrophe)
- **Used** on proper nouns before inflectional (case/possessive/bildirme) suffixes, dates, numbers,
  abbreviations: ✓ *Ankara'da, TDK'nin, 1990'da, 3'üncü, Nihat Bey'e.* ✗ *Ankarada, TDKnin.*
- **NOT used — and the real-world error is usually kesme *fazlalığı*, not eksikliği:**
  - **Cins ada kesme konmaz.** Kesme yalnızca **özel ad / kısaltma / sayı** içindir. Yabancı kökenli
    olsa bile cins ad kesme almaz — ek okunuşa göre doğrudan eklenir:
    ✗ *maniple'yi, buffer'ı, link'i* → ✓ **manipleyi, arabelleği, linki.**
    En temizi zaten Türkçe terimi kullanmaktır: *opcode'u* → ✓ **işlem kodunu.**
  - Yapım/çokluk ekleri: ✓ *Türkçe, Türklük, Amerikalı* ✗ *Türk'çe, Türk'lük, Amerika'lı.*
  - **Kurum/kuruluş adları** (a much-missed TDK exception): ✓ *Türk Dil Kurumunun, Türkiye Büyük
    Millet Meclisine* ✗ *…Kurumu'nun, …Meclisi'ne.*
  - Already-possessive proper nouns (*Boğaz Köprümüzün*), genericized/plural names (*Ahmetler*).
  - Never apostrophize+capitalize a common noun for English-style emphasis: ✗ *yeni Ürün'ünü* →
    ✓ *yeni ürününü.*

## 3. Büyük harf, İ/ı, title case {#3-buyuk-harf}

- **Özel isimler** capitalized: *Türk, Türkçe, Ağrı Dağı, Türkiye Cumhuriyeti.*
- **Unvanlar** capitalized only when attached to a specific name: ✓ *Ahmet Bey, Doktor Mehmet Yılmaz*
  but ✓ *Toplantıya başkan geldi* / *ülkenin cumhurbaşkanı* (standalone → lowercase). ✗ *…Başkan geldi.*
- **Gün, ay, mevsim — the biggest English calque.** Lowercase, capitalized only in a specific date:
  ✓ *3 Mayıs 2023* but ✓ *okullar eylülde başlar*, *perşembe günleri*, *bu kış soğuk geçti.*
  ✗ *3 mayıs 2023*, *Eylülde*, *Perşembe günleri*, *Kış.* Named holidays capitalize content words:
  *29 Ekim Cumhuriyet Bayramı.*
- **İ / ı — the dotted/dotless problem.** i → İ (not I), I → ı (not i); the dot never appears or
  disappears across case. ✓ *İstanbul, İSTANBUL, yapıyorum, Iğdır* ✗ *Istanbul, ISTANBUL, yapiyorum,
  İğdır.* Naive `toUpperCase()` (ISTANBUL, TÜRKIYE) and ASCII "i" for "ı" are mechanical AI/edit
  tells; mixed dotting in one text is a giveaway.
- **Sentence case, not Title Case, for headings:** ✓ *Yapay zekâ metinleri nasıl etkiliyor?*
  ✗ *Yapay Zekâ Metinleri Nasıl Etkiliyor?* Common nouns are never capitalized mid-sentence for
  emphasis (✗ *Misyonu ve Vizyonu*). Named creative works do capitalize content words but keep
  connectives lowercase: *Suç ve Ceza, Leyla ile Mecnun.*

## 4. Kalıp fiiller, "bir", edilgen çatı {#4-kalip}

(Overlaps with `ai-tells.md` §3–4; here with the TDK-precise test. Don't over-flag genuine idioms.)

- **Crutch-verb test:** *"Yardımcı fiilin yerine bir ek getirilebiliyorsa o yardımcı fiil
  gereksizdir."* ✓ *toplantı yaptık* (✗ gerçekleştirdik) · *değiştirdi* (✗ değişiklik sağladı) ·
  *%20 arttı* (✗ artış sağlandı). Trap: *sağlamak* implies a *positive* result — for negative/neutral
  use *neden olmak/yol açmak.* Leave real idioms: *katkıda bulunmak, iletişim kurmak, denge sağlamak.*
- **"[English verb] + etmek" plaza dili:** *update etmek → güncellemek, check etmek → kontrol etmek,
  confirm etmek → onaylamak, focus olmak → odaklanmak, aksiyon almak → harekete geçmek.* Don't touch
  established technical terms or naturalized *fark yaratmak.*
- **"bir" placement/redundancy** — no obligatory article; *bir* = genuine indefinite/counting, and
  sits directly before the noun after any adjective: ✓ *Bu, önemli bir konu* ✗ *Bu bir önemli konu* ·
  ✓ *Sistem hata verdi* ✗ *Sistem bir hata verdi* · keep real counting: *Masada bir kitap var.*
- **Passive overuse** — *"İşi yapan belliyse fiil etken olmalıdır."* The strongest tell is passive +
  a nameable agent (often + *-mıştır* + *tarafından*): ✗ *Rapor tarafımca hazırlanmıştır* →
  ✓ *Raporu hazırladım.* ✗ *Toplantı yarın gerçekleştirilecektir* → ✓ *Toplantıyı yarın yapacağız.*
  Leave legitimate passive: unknown agent (*Ev soyuldu*), haber dili, akademik (*Deney tekrarlanmıştır*),
  genel yönerge (*Burada sigara içilmez*; *Tuz eklenir, karıştırılır*). Fix over-suffixing:
  ✗ *yapılabilinir* → ✓ *yapılabilir.*

## 5. Ünlü / ünsüz mekaniği {#5-ses}

- **Ünlü uyumu:** suffix vowels harmonize to the word's last vowel. ✓ *kitaplar, öğrenciler, eviniz*
  ✗ *kitapler, öğrencilar.* Loanwords still take harmonizing suffixes (*kalemler*, not *kalemlar*).
  Uyuma girmeyen ekler: *-yor, -ken, -ki, -daş, -gil, -leyin, -(ı)mtırak* (✓ *geliyor*, never *geliyör*).
- **Ünsüz benzeşmesi (sertleşme):** after voiceless *ç f h k p s ş t* ("Fıstıkçı Şahap"), a
  consonant-initial suffix's c→ç, d→t: ✓ *kitapta, ağaçtan, sütçü, yoktur* ✗ *kitapda, ağaçdan, sütcü.*
  Note: *gidecek* is **not** this rule (*-ecek* is vowel-initial); and the conjunction *de/da* never
  devoices (✓ *Zonguldak da güzel* ✗ *Zonguldak ta*).
- **Ünsüz yumuşaması:** final p/ç/t/k → b/c/d/ğ before a vowel-initial suffix: ✓ *kitabı, ağacı,
  kulağı, gidiyor, ediyor* ✗ *kitapı, kulakı, gitiyor.* Exceptions: proper nouns don't soften in
  *writing* (✓ *Zonguldak'a, Sinop'u*); many monosyllables resist (*atı, sütü, saçı*); loanwords resist
  (*milleti, sanatı, hukukun*).
- **Ünlü düşmesi:** ✓ *oğlu, ağzı, burnu, aklı, göğsü* ✗ *oğulu, ağızı.* But written norm keeps
  *içeride, dışarıdan, burada, yukarıda* (✗ içerde, burda — spoken only).
- **-yor:** invariant (never *-yör*); a/e-final stems narrow (a→ı, e→i): ✓ *bekliyor, başlıyor,
  anlıyor, diyor* ✗ *bekleyor, anlayor.* Frozen: *deyip, deyince* (not diyip).
- **-makta/-mekte:** a stiff, formal durative that can't carry future meaning; AI overuses it for
  *-yor.* ✓ (formal) *Bakanlık açıklama yapmaktadır* but ✗ (ordinary) *Yarın katılmaktayım* →
  ✓ *Yarın katılıyorum.*
- **Kaynaştırma (y, ş, s, n):** only when a vowel-initial suffix meets a vowel-final stem: ✓ *arabaya,
  arabası, arabasına, altışar* ✗ *arabaa, arabaı.* After a consonant, none: ✓ *okula.*
- **Ünsüz türemesi** (Arabic doubles): ✓ *hakkı, hissi, reddi, tıbbı* ✗ *hakı, hisi, redi.*

## 6. Sayı, tarih, saat, birim — the mirror of English {#6-sayi}

- **Decimal = comma, thousands = period** (opposite of English): ✓ *1.234,56 · 15,2 · 49.750.812*
  ✗ *1,234.56 · 15.2.* But **label numbers take no thousands separator** (years, page/law/house nos.):
  ✓ *1453'te* ✗ *1.453'te.*
- **Percent sign BEFORE the number, no space:** ✓ *%50, %25 büyüme* ✗ *50%, % 25.*
- **Space between number and unit symbol:** ✓ *25 kg, 15 °C, 100 TL* ✗ *25kg, 15°C, 100TL.*
- **Tarih:** prose *gün + ay adı + yıl*, month capitalized, no internal punctuation: ✓ *7 Temmuz 2026*
  ✗ *Temmuz 7, 2026* (English order), *7 temmuz 2026.* Numeric *DD.MM.YYYY* with periods:
  ✓ *07.07.2026* ✗ *07/07/2026.* Suffix apostrophized: *19 Mayıs 1919'da.*
- **Saat:** period, not colon: ✓ *14.30, saat 14.30'da* ✗ *14:30.*
- **Sıra sayıları — one form only:** ✓ *3.* or *3'üncü* ✗ *3.'üncü.*

## 7. Otomasyon ve araç tuzakları {#7-otomasyon}

Türkçe metinle **kod** çalışıyorsa bunlar yazım kuralı değil, **araç kuralıdır** — ve sessizce bozarlar.
(Aşağıdaki çıktılar Unicode veri dosyalarına karşı doğrulanmıştır.)

### 7.1 Türkçe-I sorunu — dört harf, iki kutu
Türkçede **i↔İ** ve **ı↔I** eşleşir. Unicode'un *varsayılan* (İngilizce) algoritması ise **i↔I** eşler.
Fark tam olarak buradan çıkar.

| İfade | Sonuç |
|---|---|
| `"i".toUpperCase()` | `"I"` ✗ |
| `"i".toLocaleUpperCase("tr")` | `"İ"` ✓ |
| `"I".toLowerCase()` | `"i"` ✗ |
| `"I".toLocaleLowerCase("tr")` | `"ı"` ✓ |
| `"İ".toLowerCase()` | `"i" + U+0307` — **iki karakter!** (görünüşte "i", aslında i + birleşen nokta) |
| `"İ".toLocaleLowerCase("tr")` | `"i"` (tek karakter) ✓ |

**Doğru API:**
- **JS:** `toUpperCase()/toLowerCase()` **locale'den bağımsızdır** (her zaman Unicode varsayılanı).
  Kullan: `toLocaleUpperCase("tr")` / `toLocaleLowerCase("tr")`.
- **Python:** `.upper()/.lower()` de locale'den bağımsız — `setlocale` **işe yaramaz**. PyICU ya da
  elle eşleme tablosu gerekir.
- **Java:** `toUpperCase()` (argümansız) **varsayılan locale'i** kullanır — yani görünmez, ortam
  bağımlı davranış. Açıkça `Locale.forLanguageTag("tr")` ya da mantık için `Locale.ROOT` ver.
- **C#:** `ToUpper()` `CurrentCulture` kullanır. Görüntü için `tr-TR`, karşılaştırma için
  `ToUpperInvariant()` / `StringComparison.OrdinalIgnoreCase` (bkz. analiz kuralları CA1308/CA1309).
- **CSS:** `text-transform: uppercase` + doğru `lang="tr"` — spec bunu şart koşar ama **tarayıcı
  desteği tutarsızdır**. Güvenlisi: casing'i JS'te `toLocaleUpperCase("tr")` ile yapıp basmak.

### 7.2 İki ayrı dünya — karıştırma
1. **Kullanıcıya görünen metin** Türkçe casing ister: *istanbul* → **İSTANBUL** (asla *ISTANBUL*).
2. **Koda bakan dizgiler** (anahtar, enum, etiket, komut) **ordinal/invariant** olmalı. Klasik tuzak:
   `tr-TR` altında `"interesting".ToUpper()` → `"İNTERESTİNG"`, dolayısıyla `== "INTERESTING"` **false**.
   Aynı sınıf: `"FILE".toLocaleLowerCase("tr")` → **`"fıle"`** (noktasız ı!) ≠ `"file"`.
   Ve `"İstanbul"` çoğu regex motorunda `/istanbul/i` ile **eşleşmez** (İ'nin katlanması iki karakter).
   Bu, Atlassian Confluence'ı (Java) ve npm'de yargs-parser'ı vuran gerçek hata sınıfıdır.

### 7.3 Sıralama (collation)
Türk alfabesi: **a b c ç d e f g ğ h ı i j k l m n o ö p r s ş t u ü v y z** — ve **ı, i'den önce** gelir.
Naif kod-noktası sıralaması ç/ğ/ı/ö/ş/ü'yü ASCII'nin *arkasına* atar:
```js
["ıstanbul","istanbul","izmir"].sort()                              // ✗ ıstanbul en sona düşer
["ıstanbul","istanbul","izmir"].sort((a,b)=>a.localeCompare(b,"tr")) // ✓ doğru sıra
```
Kullan: `localeCompare(b,"tr")` / `Intl.Collator("tr")`.

### 7.4 Toplu bul-değiştir çekim eklerini bozar — **kelimeyi değiştirme, sar**
Türkçede ek terime yapışır ve **ekin biçimi terimin son sesine bağlıdır.** Naif değiştirme bunu kırar:
- `opcode'u` → *opcode* → *işlem kodu* değiştir → ✗ **`işlem kodu'u`** (doğrusu **işlem kodunu** —
  kaynaştırma `-n-` gerekiyor).
- `yazmaç` → çekimde **yazmacın** (ünsüz yumuşaması) — kök değişince ek de değişir.

**Kural:** ya **çekimli biçimlerin tamamını** listeleyip değiştir, ya da terimi **değiştirme, sar**
(çekimli hâli olduğu gibi bırakıp etrafına işaretleme koy). Terim değişikliği bir **korpus işlemidir**,
bir `sed` işi değil (bkz. `terminology.md`).

### 7.5 Normalleştirme
İ/Ç/Ğ/Ş **NFC↔NFD arasında temiz gidip gelir** — burada bozuk bir tur yok. Gerçek riskler:
- **Karşılaştırmadan önce normalize etmemek** (aynı harf bileşik ve ayrık iki farklı dizgi olabilir).
- **Türkçe *cedilla* (U+0327) ile Romence *virgül-altı* (U+0326)**: Ş/Ţ ile Ș/Ț **göze aynı görünür**,
  kod noktası farklıdır — arama/karşılaştırma sessizce çuvallar.
- ASCII'ye düşürme (ş→s, ı→i) **slug'da** olur, **düz metinde asla**.

## 8. Hızlı başvuru tablosu {#8-tablo}

| Kategori | ✗ (İngilizce/AI) | ✓ (TDK) |
|---|---|---|
| de / mi | geldide, gelecekmisin | geldi de, gelecek misin |
| -ki | bugünki, yarınkü | bugünkü, yarınki |
| Virgül | A, B, ve C · …için, Y | A, B ve C · …için Y |
| Uzun çizgi | metin — ara söz — devam | metin (ara söz) devam |
| Tırnak | «ifade» · başlık işaretsiz | "ifade" · "Başlık" |
| Kesme | Türk'çe · Kurumu'nun · 1990da | Türkçe · Kurumunun · 1990'da |
| Büyük harf | Istanbul, ISTANBUL, yapiyorum · 3 mayıs · Title Case | İstanbul, İSTANBUL, yapıyorum · 3 Mayıs · Sentence case |
| Kalıp fiil | toplantı gerçekleştirdik · aksiyon almak | toplantı yaptık · harekete geçmek |
| bir | Bu bir önemli konu | Bu, önemli bir konu |
| Edilgen | Rapor tarafımca hazırlanmıştır | Raporu hazırladım |
| Ünsüz | kitapda, gitiyor | kitapta, gidiyor |
| -makta | (günlük) katılmaktayım | katılıyorum |
| Sayı/tarih/saat/birim | 1,234.56 · 07/07/2026 · 14:30 · 50% · 25kg | 1.234,56 · 07.07.2026 · 14.30 · %50 · 25 kg |

All rules trace to TDK's Yazım Kuralları / SSS. Items flagged *(yumuşak)* or "leave alone" are style
guidance from reputable editing sources — treat them as soft, not hard corrections.
