import streamlit as st

st.title("🕌 Klasik Şiir Mazmun Sözlüğü")
st.write("Divan edebiyatı mazmunları - Araştırma için")

mazmunlar = {
    "Nergis": "Sevgilinin gözüdür. Renginden ve duruşundan dolayı uykulu, baygın veya hasta bakışı temsil eder.",
    "Kement / Mar / Yılan": "Sevgilinin saçıdır. Aşığın boynuna dolanır, onu esir eder ve siyahtır.",
    "Gonca": "Sevgilinin ağzıdır. Sırrını vermez, sıkı sıkıya kapalıdır; güldüğü zaman açılır.",
    "Lal": "Sevgilinin dudağıdır. Hem rengi kırmızıdır hem de aşığa hayat veren şarap (söz) oradan çıkar.",
    "Yay / Ebru": "Sevgilinin kaşıdır. Aşığın kalbine fırlatılacak oklar bu yaydan çıkar.",
    "Ok / Tir / Müje": "Sevgilinin kirpikleridir. Aşığın kalbine saplanan birer oktur.",
    "Servi / Ar'ar": "Sevgilinin boyudur. Uzun, düzgün, endamlı ve kusursuzdur.",
    "Ay / Mah": "Sevgilinin yüzüdür. Parlaktır, etrafına ışık saçar, kusursuz bir güzelliği vardır.",
    "Bade / Şarap": "İlahi aşk veya sevgilinin aşkıyla sarhoş olma durumudur.",
    "Zenehdan / Çah": "Sevgilinin çenesindeki çukurdur (gamze). Aşığın içine düşüp hapsolduğu bir kuyudur."
}

arama = st.text_input("🔍 Mazmun ara:", "")

if arama:
    bulunan = {k: v for k, v in mazmunlar.items() if arama.lower() in k.lower() or arama.lower() in v.lower()}
    if bulunan:
        st.success(f"✅ {len(bulunan)} sonuç bulundu!")
        for m, aciklama in bulunan.items():
            st.subheader(m)
            st.write(aciklama)
    else:
        st.error("❌ Bu mazmun bulunamadı.")
else:
    st.write("### Tüm Mazmunlar")
    for m, aciklama in mazmunlar.items():
        st.subheader(m)
        st.write(aciklama)