
import streamlit as st
import random
import time
from datetime import datetime, timedelta

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="SIEDLIK SYSTEM RA 8.5 INFINITY", page_icon="⚡", layout="wide")

# --- DESIGN CSS ---
st.markdown("""
<style>
    .stApp { background: #000; color: #00ffcc; font-family: 'Courier New', monospace; }
    .neon-text { text-align: center; color: #00ffcc; text-shadow: 0 0 15px #00ffcc; }
    .neon-box { border: 2px solid #00ffcc; padding: 20px; border-radius: 15px; background: rgba(0, 255, 204, 0.05); }
    .stButton>button { background: linear-gradient(90deg, #00ffcc, #0088ff); color: black; font-weight: bold; border-radius: 10px; height: 50px; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- PAMIĘĆ ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'logs' not in st.session_state: st.session_state.logs = ["[SYSTEM] RA 8.5 Booting..."]

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## 🛡️ COMMANDER")
    st.progress(st.session_state.xp / 100)
    st.write(f"Level: {st.session_state.xp}%")
    lang = st.radio("JĘZYK", ["ID", "PL", "EN"])

# --- HEADER ---
st.markdown('<h1 class="neon-text">⚡ SIEDLIK SYSTEM RA 8.5 INFINITY ⚡</h1>', unsafe_allow_html=True)

# --- GENERATOR ---
st.markdown('<div class="neon-box">', unsafe_allow_html=True)
subjekty = ["AKU", "KAMU", "DIA", "KITA"]
czasy = ["RAI", "RAO", "LAGI", "SUDAH"]
akcje = ["Makan", "Minum", "Tidur", "Jalan", "Bypass", "Scan"]

c1, c2, c3 = st.columns(3)
with c1: s_sub = st.selectbox("SUBJECT", subjekty)
with c2: s_tme = st.selectbox("TIME", czasy)
with c3: s_akc = st.selectbox("ACTION", akcje)

if st.button("🚀 EXECUTE"):
    res = f"{s_sub} {s_tme} {s_akc}"
    st.success(f"### {res}")
    st.session_state.xp = min(100, st.session_state.xp + 5)
    st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M')}] {res}")
    # Audio
    tl = lang.lower() if lang != "ID" else "id"
    st.markdown(f'<audio autoplay src="[https://translate.google.com/translate_tts?ie=UTF-8&q=](https://translate.google.com/translate_tts?ie=UTF-8&q=){res}&tl={tl}&client=tw-ob"></audio>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- LOGI ---
st.write("---")
st.code("\n".join(st.session_state.logs[-5:]))
