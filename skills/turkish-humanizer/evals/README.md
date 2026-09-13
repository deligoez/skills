# turkish-humanizer regresyon seti

`cases/*.yaml`, skill'in davranışını cümle düzeyinde sabitleyen vaka setidir. Her kural değişikliği bu
seti geçmeli; sahada yakalanan her yeni hata buraya bir vaka olarak girer.

Set, iki şeyi ölçer:

- **Düzeltme:** kokan ya da yanlış bir yapı gerçekten gidiyor mu?
- **Dokunmama:** zaten doğal olan metin (kontrol vakası) olduğu gibi kalıyor mu? Aşırı düzeltme, kaçan
  düzeltme kadar hatadır.

## SkillOpt ölçümüyle ilişkisi

v3 gövdesi SkillOpt ile paragraf düzeyinde, bir hakem modelle ölçüldü (koku azalması, anlam koruma,
insan metnine dokunmama). Bu set onun yerine geçmez, onu tamamlar. Burada vakalar kısa, çoğu
deterministik denetlenir ve her biri tek bir kurala bağlıdır: bir kural gerilediğinde hangisi olduğu
görünür. SkillOpt eğitim verisi resmî kayıttaydı; buradaki arayüz, ürün ve günlük dil vakaları o
boşluğu da kısmen kapatır.

## Vaka şeması

```yaml
cases:
- id: whatsapptan-gonder          # kebab-case, benzersiz
  source: turkish-native/p10-whatsapp-case   # saha | <referans adı> | heldout | turkish-native/<vaka id>
  ref: references/collocations.md # vakayı öğreten dosya (liste olabilir); SKILL.md de geçerli
  kind: fix                       # fix: bir şey değişmeli · control: hiçbir şey değişmemeli
  mode: rewrite                   # rewrite (varsayılan) | review
  context: ...                    # isteğe bağlı: tür, kitle, terim defteri, kast
  input: Sayfayı WhatsApp'ta gönder.
  expected: Sayfayı WhatsApp'tan gönder.
```

Denetim alanları (en az biri gerekli):

| Alan | Ne zaman |
|---|---|
| `expected` | Tek doğru biçim varsa (yazım, hâl eki, uyum). Boşluk farkı yok sayılır, harf farkı sayılmaz. |
| `expected_contains` | Korunması ya da gelmesi gereken parçalar (liste öğeleri, sayılar, terimler). |
| `expected_not_contains` | Gitmesi gereken kalk ya da düzeltmenin getirmemesi gereken tuzak. |
| `expected_sentences` | Cümle sayısı birebir korunmalıysa. |
| `expected_max_sentences` | Üst sınır yeterliyse. |
| `expected_property` | Dizgiyle denetlenemeyen şart; hakem (insan ya da model) okur. |

`contains` ve `not_contains` Türkçe büyük/küçük harf duyarsızdır (`I→ı`, `İ→i`).

Doğrulayıcının kuralları:

- **Kontrol vakası:** `expected` alanı girdiyle birebir aynı olmalı.
- **Düzeltme vakası:** `expected` alanı girdiyle aynı olamaz. `expected_not_contains` içindeki
  dizgilerden en az biri girdide geçmeli; geçmiyorsa vaka hiçbir şeyi sınamıyordur.
- **Kapsam:** her `references/*.md` dosyası (örnek dosyası `examples.md` hariç) ve `SKILL.md` en az bir
  vakada anılmalı.
- **Kontrol oranı:** kontroller setin en az %20'si olmalı.

## Çalıştırma

Betik [uv](https://docs.astral.sh/uv/) ile bağımlılığını kendisi kurar:

```bash
uv run evals/check.py validate                 # şema, id, ref, kapsam, kontrol oranı
uv run evals/check.py prompts > prompts.jsonl  # vaka başına {id, prompt}
uv run evals/check.py score outputs.jsonl      # {id, output} satırlarını puanla
```

`score` başarısız ve eksik vakaları listeler, özeti stderr'e yazar, biri bile varsa 1 ile çıkar.
Özet düzeltme vakalarını ikiye ayırır: girdisi `SKILL.md` ya da bir referans dosyasında birebir geçenler
ve geçmeyenler. Birinci grup, model örneği hatırlayarak da geçebileceği için kuralın kendisini
ölçmez; bir kuralın işe yarayıp yaramadığına ikinci gruptan bak. Yeni bir kural eklerken referansa
koyduğun örneğin yanına, referansta geçmeyen bir **varyant** vaka da ekle (`source: heldout`).

`expected_property` taşıyan vakalar deterministik denetimleri geçerse `judge` olarak işaretlenir;
onları bir hakem okumalı. Çıktının `<metin>…</metin>` sarmalayıcısı puanlamadan önce açılır.

Model çıktıları örneklemeyle üretildiği için tek koşu gürültülüdür: aynı vaka bir koşuda geçip ötekinde
kalabilir. İki sürümü karşılaştırırken her birini en az üç kez koştur ve yalnız üç koşunun en az
ikisinde yön değiştiren vakalara güven. Hakem de gürültülüdür: birebir aynı çıktıya bir kararı önbelleğe
al ki iki kol aynı metin için farklı puan almasın.

Örnek koşucu. Skill'i ajanın kurulu kopyasından değil **repodaki metinden** yükle: kurulu kopya eski
olabilir, `claude -p` da kullanıcının hook'ları ve ayarlarıyla koşar. Aşağıdaki koşu SKILL.md ile
referansları sistem istemine koyar, araçları, MCP'yi, skill yüklemeyi ve kullanıcı ayarlarını kapatır:

```bash
{ echo "Sen dikkatli bir Türkçe editörüsün. Yalnızca istenen çıktıyı döndür."
  echo "=== SKILL.md ==="; cat SKILL.md
  for f in references/*.md; do echo "=== $f ==="; cat "$f"; done
} > /tmp/th-system.txt

uv run evals/check.py prompts > /tmp/th-prompts.jsonl
while IFS= read -r row; do
  id=$(jq -r .id <<<"$row")
  out=$(jq -r .prompt <<<"$row" | claude -p --model sonnet --tools "" --strict-mcp-config \
    --disable-slash-commands --setting-sources "" --no-session-persistence \
    --system-prompt-file /tmp/th-system.txt)
  jq -nc --arg id "$id" --arg output "$out" '{id: $id, output: $output}'
done < /tmp/th-prompts.jsonl > /tmp/th-outputs.jsonl
uv run evals/check.py score /tmp/th-outputs.jsonl
```

Skill'in etkisini görmek için aynı koşuyu yalnız ilk satırı içeren bir sistem istemiyle de yap; eski
bir sürümle karşılaştırmak için sistem istemini `git show <commit>:<yol>` ile o sürümden kur.

## Vaka eklemek

1. Hatayı en küçük biçimine indir; tek bir ayrımı göstersin.
2. Kuralı öğreten referans dosyasında kural yoksa önce kuralı yaz, sonra vakayı ekle.
3. Tek doğru biçim yoksa `expected` yerine `contains` / `not_contains` / `property` kullan.
4. Kuralın yanlış pozitifi varsa (doğal olduğu bir bağlam) onu da **kontrol** vakası olarak ekle.
5. `uv run evals/check.py validate`.

## turkish-native'den alınanlar

`source: turkish-native/...` taşıyan vakalar
[oguzhankayan/turkish-native](https://github.com/oguzhankayan/turkish-native) eval setinden uyarlandı.
Birebir alınmayanlar ve nedenleri:

| Vaka | Neden alınmadı ya da değiştirildi |
|---|---|
| `p02-bureaucratic` | Beklenen *"İşlemi başlatmak için butona basın"* anlamı daraltıyor; yalnızca kalıbın gitmesi denetleniyor. |
| `p09-focus` | Beklenen çıktı *"istediğin zaman"* öğesini düşürüyordu; öğenin korunması şart koşuldu. |
| `p11-build-page`, `p12-play-page`, `p12-hour-eating`, `p14-control-offer` | Görüş ayrılığı. *Her işletmeye sayfa kurar*, *saat yiyen iş*, *daha fazla kontrol sunar* bu skill'in ölçüsüyle doğal Türkçedir; *sayfanın üstünde oynamak* ise bağlam olmadan kastı belirsiz. Referanslarda bunları hata sayan bir kural yok; üç koşuluk ölçümde eski ve yeni skill bunları neredeyse her koşuda olduğu gibi bıraktı. Setten çıkarıldı. |
| `p13-perform` | Beklenen *"Kullanıcı hesabı silebilir"* girdide olmayan bir nesne (hesap) ekliyor; uydurmama şartı eklendi. |
| `p15-passive` | Edilgeni etkene çevirmek için fail bağlamdan getiriliyor; v3 edilgeni yalnız `-mış/-makta olan` ikizinde ve fail gizlendiğinde hedefliyor. |
| `p18-*` | *"12'si telefonlu"* → *"12 telefon numarası bulundu"* anlamı değiştiriyor (12 işletme ≠ 12 numara). |
| `p25-success` | Beklenen *"Kaydedildi"* girdide olmayan bir işlemi uyduruyor; uydurmama şartı eklendi. |
| `p31`, `p32`, `p35`, `p36`, `p38`, `p39`, `p40`, `p43`, `p45` | Pazarlama iddiasını kısmak ya da silmek içerik kararıdır; bu skill'in "hiçbir bilgi eksilmez" sözleşmesiyle çelişir. Bu durumlar inceleme kipinde **öneri** olarak raporlanır. |
| `p47-agreement` | *"gönderir, tamamlarsın"* ortak ek kullanımı tartışmalı; kaynak set aynı yapıyı `p47-gezdir` vakasında doğru sayıyor. |
| `p47-gezdir` | Aynı nedenle alınmadı. |
| `p48-*` | Beklenen çıktılar tartışmalı (*"hazır bir şablondan mı hazırlanıyor"* yeni bir yakın ses tekrarı yaratıyor). |
| `p49-process-heading-template` | Aynı başlığın farklı işletmelerin sayfalarında tekrarı; tek bir girdi metnine ait bir hata değil, üretim hattının sorunu. |
| `p50-*`, `p51-nav-echo` | Yeniden yazma yerine inceleme kipine taşındı: ikinci yuvaya koyacak bilgi girdide yoksa uydurulmaz. |
| `control-dashboard` | *Dashboard'da* cins ada kesme sorusu açıyor (`mechanics.md`); kontrol olarak belirsiz. |

Kaynak projenin lisans bildirimi:

```
MIT License

Copyright (c) 2026 Oğuzhan Kayan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
