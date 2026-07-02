import streamlit as st
st.markdown("""
<style>
    .stApp {
        background-image: url("https://i.imgur.com/JAri0SO.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    /* Yazıları daha okunur yapmak için hafif gölge */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp div {
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
    .stApp {
        background-image: url("https://i.imgur.com/JAri0SO.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    /* Yazıları daha okunur yapmak için hafif gölge */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp div {
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
    .stApp {
        background-image: url("https://i.imgur.com/JAri0SO.jpg");
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
        background-color: rgba(0, 0, 0, 0.25);   /* Daha şeffaf, siyah ton */
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
    .stApp {
        background-image: url("https://i.imgur.com/JAri0SO.jpg");
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
        background-color: rgba(0, 0, 0, 0.25);   /* Daha şeffaf, siyah ton */
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
    .stApp {
        background-image: url("https://i.imgur.com/JAri0SO.jpg");
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
        background-color: rgba(248, 241, 227, 0.65);  /* Daha az beyaz */
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
    .stApp {
        background-image: url("https://i.imgur.com/JAri0SO.jpg");
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
        background-color: rgba(248, 241, 227, 0.82);
    }
</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Mazmun Sözlüğü", page_icon="🕌", layout="centered")

# Stil
st.markdown("""
<style>
    .stApp {background-color: #f8f1e3;}
    h1 {color: #8B4513; text-align: center;}
    .stTextInput > div > div > input {
        background-color: #fffaf0;
        border: 2px solid #8B4513;
        border-radius: 10px;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🕌 Klasik Türk Şiiri Mazmun Sözlüğü")
st.markdown("### Divan Edebiyatı Mazmunları")

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

arama = st.text_input("🔍 Mazmun ara:", key="unique_search")

if arama:
    arama_lower = arama.lower()
    bulunan = {k: v for k, v in mazmunlar.items() 
               if arama_lower in k.lower() or arama_lower in v.lower()}
    
    if bulunan:
        st.success(f"✅ {len(bulunan)} mazmun bulundu")
        for m, aciklama in bulunan.items():
            st.subheader(m)
            st.write(aciklama)
            st.divider()
    else:
        st.error("❌ Bu mazmun sözlükte yok.")
else:
    st.info("🔎 Bir mazmun adı veya kelime yazarak arama yapın.")

st.caption("Klasik Türk Edebiyatı Mazmun Sözlüğü")
