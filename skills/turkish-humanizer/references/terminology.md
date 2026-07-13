# Terim defteri — uzun ve iki dilli metinde tutarlılık

The rest of the skill cleans a **passage**. This file is about a **corpus** — a book, a manual, a
275-screen bilingual project. At that scale the dominant residual error is not translationese; it is
**terim kayması (term drift)** and **rezerve kelime çakışması**, and no amount of passage-level
cleaning will catch either. You need a ledger.

## Neden defter

- **Gerekçesiz kararlar kayar.** A term chosen without a recorded reason drifts six months later
  toward whatever word feels "daha doğal" that day, and nobody remembers why the original choice was
  made. The rationale is the load-bearing part, not the word.
- **Bir dildeki karar öbür dili bağlar.** In a parallel text the two versions constrain each other.
- **Rezerve kelime çakışması** — the failure only a ledger can see. Real case: the English text used
  *bounce* loosely in chapter 4 for a relay's lever. Twelve chapters later *bounce* was needed as the
  technical name for **contact bounce** — and the earlier casual use had already, silently, burned
  the name. The Turkish side had avoided this by saying *zıplama* early on. Passage-level editing
  cannot see a collision twelve chapters wide.

**Kural: bir terim olarak seçilen kelime rezerve edilir — metnin hiçbir yerinde gelişigüzel
kullanılamaz.** Term decisions constrain the *casual* vocabulary of the whole corpus, forward and
backward.

## Defterin şeması

Every entry carries all six fields. The rationale field is not optional — it is the whole point.

| Alan | Ne yazılır |
|---|---|
| **EN / TR** | Kilitli karşılık çifti |
| **Gerekçe** | Neden bu karşılık — bir cümle, ama gerçek bir gerekçe |
| **Reddedilenler** | Denenip elenen karşılıklar ve eleme sebebi |
| **Tuzak** | Neyle karışıyor, hangi yanlış çağrışımı var |
| **Bağlam** | Nerede geçiyor; hangi bağlamda başka anlama geliyor |
| **Durum** | kilitli · geçici · tartışmaya açık |

## Otorite hiyerarşisi — bir terime nasıl karar verilir

Sırayla, ve üstteki alttakini ezer:

1. **Projenin kaynak/referans eseri.** Bir ders kitabı ya da şartname temel alınıyorsa terim otoritesi
   odur. Genel yaygınlık onu ezmez.
2. **Alanın yerleşik Türkçe literatürü** (üniversite ders malzemesi, MEB modülleri, tr.wikipedia,
   kurumsal Türkçe dokümanlar). Alanlar ayrışabilir — böyleyse ayrımı yaz, birini kazanmış gibi gösterme.
3. **Betimleme.** Tanık yoksa **uydurma**: olayı anlat, kalk mintleme.

Sıra 1'in gücü somut: bilgisayar mimarisi için Prof. Dr. Oğuz Ergin'in açık erişimli *Bilgisayar
Mimarisi — RISC-V Tabanlı Yaklaşım* (v0.4.7) kitabı taranınca **register → yazmaç 931 kullanım,
*kaydedici* 0** çıkıyor; **instruction → buyruk 2114, *komut* 12.** Genel literatürde *kaydedici* (MEB/
elektrik) yaşıyor olsa da, o kitabı temel alan bir proje için tartışma kapanmıştır. Ama aynı tarama
şunu da gösteriyor: **kaynak her şeyi çözmez** — *işlem kodu* (65) ile *opcode* (61) kitapta neredeyse
başa baş. Kaynağın kararsız kaldığı yerde **proje kendi kararını verip kilitler.**

## Örnek defter

Aşağıdaki satırlar tahmin değil: her biri kaynak taramasıyla doğrulandı. "Kaynak" sütunu hangi otorite
sırasının kararı verdiğini gösterir.

| EN | TR (kilitli) | Kaynak | Tuzak |
|---|---|---|---|
| instruction | **buyruk** | ① kitap (2114 / *komut* 12) | günlük dildeki *komut*'a kayma çok kolay |
| register | **yazmaç** | ① kitap (931 / *kaydedici* 0) | EE/MEB literatüründe *kaydedici* yaşar — kitleye göre değişir |
| cache | **önbellek** | ① kitap | *ara bellek* (buffer) ile karıştırma |
| pipeline | **boru hattı** | ① kitap | — |
| stack / heap | **yığıt** / **yığın** | ① kitap (yığıt 235) | **yakın eşsesli** — en sinsi tuzak; ikisini asla karıştırma |
| bus | **veri yolu** | ① kitap (203; ayrı yazılıyor) | *adres yolu*, *kontrol yolu* ayrı türler |
| carry | **elde** | ① kitap (*elde var 1*, *elde biti*) | *taşımak* fiiline kayma |
| interrupt | **kesme** | ①② (kitap 33 / *kesinti* 6) | *kesinti* ikincil |
| logic gate | **kapı / mantık kapısı** | ①② | — |
| opcode | *(proje kilitlemeli)* | ① **kararsız**: işlem kodu 65 ~ opcode 61 | çekimde *opcode'u* ✗ → *işlem kodunu* |
| flip-flop | **flip-flop** *(çevrilmez)* | ② MEB modülü başlığı bile "FLİP-FLOP" | *çevirmece* uydurma — **mandal** çevrilir ama flip-flop çevrilmez: komşu terimler, farklı karar |
| latch | **mandal** | ② MEB: "S-R MANDALI" | türemiş biçim *mandallayıcı* |
| buffer | **arabellek** | ② (*arabellek taşması* evrensel) | ~~tampon~~ ikincil; kitap *ara bellek* yazıyor — projede birini seç |
| contact bounce | **kontak/anahtar sıçraması** | ② | ~~zıplama~~ sabit terim değil; günlükte *buton arkı* (ark ≠ sıçrama, teknik olarak yanlış); *seğirme* uydurma |
| ring oscillator | **halka salınıcı** | ② tr.wikipedia | ~~halka salıngaç~~ **sıfır tanık — uydurma** (aşağıya bak) |
| race condition | **yarış durumu** ~ **yarış koşulu** | ② ikisi de tanıklı, hiçbiri baskın değil | çoğu kaynak İngilizce bırakır — karar ver, kilitle |
| handshake | **el sıkışma** | ② *üç yollu el sıkışma* standart | — |
| black box | *(genel okurda kullanma)* | ② | Türkçede ilk çağrışım **uçuş kayıt cihazı**; *kara kutu testi* yazılımda yerleşik — o bağlamda serbest |

## Kurallar

1. **Teknik metinde eşanlamlı döngüsü YASAKTIR.** The English humanizer rightly flags *elegant
   variation* (synonym cycling) as an AI tell. In technical Turkish the conclusion is stronger, not
   weaker: **terim sabit kalır.** Varying a term for stylistic freshness is a defect, not a virtue.
   The model's repetition penalty will push you to vary it — resist.
2. **Terim olan adlaştırmalar dokunulmazdır.** The "adlaştırmayı fiile çevir" reflex destroys terms:
   **kesme** (interrupt), **kaydırma** (shift), **toplama** (addition), **adresleme**, **yazmaç**.
   These are nouns *on purpose*. Never unwind them (see `fluency.md` §2 caveat).
3. **Tanıklık kuralı — yerleşik terimi icat etme.** Before coining anything, look for an attested
   Turkish term (*kesme, elde, mandal, arabellek, el sıkışma, halka salınıcı*). **Tanık bulamıyorsan
   uydurma — betimle.** And if a term *is* attested but contested, name the split (yazmaç/kaydedici)
   rather than pretending one side won.

   > **Uyarıcı vaka — bu dosyanın yazarı da bu hataya düştü.** İlk taslakta ring oscillator için
   > *"halka salıngaç"* yazılmıştı. *Salıngaç* gerçek bir kelime, *halka* gerçek bir kelime — ama
   > **"halka salıngaç" hiçbir Türkçe teknik kaynakta geçmiyor.** Doğrusu *halka salınıcı*. Terim
   > kulağa doğru geldiği için doğru olmuyor. Aynı taslakta *bounce → zıplama* ve *buffer → tampon*
   > da tanıksız çıktı. **Kural işe yarıyor çünkü kuralı yazan da ihlal etti: her terimi ara, hiçbirini
   > kulağınla onaylama.**
4. **Yeni bağlamda kararı yeniden tart.** When a locked term surfaces in a context that strains it,
   re-weigh the decision consciously — and if it changes, change it **everywhere**, which is a
   corpus operation, not a find-and-replace (rule 5).
5. **Değiştirme, sar.** Turkish suffixes attach to the term and their form depends on the term's final
   sound. A naive find-and-replace breaks them: *opcode'u* → replace → *işlem kodu'u* ✗ (doğrusu
   *işlem kodunu*); *yazmaç* → *yazmacın* (ünsüz yumuşaması). Either replace whole **inflected**
   forms, or wrap the inflected form rather than substituting the stem. See `mechanics.md` §7.
6. **İki dilli metinde defter ortaktır.** A TR decision must be checked against the EN side and vice
   versa; a term freed up in one language may already be spent in the other.

## Süreç

1. **İlk geçişte defterle.** A term is entered the first time it appears — with its rationale.
2. **Sonra tara.** For each locked term, list every occurrence across the corpus and find the
   deviations. This is the pass that catches drift; it cannot be done passage by passage.
3. **Çakışma taraması.** For each reserved word, search for *casual* uses of the same word elsewhere.
   That is the *bounce* failure, and it is invisible without this step.
4. Karar değişirse: defteri güncelle, gerekçeyi yaz, korpusu çekimli biçimlerle güncelle.
