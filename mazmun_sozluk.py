import streamlit as st
mazmunlar = {
    "Mestâne": "Kök: Far. Zahiri Anlamı: Sarhoşça. Şiirdeki Karşılığı: Sevgilinin insanı büyüleyen, süzgün ve baygın bakışlı gözü. Örnek Beyit: \"Mestâne nigehinle n’ola kılsañ bizi teshîr Efsûn-ı nigâhın senin ey mâh-likā yok\" — Nedîm",
    "Hûb": "Kök: Far. Zahiri Anlamı: Güzel, iyi, hoş. Şiirdeki Karşılığı: Sevgiliyi niteleyen en temel sıfattır; hem dış güzelliği hem de güzel huyu temsil eder. Örnek Beyit: \"Hûblar mihr ü vefâ göstermeseler n’ola kim Padişahlar her ne kim dilerse anı eylerler\" — Ahmed Paşa",
    "Dildâr": "Kök: Far. Zahiri Anlamı: Gönül tutan. Şiirdeki Karşılığı: Âşığın gönlünü kendine bağlamış olan kişi, sevgili. Örnek Beyit: \"Etti o dildâr kûyunu bana mesken N'eyleyeyim gayrı ben bağı çemeni\" — Nedîm",
    "Dilber": "Kök: Far. Zahiri Anlamı: Gönül götüren. Şiirdeki Karşılığı: Güzelliğiyle âşığın aklını başından alıp kalbini çalan sevgili. Örnek Beyit: \"Dilberâ lutf eyle gel bir kez güler yüzle bize Gül yüzün görmek müyesser eyle bir kez her gize\" — Şeyhî",
    "Mâr": "Kök: Far. Zahiri Anlamı: Yılan. Şiirdeki Karşılığı: Sevgilinin siyahlığı ve kıvrımlarıyla yılana benzetilen saçı (zülf). Örnek Beyit: \"Gönül o zülf-i siyehte hayâl-i hâl eyler Sanır ki genc-i hümâyûn üzerinde mâr uyur\" — Şeyhülislâm Yahyâ",
    "Sünbül": "Kök: Far. Zahiri Anlamı: Sümbül çiçeği. Şiirdeki Karşılığı: Sevgilinin siyah, kokulu ve büklüm büklüm saçları. Örnek Beyit: \"Sünbül-i zülfün perîşân etme ey bâd-ı sabâ Can verir her târına bin nâ-tüvân u bî-nevâ\" — Bâkî",
    "Rûy": "Kök: Far. Zahiri Anlamı: Yüz, çehre. Şiirdeki Karşılığı: Nur ve parlaklık bakımından Ay veya Güneş ile kıyaslanan sevgili yüzü. Örnek Beyit: \"Rûy-i pâkin görenler dirler şems-i enverdir Sözlerini işidenler dirler dürr-i mu’berdir\" — Necâtî Bey",
    "Ruhsâr": "Kök: Far. Zahiri Anlamı: Yanak. Şiirdeki Karşılığı: Rengiyle gülün kırmızılığını, parlaklığıyla mumun (şem) ışığını temsil eden yanak. Örnek Beyit: \"Ruhsârına ayîne-i hurşîd mukābil Lâ’l-i lebi yanınca leb-i câm-ı mey bî-dil\" — Nef’î",
    "Leb": "Kök: Far. Zahiri Anlamı: Dudak. Şiirdeki Karşılığı: Kırmızılığıyla şaraba, can veren etkisiyle \"Âb-ı Hayat\"a benzetilen dudak. Örnek Beyit: \"Leblerin şerbet-i nâb oldu bana Sözlerin dâne-i nâb oldu bana\" — Ahmedî",
    "Dem-be-dem": "Kök: Far. Zahiri Anlamı: Soluk soluk, anbean. Şiirdeki Karşılığı: Aşk acısının veya sevgilinin hayalinin hiç bitmeden sürekli devam etmesi. Örnek Beyit: \"Dem-be-dem artar figānım rûy-ı zerdin görmeden Gonca veş gülşende kalsam dahi derdin görmeden\" — Lâmiî Çelebi",
    "Câm": "Kök: Far. Zahiri Anlamı: Kadeh, içki bardağı. Şiirdeki Karşılığı: İlahi aşkın kalbi veya meclisteki neşeyi sağlayan araç. Örnek Beyit: \"Ezelden şâh-ı aşkın bende-i fermânıyız cânâ Muhabbet mülkünün sultân-ı âlî-şânıyız cânâ\" — Bâkî",
    "Pinhân": "Kök: Far. Zahiri Anlamı: Gizli, saklı. Şiirdeki Karşılığı: Aşkın ve aşka dair sırların başkalarından korunması, gizli tutulması. Örnek Beyit: \"Tedbîr-i katlimizde o gaddâr gizlesin Sırr-ı mahabbeti dilde pinhân gerekse\" — Şeyh Gâlib",
    "Peymâne": "Kök: Far. Zahiri Anlamı: Büyük kadeh. Şiirdeki Karşılığı: Gönlün aşkla dolup taşması veya ömür vadesinin sona ermesi. Örnek Beyit: \"Peymâne-i aşkınla mest olan ârif Dünyâ vü mâ-fîhâyı n'eyler efendim\" — Nesîmî",
    "Peykân": "Kök: Far. Zahiri Anlamı: Okun ucu. Şiirdeki Karşılığı: Sevgilinin kirpiklerinin birer ok ucu gibi âşığın kalbine saplanması. Örnek Beyit: \"Oklarun peykânı cânımda mekân etsin diler Cânım ol peykânların cânında cân etsin diler\" — Fuzûlî",
    "Tîr": "Kök: Far. Zahiri Anlamı: Ok. Şiirdeki Karşılığı: Sevgilinin delici ve yaralayıcı bakışı veya kirpiği. Örnek Beyit: \"Gözlerin tîr-i gamzen sînem deler Zülf-i şeb-rengin gönlümü bağlar\" — Kadı Burhaneddin",
    "Müjgân": "Kök: Far. Zahiri Anlamı: Kirpikler. Şiirdeki Karşılığı: Âşığı yaralayan veya öldüren ok ve hançer takımı. Örnek Beyit: \"Müjgânların hayâli gözümden gitmez Tîr-i gamzen sînemi deler geçmez\" — Hayâlî Bey",
    "Kâmet": "Kök: Ar. Zahiri Anlamı: Boy, endam. Şiirdeki Karşılığı: Sevgilinin servi ağacı gibi uzun, düz ve kusursuz boyu. Örnek Beyit: \"Kāmetin serv-i revânın kıldılar kaddim dütâ Ayrılığın nârına yaktın beni ey bî-vefâ\" — Ahmed Paşa",
    "Kadd": "Kök: Ar. Zahiri Anlamı: Boy. Şiirdeki Karşılığı: Sevgilinin ölçülü ve uzun boyu. Örnek Beyit: \"Kaddi mevzûn hûblar içre seçilmez bir dahi Şems-i meclistir yüzün nûrun gören eyler duâ\" — Zâtî",
    "Bâlâ": "Kök: Far. Zahiri Anlamı: Yüksek, yukarı. Şiirdeki Karşılığı: \"Kadd-i bâlâ\" tamlamasıyla sevgilinin ulaşılamayan, yüce ve uzun boyu. Örnek Beyit: \"O kadd-i bâlâya ermez elimiz neyleriz Gönül o serv-i âzâda muallaktır neyleriz\" — Nâilî",
    "Hadd": "Kök: Ar. Zahiri Anlamı: Yanak. Şiirdeki Karşılığı: Gül gibi taze, ateş gibi parlak ve kırmızı olan sevgili yanağı. Örnek Beyit: \"Lâle-hadler yine gülşende neler etmediler Servi yürütmediler goncayı söyletmediler\" — Necâtî Bey"
}
mazmunlar = {
    "Mestâne": "Kök: Far. Zahiri Anlamı: Sarhoşça. Şiirdeki Karşılığı: Sevgilinin insanı büyüleyen, süzgün ve baygın bakışlı gözü. Örnek Beyit: \"Mestâne nigehinle n’ola kılsañ bizi teshîr Efsûn-ı nigâhın senin ey mâh-likā yok\" — Nedîm",
    "Hûb": "Kök: Far. Zahiri Anlamı: Güzel, iyi, hoş. Şiirdeki Karşılığı: Sevgiliyi niteleyen en temel sıfattır; hem dış güzelliği hem de güzel huyu temsil eder. Örnek Beyit: \"Hûblar mihr ü vefâ göstermeseler n’ola kim Padişahlar her ne kim dilerse anı eylerler\" — Ahmed Paşa",
    "Dildâr": "Kök: Far. Zahiri Anlamı: Gönül tutan. Şiirdeki Karşılığı: Âşığın gönlünü kendine bağlamış olan kişi, sevgili. Örnek Beyit: \"Etti o dildâr kûyunu bana mesken N'eyleyeyim gayrı ben bağı çemeni\" — Nedîm",
    "Dilber": "Kök: Far. Zahiri Anlamı: Gönül götüren. Şiirdeki Karşılığı: Güzelliğiyle âşığın aklını başından alıp kalbini çalan sevgili. Örnek Beyit: \"Dilberâ lutf eyle gel bir kez güler yüzle bize Gül yüzün görmek müyesser eyle bir kez her gize\" — Şeyhî",
    "Mâr": "Kök: Far. Zahiri Anlamı: Yılan. Şiirdeki Karşılığı: Sevgilinin siyahlığı ve kıvrımlarıyla yılana benzetilen saçı (zülf). Örnek Beyit: \"Gönül o zülf-i siyehte hayâl-i hâl eyler Sanır ki genc-i hümâyûn üzerinde mâr uyur\" — Şeyhülislâm Yahyâ",
    "Sünbül": "Kök: Far. Zahiri Anlamı: Sümbül çiçeği. Şiirdeki Karşılığı: Sevgilinin siyah, kokulu ve büklüm büklüm saçları. Örnek Beyit: \"Sünbül-i zülfün perîşân etme ey bâd-ı sabâ Can verir her târına bin nâ-tüvân u bî-nevâ\" — Bâkî",
    "Rûy": "Kök: Far. Zahiri Anlamı: Yüz, çehre. Şiirdeki Karşılığı: Nur ve parlaklık bakımından Ay veya Güneş ile kıyaslanan sevgili yüzü. Örnek Beyit: \"Rûy-i pâkin görenler dirler şems-i enverdir Sözlerini işidenler dirler dürr-i mu’berdir\" — Necâtî Bey",
    "Ruhsâr": "Kök: Far. Zahiri Anlamı: Yanak. Şiirdeki Karşılığı: Rengiyle gülün kırmızılığını, parlaklığıyla mumun (şem) ışığını temsil eden yanak. Örnek Beyit: \"Ruhsârına ayîne-i hurşîd mukābil Lâ’l-i lebi yanınca leb-i câm-ı mey bî-dil\" — Nef’î",
    "Leb": "Kök: Far. Zahiri Anlamı: Dudak. Şiirdeki Karşılığı: Kırmızılığıyla şaraba, can veren etkisiyle \"Âb-ı Hayat\"a benzetilen dudak. Örnek Beyit: \"Leblerin şerbet-i nâb oldu bana Sözlerin dâne-i nâb oldu bana\" — Ahmedî",
    "Dem-be-dem": "Kök: Far. Zahiri Anlamı: Soluk soluk, anbean. Şiirdeki Karşılığı: Aşk acısının veya sevgilinin hayalinin hiç bitmeden sürekli devam etmesi. Örnek Beyit: \"Dem-be-dem artar figānım rûy-ı zerdin görmeden Gonca veş gülşende kalsam dahi derdin görmeden\" — Lâmiî Çelebi",
    "Câm": "Kök: Far. Zahiri Anlamı: Kadeh, içki bardağı. Şiirdeki Karşılığı: İlahi aşkın kalbi veya meclisteki neşeyi sağlayan araç. Örnek Beyit: \"Ezelden şâh-ı aşkın bende-i fermânıyız cânâ Muhabbet mülkünün sultân-ı âlî-şânıyız cânâ\" — Bâkî",
    "Pinhân": "Kök: Far. Zahiri Anlamı: Gizli, saklı. Şiirdeki Karşılığı: Aşkın ve aşka dair sırların başkalarından korunması, gizli tutulması. Örnek Beyit: \"Tedbîr-i katlimizde o gaddâr gizlesin Sırr-ı mahabbeti dilde pinhân gerekse\" — Şeyh Gâlib",
    "Peymâne": "Kök: Far. Zahiri Anlamı: Büyük kadeh. Şiirdeki Karşılığı: Gönlün aşkla dolup taşması veya ömür vadesinin sona ermesi. Örnek Beyit: \"Peymâne-i aşkınla mest olan ârif Dünyâ vü mâ-fîhâyı n'eyler efendim\" — Nesîmî",
    "Peykân": "Kök: Far. Zahiri Anlamı: Okun ucu. Şiirdeki Karşılığı: Sevgilinin kirpiklerinin birer ok ucu gibi âşığın kalbine saplanması. Örnek Beyit: \"Oklarun peykânı cânımda mekân etsin diler Cânım ol peykânların cânında cân etsin diler\" — Fuzûlî",
    "Tîr": "Kök: Far. Zahiri Anlamı: Ok. Şiirdeki Karşılığı: Sevgilinin delici ve yaralayıcı bakışı veya kirpiği. Örnek Beyit: \"Gözlerin tîr-i gamzen sînem deler Zülf-i şeb-rengin gönlümü bağlar\" — Kadı Burhaneddin",
    "Müjgân": "Kök: Far. Zahiri Anlamı: Kirpikler. Şiirdeki Karşılığı: Âşığı yaralayan veya öldüren ok ve hançer takımı. Örnek Beyit: \"Müjgânların hayâli gözümden gitmez Tîr-i gamzen sînemi deler geçmez\" — Hayâlî Bey",
    "Kâmet": "Kök: Ar. Zahiri Anlamı: Boy, endam. Şiirdeki Karşılığı: Sevgilinin servi ağacı gibi uzun, düz ve kusursuz boyu. Örnek Beyit: \"Kāmetin serv-i revânın kıldılar kaddim dütâ Ayrılığın nârına yaktın beni ey bî-vefâ\" — Ahmed Paşa",
    "Kadd": "Kök: Ar. Zahiri Anlamı: Boy. Şiirdeki Karşılığı: Sevgilinin ölçülü ve uzun boyu. Örnek Beyit: \"Kaddi mevzûn hûblar içre seçilmez bir dahi Şems-i meclistir yüzün nûrun gören eyler duâ\" — Zâtî",
    "Bâlâ": "Kök: Far. Zahiri Anlamı: Yüksek, yukarı. Şiirdeki Karşılığı: \"Kadd-i bâlâ\" tamlamasıyla sevgilinin ulaşılamayan, yüce ve uzun boyu. Örnek Beyit: \"O kadd-i bâlâya ermez elimiz neyleriz Gönül o serv-i âzâda muallaktır neyleriz\" — Nâilî",
    "Hadd": "Kök: Ar. Zahiri Anlamı: Yanak. Şiirdeki Karşılığı: Gül gibi taze, ateş gibi parlak ve kırmızı olan sevgili yanağı. Örnek Beyit: \"Lâle-hadler yine gülşende neler etmediler Servi yürütmediler goncayı söyletmediler\" — Necâtî Bey"
}
st.markdown("""
<style>
    .stApp {
        background-image: url("https://i.imgur.com/vy5O4q3.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.45);
    }
    h1, h2, h3, p, .stMarkdown, label, .st-emotion-cache {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<h1 style="color: white; text-align: center;">KLASİK TÜRK ŞİİRİ MAZMUN SÖZLÜĞÜ</h1>', unsafe_allow_html=True)


st.set_page_config(page_title="Mazmun Sözlüğü", layout="centered")

st.markdown("""
<style>
    .stApp {
        background-image: url("https://i.imgur.com/vy5O4q3.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.45);
    }
</style>
""", unsafe_allow_html=True)


st.info("""
**Mazmun** (Ar. mażmūn)  

Klasik Divan şiirinde kullanılan klişeleşmiş, kalıplaşmış anlam, kavram veya imgedir.
""")

mazmunlar = {
    "Nergis": "Sevgilinin gözü. Uykulu, baygın bakış.",
    "Kement / Yılan": "Sevgilinin saçı. Aşığı esir eden siyah teller.",
    "Gonca": "Sevgilinin ağzı. Sıkı kapalı, sır vermez.",
    "Lal": "Sevgilinin dudağı. Kırmızı, şarap gibi.",
    "Yay / Ebru": "Sevgilinin kaşı. Ok atan yay.",
    "Ok / Müje": "Sevgilinin kirpiği. Kalbe saplanan ok.",
    "Servi": "Sevgilinin boyu. Uzun, düzgün, endamlı.",
    "Ay / Mah": "Sevgilinin yüzü. Parlak ve kusursuz.",
    "Bade / Şarap": "Aşk şarabı, ilahi sarhoşluk.",
    "Zenehdan / Çah": "Sevgilinin gamzesi (çene çukuru). Aşığın düştüğü kuyu.",
    "Hat": "Sevgilinin yüzündeki tüyler (yeşil reyhan gibi).",
    "Ben / Hal": "Sevgilinin yüzündeki siyah ben.",
    "Dürr / İnci": "Sevgilinin dişleri.",
    "Gerdan": "Sevgilinin beyaz boynu.",
    "Sine": "Sevgilinin göğsü (ayna gibi).",
    "Gül": "Sevgilinin yanağı.",
    "Saki": "Aşk şarabı sunan, meclis düzenleyen.",
    "Mecnun": "Aşkından aklını yitirmiş aşık tipi.",
    "Geda": "Aşık (fakir, dilenci).",
    "Harabat": "Meyhane, ilahi aşkın mekanı.",
    "Pir-i Mugan": "Meyhanenin bilge mürşidi.",
    "Zahid": "Aşktan anlamayan kuru sofu.",
    "Şeb-i Yelda": "En uzun gece, bitmeyen hasret gecesi.",
    "Ağyar / Rakip": "Aşığa engel olan rakip.",
    "Çeşm-i Giryan": "Gözyaşı döken göz.",
    "Hüma": "Uğurlu talih kuşu.",
    "Anka": "Efsanevi nadir kuş.",
    "Saba": "Sevgiliden haber getiren rüzgar.",
    "Nilüfer": "Boynu bükük, mahcup çiçek."
}

arama = st.text_input("🔍 Mazmun ara:", "", key="main_search")

if arama:
    arama_lower = arama.lower()
    bulunan = {k: v for k, v in mazmunlar.items() if arama_lower in k.lower() or arama_lower in v.lower()}
    if bulunan:
        st.success(f"✅ {len(bulunan)} mazmun bulundu")
        for m, aciklama in bulunan.items():
            st.subheader(m)
            st.write(aciklama)
            st.divider()
    else:
        st.error("❌ Bu mazmun sözlükte yok.")
else:
    st.info("🔎 Bir mazmun adı veya kelime yazın.")

st.caption("Geliştiren: **Ayşe GÜLMEZ**")

