
import streamlit as st
import streamlit as st

st.set_page_config(page_title="Mazmun Sözlüğü", page_icon="🕌", layout="wide")

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
        background-color: rgba(15, 23, 42, 0.75);
    }
    .main-title {
        color: #f1e8d4;
        text-align: center;
        font-size: 3rem;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.9);
        margin: 30px 0;
    }
    .stButton>button {
        background-color: #8B4513;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">KLASİK TÜRK ŞİİRİ<br>MAZMUN SÖZLÜĞÜ</h1>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #d4c3a3; font-size: 1.2rem;'>Divan Edebiyatı Mazmunları • Araştırma ve Eğitim Aracı</p>", unsafe_allow_html=True)

st.info("""
**Mazmun** (Ar. mażmūn): Klasik Divan şiirinde kullanılan klişeleşmiş, kalıplaşmış anlam ve imgedir. Şairler sevgiliyi, aşkı ve doğayı bu geleneksel mazmunlarla anlatır.
""")

# Sidebar - Kategoriler
with st.sidebar:
    st.header("📚 Kategoriler")
    kategori = st.selectbox("Kategori seçin", [
        "Tüm Mazmunlar",
        "Göz ve Bakış Mazmunları",
        "Saç ve Vücut Mazmunları",
        "Aşk ve Sarhoşluk Mazmunları",
        "Tasavvufi Mazmunlar"
    ])

# Mazmunlar (örnek)
mazmunlar = { ... }  # önceki mazmunları buraya koy

arama = st.text_input("🔍 Mazmun ara:", "")

if arama:
    # arama kodu
    pass

st.caption("Geliştiren: **Ayşe GÜLMEZ** • Klasik Türk Edebiyatı Projesi")

st.set_page_config(page_title="Mazmun Sözlüğü", page_icon="🕌", layout="centered")

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
    .main-title {
        color: white;
        text-align: center;
        font-size: 3.2rem;
        text-shadow: 4px 4px 12px rgba(0,0,0,0.9);
        margin-top: 80px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Klasik Türk Şiiri Mazmun Sözlüğü</h1>', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: white;'>Divan Edebiyatı Mazmunları Araştırma Aracı</h3>", unsafe_allow_html=True)

st.info("""
**Mazmun** (Ar. mażmūn)  

Klasik Divan şiirinde kullanılan **klişeleşmiş, kalıplaşmış anlam, kavram veya imgedir**.  

Şairler, sevgilinin fiziksel özelliklerini veya soyut kavramları geleneksel mazmunlarla anlatır.  
Örnek: Göz → Nergis, Kaş → Keman, Saç → Yılan.
""")

# Mazmunlar
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

arama = st.text_input("🔍 Mazmun ara:", "", key="unique_search")

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
