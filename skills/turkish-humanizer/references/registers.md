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
- **Kişi başlıkta da sabit.** Başlıklar gövde metninden ayrı yazıldığı için *sen/siz* kayması en çok
  orada kaçar. Sayfa okura *siz* diyorsa: ✗ *Seviyene özel, hedefe odaklı.* → ✓ *Seviyenize özel,
  hedefe odaklı.*
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
- SaaS kalıpları da aynı yoldan gelir: ✗ *Kart istemiyoruz* (No card required) → ✓ *Kredi kartı
  gerekmez.* ✗ *Kota tüketildi* → ✓ *Kullanım hakkınız doldu.*
- **Meşru:** yerleşmiş ürün dili kalır. *Planını yükselt*, *Linki gönder*, *Demo hazır* ürünün sesi
  buysa doğrudur; *bağlantıyı ilet* diye resmîleştirmek metni yabancılaştırır. Ölçüt kaynak dile
  benzemek değil, Türk kullanıcının o üründe gerçekten okuduğu dil.

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
**Sayı biçimi de kullanıcıya görünen metnin parçasıdır.** Kısa bir etiket ya da veri satırı olması onu
makine biçimi yapmaz: ✗ *12 yorum, 4.8 puan* → ✓ *12 yorum, 4,8 puan* · ✗ *%15.5 indirim* →
✓ *%15,5 indirim*. Nokta yalnız makinenin okuduğu yerde kalır: JSON, CSV, API alanı, kod, sürüm
numarası (*v2.4*). Kural ve istisnalar için `mechanics.md` §6.

### 5.7 Ürünün iç dili kullanıcıya sızmaz

Kullanıcı **kendi nesnesini** okur (işletme, hesap, tarama), sistemin temsilini değil (kayıt, aday,
run).
- **İç jargon:** ✗ *Gerçek İstanbul run'ı tamamlandı.* → ✓ *Gerçek İstanbul taraması tamamlandı.*
  ✗ *Orchestrator adayları pipeline'a taşır* (ürün sayfasında) → kullanıcının gördüğü sonucu yaz.
- **Veritabanı dili:** ✗ *Aynı işletme için tekrar kayıt oluşturulmaz.* → ✓ *Aynı işletme ikinci kez
  eklenmez.* ✗ *Kayıt silindi* (müşteri hesabı için) → ✓ *Hesap silindi.*
- **Meşru:** geliştirici belgesinde, API başvurusunda ya da yönetici panelinde iç terim konunun
  kendisidir; orada kalır.

### 5.8 Arayüz metni belge gibi konuşmaz

Düğme **eylemi**, durum mesajı **sonucu** söyler; ikisi de sistemin nasıl çalıştığını anlatmaz.
- ✗ *İşlem başarıyla gerçekleştirilmiştir.* → sonucu adlandır: ✓ *Değişiklikler kaydedildi.* Hangi
  işlem olduğu bağlamdan bilinmiyorsa uydurma: ✓ *İşlem tamamlandı.*
- ✗ *Bu butona basıldığında sistem yeni bir kayıt oluşturur.* → düğmeyse eylem (*Yeni işletme ekle*),
  durumsa sonuç (*İşletme eklendi*).
- ✗ *İlgili kayıt için düzenleme işlemi gerçekleştirilebilir.* → ✓ *Düzenleyebilirsiniz.*
- **Etiketin görevine bak:** *Telefon doğrulama* bir **düğme** ise ✓ *Telefonu doğrula*; bir **gezinme
  başlığı** ya da ayar bölümünün adıysa ad öbeği doğrudur, dokunma (bkz. §5.1 istisnası).

## 6. Register karışımının kendisi bir izdir

Mixing registers mid-text — a bureaucratic *-maktadır* inside a chatty blog, a motivational closer
at the end of a technical explainer, a slogan's ellipsis inside body prose — is itself the tell,
independent of whether either register is individually correct. Infer the target register, hold it,
and change it only at a real boundary (a pull-quote, a caption, a button).

## 7. Sayfa düzeyi — başlıklar bir küme olarak okunur

Cümle cümle kusursuz bir sayfa, küme olarak şablon kokabilir. Aşağıdaki üç sınıf **tek cümleye
bakılarak görülmez**; başlıkları, bantları ve etiketleri alt alta yazıp birlikte oku.

**Kip sınırı.** İnceleme kipinde bunları bildir; konum sütununa kümedeki bütün satırları yaz. Yeniden
yazma kipinde yalnız başlık, bant ve etiket kümelerinde uygula; gövde nesrini bu gerekçeyle yeniden
kurma (SKILL.md: fark dar ve tek eksenli kalır). Hiçbir düzeltme yeni bilgi eklemez: bir yuvaya
koyacak başka bilgi yoksa uydurma, **öneri** olarak yazarı sor.

### 7.1 Tek kalıba çökme — yüklem sonu tekdüzeliği

Türkçede çekimli fiil sona gelir ve kişiyi ekte taşır; satırın en görünür yeri sonudur. Dört
başlığın dördü de `-ırız` ile bitince sayfa yazı gibi değil kalıp gibi okunur, oysa her başlık tek
başına doğrudur.

**Kötü, küme olarak:**
- *Ekmeği her sabah taze pişiririz.*
- *Pastayı siparişe göre hazırlarız.*
- *Siparişi aynı gün teslim ederiz.*

**İyi, küme olarak:**
- *Ekmek her sabah fırından taze çıkar.*
- *Pastayı siparişe göre hazırlarız.*
- *Sipariş aynı gün teslim edilir.*

Aynı olgu için Türkçenin birkaç doğal kalıbı var; bir sayfa birden fazlasını kullanmalı:

| Kalıp | Örnek |
|---|---|
| Ad yüklem | *Pazar günleri kahvaltı da var.* |
| Okur özne | *Yorgunluğunuzu kapıda bırakırsınız.* |
| Nesne özne | *Fırın her sabah erken yanar.* |
| Edilgen | *Arıza cihazla tespit edilir.* |
| Eksiltili dizi (başlıkta) | *Keşiften teslime üç adım.* |
| Birinci çoğul | *Sütü köyden alırız.* |

Ölçü sayfadır, cümle değil: bir `-ırız` bir sestir, dördü tiktir. Edilgen de aynı yolla çöker: üç
edilgen başlık üst üste gelince işletme sayfadan tamamen kaybolur. Bizim kendi tuzak yönümüz de bu:
`-maktadır` yığınını topluca `-yor`'a çevirmek aynı çöküşü başka bir ekle üretir. Kişi değişince
fail de değişir; *biz*'den edilgene geçerken yazının kimin ne yaptığını hâlâ söylediğinden emin ol.

### 7.2 Aynı cümle iki yuvada

Türkçede söz dizimi serbest olduğu için tekrar tek kelime tekrarlanmadan yaşayabilir: ikinci yuva
çoğu kez aynı cümlenin sırası değişmiş hâlidir ve başka bir cümle gibi görünür.

- ✗ Başlık *Sofranız katkısız, üreticimiz belgeli.*, altındaki bant *Üreticimiz belgeli, ürünümüz
  katkısız.*
- Dizgiyi değil anlamı karşılaştır: aynı soruyu yanıtlayan iki yuva tek yuvadır. Sayfada ikinci yuvaya
  koyacak başka bir olgu varsa onu kullan; yoksa **öneri** olarak bildir, bilgi uydurma.
- **Meşru:** benzer görünüp farklı olgu söyleyen yuvalar (*Ekmeği her gün taze pişiririz* /
  *Pastayı siparişe göre yaparız*). Dokunma.

### 7.3 Menüyü tekrarlayan bölüm etiketi

Türkçe gezinme ve bölüm etiketleri aynı adlara uzanır (*Hizmetler, Galeri, İletişim*); başlığın
üstündeki küçük etiket çoğu zaman okurun oraya gelmek için tıkladığı bağlantıyı tekrarlar.

- ✗ Menüde *Hizmetler* → etiket *Hizmetler* → başlık *Bakım menüsü*.
- ✓ Etiket okurun **nerede** olduğunu değil bölümün **neyle** ilgili olduğunu söylesin:
  *Güzellik ve bakım* → *Bakım menüsü*.
- Etiket konu, yer ya da vesile ekliyorsa yerini hak eder (*Kadıköy · Güzellik ve bakım*). Yalnız
  bölümün adını yineliyorsa kaldırılmasını **öner**; yerine koyulacak konu sayfadan çıkmıyorsa uydurma.
