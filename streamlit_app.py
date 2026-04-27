
import streamlit as st
import random
import time
import base64
from datetime import datetime
from gtts import gTTS
from io import BytesIO

# --- SIEDLIK SYSTEM RA 8.5 INFINITY ENGINE ---
st.set_page_config(page_title="SIEDLIK RA 8.5 INFINITY", page_icon="⚡", layout="wide")

# --- CYBER-HUD DESIGN (CUSTOM CSS) ---
st.markdown("""
    <style>
   .stApp {
        background-color: #0a0a0f;
        background-image: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                          linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        background-size: 100% 4px, 6px 100%;
        color: #00f0ff;
        font-family: 'Courier New', monospace;
    }
   .neon-title {
        color: #fff;
        text-shadow: 0 0 7px #fff, 0 0 10px #fff, 0 0 42px #00f0ff, 0 0 82px #00f0ff;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
   .cyber-card {
        background-color: rgba(10, 2, 30, 0.85);
        border: 2px solid #00f0ff;
        padding: 20px;
        box-shadow: 0 0 15px #00f0ff;
        clip-path: polygon(0 15px, 15px 0, 100% 0, 100% calc(100% - 15px), calc(100% - 15px) 100%, 0 100%);
    }
   .stButton>button {
        background: transparent;
        border: 2px solid #39ff14;
        color: #39ff14;
        text-shadow: 0 0 5px #39ff14;
        font-weight: bold;
        width: 100%;
        height: 60px;
        text-transform: uppercase;
        transition: 0.4s;
    }
   .stButton>button:hover {
        background: #39ff14;
        color: black;
        box-shadow: 0 0 40px #39ff14;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALIZATION ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'logs' not in st.session_state: st.session_state.logs =

# --- 300 CORES DATABASE (BAZA MOCY) ---
cores = {
    "BIOLOGIA/SURVIVAL": {"Makan": "Jeść", "Minum": "Pić", "Tidur": "Spać", "Bisa": "Móc", "Tahu": "Wiedzieć"},
    "LOGISTYKA/MIASTO": {"Pergi": "Iść", "Datang": "Przyjść", "Naik": "Wsiadać", "Turun": "Wysiadać", "Belok": "Skręcać"},
    "STATUS/EMOCJE": {"Bagus": "Fajne", "Mahal": "Drogie", "Murah": "Tanie", "Sakit": "Boli", "Sayang": "Kochać/Troska"}
}

# --- SIDEBAR: OPERATOR STATUS ---
with st.sidebar:
    st.markdown("### 🖥️ DASHBOARD")
    st.write(f"🔥 STREAK: {st.session_state.get('streak', 1)} DNI")
    st.progress(st.session_state.xp % 100 / 100)
    st.write(f"SYNCHRONIZACJA XP: {st.session_state.xp}")
    lang_mode = st.radio("INTERFACE:",)

# --- HEADER ---
st.markdown('<div class="neon-title">⚡ SIEDLIK RA 8.5 INFINITY ⚡</div>', unsafe_allow_html=True)

# --- OPERATIONAL PANEL ---
st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: sub = st.selectbox("SUBJECT",)
with col2: wak = st.selectbox("TIME ENGINE",)
with col3: kat = st.selectbox("CATEGORY", list(cores.keys()))

kata_sel = st.selectbox("ACTION / CORE WORD", list(cores[kat].keys()))

if st.button("🚀 EXECUTE REVOLUTION CODE"):
    t_code = wak.split(" ")
    res = f"{sub} {t_code} {kata_sel}"
    st.session_state.xp += 10
    st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M')}] Decoded: {res}")
    
    # TTS Autoplay Engine
    tts = gTTS(text=res, lang='id')
    fp = BytesIO()
    tts.write_to_fp(fp)
    b64 = base64.b64encode(fp.getvalue()).decode()
    st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}"></audio>', unsafe_allow_html=True)
    st.success(f"### SYSTEM OUTPUT: {res}")
st.markdown('</div>', unsafe_allow_html=True)

# --- CRISIS & GPS ---
st.write("")
cs1, cs2 = st.columns(2)
with cs1:
    if st.button("🚨 TRIGGER SOS"):
        st.error("!!! SOS BROADCAST: TOLONG!!!")
        st.markdown('<audio autoplay src="https://translate.google.com/translate_tts?ie=UTF-8&q=Tolong+Sakit&tl=id&client=tw-ob"></audio>', unsafe_allow_html=True)
with cs2:
    if st.button("📍 GPS PING"):
        st.code("Lat: -6.2088, Lon: 106.8456 (HQ JAKARTA)")
        st.toast("Lokalizacja pobrana.", icon="📍")

# --- TERMINAL LOGS ---
st.write("---")
st.markdown("### 📡 SYSTEM LOGS (LIVE)")
log_box = "<br>".join(st.session_state.logs[-5:])
st.markdown(f'<div style="background:#050505; border-left:4px solid #ff00ff; padding:15px; color:#ff00ff; font-size:0.9em;">{log_box}</div>', unsafe_allow_html=True)
