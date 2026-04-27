import streamlit as st
import random
import urllib.parse

# --- KONFIGURACJA ---
st.set_page_config(page_title="SIEDLIK SYSTEM RA", page_icon="⚡")

# --- STYLE ---
st.markdown("""
    <style>
    .main { background-color: #000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { width: 100%; background-color: #ff0055; color: white; border-radius: 10px; }
    .result-box { background-color: #111; border: 2px solid #00ff41; padding: 20px; border-radius: 15px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ SIEDLIK SYSTEM RA 6.5")
lang = st.radio("JĘZYK / LANGUAGE:", ("POLSKI", "ENGLISH"), horizontal=True)

# --- LOGIKA BAZY ---
osoby = ["AKU", "KAMU", "DIA", "KAMI", "MEREKA"]
czasy = ["RAO", "RAO LAGI", "RAI", "RAI LAGI", "RAU", "RAU LAGI"]
slowa = ["Makan", "Minum", "Pergi", "Tidur", "Beli", "Mandi", "Jalan", "Sakit", "Tolong"]

if st.button("🚀 GENERUJ HACK / GENERATE"):
    res = f"{random.choice(osoby)} {random.choice(czasy)} {random.choice(slowa)}"
    st.markdown(f"<div class='result-box'><h1>{res}</h1></div>", unsafe_allow_html=True)
    
    # Audio
    query = urllib.parse.quote(res)
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={query}&tl=id&client=tw-ob"
    st.markdown(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', unsafe_allow_html=True)

# --- SEKCJA PDF ---
st.write("---")
kod = st.text_input("ODBLOKUJ PDF (WPISZ HASŁO):", type="password")
if kod == "RA2024":
    st.success("DOSTĘP PRZYZNANY!")
    st.markdown('< style="color:#00ff41;" href="LINK_DO_TWOJEGO_PDF">Pobierz Pełny System PDF</a>', unsafe_allow_html=True)

st.caption("Siedlik System RA © 2024")
