
import streamlit as st

# =====================================================
# KONFIGURASI
# =====================================================

st.set_page_config(
    
# =====================================================
# KONFIGURASI
# =====================================================

st.set_page_config(
    page_title="AquaFCR - Budidaya Ikan",
    page_icon="🐟",
    layout="wide"
)

# =====================================================
# DESAIN DAN WARNA APLIKASI
# =====================================================

st.markdown("""
<style>

/* Background utama */
.stApp {
    background: linear-gradient(
        135deg,
        #E0F7FA 0%,
        #F0FDFA 50%,
        #DBEAFE 100%
    );
}

/* Area konten */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Judul utama */
h1 {
    color: #075985 !important;
    font-weight: 800 !important;
}

/* Subjudul */
h2, h3 {
    color: #0F766E !important;
    font-weight: 700 !important;
}

/* Metric */
[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #0D9488;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

/* Tombol */
.stButton > button {
    background: linear-gradient(
        90deg,
        #0F766E,
        #0891B2
    );
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 25px;
    font-weight: bold;
    transition: 0.3s;
}

/* Efek tombol */
.stButton > button:hover {
    background: #075985;
    color: white;
    border: none;
    transform: scale(1.02);
}

/* Input */
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}

/* Pesan hasil */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Garis pembatas */
hr {
    border-color: #99D5D8;
}

</style>
""", unsafe_allow_html=True)

    
)

st.title("🐟 Aplikasi Perhitungan Feed Conversion Ratio (FCR)")
st.write(
    "Aplikasi untuk menghitung rasio konversi pakan "
    "pada kegiatan budidaya ikan."
)

st.divider()

# =====================================================
# INPUT DATA
# =====================================================

st.subheader("Data Budidaya Ikan")

col1, col2 = st.columns(2)

with col1:

    jenis_ikan = st.selectbox(
        "Jenis Ikan",
        [
            "Ikan Lele",
            "Ikan Nila",
            "Ikan Gurami",
            "Ikan Mas",
            "Ikan Patin",
            "Lainnya"
        ]
    )

    jumlah_ikan = st.number_input(
        "Jumlah Ikan (ekor)",
        min_value=1,
        value=1000,
        step=100
    )

    biomassa_awal = st.number_input(
        "Biomassa Awal (kg)",
        min_value=0.01,
        value=10.0,
        step=1.0
    )

with col2:

    total_pakan = st.number_input(
        "Total Pakan yang Diberikan (kg)",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    biomassa_akhir = st.number_input(
        "Biomassa Akhir (kg)",
        min_value=0.0,
        value=90.0,
        step=1.0
    )

    lama_budidaya = st.number_input(
        "Lama Budidaya (hari)",
        min_value=1,
        value=90,
        step=1
    )

st.divider()

# =====================================================
# PERHITUNGAN FCR
# =====================================================

if st.button("Hitung FCR", type="primary"):

    # ---------------------------------------------
    # Menghitung pertambahan biomassa
    # ---------------------------------------------

    pertambahan_biomassa = biomassa_akhir - biomassa_awal

    # ---------------------------------------------
    # Validasi data
    # ---------------------------------------------

    if biomassa_akhir <= biomassa_awal:

        st.error(
            "Biomassa akhir harus lebih besar "
            "dari biomassa awal!"
        )

        st.stop()

    if total_pakan <= 0:

        st.error("Total pakan harus lebih dari 0 kg!")

        st.stop()

    # ---------------------------------------------
    # Menghitung nilai FCR
    # ---------------------------------------------

    fcr = total_pakan / pertambahan_biomassa

    # ---------------------------------------------
    # Menghitung rata-rata pertumbuhan
    # ---------------------------------------------

    pertumbuhan_harian = (
        pertambahan_biomassa / lama_budidaya
    )

    # ---------------------------------------------
    # Menghitung rata-rata berat ikan
    # ---------------------------------------------

    berat_awal = biomassa_awal * 1000 / jumlah_ikan

    berat_akhir = biomassa_akhir * 1000 / jumlah_ikan

    # =================================================
    # HASIL PERHITUNGAN
    # =================================================

    st.success("Perhitungan FCR berhasil dilakukan!")

    st.subheader("Hasil Perhitungan")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Nilai FCR",
            f"{fcr:.2f}"
        )

        st.metric(
            "Pertambahan Biomassa",
            f"{pertambahan_biomassa:.2f} kg"
        )

    with col2:

        st.metric(
            "Berat Awal per Ikan",
            f"{berat_awal:.2f} gram"
        )

        st.metric(
            "Berat Akhir per Ikan",
            f"{berat_akhir:.2f} gram"
        )

    st.metric(
        "Rata-rata Pertumbuhan Biomassa",
        f"{pertumbuhan_harian:.2f} kg/hari"
    )

    # =================================================
    # INTERPRETASI HASIL
    # =================================================

    st.subheader("Interpretasi Nilai FCR")

    if fcr <= 1.0:

        st.success(
            "FCR sangat baik. Penggunaan pakan relatif "
            "efisien berdasarkan pertambahan biomassa."
        )

    elif fcr <= 1.5:

        st.success(
            "FCR baik. Penggunaan pakan tergolong efisien."
        )

    elif fcr <= 2.0:

        st.info(
            "FCR cukup baik. Penggunaan pakan masih "
            "dapat ditingkatkan efisiensinya."
        )

    else:

        st.warning(
            "FCR kurang efisien. Perlu dilakukan evaluasi "
            "terhadap pemberian pakan dan kondisi budidaya."
        )

    # =================================================
    # RINGKASAN DATA
    # =================================================

    st.divider()

    st.subheader("Ringkasan Data Budidaya")

    st.write(f"**Jenis Ikan:** {jenis_ikan}")

    st.write(f"**Jumlah Ikan:** {jumlah_ikan} ekor")

    st.write(f"**Total Pakan:** {total_pakan:.2f} kg")

    st.write(f"**Biomassa Awal:** {biomassa_awal:.2f} kg")

    st.write(f"**Biomassa Akhir:** {biomassa_akhir:.2f} kg")

    st.write(f"**Lama Budidaya:** {lama_budidaya} hari")

    st.write(f"**Nilai FCR:** {fcr:.2f}")

  
