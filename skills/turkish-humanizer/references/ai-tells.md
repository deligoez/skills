# AI/çeviri kokan Türkçe — the catalog of tells and fixes

The patterns that mark Turkish as AI-generated or translated-from-English, each with a natural fix.
Format: **AI pattern → doğal Türkçe**, with a one-line *why*.

**The master mechanism.** Turkish is pro-drop and agglutinative — suffixes already carry person,
tense, and much of the connective logic English needs separate words for. So AI-Turkish reads as
**translationese** (an implicit translation from English): it is systematically **over-explicit**,
restating with a separate word (a connector, a pronoun, "bir şekilde," "sahip olmak," a light verb)
what Turkish already says through a suffix or context. Across nearly every tell below, the most
reliable fix is not a synonym swap but **deletion** — cut the redundant word and let the morphology
carry the meaning. Look for **clusters**, not single instances (see the false-positive guard in
`SKILL.md`).

**Deletion means words, never information.** `SKILL.md` wins over this catalog: in rewrite mode no
list item, claim, qualifier, or sentence is dropped. Delete the redundant *word* (a signpost, a
pronoun, a light verb, `bir şekilde`); when a tell below seems to call for dropping an *item* or a
*sentence* (a third adjective, a scene-setting opener, a motivational closer, an unsourced claim),
simplify how it is said and keep what it says. If it truly should go, that is the author's call:
report it in review mode as **öneri**.

## Table of contents
1. [Overused connectors / discourse markers](#1-connectors)
2. [Bureaucratic / over-formal verb forms](#2-bureaucratic-verbs)
3. [Over-nominalization and light verbs](#3-nominalization)
4. [Calques from English](#4-calques)
5. [English-style rhetoric](#5-rhetoric)
6. [Punctuation / mechanics tells](#6-punctuation)
7. [Register / tone tells](#7-register)
8. [Overused AI vocabulary](#8-vocabulary)
9. [Universal tells that also apply to Turkish](#9-universal)
10. [English tells that do NOT port to Turkish](#10-do-not-port)
11. [**Metafor kalkı — çağrışım taşınmaz**](#11-metafor)
12. [**Türkçeye özgü izler** (baskın sinyaller)](#12-turkceye-ozgu)
13. [Aşırı düzeltme yasağı — iyi Türkçeyi bozma](#13-asiri-duzeltme)
14. [**Söylem iskeleti izleri** — cümle tek tek temiz, iskelet makine](#14-iskelet)
15. [İnceleme kipinde ağırlık — kesin imza, yumuşak sinyal, insan izi](#15-agirlik)

## 1. Connectors / discourse markers {#1-connectors}

AI opens nearly every sentence with a signpost word, mirroring English's need for explicit
transitions — which Turkish usually encodes through a suffix, word order, or nothing at all. Usually
just **delete** the opener.

- **Ayrıca** on a sentence that already has the `de/da` clitic: *Ayrıca, bu ürün deneyimi de
  artırmaktadır.* → *Bu ürün deneyimi de artırıyor.* (the `de` already adds; the word is redundant)
- **Bununla birlikte / Bununla beraber** as a reflex paragraph-opener with no real contrast:
  *Bununla birlikte, sonuçlar beklentileri karşılamadı.* → *Ne var ki sonuçlar beklentileri
  karşılamadı.* / just drop it. Reserve contrast markers for genuine contrast.
- **Dolayısıyla** for weak causality: *Fiyatlar arttı. Dolayısıyla talep azaldı.* → *Fiyatlar artınca
  talep azaldı.* (fold the cause into the clause — see `fluency.md` §3)
- **Sonuç olarak** as an automatic final-paragraph flag: cut it; end on the actual point. Use
  *Kısacası…* only when genuinely summarizing several points.
- **Öte yandan / Diğer taraftan** for any second list item, not real opposition: usually delete, or
  *Buna karşılık…* only if there's a real trade-off.
- **İlk olarak / İkinci olarak / Son olarak** narrating a numbered structure inside prose:
  *Öncelikle maliyet, sonra da hız devreye giriyor.* — or use real bullets if it's actually a list.
- **Özetle / Kısacası** opening a paragraph that isn't summarizing anything: state the point directly.
- **Bu bağlamda / Bu noktada / Bu aşamada** as a content-free bridge: delete; move to the next
  sentence. *Bu noktada ekipler arası iletişim belirleyici oluyor.* → *Ekipler arası iletişim
  belirleyici oluyor.* **Meşru:** a real point in time or in a process (*Kurulum bu noktada durur ve
  onay bekler*) — there the phrase carries information; keep it.
- **Söz konusu** as a stiff demonstrative: *Söz konusu ürün…* → *Bu ürün…* / just repeat the noun.
  (`söz konusu` is legal/bureaucratic register — a dead giveaway in ordinary prose.)
- **Nitekim** as generic glue (it should introduce actual confirming evidence): usually delete.
- **Şüphesiz / Kuşkusuz / Hiç şüphesiz** as an empty certainty opener: *Şüphesiz, bu sektörü
  değiştirecek.* → *Bu, sektörü değiştirecek.* (or hedge honestly if it isn't actually certain)

## 2. Bureaucratic / over-formal verb forms {#2-bureaucratic-verbs}

- **`-mektedir/-maktadır`** as the default instead of natural present `-Iyor` or aorist `-Ir`. The
  single most recognizable "government form letter" tell. *Bu yöntem avantaj sağlamaktadır.* → *Bu
  yöntem avantaj sağlıyor.* (It's fine in official gazettes/encyclopedic entries — not as the default
  for ordinary explanation.)
- **Agent-hiding passive** stacked to avoid naming anyone: *Bu konuya aşağıda değinilecektir.* →
  *Aşağıda bu konuyu ele alıyoruz.* / *Gerekli önlemler alınmıştır.* → *Gerekli önlemleri aldık.*
  (when the actor is known/relevant). Natural Turkish exposition is comfortable saying *biz*.
- **Passive + necessitative for instructions:** *Bu noktaya dikkat edilmelidir.* → *Buna dikkat
  edin.* / *Buna dikkat etmelisiniz.*
- **`-tır/-dır` copula padding** on an already-marked verb: *…sunulacaktır* → *…sunulacak* (the extra
  `-tır` adds weight, not meaning).
- **Impersonal distancing in first/second-person contexts** (a how-to that never says biz/siz):
  *Kullanıcıların giriş yapması gerekmektedir.* → *Sisteme giriş yapmanız gerekiyor.* / *Önce giriş
  yapın.*

## 3. Over-nominalization and light verbs {#3-nominalization}

AI reaches for a semantically empty light verb (`gerçekleştirmek, sağlamak, oluşturmak`) plus an
abstract noun, instead of one plain verb.

- **`gerçekleştirmek`** as all-purpose filler: *Toplantı dün gerçekleştirilmiştir.* → *Toplantı dün
  yapıldı.* / *Dün toplandık.*
- **`sağlamak`** + abstract noun (calque of "provide an increase in"): *Bu güncelleme performans
  artışı sağlamaktadır.* → *Bu güncelleme performansı artırıyor.*
- **`oluşturmak`** for vague abstractions: *…güçlü bir sinerji oluşturmaktadır.* → *…gerçekten uyum
  içinde çalışıyor.*
- **"önemli bir rol oynamaktadır"** (plays an important role) — name the actual mechanism instead:
  *Eğitim, kalkınmada önemli bir rol oynamaktadır.* → *Ekonomik kalkınma büyük ölçüde eğitime bağlı.*
- **"büyük önem arz etmektedir" / "hayati önem taşımaktadır"**: → *…çok önemli.* / *…olmazsa olmaz.*
- **Noun doubled with its own light verb:** *değerlendirme yapmak* → *değerlendirmek*; *kontrol
  sağlamak* → *kontrol etmek*; *analiz gerçekleştirmek* → *analiz etmek* / *incelemek*.
- **`-mA/-Iş` chains** as a dense subject: *Kullanıcıların sistemi verimli kullanmalarını sağlamak
  amacıyla yeni bir arayüz tasarlanmıştır.* → *Kullanıcılar sistemi daha verimli kullansın diye yeni
  bir arayüz tasarladık.*

> **Do not overcorrect.** Turkish's normal formal register is natively *more* nominal than English's.
> The target is the *puffed-up crutch-verb shell*, not nominalization as such. *"Okumanın faydaları
> saymakla bitmez"* is perfect Turkish — leave it. See `fluency.md` §2.

## 4. Calques from English {#4-calques}

- **`sahip olmak`** as reflex "have" for simple features: *Bu ürün birçok özelliğe sahiptir.* → *Bu
  ürünün birçok özelliği var.* (`var/yok` is the native construction; reserve `sahip olmak` for real
  ownership.)
- **`-lI bir şekilde`** for manner adverbs — arguably *the* signature translationese tell (mirrors
  English "-ly"): *başarılı bir şekilde* → *başarıyla*; *hızlı bir şekilde* → *hızla*; *kolay bir
  şekilde* → *kolayca*. Turkish has native adverb suffixes (`-CA, -lIkla, -Ile`).
- **Redundant `bir`** (mirrors English a/an), especially with fixed collocations: *…için bir fırsat
  sunuyor* → *…fırsat sunuyor*; *bir araç olarak* → *araç olarak*.
- **`adreslemek`** (address an issue): → *ele almak / çözmek*. (`adres` means a postal address.)
- **`deneyimlemek` / `deneyim yaşamak`**: → use the plain verb — *sorunsuz bir deneyim yaşayacaktır*
  → *bunu sorunsuzca kullanacak*. (`deneyim` already implies lived experience.)
- **`değer katmak`** (add value): → say what it concretely improves — *ürüne değer katıyor* → *ürünü
  çok daha kullanışlı yapıyor*.
- **`aksiyon almak`** (take action): → *harekete geçmek / önlem almak*.
- **Deyimi kelimesiyle çevirmek** — the idiom's words arrive, its meaning does not. *walk in* (no
  appointment): ✗ *Yürüyerek gelebilirsiniz* (okur ulaşım biçimi anlıyor) → ✓ *Randevusuz
  gelebilirsiniz.* *close the deal / close the customer:* ✗ *müşteriyi kapatmak* → ✓ *satışı
  tamamlamak / bağlamak* (see §12.11). Ask what the reader of the Turkish sentence pictures.
- **`günün sonunda`** (at the end of the day) as a hedge: → *sonuçta / neticede*.
- **`realize etmek`, `farkındalık yaratmak`, `vizyon/misyon belirlemek`, `kolektif bilgelik`** —
  management-speak transplants; prefer plain equivalents (*hayata geçirmek*, *dikkat çekmek /
  bilinçlendirmek*, etc.) outside genuinely corporate contexts.

- **Kişileştirme kalkı** — İngilizce nesneleri özneleştirir (*this book thinks in X*, *the code
  wants*, *the data says*); Türkçede *düşünmek/istemek/söylemek* insana aittir. *Bu kitap Türkçe
  düşünür* → eylemi **gerçekten yapan** özneye ver (*kurduğun makine Türkçenin harfleriyle
  konuşur*) ya da olguyu düz söyle. Nesne ancak dilde yerleşikse *ister/söyler* (yasa, tablo…).

## 5. English-style rhetoric {#5-rhetoric}

- **Rule of three** — three near-synonymous adjectives padding a claim: *Hızlı, güvenilir ve verimli
  bir çözüm.* In rewrite mode **the three items stay** (each is the author's claim); fix only how the
  list is said. If the third is pure synonym padding, flag it in review mode as **öneri**
  (*"verimli" ile "hızlı" aynı iddiayı taşıyor*) — never drop it silently. Keep three items without
  comment when they are three distinct points.
- **"sadece X değil, aynı zamanda Y de"** (not only… but also) — calque; use the idiomatic
  coordinator: → *hem X hem de Y*. *…sadece maliyetleri düşürmüyor, aynı zamanda verimliliği de
  artırıyor* → *…hem maliyetleri düşürüyor hem de verimliliği artırıyor.*
- **"X'ten Y'ye"** as a "spanning the spectrum" flourish (not a literal range): *Küçük işletmelerden
  büyük şirketlere kadar herkes…* → *Her ölçekten işletme…*
  - **Başsız `kadar` listeyi kapatınca:** ✗ *levrek, çipura, hamsi, palamuta kadar birçok balık* —
    `-a kadar` bir sınır ya da ölçü bildirir (*palamut büyüklüğünde?*); ortada başlangıç noktası
    (`-dAn`) ve sıralanabilir bir ölçek yok. ✓ *levrek, çipura, hamsi, palamut gibi birçok balık.*
    Liste öğeleri eksiksiz kalır; yalnız kapanış edatı değişir.
- **Hollow scene-setting intro:** *Günümüzün hızla değişen dünyasında, teknoloji hayatımızın her
  alanına nüfuz etmiş durumdadır.* → shrink the frame, keep the claim: *Günümüzde teknoloji
  hayatımızın her alanına girdi.* Deleting the whole sentence is an **öneri** for review mode.
- **Hollow / restating conclusion:** a *Sonuç olarak…* paragraph that re-lists what was said → drop
  the reflex connector and the bureaucratic predicate; the sentence stays. Cutting the paragraph is an
  **öneri**. Never add a "genuinely new" closing thought: that is new information.
- **"unutmayın ki"** (don't forget that): → drop the imperative frame; state the fact.
- **"şunu belirtmek gerekir ki"** (it should be noted that): → delete; the clause after it is the
  sentence.
- **Fake rhetorical-question transitions:** *Peki, bu ne anlama geliyor?* used as glue → state the
  implication directly.

## 6. Punctuation / mechanics tells {#6-punctuation}

Brief here; full rules in `mechanics.md`.

- **Em dash "—" used the English parenthetical way** (a mid-sentence aside). This has **essentially
  zero native footprint** in Turkish typography (the long dash is mainly the line-initial *konuşma
  çizgisi* for dialogue), so it's one of the strongest single tells — treat any mid-sentence em dash
  as near-automatic. Replace with parentheses, commas, or a period.
- **Title-case headings** ("Yapay Zeka İle Metin Nasıl Yazılır") → Turkish uses sentence case:
  *"Yapay zekayla metin nasıl yazılır."*
- **Comma before "ve"** (Oxford-style): *Hız, güvenlik, ve verimlilik* → *Hız, güvenlik ve
  verimlilik.*
- **Semicolon splicing two full clauses** (English essay style) → new sentence or *hem…hem*.
- **Mechanical bold** on individual words for emphasis → let word order and particles (*bile, zaten,
  tam da*) carry stress.
- **Bullet/heading skeletons dropped into what should be flowing prose** → convert to connected
  sentences when the content is genuinely prose.

## 7. Register / tone tells {#7-register}

- **Uniform over-politeness / customer-service smoothness** regardless of context: *Elbette, bu
  konuda size yardımcı olmaktan memnuniyet duyarım.* (before a routine answer) → just answer.
- **Motivational-poster closers** on neutral content: *Unutmayın, her adım önemlidir!* → drop the
  imperative frame and the `!`: *Her adım önemli.* Cutting the line is an **öneri**.
- **Over-explaining / restating the previous sentence** in near-synonyms → in review mode, flag the
  pair as **öneri**; in rewrite mode keep both and make the second one lighter.
- **Marketing superlatives on mundane facts:** *harika bir şekilde performansı artırıyor* → undo the
  calque, keep the claim: *performansı çok artırıyor.* Whether the claim is inflated is the author's
  call (**öneri**).
- **Hedge-stacking:** *muhtemelen, genel olarak, bir dereceye kadar daha etkili olabilir* →
  *genellikle daha etkili.* (one honest degree of certainty)
- **No genuine casual register even when asked** — AI stays one register too formal (full vowels, no
  elision, no particles). If casual is requested: *ne yapacağımızı bilmiyorum* → *n'apacağımızı
  bilmiyorum valla* / add *ya, yani, işte* where natural. (Don't force this in formal text.)
- **Avoidance of direct address (sen/siz)** in genuinely second-person contexts: *Bu adımların takip
  edilmesi önerilir.* → *Bu adımları izleyin.*

## 8. Overused AI vocabulary {#8-vocabulary}

Words that recur so often in AI-Turkish they read as tells on their own. Reserve them for cases that
genuinely merit them; otherwise cut or use a concrete descriptor.

| Overused | More natural / when to cut |
|---|---|
| adeta / âdeta | usually just delete |
| muhteşem, harika, büyüleyici, eşsiz, benzersiz | only for things that merit it; else a concrete descriptor |
| kapsamlı | *ayrıntılı*; only when truly broad |
| sağlam (for "robust") | *güvenilir, dayanıklı* (context) |
| sorunsuz(ca) | fine in moderation — don't attach to every claim |
| sinerji | *uyum, birlikte iyi çalışmak* |
| güçlendirmek (for "empower") | *yetkilendirmek, olanak tanımak* (context) |
| potansiyelini ortaya çıkarmak | *gerçek kapasitesine ulaşmasını sağlamak* |
| dönüştürücü, çığır açan, oyun değiştirici | only for genuinely major change; else describe the effect |
| yenilikçi | *yeni, özgün*; reserve for real innovation |
| kilit rol / kilit öneme sahip | *önemli, belirleyici* |
| yol haritası | *plan, izlenecek yol* |
| yolculuk (metaphor) | *süreç, deneyim*; "journey" metaphors read as imported |
| sınırları zorlamak / kapılarını aralamak | describe the concrete new capability |
| uçtan uca, baştan sona | fine occasionally; flag only if in every paragraph |

## 9. Universal tells that also apply to Turkish {#9-universal}

These come from LLM decoding itself, not English specifically, so they surface in Turkish too (fuller
treatment in the English `humanizer` skill; here are the Turkish forms):

- **Vague attribution:** *Uzmanlara göre… / Araştırmalar gösteriyor ki…* with no named source → flag
  it (**öneri**: kaynak adı gerekli). Never invent a source; never cut the claim on your own.
- **Puffery / significance inflation:** *…tarihi bir dönüm noktasıdır*, *…kalıcı bir iz bırakmıştır*
  → simplify the wording (*…bir dönüm noktası oldu*); whether the significance is earned is an
  **öneri**.
- **Trailing "-arak/-ması" significance clauses** (the Turkish analog of English's trailing "-ing"):
  *…tamamlandı, bölgenin gelişimine katkıda bulunarak.* → turn the tacked-on converb into a real
  clause: *…tamamlandı ve bölgenin gelişimine de katkıda bulundu.* Deleting it is an **öneri**.
- **Uniform sentence rhythm (low burstiness):** vary length — follow a long sentence with a short one.
- **Formatting:** emoji as bullets, chat preambles (*Tabii ki! İşte…*, *Umarım yardımcı olmuştur!*),
  Markdown bleeding into plain text → remove.

## 10. English tells that do NOT port to Turkish {#10-do-not-port}

A naive port of an English humanizer would wrongly "fix" these. Do **not** apply:

- **"Avoid nominalization" (as a blanket rule).** Turkish's normal formal register is natively more
  nominal; blanket de-nominalizing makes it sound *more* foreign. Only unwind the bureaucratic
  crutch-verb shell (§3).
- **Hyphenated compound-adjective overuse** (*cross-functional, data-driven*) — no structural
  equivalent in agglutinative Turkish; nothing to fix.
- **English "-ing superficial analysis" as a gerund rule** — Turkish has no gerund; the analog lives
  in `-arak/-ması` converbs (§9), which needs its own judgment, not a find-replace.
- **Curly vs. straight quotes** — Turkish typographically uses «…» or "…"; don't force straight ASCII
  quotes as if it were an English tell (see `mechanics.md`).
- **Over-aggressive de-hedging / de-complexifying to "beat a detector."** Detectors are biased against
  simple, clear, non-native-shaped prose; flattening real nuance to dodge one produces worse Turkish.
  Aim at genuine fluency, never at a detector score (see `SKILL.md`).

## 11. Metafor kalkı — çağrışım taşınmaz {#11-metafor}

**En sinsi sınıf.** A metaphor translates literally and its **connotation does not come with it.** The
words are right; what the reader's head does with them is wrong.

**İki soruluk test:**
1. **Bu ifade Türkçede ne çağrıştırıyor?** *kara kutu* → Türk okurun aklına önce **uçuş kayıt cihazı**
   gelir. Genel bir kitap için "kara kutu yok" cümlesi hiçbir şey söylemez.
   → *"Sihir yok: her parçanın içini açarsın."*
2. **Bu kalk Türkçede yerleşik/tanıklı mı?** Yerleşikse serbest, değilse **uydurma — betimle.**
   - ✅ Yerleşik: *kara kutu testi* (yazılım testi), *el sıkışma* (TCP), *yarış durumu*, *karbon ayak izi*.
   - ✗ Uydurma: *ak-sıcak* (white-hot) → doğrusu **akkor**. *gerilim sivrisi* (voltage spike) →
     **ani gerilim darbesi** (*sivri* Türkçede bu anlamda ad değil).

**Kontrol listesi — genel:** kara kutu · kırmızı bayrak · gümüş kurşun · düşük asılı meyve · oyun
değiştirici · yol haritası · ayak izi · buzdağının görünen kısmı.
**Başarısızlık/tükenme mecazları — `bırakmak` Türkçede bunu YAPMAZ:** *break down · give out ·
fall apart* için ✗ *"her benzetme bir yerde **bırakır**"* → ✓ *"her benzetme bir yerden sonra
**yürümez**"* · *"...geçerliliğini yitirir"* · *"...çöker"*. (`bırakmak` Türkçede terk/vazgeçme
bildirir; öznesi bir *benzetme* olamaz.)
**Teknik:** spike · bounce · flush · drain · handshake · race · starve · deadlock · overhead.
Her biri için: yerleşik karşılığı var mı? Yoksa olayı anlat.

> **Kural, yazarını da vurdu.** Bu skill'in terim defteri taslağında ring oscillator için
> *"halka salıngaç"* yazılmıştı — hiçbir Türkçe kaynakta geçmiyor. Doğrusu **halka salınıcı**.
> Kulağa doğru gelmesi doğru olduğu anlamına gelmiyor. Bkz. `terminology.md`.

## 12. Türkçeye özgü izler — baskın sinyaller {#12-turkceye-ozgu}

Bunlar İngilizce humanizer'dan devşirilmiş izlerden **daha güçlüdür**. Önce bunları ara.

### 12.1 Bürokratik sarmalayıcı — tek kuralla çöker
**Teşhis:** Türkçenin **hâl eki** varken bürokrasi araya iki kelimelik bir sarmalayıcı sokuyor.
**Tedavi: sarmalayıcıyı hâl ekine çök.**

| ✗ Sarmalayıcı | ✓ Hâl eki |
|---|---|
| Transfer **noktasında** gelişme yok | Transfer**de** gelişme yok |
| Eğitim **konusunda** adımlar atıldı | Eğitim**de** adımlar atıldı |
| Yöntem **bakımından** sakınca yok | Yöntem**de** sakınca yok |
| Bu konuyla **ilgili olarak** açıklama yapıldı | Bu konu**da** açıklama yapıldı |
| Kaliteli hizmet **anlamında** ayrışıyoruz | Kaliteli hizmet**te** ayrışıyoruz |
| **Söz konusu** belge gönderildi | Belge gönderildi |
| **Bu anlamda**, yeni strateji belirledik | Yeni strateji belirledik *(sil)* |
| Müşteriye e-posta **üzerinden** ulaşabilirsin | Müşteriye e-posta**yla** ulaşabilirsin |

**Ama fazla düzeltme yapma:** *açısından* gerçek bir bakış açısı değişimi için doğrudur
("hukuki açıdan bakıldığında"). ***bakımından* hukuk dilinde terimdir** ("usul bakımından", "esas
bakımından") — orada dokunma. *söz konusu* gerçek belirsizlikte meşrudur ("söz konusu üç şirketten
hangisi"). *üzerinden* gerçek bir kanal ya da aracı adlandırıyorsa kalır: *API üzerinden bağlanır*,
*sunucu üzerinden yönlendirilir*. İz olan, **yığılma** ve **hâl ekinin işini gasp etmesi**.

### 12.2 Cümle sonu `-dır` — hata değil, **register uyuşmazlığı**
Dilbilgisel olarak doğru (bildirme eki) ve sözlük/hukuk/akademi register'ında **gereklidir**. Sohbet
eden bir metinde toptan korunması İngilizce-kaynak izidir.
- ✗ *Bu bir fonksiyondur.* → ✓ *Bu bir fonksiyon.*
- **Kural:** tanım/hukuk/akademi → tut. Anlatım, doküman, arayüz, diyalog → düşür.

### 12.3 `olarak` şişmesi
Yerli zarf biçimi varken `olarak` ekleniyor: *genel olarak* → **genelde** · *kesin olarak* →
**kesinlikle** · *hızlı bir şekilde/olarak* → **hızlıca**. Yığılma bariz iz: ✗ *genel olarak, temel
olarak ve kişisel olarak katılıyorum* → ✓ *Bu fikre katılıyorum.*
**Meşru:** gerçek rol/sıfat bildirimi — *bir doktor olarak görüşüm şu.*

### 12.4 Gereksiz yardımcı fiil — **en iyi kaynaklı madde**
Yardımcı fiil tek türemiş fiile çöküyorsa gereksizdir.
*başvuruda bulunmak* → **başvurmak** · *görüşmelerde bulunmak* → **görüşmek** · *etki etmek* →
**etkilemek** · *umut etmek* → **ummak** · *duyurusunu yapmak* → **duyurmak**.

### 12.5 İkili edilgen + `olan`
✗ *yapılmış olan çalışmalar* → ✓ **yapılan** çalışmalar · ✗ *yürütülmekte olan projeler* →
✓ **yürütülen** projeler. (Edilgenin kendisi Türkçede İngilizceden daha doğaldır — ona savaş açma;
sadece `-mış/-makta + olan` ikizini ve **failin gizlenmesini** hedefle.)

### 12.6 `-mış durumda`
✗ *Enflasyon artmış durumda.* → ✓ *Enflasyon arttı.* (Gerçek bir *durum* karşıtlığı yoksa periphrastik
şişmedir.)

### 12.7 `ve … ve … ve` zinciri
İngilizce "X and Y and Z"nin birebir izi. Türkçe virgülle listeler, tek bir `ve` ile kapatır — ya da
ulaçla bağlar (`-ip`, `-erek`). ✗ *Bütçe konuşuldu ve proje ele alındı ve görev dağıtıldı.* →
✓ *Bütçe konuşuldu, proje ele alındı ve görevler dağıtıldı.* (Yazınsal yineleme ayrı: *geldi, gördü
ve fethetti* — dokunma.)

### 12.8 Ritim için virgül bolluğu
Türkçe **dilbilgisel ilişkiye** göre virgüller, İngilizce gibi nefes/ritim için değil.
✗ *Bu proje, gerçekten, oldukça, önemli bir adım.* → ✓ *Bu proje gerçekten önemli bir adım.*
(Gerçek ara söz, hitap, uzun yan cümle virgülü doğrudur — onları silme.)

### 12.9 Doldurucu zarflar — **liste değil, tayf**
Ban list yapma; işlevine bak.
| Kelime | Durum |
|---|---|
| **aslında / esasında / temelde** | En güçlü tik ("actually/basically" kalkı). Karşıtlık yapmıyorsa **sil**. |
| **artık** | **Doldurucu DEĞİL** — gerçek anlamı var (bundan sonra / bir daha). Dokunma. |
| **tam olarak / kesinlikle** | Karşıtlık/pekiştirme yapıyorsa meşru; refleks ise sil. |
| **adeta / resmen / bir nevi** | Klişeleşince iz; gerçek benzetme/yaklaştırma ise meşru. |

### 12.10 Klişe açılışlar ve çift yaklaştırma
✗ *Bilindiği üzere…* · *Şüphesiz ki…* → sil.
✗ *yaklaşık olarak 100 civarında kişi* → ✓ *yaklaşık 100 kişi* **ya da** *100 civarında kişi* — birini seç.

### 12.11 Plaza dili
*deadline* → teslim tarihi · *assign etmek* → atamak · *attach etmek* → eklemek · *update etmek* →
güncellemek · *focuslanmak* → odaklanmak · *aksiyon almak* → harekete geçmek (ya da somut eylemi
yaz: *Bildirim gelince müşteriye yaz*) · *satışı kapatmak* → satışı tamamlamak / bağlamak.
**Meşru:** hedef kitle satışçıysa ve terim o ekipte gerçekten dolaşıyorsa (iç raporda *lead*,
*pipeline*) dokunma; müşteriye giden metinde düzelt.

### 12.12 Eksiltili soruda hâl eki YANLIŞ BAŞA bağlanır

**Teşhis:** İngilizce eksiltili soruda yer/araç belirteci fiilsiz de yerinde durur:
*"A flashlight at the window?"* Türkçede aynı yapı kurulunca hâl ekli öğe **önündeki ada**
bağlanır ve çoğu kez **madde/köken** okunur.

- ✗ **"Camdan el feneri?"** → okur *"camdan **yapılmış** fener"* anlıyor.
- ✓ *"Camdan el feneri mi sallasan?"* · *"Pencereden fener mi yaksan?"*

**Kural:** eksiltili soruda hâl ekli bir öğe adın önüne geliyorsa **fiili geri koy.** Türkçe
İngilizceden daha az eksilti kaldırır (`registers.md` → başlık eksiltisi); **soru cümlesinde bu
daha da sıkıdır**, çünkü okurun ayırt edecek bağlamı yok. En riskli ekler: `-DAn` (madde/köken),
`-lI` (nitelik), tamlayan eki.

### 12.13 Gömülü soru çekimli fiille kalıyor

**Teşhis:** İngilizce gömülü soruyu çekimli fiille kurar (*see who opened it*). Bu iskelet Türkçeye
taşınınca soru cümlesi, onu nesne olarak alan fiilin önünde çıplak kalır.

- ✗ *Kim açtı, kim düzenledi gör.* → ✓ *Kimin açtığını, kimin düzenlediğini gör.*
- ✗ *Hangi dosyalar değişti öğren.* → ✓ *Hangi dosyaların değiştiğini öğren.*

**Kural:** soru, `görmek / bilmek / öğrenmek / sormak` gibi bir fiilin nesnesiyse `-DIğI / -(y)AcAğI`
ile ad cümlesine çevir. **Meşru:** gerçek soru (*Kim açtı?*); konuşma dilinin yerleşik kalıbı
(*Kim geldi kim gitti, belli değil*); diyalog. Sorun, yazılı yönerge ve arayüz metninde çıkar.

### 12.14 Ettirgen yığını — *have something done* kalkı

✗ *Sisteme listeyi tarattırıp demoları hazırlattırabilirsin.* → ✓ *Sisteme listeyi taratıp demoları
hazırlatabilirsin.* Ettirgen eki kadar **fail** olmalı: tek ettirgen (`tarat-`) bir başkasına
yaptırmaktır; ikinci ek (`tarattır-`) araya üçüncü bir kişi sokar. Say: kim istiyor, kim yaptırıyor,
kim yapıyor? İki kişi varsa tek ek yeter. **Meşru:** zincirde gerçekten bir halka daha varsa
(*ölmek → öldürmek → öldürtmek*: ölen, öldüren, öldürten).

### 12.15 Emir + `ve` + bildirme — ilişki gizleniyor

İngilizcenin *Do X and Y happens* kalıbı koşul ya da zaman ilişkisini `and` ile kurar. Türkçede emirle
bildirme cümlesini `ve` bağlamaz; ilişki eke taşınır.

- ✗ *Listeyi onayla ve demolar hazırlanır.* → ✓ *Listeyi onaylayınca demolar hazırlanır.* /
  *Listeyi onaylarsan demolar hazırlanır.*
- ✗ *Butona bas ve dosya iner.* → ✓ *Butona basınca dosya iner.*

**Meşru:** iki emir (*Kaydet ve çık*); iki bağımsız bildirme (*Liste onaylandı ve demolar
hazırlandı*). Zincir ayrıca `ve … ve` ise §12.7'yi de uygula.

### 12.16 Geniş zaman: yetenek ve okura dönük metin

Geniş zaman Türkçede **alışkanlık ve genel doğru** bildirir. İki yerde yanlış kipe kayar:

- **Yetenek `-ebilir` ister.** İngilizce *"counting says everything"* der; Türkçesi **"her şeyi
  söyleyebilir"**dir. Bir aracın ya da yöntemin **kapasitesini** anlatan cümlede geniş zaman
  alışkanlık iddiasına döner: ✗ *Saymak her şeyi söyler ama yavaş* → ✓ *Saymak her şeyi söyleyebilir
  ama yavaş.* Bu, "gereksiz `-ebilir` ihtimalini azalt" öğüdünün zıddı değil: orada *ihtimal*, burada
  *yetenek* var. Karşılaştırmada ikinci yarıya **`da`** paralelliği kurar: *Anlaşmak **da** hızlı ama
  az şey söyleyebilir.*
- **Kof geniş zaman — okura dönük metinde genel doğru pozu.** ✗ *Pro planda bu özellik ücretsiz
  **olur**.* Cümlede ne özne var ne okur ne eylem; `olmak` boş bir yüklem. Üst üste dizilince
  (*çalışır, ölçer, verir, yazdırır*) broşür sesi gelir. Çare: okur özne olabiliyorsa onu özne yap,
  boş `olmak` yerine işin fiilini koy: ✓ *Pro plandaysanız bu özelliği ücretsiz kullanabilirsiniz.*
  **İddianın gücünü koru:** *ücretsiz olur* bir olanak bildirir, *kullanabilirsiniz* de öyle;
  *kullanıyorsunuz* ise olanağı olguya çevirir.
- **Dokunma:** sistem tanımı ve değişmez kural geniş zamanla doğrudur (*Redis veriyi bellekte
  tutar*). Atasözü, şartnamedeki gereklilik kipi ve akademik genelleme de kalır. Hata geniş zamanın
  kendisi değil, okura dönük açıklamada kof kalmasıdır. Kaynak: insanca §56 (Tahir Yıldız, MIT).

## 13. Aşırı düzeltme yasağı — iyi Türkçeyi bozma {#13-asiri-duzeltme}

Bu skill **kuralcı bir dil polisi değildir.** Necmiye Alpay'ın uyarısı yerinde: doğruluğu "arılık/
temizlik" fetvasına çevirmek dili fakirleştirir. Amaç, metnin işini yapması.

**Asla düzeltme:**
- **Gerçek ikileme** — *kılık kıyafet, sağ salim, akıl fikir, mal mülk*. Bunlar Türkçenin öz anlatım
  aracıdır. Sadece **bürokratik yakın-eşanlamlı ikiliyi** hedefle: ✗ *hukuki ve yasal* → ✓ *hukuka
  uygun*; ✗ *amaç ve gaye*, *açık ve net*. (*usul ve esaslar* hukukta **terimdir** — dokunma.)
- **Hata/durum mesajlarında edilgen** — *silinemiyor, gönderilemedi, bulunamıyor* **doğrudur** ve
  kullanıcıyı suçlamamak için bilinçlidir (bkz. `registers.md`). Burada edilgeni iz sayma.
- **Meşru `-maktadır`** resmî yazışmada (mevzuatın kendisi bunu şart koşar), ansiklopedide, hukukta.
- **Terim olan adlaştırmalar** (`terminology.md`) ve **yerleşik alıntılar**.
- **Tek örnek.** Küme ara: yığılma iz, tekil kullanım değil.
- **Kasıtlı eksiltili vuruş.** Tek başına duran kısa bir dramatik paragraf (*"Bir sır."*) bir üslup
  aracıdır — başlık/slogan eksiltisi **hatası değildir.** Ayrım niyettedir: *çeviri* eksiltisi
  (kaynağın fiilsiz yapısını taşıyan bir slogan) izdir; *kasıtlı* vuruş (üslup sözleşmesinin izin
  verdiği, ritim için tek satır) doğrudur. Üslup sözleşmesi varsa ona bak; yoksa çevredeki ritme.

## 14. Söylem iskeleti izleri — cümle tek tek temiz, iskelet makine {#14-iskelet}

Bu sınıfta tek bir kelime yanlış değildir; iz, cümlenin ya da paragrafın **kuruluşundadır.** Kelimeyi
eşanlamlısıyla değiştirmek izi silmez, kılığını değiştirir (bkz. §14.10). Kaynak: insanca skill'inin
(Tahir Yıldız, MIT) kalıp dizini; bu skill'in ölçüsüne göre süzüldü. Düzeltmeler **dar** tutulur:
yeniden yazma kipinde bile iskeleti kır ama bilgiyi, sırayı ve paragraf düzenini koru (`SKILL.md`).

### 14.1 "X değil, Y" iskeleti — ailesiyle birlikte
`sadece X değil, aynı zamanda Y` (§5) bu ailenin yalnız bir üyesidir. Ötekiler:
- **Çıplak ret-vurgu:** *Mesele daha çok içerik değil, doğru içerik.* · *Başarı tesadüf değil, tercihtir.*
- **Geçmiş zaman kılığı:** *Bu yalnızca bir araç değildi, bir dönüşümün başlangıcıydı.*
- **Kesik kılık:** *Tek başına yeterli değil. Kültür gerekiyor.*
- **Üç aşamalı ret:** *Ne hız. Ne fiyat. Sadece güven.*
- **"yerine" kılığı:** *gösteriş yerine işlevselliği öne çıkarıyor.*

**Ölçü:** metindeki vurgu amaçlı "değil"leri say; üçü geçiyorsa kalıp iskelete dönmüştür. **Çare:**
iddiayı olumlu kur (*Doğru içerik üretmek gerekiyor*). Kendi metnini yazarken iki kanattan yalnız
önemlisini söyleyebilirsin; **yeniden yazma kipinde reddedilen kanat bilgi taşıyorsa düşürme** (hiçbir
bilgi eksilmez): olumlu cümleye bağla (*X yetmez, Y de gerekir*) ya da dokunma. İnceleme kipinde
iskeleti bulgu olarak göster. Tek bir
"X değil, Y" meşrudur, özellikle gerçek bir yanlış anlamayı düzeltiyorsa.

### 14.2 "Asıl" takıntısı ve katafor iki nokta
- **"Asıl" enflasyonu:** *asıl mesele, asıl değer, asıl beceri, asıl soru şu* — bir metinde üç dörtten
  fazlaysa vurgu değerini yitirmiştir.
- **Önden anons + iki nokta + tek cümlelik vuruş:** *Sorun şu: Çalışanlar kullanmıyor.* · *Cevap
  basit: güven.* · *Ortak nokta şu: …* İnsan önce söyler, sonra adlandırır: *…değiştirecek mi? Asıl
  soru bu.* Ya da etiketi hiç kurmaz: *Çalışanlar kullanmıyor.*
- **Meşru iki nokta** arkasından liste, alıntı ya da örnek dizisi getirir (*birleşik kelimeler bitişik
  yazılır: gökdelen, dedikodu*). Arkasından tek cümlelik vuruş geliyorsa kalıptır.

### 14.3 Koşaç kaçışı — "-dır" diyememek
Düz bir bilgi tören kıyafeti giyer: *işlevi görmektedir · konumundadır · olarak hizmet vermektedir ·
niteliği taşımaktadır · olma özelliğine sahiptir · olarak öne çıkmaktadır · barındırmaktadır.*
(İngilizce *serves as* kalkı.) ✗ *Galeri, derneğin sergi alanı işlevi görmektedir.* → ✓ *Galeri,
derneğin sergi alanı.* ✗ *Bina dört salona sahip olma özelliğiyle öne çıkmaktadır.* → ✓ *Binada dört
salon var.* (§3'teki kalıp fiil şişkinliğinin koşaçtaki kardeşi.)

### 14.4 Sağa dallanma — niteleyici ismin arkasında
İngilizce niteleyiciyi ismin arkasına koyar (*a system that…*); Türkçe sola dallanır, niteleyici
sıfat-fiille (`-an, -dık, -acak`) önden gelir. İki kalk biçimi:
- **İsmi zamirle tekrarlamak:** ✗ *Bir raporlama aracı geliştirdik, bu araç her sabah satışları
  özetliyor.* → ✓ *Her sabah satışları özetleyen bir raporlama aracı geliştirdik.*
- **İlgi "ki"si:** ✗ *Öyle bir altyapı kurduk ki yoğun trafikte bile çökmüyor.* → ✓ *Yoğun trafikte bile
  çökmeyen bir altyapı kurduk.* Konuşmadaki şaşkınlık *ki*'si (*öyle yorulmuşum ki…*) meşrudur.
- Soru zamirli yan cümle ad-fiile döner: ✗ *kim açtı, kim düzenledi gör* → ✓ *kimin açıp
  düzenlediğini gör.*

### 14.5 Gereksiz "kendi" ve zamir
İngilizce *own* kalıntısı: iyelik eki aitliği zaten taşır. ✗ *Her servis kendi veritabanına bağlanır ve
onun kendi ayarlarını okur.* → ✓ *Her servis kendi veritabanına bağlanıp ayarlarını okur.* Karşıtlık
yoksa (*başkasınınkini değil, kendininkini*) ikinci "kendi"yi at. Aynı mantıkla her cümlede yinelenen
*siz/ben/o* zamiri de düşer (pro-drop; `fluency.md` ilke 4 — nesne karşı kuralını unutma).

### 14.6 Boş doğrular
Kimsenin itiraz etmeyeceği, hiçbir şey söylemeyen cümle: *güven zamanla inşa edilir · iletişim her
ilişkinin temelidir · başarı bir gecede gelmez · değişim kaçınılmazdır.* **Test:** tersini savunacak
biri var mı? Yoksa cümle bilgi taşımıyordur. Yeniden yazma kipinde bilgi eklenemez (`SKILL.md`), o
yüzden çare çoğu kez söyleyişi yalınlaştırmaktır; **inceleme kipinde** "kalıp" olarak işaretle ve
somut iddiayı yazara sor.

### 14.7 Yağcı ton ve terapist modu
- **Yağcılık** (iltifat muhataba): *Harika bir soru! · Kesinlikle haklısınız · Bu çok önemli bir nokta.*
- **Terapist modu** (duygusal onay, istenmediği bağlamda): *Yalnız değilsiniz · Bunu hissetmeniz çok
  normal · Kendinize karşı nazik olun.* İş yazısında, teknik rehberde, ürün metninde tuhaf ve
  manipülatif durur. Gerçekten duygusal bir bağlamda (hastaya giden metin) tek ve somut bir sıcak
  cümle yerindedir; kalıp hâlinde tekrar eden teselli değil.
- **Bilgi sınırı artığı:** *eldeki bilgilere göre · kamuya açık kaynaklarda yer almamaktadır ·
  muhtemelen … olduğu düşünülmektedir* — modelin kendi sınırını anlatan cümle metne sızmıştır;
  bilinmeyeni açıkça söyle ya da cümleyi at, tahmini bilgi gibi sunma.

### 14.8 Paragraf mühürleri ve özet sandviçi
- **Mini özet:** her paragraf *Kısacası…, Bu da gösteriyor ki…, Bu sayede…* ile ve çoğu zaman ilk
  cümlesini başka kelimelerle tekrarlayarak kapanır. İnsan paragrafı fikir geçişiyle bırakır.
- **Yol haritalı giriş:** *Bu yazıda önce X'i, ardından Y'yi ele alacağız.*
- **Özet sandviçi:** kapanış girişin kelimelerini geri çağırıp aynı şeyi yeniden söyler.
- **Kapanış tekdüzeliği:** jenerik kapanışı (§5) silip her metinde aynı yedek hamleyi (okura soru,
  *Peki ya siz?*, *Belki de…* vecizesi) koymak da kalıptır.

### 14.9 Gönderim merdiveni — ad öbeğini her cümlede yeniden kurmak
Model aynı ad öbeğini her cümlede tekrar kurar (*Uygulama zaman kazandırıyor. Uygulama ayrıca… Uygulama
bu yönleriyle…*) ya da tekrar cezasından kaçmak için eşanlamlı döndürür (*şirket… firma… kuruluş…
marka*). Türkçe yolu: adı **bir kez** tam kur, sonra adıla ve gizli özneye bırak; ad öbeğini ancak konu
gerçekten değişince yeniden kur. Aynı kelimeyle açılan art arda cümleler (açılış tekrarı) bu kusurun
yüzeydeki görünüşüdür. **Sınır:** teknik metinde terim sabit kalır, eşanlamlıyla çeşitlendirme hatadır
(`terminology.md`) — burada hedef, terimi değiştirmek değil, gereksiz yinelemeyi fiil çekimine
bırakmaktır.

### 14.10 Yapı nakli ve ikame tiki — düzeltmenin kendi izleri
- **Yapı nakli:** kalıbı kelime değiştirerek yeniden giydirmek. *Sadece X yapmıyor, Y yapıyor* →
  *X'le kalmıyor, Y oluyor* hâlâ aynı çift kanatlı iskelettir; iki noktayı silip *kazandıran beceri, X*
  yazmak katafor tanımı kaldırmaz; uzun tireyi noktalı virgüle çevirip aynı "iddia — dramatik ek"
  vuruşunu korumak izi taşır. Kendi çıktına sor: **kalıbı kaldırdım mı, yeniden mi giydirdim?**
- **İkame tiki:** *kritik bir rol oynuyor*, *kusursuz bir şekilde* gibi öbekleri silerken her cümleye
  refleksle *doğrudan, aslında, gerçekten, ciddi ölçüde* sokmak. Model yeni bir dolgu kelimesine
  kilitlenir; çoğu zaman en doğal çözüm zarfı tamamen atıp fiili yalnız bırakmaktır.
- **Anti-slop sicili:** zorlama kesik cümleler (*Verim mi? Arttı. Hem de nasıl.*), sahte pürüz,
  yapmacık argo. Doğallık ölçülü olandır.

## 15. İnceleme kipinde ağırlık — kesin imza, yumuşak sinyal, insan izi {#15-agirlik}

İzler eş ağırlıkta değildir; inceleme tablosunda bulguyu buna göre sınıfla.

- **Kesin imza** — tek başına yeterli, kümelenme beklemeden işaretle: sohbet artıkları (*Umarım
  yardımcı olur, Elbette!, Bir yapay zekâ dil modeli olarak, Dilerseniz … da açıklayabilirim*),
  arayüz artıkları (*Regenerate response*), kopyala-yapıştır kekemeliği, bilgi sınırı artığı (§14.7).
- **Yumuşak sinyal** — tek başına hiçbir şey değildir, **küme** bekle: tek bir *kapsamlı*, tek bir
  üçleme, tek bir *ayrıca*, tek bir retorik soru, tek bir *dürüst olmak gerekirse*, tek bir *belki de*.
- **İnsan hatası ≠ yapay zekâ izi.** Özne-yüklem uyumsuzluğu, mantık yanlışı, öge eksikliği, sıra
  yanlışlığı gibi anlatım bozuklukları çoğunlukla insan işidir; model bunları nadiren yapar. Bunları
  **hata** sınıfında, nazikçe düzelt — **kalıp** diye etiketleme.
- **Cila yapay zekâ demek değildir.** Kusursuz dilbilgisi ve tutarlı üslup editörden geçmiş insan
  yazısında da vardır. O teller yoksa kuruluk yalnız kuruluktur.
- **İnsan yazısının işaretleri — bunları koru:** uydurması zor, tuhaf ve somut ayrıntı; çözülmemiş,
  karışık duygu; döneme özgü gönderme; ara söz ve kendini düzeltme (*burada "neredeyse" diyesim var ama
  …*); noktalamaya sızan duygu (ünlem, üç nokta, yarım cümle); bilinçli devrik. Bunları görünce
  metne dokunmamaya meyilli ol: fazla düzenleme metni insan yapan şeyi öldürür.
- **Dedektör puanı hedef değildir.** Dedektörler sade, resmî, kusursuz insan yazısını da işaretler.
  Bu skill'in işi iyi Türkçe yazmaktır; düşük puan için insan metnini "daha insansı" yapmaya kalkma
  (§10).
