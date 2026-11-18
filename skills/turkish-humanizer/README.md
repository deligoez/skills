# turkish-humanizer

> *Günümüzün hızla değişen dünyasında, verimlilik kritik bir öneme sahiptir.*

Bu cümleyi okuyunca "bunu bir model yazmış" dediysen, neye takıldığını da biliyorsun: boş bir
açılış, İngilizceden birebir gelmiş *öneme sahip olmak*, cümle sonunda *-dir* ağırlığı.

`turkish-humanizer`, yapay zekâ ile yazılmış ya da İngilizceden çevrilmiş kokan Türkçeyi **dikkatli
bir Türk yazarın elinden çıkmış gibi** okunur hâle getiren bir ajan skill'idir. Metni baştan yazmaz:
kokan yeri bulur, yalnız onu düzeltir, söyleneni olduğu gibi bırakır.

```
Öncesi : Günümüzün hızla değişen dünyasında, işletmeler için verimlilik her zamankinden daha
         kritik bir öneme sahiptir.
Sonrası: Günümüzde verimlilik işletmeler için her zamankinden daha kritik.
```

## Üç söz

1. **Cümleyi düzelt, metni yeniden yazma.** Yalnız kokan öbek değişir; cümlenin geri kalanı olduğu gibi kalır. Zaten doğal olan bir
   ifade eşanlamlısıyla değiştirilmez; doğal bir metin olduğu gibi geri döner.
2. **Hiçbir bilgi eksilmez.** Ad, sayı, tarih, oran, liste öğesi, niteleyici ve iddianın gücü korunur.
   Paragraf sayısı ve cümle sırası girdiden gelir.
3. **Hedef dedektör değil, okur.** Puan düşürmek için metne hata, kişilik ya da süs eklenmez.

## Yapay zekâ Türkçesi nasıl kokar?

Skill'in yakaladığı aileler, her biri birer örnekle. Tam katalog `references/` altında.

| Aile | ✗ Kokan | ✓ Türkçesi |
|---|---|---|
| Bürokratik yüklem | Toplantı gerçekleştirilmiştir. | Toplantı yapıldı. |
| *Sahip olmak* kalkı | Bu karar büyük bir öneme sahiptir. | Bu karar büyük önem taşıyor. |
| *-lı bir şekilde* | Sorunu hızlı bir şekilde çözdük. | Sorunu hızla çözdük. |
| Tabela bağlaç | Ayrıca, bununla birlikte, söz konusu… | (gerekmiyorsa düşer; cümleler ekle bağlanır) |
| *Sadece… değil, aynı zamanda* | sadece hızlandırmıyor, aynı zamanda kolaylaştırıyor | hem hızlandırıyor hem kolaylaştırıyor |
| Eşdizim ve değerlik | Kapı ses eder. · Seni güvenmek | Kapı ses çıkarır. · Sana güvenmek |
| Metafor kalkı | Kara kutu yok. | Sihir yok: her parçayı açıp bakarsın. |
| Gömülü soru | Kim açtı, kim düzenledi gör. | Kimin açtığını, kimin düzenlediğini gör. |
| Hâl eki kopyası | Raporu WhatsApp'ta gönder. | Raporu WhatsApp'tan gönder. |
| Yetenek kipi | Saymak her şeyi söyler ama yavaş. | Saymak her şeyi söyleyebilir ama yavaş. |
| Söylem iskeleti | Paragraf paragraf "X değil, Y", "Asıl mesele şu:" | İddia olumlu kurulur; kalıp tekrar etmez |
| İngilizce tire ve başlık | Hız — ve güven. · Yapay Zekâ İle Metin Nasıl Yazılır | Hız ve güven. · Yapay zekâyla metin nasıl yazılır |
| TDK yazımı | Bende geliyorum. · birşey · renderı | Ben de geliyorum. · bir şey · render'ı |

## İki kip

**Yeniden yazma** (varsayılan): bir paragraf, bir arayüz metni, bir e-posta verirsin; düzeltilmiş
metni alırsın. Çıktı yalnız metindir, açıklama eklenmez.

**İnceleme**: uzun ve büyük ölçüde doğru metinler için (kitap, kılavuz, ürün metni, korpus). Metin
yeniden yazılmaz; konumlu bir bulgu listesi döner, çünkü yazar yalnız bozuk olana dokunmak ister:

| Konum | Alıntı | Sınıf | Sorun | Öneri |
|---|---|---|---|---|
| Ekran 42 | "kapı ses eder" | hata | *ses etmek* = konuşmak, itiraz etmek | "kapı ses çıkarır" |
| Ekran 7 | "kara kutu yok" | kalıp | Türkçede ilk çağrışım uçuş kayıt cihazı | "Sihir yok: her parçayı açıp bakarsın" |

Sınıflar ayrıdır: **hata** yanlıştır ve düzeltilir, **kalıp** yanlış değildir ama yapay zekâ ya da çeviri izidir, **öneri**
üslup tercihidir ve dayatılmaz.

## Neye dokunmaz

- Birebir ve tarihî alıntılar, özel adlar, kod, komut ve dosya adları, markup.
- Terim defterindeki kilitli terimler. Ekibin her gün kullandığı *deadline* zorla Türkçeleştirilmez.
- Doz, faiz oranı, tarih ve madde numarası; yasal uyarı ve bilgilendirme cümleleri.
- Şiir (varsayılan kip incelemedir) ve hukuki sonucu olabilecek cümleler.
- Kaydın kendisi: kurumsal metin kurumsal, resmî duyuru resmî, blog samimi kalır.
- İnsan yazısının izleri: kendi ritmi, deyimi, kasıtlı tekrarı. Özenli, cilalı yazı yapay zekâ işareti sayılmaz.

## Örnek

**Öncesi**

> Günümüzün hızla değişen dünyasında, işletmeler için verimlilik her zamankinden daha kritik bir
> öneme sahiptir. Yeni platformumuz, sadece iş akışlarınızı hızlandırmakla kalmıyor, aynı zamanda
> ekipler arasında güçlü bir sinerji de oluşturuyor. Kullanıcılar, sorunsuz ve kesintisiz bir
> deneyim yaşayacaktır. Sonuç olarak, platformumuz işletmenize gerçek anlamda değer katmaktadır.

**Sonrası**

> Günümüzde verimlilik işletmeler için her zamankinden daha kritik. Yeni platformumuz hem iş
> akışlarınızı hızlandırıyor hem de ekiplerin güçlü bir uyum içinde çalışmasını sağlıyor.
> Kullanıcılar platformu sorunsuz ve kesintisiz kullanacak. Platformumuz işinize gerçek anlamda
> fayda getiriyor.

Dört cümle yine dört cümle kaldı, sıraları da değişmedi. *Sorunsuz ve kesintisiz*, *güçlü*, *gerçek anlamda*
metnin iddiasıdır; silinmedi. Abartılı bulunursa inceleme kipinde **öneri** olarak işaretlenir. Beş
farklı üslupta daha fazla örnek: [`references/examples.md`](references/examples.md).

## Nasıl ölçüldü

- **SKILL.md'nin ana metni (v3)** SkillOpt ile paragraf düzeyinde, bir hakem modelle ölçülerek iyileştirildi: koku
  azalması, anlam koruma ve insan metnine dokunmama birlikte puanlandı. O ölçüm resmî üsluptaki
  metinler üzerindeydi.
- **Regresyon seti** ([`evals/`](evals/README.md)): 178 kısa vaka, 43'ü "dokunma" kontrolü. Her vaka
  tek bir kurala bağlı; bir kural gerilediğinde hangisi olduğu görünür. 135 düzeltme vakasının
  98'inin girdisi skill metninde geçmez; model bu vakaları örneği hatırlayarak geçemez, kuralı
  uygulaması gerekir. Puanlama bu iki grubu ayrı raporlar.
- Aşırı düzeltme, kaçan düzeltme kadar hata sayılır. Kontrol vakaları bunun için var.

## Kurulum

```bash
npx skills add -g deligoez/skills --skill turkish-humanizer
```

Güncellemek için:

```bash
npx skills update -g
```

Claude Code, Codex, Cursor, OpenCode ve Agent Skills biçimini okuyan öteki ajanlarla çalışır.

## Kullanım

Skill kendiliğinden tetiklenir; adını söylemen gerekmez:

- "Bu metni akıcı yap." · "Yapay zekâ gibi durmasın." · "Çeviri kokmasın."
- "Bu kitabın Türkçesini incele, hataları konumlarıyla listele."

Uzun bir işte şunları da verirsen skill kendi varsayılanları yerine onlara uyar:

- **Üslup sözleşmesi**: kişi ve kip, cümle uzunluğu, ton, nelerin serbest olduğu.
- **Terim defteri**: kilitli karşılıklar. Eşanlamlıyla çeşitlendirilmez.
- **Dokunma listesi**: alıntı, kod, kasıtlı vuruş.

## Dosyalar

| Dosya | İçerik |
|---|---|
| [`SKILL.md`](SKILL.md) | Giriş noktası: iki kip, girdiler, temel ölçü, bilgi koruma |
| [`references/ai-tells.md`](references/ai-tells.md) | Tam iz kataloğu, söylem iskeleti, inceleme kipinde bulguların ağırlığı |
| [`references/collocations.md`](references/collocations.md) | Eşdizim, fiil değerliği, İngilizce fiil mecazı |
| [`references/fluency.md`](references/fluency.md) | Akıcılık, düşen nesne, ulaç zinciri |
| [`references/mechanics.md`](references/mechanics.md) | TDK yazımı, noktalama, kesme, sayı ve saat |
| [`references/registers.md`](references/registers.md) | Nesir, başlık, slogan, arayüz, ürün ve e-posta şablonları |
| [`references/turler-ve-alanlar.md`](references/turler-ve-alanlar.md) | Tür ve alan dokunulmazları, kitleye göre terim kararı |
| [`references/terminology.md`](references/terminology.md) | Uzun ve iki dilli metinde terim defteri |
| [`references/anlati.md`](references/anlati.md) | İyi nesrin zanaatı, gündelik ve anlatı dokusu, deyim dozu |
| [`references/ceviri-teknikleri.md`](references/ceviri-teknikleri.md) | Düzeltme işlemleri: transpozisyon, modülasyon, açımlama |
| [`references/examples.md`](references/examples.md) | Üsluba göre öncesi/sonrası ve inceleme kipi örneği |

## Kaynaklar ve teşekkür

- Nurullah Ataç'ın sadelik ve konuşur gibi yazma ilkeleri; Feyza Hepçilingirler'in *Türkçe Off*'u;
  Türkçe kompozisyon pedagojisinin anlatım bozukluğu çerçevesi.
- TDK Yazım Kılavuzu ve Güncel Türkçe Sözlük. Çok anlamlı deyimlerin anlamları sözlükten doğrulandı.
- [turkish-native](https://github.com/oguzhankayan/turkish-native) (Oğuzhan Kayan, MIT): bazı
  kalıplar ve regresyon vakaları. Alınan vakalar `source: turkish-native/…` taşır.
- [insanca](https://github.com/tahiryildiz/insanca) (Tahir Yıldız, MIT): söylem iskeleti izleri, tür
  ve alan dokunulmazları, gündelik ve anlatı akış kuralları, deyim derlemesi, ürün ve e-posta
  şablonları. Onun da kaynakları:
  [insanlik-oldu-mu](https://github.com/MesutARIDORU/insanlik-oldu-mu) (MesutARIDORU, MIT) ve
  [turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill) (yucezerey, MIT).
  Metni baştan kurma ve kişilik ekleme yaklaşımı bu skill'in "dar düzeltme" ilkesiyle çeliştiği
  için alınmadı.

## English summary

`turkish-humanizer` is an Agent Skill that makes AI-generated or translated Turkish read as if a
careful Turkish writer wrote it, without changing what it says. It fixes the smell, not the text:
edits are narrow, no information is dropped, paragraph structure and register are preserved, and
natural text is returned untouched. A review mode returns positioned findings (error / pattern /
suggestion) for long, mostly correct texts. The body was optimised with SkillOpt; a 178-case
regression set with held-out variants and do-not-touch controls guards each rule. Install with
`npx skills add -g deligoez/skills --skill turkish-humanizer`.

## Lisans

[MIT](../../LICENSE) © Yunus Emre Deligöz.
