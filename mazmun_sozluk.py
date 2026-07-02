import streamlit as st

st.set_page_config(page_title="Mazmun Sözlüğü", page_icon="🕌", layout="centered")

# Arka plan
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
        font-size: 3.5rem;
        text-shadow: 4px 4px 12px rgba(0,0,0,0.9);
        margin-top: 80px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🕌 Klasik Türk Şiiri<br>Mazmun Sözlüğü</h1>', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: white;'>Divan Edebiyatı Mazmunları Araştırma Aracı</h3>", unsafe_allow_html=True)

arama = st.text_input("🔍 Mazmun ara:", "", key="search1")

st.caption("Geliştiren: **Ayşe GÜLMEZ**")
