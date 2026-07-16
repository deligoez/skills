# Çeviri teknikleri — kendi İngilizceni Türkçeye çevir

**Merkez model:** humanizer'ın gerçek işi, **kendi örtük İngilizce taslağını
deyimsel Türkçeye çevirmek.** Çeviri kokusu = kaynağın (İngilizce) hedefin içinden
*sızması* (source shining through). Çeviribilim, birebiri deyimsele döndüren
operasyonlara ad koymuş. `ai-tells.md` KOKUYU adlandırır (isimler); bu dosya
DÜZELTMEYİ adlandırır (fiiller): bir cümle kokuyorsa hangi operasyonu uygulayacağın.

Dayandığı çerçeve: **Vinay & Darbelnet** (7 çeviri işlemi), **Blum-Kulka**
(açımlama/explicitation hipotezi), **Venuti** (yerlileştirme/yabancılaştırma).

---

## Tek kök mekanizma: açımlama (explicitation) — fazla açıklık

Çeviriler, kaynağın örtük bıraktığını **açık eder.** İngilizce ayrı kelimeyle
söyler; Türkçe eki, bağlamı, pro-drop'u ile taşır. "Çevirmen" (sen) fazla
belirtince → çeviri kokusu. **Usta çare: SİL.** Eke, fiile, bağlama bırak. (Bu
skill'in ana tezidir; artık adı ve kuramı var. bkz. SKILL.md "fazla açıklık".)

## Vinay & Darbelnet: yedi işlem, EN→TR

İki aile. **Direkt** (kaynağa yakın — yapıyı taşır, tetikte ol) · **Dolaylı**
(hedefe döner — düzeltmelerin çoğu burada, BUNLARI KULLAN).

**Direkt — ölçülü:**
1. **Ödünçleme** — kelimeyi olduğu gibi al. Meşru: yerleşik/teknik slug (`byte`,
   `latch` kalıcı kimlik). Tuzak: gereksiz İngilizce ("feature", "insight").
2. **Öyküntü / Kalk (calque)** — yapıyı birebir kopyala. **DÜŞMAN.** Çeviri
   kokusunun çoğu budur: "kara kutu", "değer katmak", "kitap düşünür",
   "hazır almak". Gördüğün an dolaylı bir işleme çevir.
3. **Birebir çeviri** — kelime kelime. İki dilin yapısı çakışırsa (nadir) tutar;
   EN→TR'de SOV ve isim/fiil farkı yüzünden genelde kokar.

**Dolaylı — düzeltme takımı:**
4. **Transpozisyon (sözcük türü değiştir).** İngilizce İSİM ağırlıklı, Türkçe
   FİİL ağırlıklı — **en büyük tek düzeltme.** İsim yığınını fiile çevir:
   *"the construction of the machine"* → **makineyi kurmak** (makinenin kuruluşu
   DEĞİL); *"upon completion"* → **bitince**; *"with the help of X"* →
   **X'i kullanarak / X ile**. (ai-tells §3 adcıl kuruluş/light-verb'ün
   operasyonu budur.)
5. **Modülasyon (bakış açısı değiştir).** Çerçeveyi çevir: olumsuz→olumlu
   (*"it is not hard"* → **kolay**), edilgen→etken (*"the wire is burned"* →
   **teli yakarsın**), soyut→somut aktör (*"bu kitap Türkçe düşünür"* →
   **kurduğun makine Türkçenin harfleriyle konuşur**). Kalıp bir framing'i
   Türkçenin doğal bakışına döndür.
6. **Eşdeğerlik (deyim için deyim).** Aynı etki, farklı söz. Atasözü/deyim/klişe
   KELİME KELİME çevrilmez: Türkçenin kendi deyimini bul, yoksa BETİMLE.
   *"kara kutu yok"* → **sihir yok: her parçanın içini açarsın**. (ai-tells §11
   metafor kalkının operasyonu.)
7. **Uyarlama (kültürel ikame).** Kaynak kültür ögesini hedefe taşı:
   Alice/Bob → **Ali/Veli**; inç/feet → doğal ölçü. (CLAUDE.md'de zaten karar.)

## Yön asimetrisi: EN→TR (kalkın kaynağı)

Kalkların çoğu bu beş yapısal farktan doğar — düzeltme hep aynı yöne çeker:

- **İsim → fiil** (transpozisyon). EN nominalizasyon sever, TR fiil. Çeviri
  kokusunun yarısı bu tek eksende.
- **Ayrı kelime → ek.** EN *"in a … way / by …ing / of the"* → TR eki
  (`-CA, -erek, -in`). Açımlamanın panzehiri.
- **SVO → SOV.** Yüklem sona. İngilizce sırayı koruma; Türkçe dizilişe göre kur.
- **Zorunlu özne → pro-drop.** *"It is important that you check"* →
  **kontrol etmen önemli** (özne ekte).
- **Edilgen bolluğu → etken.** EN edilgeni sever; TR etken daha canlı:
  *"yapılmaktadır"* → **yaparız / yapılır**.

## Yerlileştirme vs yabancılaştırma (Venuti)

Doğal Türkçe için **YERLİLEŞTİR** (domestication): deyim, kültür ve yapı hedefe
döner, kaynak görünmez olur. Yabancılaştırma (kaynağı bilerek hissettirme) edebî
bir tercih olabilir — ama bizim amacımız değil; **çeviri kokusu = istenmeyen
yabancılaştırma.** Tek istisna: terim/slug'lar (`latch`, `byte`) bilerek yabancı
kalır (kalıcı kimlik, bkz. `terminology.md`).

## İşleyiş — bir cümle kokuyorsa

1. **Kalk mı?** Yapıyı İngilizceden kopyaladım mı → transpozisyon/modülasyonla
   yeniden kur.
2. **Fazla mı açtım?** (açımlama) → sil; eke/bağlama/bağlama bırak.
3. **İsim yığını mı?** → fiile çevir (transpozisyon).
4. **Çerçeve İngilizce mi?** → modülasyonla Türkçenin bakışına çevir.
5. **Deyim birebir mi?** → eşdeğerlik, yoksa betimle.

Çapraz: `ai-tells.md` (kokular) · `anlati.md` (pozitif craft) ·
`collocations.md` (değerlik) · bu dosya (düzeltme operasyonları).

---

*Kaynak sızıyorsa çevir; sen kendi İngilizceni Türkçeye çeviren çevirmensin.
Amaç birebir sadakat değil, kokusuz ve yaşayan hedef metin.*
