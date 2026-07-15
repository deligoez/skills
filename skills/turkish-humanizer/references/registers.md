# Metin türüne göre üslup — nesir, başlık, slogan, arayüz

Prose rules are not heading rules are not slogan rules. Applying prose instincts to a cover line, or
English headline instincts to a Turkish heading, produces text that is grammatical and still wrong.

**The governing rule: Türkçe, İngilizceden daha az eksilti (ellipsis) kaldırır.** English headline
and slogan register compresses hard — it drops verbs, objects, and articles and still reads. Turkish
does not have that licence. When a compressed English line is carried over, the Turkish reader is
left asking "ne demek bu?" **Fiili ve nesneyi geri koy.**

## 1. Nesir (the default)

The rest of the skill. Full predicates, suffix-chained clauses, register held constant.

## 2. Başlık (headings)

- **Cümle düzeni büyük harf, Title Case değil.** ✓ *Yapay zekâ metni nasıl etkiliyor?*
  ✗ *Yapay Zekâ Metni Nasıl Etkiliyor?* (see `mechanics.md` §3)
- **Yüklemi koru.** English noun-phrase headlines ("Voltage Spike Protection") translate into
  unreadable Turkish. Turkish headings tolerate — and often want — a verb or a question.
- **Tamlama zinciri tuzağı.** English stacks nouns freely; Turkish renders that as an izafet chain
  that collapses under its own weight:
  - ✗ *gerilim darbesi koruma devresi tasarımı* (four levels deep — parse it aloud and you'll stall)
  - ✓ *Gerilim darbelerine karşı koruma devresi nasıl tasarlanır* / *Koruma devresini tasarlamak*
  - **Rule:** ikiden fazla ad tamlaması katı varsa cümleyi yeniden kur — bir fiil ya da bir ilgi
    cümlesiyle böl.
- Soru başlıkları Türkçede doğal çalışır. Ama "X: Neden Önemli?" tarzı iki noktalı listicle başlığı
  İngilizce içerik pazarlamasının kalıbıdır — kaçın.

## 3. Slogan / kapak / vurgu cümlesi

This is where English ellipsis does the most damage, because a slogan is read **alone, with no
context to repair it.**

- ✗ **"okumazsın, kurarsın"** — nesnesiz kaldığı için havada duruyor; nesirde *"devreyi kurarsın"*
  doğal olurdu, sloganda çıplak "kurarsın" çeviri kokuyor.
  ✓ *"Okumakla kalmazsın; kendin kurarsın."*
- ✗ **"adı en sonda"** ← *the name comes last.* İngilizce başlık dili bu sıkıştırmayı kaldırır,
  Türkçe kaldırmaz — okur "ne demek bu?" diye soruyor.
  ✓ *"Önce keşfedersin, adını sonra öğrenirsin."*
- **Test:** sloganı bağlamsız, tek başına oku. Anlaşılmıyorsa eksiltiyi geri al.
- İngilizce slogan eksilti + paralellik üstüne kurulur; Türkçe slogan **fiil + ritim** üstüne kurulur.
  Paralelliği taşımaya çalışırken fiili feda etme.

## 4. BÜYÜK HARF etiketler

Avoid them.
- **i/ı ayrımını öldürür.** Turkish has four letters where ASCII has two; all-caps produced by a
  naive tool turns *İstanbul* into *ISTANBUL* and destroys the distinction. If caps are unavoidable,
  they must be generated locale-aware (`mechanics.md` §7).
- **Daha yavaş okunur** — capitals flatten the ascender/descender contour the eye uses.
- Vurgu gerekiyorsa **punto, kalınlık ve boşluk** kullan; caps'e mecbursan kısa tut ve harf aralığı
  ver.

## 5. Arayüz metni (UI)

Kaynak: Microsoft Türkçe Yerelleştirme Stil Kılavuzu + Chromium/Inno Setup'ın gerçek Türkçe dizgileri.

### 5.1 Fiil biçimi — düğme ile gövde metni FARKLI

| Bağlam | Biçim | Örnek |
|---|---|---|
| Düğme / menü | **yalın emir** (eksiz) | *Kaydet · Sil · Uygula · Kur* |
| Yönerge (gövde metni) | **siz-emri** `-(y)ın/-(y)in` | "Önce bu işlemleri **tamamlayın**." |
| ✗ Asla | kibar `-ınız` | ~~*yapınız*~~ (fazla buyurgan) |
| ✗ Asla | mastar | ~~*Kaydetmek*~~ (sözlük biçimi, komut değil) |

Tek istisna: `-ma/-me` adlaştırması bir **akışı/kategoriyi** adlandırır, tıklanabiliri değil
(*Kayıt olma* bir tür; *Kaydet* bir düğme).

### 5.2 Hata mesajı
Yapı: **ne oldu → (gerekiyorsa) neden → ne yapmalı.**
- **Kullanıcıyı suçlama.** ✗ *E-postanızı yanlış girdiniz* → ✓ *Lütfen geçerli bir e-posta adresi
  girin (örn. ad@site.com).*
- **`siz` varsayılan.** BÜYÜK HARF ve gereksiz `!` yok (bağırmak gibi okunur).
- **Özrü tasarrufla kullan:** *özür dileriz* yalnız ciddi arızada (veri kaybı); yoksa *maalesef / ne
  yazık ki*. **Asla *üzgünüz*** — "we're sorry" kalkı.
- Hazır kalıp sözlüğü: *… yapılamıyor · … yapılamadı · … bulunamıyor · Bellek yetersiz · …
  kullanılamıyor.*

> **⚠ Bu, edilgen kuralının gerçek istisnasıdır.** Hata ve durum mesajlarında **edilgen doğrudur ve
> bilinçlidir** (*silinemiyor, gönderilemedi*) — kullanıcıyı suçlamamak için. Burada edilgeni AI izi
> sayma (bkz. `ai-tells.md` §13).

### 5.2b Durum etiketi İngilizcesi — "ready-to" kalkı
Arayüz durum/rozet etiketleri İngilizceden birebir sızar. Sözcükleri değil, **ekranda ne demek
istediğini** Türkçeye taşı.
- ✗ *Okumaya hazır:* (Ready to read) → ✓ *Bugün:* / *Başla* · ✗ *Devam ediyor* (In progress) →
  ✓ *Sürüyor* · ✗ *Tamamlandı olarak işaretle* → ✓ *Tamamlandı.*
- Bu sınıf arayüzde sık: kısa etiket, İngilizce kalıbı taşıyıp Türkçede tuhaf duruyor.

### 5.3 Onay kutusu
Sonucu olan eylemde **fiili düğmeye yaz**: ✓ *Sil / Vazgeç*, *Kaldır / İptal*. *Evet / Hayır* yalnız
gerçekten düşük riskli ikili sorularda. Gövde tam soru sorar: *"…kaldırmak istediğinize emin misiniz?"*

### 5.4 Etiket ≠ yer tutucu
Etiket **ad** (*İsim*), yer tutucu **örnek** (*İsminizi girin*). Yer tutucuyu etiket yerine kullanma.

### 5.5 Değişken + ek — Türkçe yazılım metninin asıl belası

Türkçe eklemeli: eke gelen biçim, **önündeki kelimenin son sesine** bağlı. Kod bunu bilemez
(*Dosya'yı sil* / *Klasör'ü sil*). Çözüm sırasıyla:

1. **Cümleyi öyle kur ki değişken hiç ek almasın.** Microsoft'un kendi kuralı:
   ✓ `%s silinemiyor` — ✗ `%s'yi sil`.
2. **Taşıyıcı kelime kullan** (Chromium'un yaptığı): eki **sabit** Türkçe kelime alsın.
   ✓ `{DOSYA} adlı dosya silinsin mi?` · `{KULLANICI} adlı kullanıcı` · `{SİTE} sitesi`.
3. **Sayıdan sonra ad çoğullanmaz.** ✓ `3 öğe` — ✗ `3 öğeler`. (Bu bir kaçamak değil, doğru Türkçe;
   çoğul sorununu da kendiliğinden çözer.) Türkçede CLDR'ye göre yalnız `one`/`other` var; adı ancak
   **sayı görünmüyorsa** çoğullarsın (*Sayfa* / *Sayfalar*).
4. **Eki hesaplamak son çaredir** — ve son harfe bakmakla olmaz: ünlü uyumu **+** ünsüz yumuşaması
   (*kitap→kitabı*) **+** ünlü düşmesi (*akıl→aklı*) gerektirir. Gerçek bir biçimbilim motoru ister.

### 5.6 Tutarlılık
Aynı eylem her yerde aynı fiille. *Sil* bir yerde *Kaldır* olmasın (bkz. `terminology.md`).
Büyük harf: **cümle düzeni** — Title Case İngilizce ithalidir.

## 6. Register karışımının kendisi bir izdir

Mixing registers mid-text — a bureaucratic *-maktadır* inside a chatty blog, a motivational closer
at the end of a technical explainer, a slogan's ellipsis inside body prose — is itself the tell,
independent of whether either register is individually correct. Infer the target register, hold it,
and change it only at a real boundary (a pull-quote, a caption, a button).
