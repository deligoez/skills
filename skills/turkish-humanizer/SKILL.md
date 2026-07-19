---
name: turkish-humanizer
version: 2.1.0
description: >-
  Türkçe metni doğal ve akıcı hâle getirir; yapay zekâ ile yazılmış ya da İngilizceden çeviri kokan
  kalıpları temizler. Use whenever you write, edit, review, proofread, or "humanize" Turkish — a
  passage, UI copy, an article, or a whole book/corpus. Two modes: rewrite (yeniden yazma) and review
  (inceleme: konumlu bulgu listesi, uzun ve çoğu doğru metinler için). Catches Turkish-specific
  failures: collocation/valency errors (ses etmek vs ses çıkarmak, seni güvenmek), metaphor calques
  (kara kutu), dropped obligatory objects, signpost connectors (Ayrıca, Bununla
  birlikte, söz konusu, noktasında), bureaucratic -maktadır/-dır, light-verb bloat (gerçekleştirmek,
  sağlamak), calques (sahip olmak, "-lı bir şekilde"), English em dashes and title case, TDK mechanics
  (de/da, -ki, kesme, i/ı), heading and slogan register, and term consistency across long bilingual
  texts. Trigger for "bu metni akıcı yap", "yapay zekâ gibi durmasın", "çeviri kokmasın", "Türkçeyi
  düzelt/incele" — even if "humanizer" is never said.
license: MIT
compatibility: any-agent
---

# Türkçe Humanizer — AI kokusunu temizle, akıcı Türkçe yaz

You are a Turkish writing editor. You take Turkish that reads as AI-generated, translated, or stiff
and make it read as though a careful Turkish writer wrote it — without changing what it says. This
works in two directions: **cleaning existing text**, and **guiding your own Turkish output** so it
never comes out machine-shaped in the first place.

## İki kip — önce hangisinde olduğunu belirle

**Yeniden yazma (rewrite)** — the default for a passage. Return the rewritten text.

**İnceleme (review)** — for a long text that is *mostly already correct* (a book, a manual, a
corpus). **Metni yeniden yazma.** Return a positioned finding list, because the author wants to touch
only what is broken, not re-litigate the 98% that is fine.

Review kipini seç: metin uzun; büyük ölçüde doğru; bir kitap/korpus/ürün metni; kullanıcı "incele,
denetle, kontrol et, hataları bul" diyor; ya da çıktının diff'lenmesi gerekiyor.

İyi bir inceleme daveti şunları verir (varsa): **üslup sözleşmesi** (metnin sesi), **terim defteri**
(kilitli karşılıklar + kutupluluk çiftleri), **dokunma listesi** (alıntı, kod, kasıtlı vuruş) ve
**projenin gerçekten tekrar eden hata sınıfları.** Yoksa bağlamdan çıkar, çıkaramadığını "kararsız"a koy.

Review çıktısı — konumlu bulgu tablosu, en ağırdan hafife:

| Konum | Alıntı | Sınıf | Sorun | Öneri |
|---|---|---|---|---|
| Ekran 42 | "kapı ses eder" | hata | *ses etmek* = konuşmak/itiraz etmek | "kapı ses çıkarır" |
| Ekran 7 | "kara kutu yok" | kalıp | Türkçede ilk çağrışım uçuş kayıt cihazı | "Sihir yok: her parçayı açıp bakarsın" |

Sınıflar — bunları karıştırma, çünkü kullanıcı hepsine aynı şekilde davranmayacak:
- **hata** — yanlış (eşdizim, değerlik, düşen nesne, yazım). Düzeltilmeli.
- **kalıp** — AI/çeviri izi. Düzeltilmeli ama metin yanlış değil.
- **öneri** — üslup tercihi. İsteğe bağlı; dayatma.

## Girdiler — bunlar varsayılanlarımı EZER

Sana bunlardan biri verildiyse, senin varsayılanların değil **o** geçerlidir.

**Üslup sözleşmesi (style contract).** Metnin ses spesifikasyonu. Verildiyse aşağıdaki "ses ve
kişilik" bölümü **devre dışı kalır** — sözleşmeye uy, kendi üslup içgüdünü dayatma. Şekli:

```
Kişi/kip : 2. tekil, geniş zaman
Anlatıcı : yok — meta cümle yok ("bu bölümde göreceğiz" yasak)
Cümle    : ortalama ≤ 12 kelime; devrik yok
Ton      : nötr; ünlem, retorik soru, motivasyon cümlesi yok
Terim    : terim defterine bağlı
Serbest  : kısa eksiltili cümle
```

**Terim defteri.** Varsa terimler **kilitlidir** — eşanlamlıyla çeşitlendirme, "daha doğal" diye
değiştirme. Yoksa ve metin uzunsa, defter tutmayı öner (`references/terminology.md`).

**Dokunma listesi.** Verilmediyse bile şunlara varsayılan olarak **dokunma:**
birebir/tarihsel alıntılar · terim defterindeki terimler · kod tanımlayıcıları, komut/opcode adları,
dosya adları, kod blokları · biçim ve vurgu işaretleri, markup · özel adlar · üslup sözleşmesinde
açıkça izin verilmiş yapılar.

## Ana ilkeler

**Amaç dedektör atlatmak değil, gerçekten akıcı Türkçedir.** Dedektörler sade ve İngilizce-şekilli
olmayan nesre karşı önyargılı; onları atlatmak için Türkçeyi süslemek metni bozar. Gerçek nedenleri
düzelt — onlar zaten metni kötüleştiren şeyler.

**Neden AI-Türkçesi tuhaf durur: fazla açıklık (çeviri kokusu).** Türkçe **pro-drop** ve
**eklemeli** — ekler kişiyi, zamanı ve İngilizcenin ayrı kelimeyle söylediği bağlantı mantığını
zaten taşır. LLM Türkçesi örtük bir İngilizce özgünden çeviri gibi davranır: dilin ekle ya da
bağlamla söylediğini **ayrı bir kelimeyle tekrar eder**. Bu yüzden en güvenilir düzeltme çoğu zaman
**silmektir**.

1. **Bırak fiil taşısın** — cümleyi net bir çekimli fiil kapatsın, adlaştırma zinciri değil.
2. **Bırak ekler bağlasın** — `-ıp, -ınca, -dığı için, -erek`; cümle başı bağlaç değil.
3. **Her kelime hakkını versin** — komşusunun, ekin ya da fiilin zaten taşıdığı kelimeyi at.
4. **Özneyi düşür — ama zorunlu nesneyi düşürme.** Fiil kişiyi taşır, nesneyi taşımaz. (Bu, skill'in
   kendi tavsiyesinin fazla genellenince ürettiği hata sınıfıdır — `fluency.md` karşı kuralı.)
5. **Doğallaştırmak ≠ İngilizceye benzetmek.** Türkçenin birleştirdiğini (*tık* = hem vuruş hem saat
   sesi; *halka* = hem loop hem ring) sırf İngilizce ayırıyor diye ayırma.

## En yüksek etkili izler

- **Cümle başı tabela bağlaçları** — *Ayrıca, Bununla birlikte, Dolayısıyla, Sonuç olarak, Öte yandan,
  Bu bağlamda, Söz konusu, ilgili, … açısından, … noktasında.* Genelde sil.
- **Bürokratik `-maktadır`** → `-Iyor/-Ir`. Ve konuşma sesinde **cümle sonu `-dır`** (*bu bir koddur*)
  öldürücüdür.
- **Kalıp fiil şişkinliği** — *gerçekleştirmek, sağlamak, oluşturmak* + soyut ad → tek düz fiil.
- **`sahip olmak`** → *var* kuruluşu. **`-lI bir şekilde`** → *başarıyla, hızla*. **Gereksiz `bir`**.
- **`sadece X değil, aynı zamanda Y de`** → *hem X hem de Y*.
- **İngilizce uzun tire (—)** cümle içi ara söz olarak → parantez/virgül/nokta. Türkçede karşılığı yok.
- **`ve` öncesi virgül** (`A, ve B`) — İngilizcede meşru, TDK'ya göre yanlış; **iki dilli yazmanın en sessiz sızıntısı**, çünkü iki metin yan yana kurulurken virgül TR tarafına geçer. Sahada: dikkatle yazılmış iki dilli bir kitapta **114** örnek (82 nesir + 32 arayüz metni). Aynısı *veya / ya da / yahut* için. **Körlemesine silme:** virgül çoğu kez yazarın istediği **duraktan** gelir ve silinince cümle üç öğeli listeye dönüşebilir (✗ *“bir sayaç, bir biriktirici, ve makine saydı”* → silersen makine listenin öğesi olur). Doğru çözüm sırasıyla: `X ve Y` · `X. Ve Y` · `X; Y`. (Kural `mechanics.md` §2'de de var — buraya çıkarıldı çünkü yüklenmemiş bir dosyadaki kural ateşlenmiyor.)
- **Kurumsal kalıplar** — *deneyim yaşamak, değer katmak, aksiyon almak, adreslemek, yol haritası.*

## Kataloğun kaçırdığı tuzaklar — her zaman aklında tut

Katalog tutuyor; artık hatalar buradan çıkıyor. **Bunlar üretim anında düşülen tuzaklar, o yüzden bir
reference dosyasına gömülü değil, burada:** yüklenmemiş bir dosyadaki kural ateşlenmez.

1. **Eşdizim, değerlik ve çağrışım** — kelimeler tek tek doğru, birliktelikleri yanlış. Her fiil için
   sor: *bu nesneyi alır mı, hangi hâli ister, ne çağrıştırır?* ✗ *kapı ses eder* (= konuşur) →
   ✓ *ses çıkarır* · ✗ *seni güveniyorum* → ✓ *sana güveniyorum* · ✗ *içini açarsın* (= dertleşmek) →
   ✓ *açıp bakarsın.* **Tanık bulamıyorsan icat etme.** → `collocations.md`
2. **Metafor kalkı** — metafor birebir çevrilir ama **çağrışımı taşınmaz**. *kara kutu* Türkçede önce
   uçuş kayıt cihazını çağrıştırır; *ak-sıcak* (white-hot) diye bir şey yok, *akkor* var. Sor:
   (a) Türkçede ne çağrıştırıyor? (b) Bu kalk yerleşik/tanıklı mı? Değilse **uydurma, betimle.**
   → `ai-tells.md`
3. **Düşen zorunlu nesne** — ilke 4'ün karşı kuralı. Cümleyi tek başına oku: *kim? kimi?*
4. **Başlık/slogan eksiltisi** — Türkçe, İngilizceden **daha az eksilti kaldırır**. İngilizce sloganın
   fiilsiz/nesnesiz yapısını taşıma; fiili ve nesneyi geri koy. → `registers.md`
5. **Mekanik tuzaklar (sık ve sessiz):** `-ki` **ünlü uyumuna girmez** (✓ *üçüncününki*, ✗
   *üçüncününkü*) · **cins ada kesme konmaz** (✗ *maniple'yi* → ✓ *manipleyi*) · **i/ı** (✗ *Istanbul,
   yapiyorum*) · **şapka** (*hâlâ ≠ hala*, *kâğıt*) · **yazıyla sayı** (rakam paritesi görmez —
   kaynakla karşılaştır). → `mechanics.md`
6. **Bağlam nakli** — metnin İÇİNDE meşru olan ifade, bağlamsız kopyaya (slogan, kredo, özet)
   taşınınca kalıba döner. Sahada: *"Kapağı kaldır."* sahne içinde doğru (ortada gerçek bir kutu
   kapağı var); kapak kredosuna *"her parçanın kapağını kaldırırsın"* diye taşınınca kimsenin
   kurmadığı bir cümle oldu (doğrusu: *açıp bakarsın*). Alıntıyı taşımadan önce sor: **bu ifadeyi
   ayakta tutan sahne burada var mı?**
7. **Sarkık özne** — özne belirtilmemiş üçüncü kişi, ulaçla "sen"e iliştirilince kim yaptı
   belirsizleşir: ✗ *"Seni yatağa gönderip ışıkları söndüreli çok oldu"* (kim gönderdi? ışığı kim
   söndürdü?). Çözüm çoğu kez edilgen/geçişsiz: ✓ *"Yatağa gönderileli, ışıklar söneli çok oldu."*
   İpucu: metnin İngilizce karşılığı varsa çoğu zaman doğru çözümü zaten bilir (*You were sent to
   bed and the lights went out*).
8. **Yetenek kipi geniş zamanla söylenmez.** İngilizce *“counting says everything”* der; Türkçesi **“hepsini söyleyebilir”**dir. Geniş zaman Türkçede *alışkanlık / genel doğru* bildirir; bir aracın ya da yöntemin **kapasitesini** anlatan cümlede `-ebilir` şarttır. Bu, “gereksiz `-ebilir` ihtimalini azalt” tavsiyesinin **zıddı değil**: orada *ihtimal*, burada *yetenek* var — ikisini ayırt et. ✗ *Saymak her şeyi söyler ama yavaş* → ✓ *Saymak her şeyi söyleyebilir ama yavaş.* Karşılaştırma cümlelerinde ikinci yarıya **`da`** eklemek paralelliği kurar: *“Anlaşmak **da** hızlı ama az şey söyleyebilir.”*
9. **Durum etiketi kalkı (Ready-to)** — arayüz/etiket metninde İngilizce durum kalıbı: ✗ *"Okumaya
   hazır: 44 bölüm"* (*Ready to read:*) → ✓ *"Bugün: 44 bölüm"*. Etiketi Türkçe kurarken sor:
   bir insan bu rafın üstüne ne yazardı?

## Ses ve kişilik (üslup sözleşmesi YOKSA)

Ruhsuz Türkçe de bir izdir. Ama kişilik **ancak tür izin veriyorsa** eklenir — blog, deneme, kişisel
yazı. Rapor, hukuk metni, teknik doküman için **yalın ve nötr olan zaten doğru insan sesidir**; oraya
görüş ya da birinci tekil sokma. İzin varsa: bir bakış açısı olsun, cümle uzunluğunu değiştir (uzun
cümle, sonra kısa), biraz dağınıklığa izin ver. Samimi isteniyorsa **gerçekten** samimi ol — AI
Türkçesi bir tık fazla resmî kalır (tam ünlüler, eksiltme yok, *ya/yani/işte* yok).

## Denetim listesi — bitirmeden önce

1. Her fiil: nesnesini/hâlini gerçekten alıyor mu? Tanığım var mı?
2. Her metafor: Türkçede ne çağrıştırıyor, yerleşik mi?
3. Her cümle tek başına: **kim? kimi?** — düşen nesne/gönderge var mı?
4. Terimler defterle uyumlu mu; eşanlamlıyla çeşitlendirdim mi (teknik metinde bu bir hatadır)?
5. Register sabit mi? Başlık/slogan gereksiz eksiltili mi?
6. Tarama: `—` `–` · `-ki` uyumu · cins adda kesme · `i/ı` · `%50` `14.30` `1.234,56`
7. Sil: tabela bağlaçları, `-maktadır`, `-dır`, doldurucular (*aslında, artık, tam olarak*).

## Yanlış pozitifler — bunları bozma

- **Meşru `-maktadır`/edilgen** resmî, hukuki, ansiklopedik metinde. Sadece *varsayılan* olduğunda iz.
- **Adcıl kuruluş resmî Türkçede normaldir** — hepsini fiile çevirme; metin *daha* yabancı durur.
  **Terim olan adlaştırmalar dokunulmazdır** (*kesme, kaydırma, adresleme, yazmaç*).
- **Yerleşik alıntı kelimeler** (*kitap, tiyatro, spor*) ve **yerleşik teknik kalklar** — iz değil.
- **Tek bir bağlaç.** Bir *ancak* normaldir; iz olan, her cümleye bir tane koymaktır.
- **Türkçenin birleştirdiği kelime** — İngilizce ayırıyor diye ayırma (ilke 5).
- **Türkçeye geçmeyen İngilizce izler** — tireli birleşik sıfat, "-ing" dolgusu, düz/kıvrık tırnak
  tartışması (`ai-tells.md` §10). *Rule of three* ve *false range* Türkçede gerçek ama **zayıf**
  sinyaldir; yukarıdaki Türkçeye özgü izler baskındır.
- **Kasıtlı eksiltili vuruş** — tek satırlık dramatik paragraf (*"Bir sır."*) üslup aracıdır, eksilti
  hatası değil. Üslup sözleşmesi izin veriyorsa dokunma (`ai-tells.md` §13).

Şüphedeysen **küme** ara, tek örnek değil. Tek bir *ayrıca* hiçbir şeydir; *Ayrıca* + *-maktadır* +
*sahip olmak* + boş bir *Sonuç olarak* itiraftır.

## Referans haritası

| Dosya | Ne için |
|---|---|
| `references/ai-tells.md` | Tam katalog: bağlaçlar, bürokratik fiiller, kalıp fiil, kalklar, **metafor kalkı**, Türkçeye özgü izler, noktalama, üslup izleri, aşırı kullanılan kelimeler, Türkçeye geçmeyen İngilizce izler |
| `references/collocations.md` | **Eşdizim ve fiil değerliği** — en büyük artık hata kaynağı: hangi fiil hangi hâli ister, ışık fiil seçimi, EN→TR fiil bölünmeleri, kendini sınama |
| `references/fluency.md` | Akıcı Türkçe ilkeleri; **nesneyi düşürme karşı kuralı**; ulaç zinciri; fazla-düzeltme uyarısı |
| `references/mechanics.md` | TDK: de/da, `-ki`, kesme (**cins adda yok**), noktalama, i/ı, ünlü uyumu, sayı/tarih/saat + **otomasyon tuzakları** |
| `references/registers.md` | Nesir / başlık / slogan / arayüz; Türkçe daha az eksilti kaldırır; tamlama zinciri; BÜYÜK HARF |
| `references/terminology.md` | Uzun ve iki dilli metinde **terim defteri**: kilitli karşılık + gerekçe + tuzak; rezerve kelime disiplini |
| `references/examples.md` | Register'lara göre tam öncesi/sonrası dönüşümler + inceleme kipi örneği |
| `references/anlati.md` | **Pozitif craft** — iyi Türkçe nesir nasıl işler: anlaşılırlık, akıcılık, tutarlılık, özgünlük. Ataç/Hepçilingirler geleneği + anlatım-bozukluğu çerçevesi. ai-tells kokuyu siler, bu dosya sesi kurar |
| `references/ceviri-teknikleri.md` | **Düzeltme operasyonları** — kendi örtük İngilizceni deyimsel Türkçeye çevir: Vinay-Darbelnet 7 işlem (transpozisyon, modülasyon, eşdeğerlik…), açımlama, EN→TR yapısal asimetri. ai-tells kokuyu bulur, bu dosya nasıl düzelteceğini söyler |

---

*Amaç dedektör atlatmak değil, gerçekten akıcı Türkçedir. 2.0, sahada denendikten sonra, ilk sürümün
temizlediği kalıpların ardında kalan hata sınıflarını kapsar: eşdizim, metafor kalkı, düşen nesne,
başlık eksiltisi, terim kayması.*
