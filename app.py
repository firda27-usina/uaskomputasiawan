
import streamlit as st
import base64
from pathlib import Path

# =====================================================
# 1. KONFIGURASI
# =====================================================

st.set_page_config(
    page_title="AquaFCR - Budidaya Ikan",
    page_icon="🐟",
    layout="wide"
)

# =====================================================
# 2. MEMBACA GAMBAR BACKGROUND
# =====================================================


image_path = Path(__file__).parent / "underwater.jpg"

try:
    encoded_image = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    background_image = (
        f'url("data:image/jpeg;base64,{encoded_image}")'
    )

except FileNotFoundError:
    background_image = (
        "linear-gradient(135deg, #38BFD5, #075985)"
    )
    st.warning("Gambar underwater.jpg tidak ditemukan.")

except PermissionError:
    st.error(
        "Windows menolak akses gambar. "
        "Periksa izin file underwater.jpg."
    )
    st.stop()


# =====================================================
# 3. BACKGROUND AQUA + ANIMASI IKAN
# =====================================================

animation_html = """
<style>

/* BACKGROUND UTAMA */
.stApp {
    background: #B9F3F5 !important;
    position: relative;
    isolation: isolate;
}

/* FOTO BAWAH LAUT */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;

    background-image:
        linear-gradient(
            rgba(0, 105, 140, 0.38),
            rgba(0, 120, 150, 0.38)
        ),
        __BACKGROUND_IMAGE__;

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    filter: blur(6px);
    transform: scale(1.03);
}

/* LAPISAN ANIMASI */
.fish-background {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    pointer-events: none;
    z-index: 0;
}

/* IKAN */
.swimming-fish {
    position: absolute;
    white-space: nowrap;
    opacity: 0.75;
    font-size: 36px;
}

/* IKAN KE KANAN */
.fish1 {
    top: 15%;
    left: -100px;
    animation: swim-right 28s linear infinite;
}

.fish2 {
    top: 40%;
    left: -100px;
    font-size: 28px;
    animation: swim-right 35s linear infinite;
    animation-delay: -12s;
}

.fish3 {
    top: 75%;
    left: -100px;
    font-size: 42px;
    animation: swim-right 32s linear infinite;
    animation-delay: -20s;
}

/* IKAN KE KIRI */
.fish4 {
    top: 28%;
    right: -100px;
    animation: swim-left 30s linear infinite;
    animation-delay: -8s;
}

.fish5 {
    top: 60%;
    right: -100px;
    font-size: 30px;
    animation: swim-left 38s linear infinite;
    animation-delay: -15s;
}

/* ANIMASI IKAN */
@keyframes swim-right {
    0% {
        transform: translateX(0);
    }
    50% {
        transform: translateX(55vw) translateY(-18px);
    }
    100% {
        transform: translateX(110vw) translateY(12px);
    }
}

@keyframes swim-left {
    0% {
        transform: translateX(0) scaleX(-1);
    }
    50% {
        transform: translateX(-55vw) translateY(15px) scaleX(-1);
    }
    100% {
        transform: translateX(-110vw) translateY(-12px) scaleX(-1);
    }
}

/* GELEMBUNG AIR */
.bubble {
    position: absolute;
    bottom: -30px;
    width: 12px;
    height: 12px;
    border: 2px solid rgba(255,255,255,0.8);
    border-radius: 50%;
    animation: bubble-up 12s linear infinite;
}

.bubble1 { left: 15%; }
.bubble2 { left: 35%; animation-delay: 3s; }
.bubble3 { left: 55%; animation-delay: 6s; }
.bubble4 { left: 75%; animation-delay: 2s; }
.bubble5 { left: 90%; animation-delay: 5s; }

@keyframes bubble-up {
    0% {
        transform: translateY(0);
        opacity: 0;
    }
    20% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-110vh);
        opacity: 0;
    }
}

/* KONTEN UTAMA */
.block-container {
    position: relative;
    z-index: 1;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* JUDUL */
h1 {
    color: #075985 !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #0F766E !important;
    font-weight: 700 !important;
}

/* KARTU METRIK */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.82);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.7);
    border-left: 5px solid #0891B2;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 8px 25px rgba(0,60,90,0.12);
}

/* INPUT */
.stNumberInput input {
    border-radius: 10px;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}

/* TOMBOL */
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

.stButton > button:hover {
    background: #075985;
    color: white;
    transform: scale(1.02);
}

/* ALERT */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* PEMBATAS */
hr {
    border-color: rgba(255,255,255,0.7);
}

.stApp {
    background: transparent !important;
}

[data-testid="stAppViewContainer"] {
    position: relative;
    z-index: 1;
}

[data-testid="stMain"] {
    position: relative;
    z-index: 2;
}

h1, h2, h3 {
    color: #FFFFFF !important;
    text-shadow: 0 2px 8px rgba(0, 25, 45, 0.7);
}

p {
    color: #E5F7FF !important;
}

label,
[data-testid="stWidgetLabel"] p {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

[data-testid="stNumberInput"],
[data-testid="stSelectbox"] {
    border-radius: 12px;
}

[data-testid="stWidgetLabel"] {
    text-shadow: 0 1px 5px rgba(0, 20, 40, 0.8);
}

/* KARTU HASIL PERHITUNGAN */
[data-testid="stMetric"] {
    background: rgba(4, 43, 65, 0.88) !important;
    border: 1px solid rgba(53, 214, 207, 0.7);
    border-left: 6px solid #35D6CF;
    border-radius: 18px;
    padding: 24px !important;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.2);
}

/* LABEL METRIK */
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: #BDEFFF !important;
    font-weight: 600 !important;
}

/* ANGKA HASIL */
[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

</style>

<div class="fish-background">

    <div class="swimming-fish fish1">🐟</div>
    <div class="swimming-fish fish2">🐠</div>
    <div class="swimming-fish fish3">🐟</div>
    <div class="swimming-fish fish4">🐠</div>
    <div class="swimming-fish fish5">🐟</div>

    <div class="bubble bubble1"></div>
    <div class="bubble bubble2"></div>
    <div class="bubble bubble3"></div>
    <div class="bubble bubble4"></div>
    <div class="bubble bubble5"></div>

</div>
"""

animation_html = animation_html.replace(
    "__BACKGROUND_IMAGE__",
    background_image
)

st.html(animation_html)

# =====================================================
# 4. HEADER APLIKASI
# =====================================================

st.title("🐟 AquaFCR")

st.subheader(
    "Aplikasi Perhitungan Feed Conversion Ratio"
)

st.write(
    "Aplikasi untuk membantu menghitung dan mengevaluasi "
    "efisiensi penggunaan pakan dalam kegiatan budidaya ikan."
)

st.divider()

# =====================================================
# 5. INPUT DATA BUDIDAYA
# =====================================================

st.subheader("📋 Data Budidaya Ikan")

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
# 6. PERHITUNGAN FCR
# =====================================================

if st.button("🐟 HITUNG FCR", type="primary"):

    pertambahan_biomassa = (
        biomassa_akhir - biomassa_awal
    )

    # VALIDASI DATA

    if biomassa_akhir <= biomassa_awal:

        st.error(
            "Biomassa akhir harus lebih besar "
            "daripada biomassa awal!"
        )

        st.stop()

    if total_pakan <= 0:

        st.error(
            "Total pakan harus lebih dari 0 kg!"
        )

        st.stop()

    # PERHITUNGAN

    fcr = total_pakan / pertambahan_biomassa

    pertumbuhan_harian = (
        pertambahan_biomassa / lama_budidaya
    )

    berat_awal = (
        biomassa_awal * 1000 / jumlah_ikan
    )

    berat_akhir = (
        biomassa_akhir * 1000 / jumlah_ikan
    )

    # =================================================
    # 7. HASIL PERHITUNGAN
    # =================================================

    st.success(
        "Perhitungan FCR berhasil dilakukan!"
    )

    st.subheader("📊 Hasil Perhitungan")

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
    # 8. INTERPRETASI FCR
    # =================================================

    st.subheader("🔎 Interpretasi Nilai FCR")

    if fcr <= 1.0:

        st.success(
            "FCR sangat baik. Penggunaan pakan "
            "relatif efisien berdasarkan pertambahan biomassa."
        )

    elif fcr <= 1.5:

        st.success(
            "FCR baik. Penggunaan pakan tergolong efisien."
        )

    elif fcr <= 2.0:

        st.info(
            "FCR cukup baik. Efisiensi penggunaan "
            "pakan masih dapat ditingkatkan."
        )

    else:

        st.warning(
            "FCR kurang efisien. Perlu evaluasi "
            "pemberian pakan dan kondisi budidaya."
        )

    st.caption(
        "Catatan: Kategori interpretasi merupakan panduan umum. "
        "Standar FCR dapat berbeda berdasarkan jenis ikan, "
        "jenis pakan, dan sistem budidaya."
    )

    # =================================================
    # 9. RINGKASAN DATA
    # =================================================

    st.divider()

    st.subheader("📑 Ringkasan Data Budidaya")

    st.write(f"**Jenis Ikan:** {jenis_ikan}")

    st.write(
        f"**Jumlah Ikan:** {jumlah_ikan} ekor"
    )

    st.write(
        f"**Total Pakan:** {total_pakan:.2f} kg"
    )

    st.write(
        f"**Biomassa Awal:** {biomassa_awal:.2f} kg"
    )

    st.write(
        f"**Biomassa Akhir:** {biomassa_akhir:.2f} kg"
    )

    st.write(
        f"**Pertambahan Biomassa:** "
        f"{pertambahan_biomassa:.2f} kg"
    )

    st.write(
        f"**Lama Budidaya:** {lama_budidaya} hari"
    )

    st.write(
        f"**Nilai FCR:** {fcr:.2f}"
    )

    st.divider()

    st.success(
        "Terima kasih telah menggunakan AquaFCR! 🐟"
    )
