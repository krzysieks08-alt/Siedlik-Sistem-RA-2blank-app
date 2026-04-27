```python
import streamlit as st
import random
import time
from datetime import datetime, timedelta

# --- KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="SIEDLIK SYSTEM RA 8.5 INFINITY",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ZAAWANSOWANY DESIGN CSS (HAKERSKI LOOK + ANIMACJE) ---
st.markdown("""
<style>
    /* Główny motyw */
    .stApp {
        background: #000000;
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Neonowe napisy */
    .neon-text {
        text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
        color: #00ffcc;
        text-align: center;
        font-weight: bold;
    }
    
    .crisis-text {
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000;
        color: #ff0000;
        text-align: center;
        animation: blinker 1s linear infinite;
    }
    
    @keyframes blinker {
        50% { opacity: 0; }
    }
    
    /* Stylowanie ramek */
    .neon-box {
        border: 2px solid #00ffcc;
        padding: 20px;
        border-radius: 15px;
        background: rgba(0, 255, 204, 0.05);
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
        margin-bottom: 20px;
    }
    
    .flashcard {
        background: #111;
        border: 1px solid #ff00ff;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: #ff00ff;
        box-shadow: 0 0 10px rgba(255, 0, 255, 0.3);
    }
    
    /* Przyciski */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #00ffcc, #0088ff);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px #00ffcc;
    }
    
    /* Terminal */
    .terminal-window {
        background: #050505;
        border-left: 4px solid #ff00ff;
        padding: 15px;
        color: #ff00ff;
        font-size: 0.85rem;
        border-radius: 5px;
        font-family: 'Consolas', monospace;
    }
</style>
""", unsafe_allow_html=True)

# --- SYSTEM STATE (PAMIĘĆ APLIKACJI) ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'streak' not in st.session_state: st.session_state.streak = 1
if 'last_action' not in st.session_state: st.session_state.last_action = datetime.now().date()
if 'logs' not in st.session_state: st.session_state.logs = ["[SYSTEM] RA 8.5 INFINITY Booting..."]
if 'crisis' not in st.session_state: st.session_state.crisis = False
if 'daily_word' not in st.session_state:
    words = {"Makan": "Jeść", "Minum": "Pić", "Tidur": "Spać", "Jalan": "Iść/Droga", "Cinta": "Miłość", "Beli": "Kupować"}
    st.session_state.daily_word = random.choice(list(words.items()))

# --- LOGIKA PASSY (STREAK GUARD) ---
today = datetime.now().date()
if today > st.session_state.last_action + timedelta(days=1):
    st.session_state.streak = 0
    st.session_state.xp = max(0, st.session_state.xp - 10)

# --- SIDEBAR (COMMAND CENTER) ---
with st.sidebar:
    st.markdown('<h2 class="neon-text">COMMAND CENTER</h2>', unsafe_allow_html=True)
    st.metric("STREAK 🔥", f"{st.session_state.streak} DAYS")
    st.write("---")
    st.subheader("📊 SYNCHRONIZATION")
    st.progress(st.session_state.xp / 100)
    st.write(f"Experience Level: {st.session_state.xp}%")
    
    st.write("---")
    st.subheader("🌐 LANGUAGE PROTOCOL")
    lang = st.radio("Select Output Language:", ["Indonesian", "Polish", "English"])
    
    st.write("---")
    if st.button("💾 SAVE DAILY PROGRESS"):
        st.session_state.last_action = today
        st.session_state.streak += 1
        st.session_state.xp = min(100, st.session_state.xp + 10)
        st.toast("Progress Synchronized!", icon="🛡️")

# --- NAGŁÓWEK ---
if st.session_state.crisis:
    st.markdown('<h1 class="crisis-text">⚠️ SYSTEM CRISIS: LOCKDOWN ACTIVE ⚠️</h1>', unsafe_allow_html=True)
else:
    st.markdown('<h1 class="neon-text">⚡ SIEDLIK SYSTEM RA 8.5 INFINITY ⚡</h1>', unsafe_allow_html=True)

# --- DANE BAZOWE ---
subjekty = ["AKU", "KAMU", "DIA", "KITA", "MEREKA"]
czasy = ["RAI", "RAO", "LAGI", "SUDAH"]
kategorie = {
    "🛠️ CORE": ["Makan", "Minum", "Tidur", "Lari", "Mandi"],
    "💻 HACK": ["Bypass", "Decrypt", "Link", "Scan", "Analyze"],
    "🔥 SOCIAL": ["Bicara", "Cinta", "Dengar", "Bantu", "Teman"]
}
crisis_actions = ["SOS", "HELP", "ESCAPE", "LOCKDOWN", "REBOOT"]

# --- MODUŁY SPECJALNE (FISZKI I GPS) ---
col_f1, col_f2 = st.columns([2, 1])

with col_f1:
    st.markdown("### 🗂️ DAILY FLASHCARD (Bonus XP)")
    word, trans = st.session_state.daily_word
    st.markdown(f'<div class="flashcard"><h2>{word}</h2><p>Znaczenie: {trans}</p></div>', unsafe_allow_html=True)

with col_f2:
    st.markdown("### 📍 GPS PING")
    if st.button("GET LOCATION"):
        st.code("Lat: -6.2088, Lon: 106.8456\nJAKARTA CORE")
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M')}] GPS Signal Acquired.")

# --- GŁÓWNY INTERFEJS GENERATORA ---
st.write("---")
st.markdown('<div class="neon-box">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: s_sub = st.selectbox("USER ID (Subjek)", subjekty)
with c2: s_tme = st.selectbox("TIME UNIT (Waktu)", czasy)
with c3: s_kat = st.selectbox("PROTOCOL (Kategoria)", list(kategorie.keys()))

voice_cmd = st.text_input("🎤 VOICE INPUT / SEARCH", placeholder="Wpisz lub powiedz komendę...")

if st.button("🚀 EXECUTE GENERATION"):
    akcja = voice_cmd if voice_cmd else random.choice(kategorie[s_kat])
    wynik = f"{s_sub} {s_tme} {akcja}"
    st.session_state.crisis = False
    
    st.success(f"### WYNIK: {wynik}")
    st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M')}] Generated: {wynik}")
    st.session_state.xp = min(100, st.session_state.xp + 5)
    
    # Audio TTS
    tl_code = "id" if lang == "Indonesian" else "pl" if lang == "Polish" else "en"
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={wynik}&tl={tl_code}&client=tw-ob"
    st.markdown(f'<audio autoplay src="{audio_url}"></audio>', unsafe_allow_html=True)
    st.toast("Packet Sent Successfully!", icon="✅")

st.markdown('</div>', unsafe_allow_html=True)

# --- SYTUACJE KRYZYSOWE I CZAT ---
col_c1, col_c2 = st.columns(2)

with col_c1:
    st.subheader("🚨 EMERGENCY PROTOCOL")
    if st.button("🔴 TRIGGER CRISIS MODE"):
        st.session_state.crisis = True
        akcja_c = random.choice(crisis_actions)
        wynik_c = f"ALERT {s_sub} {akcja_c}"
        st.error(f"### {wynik_c}")
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M')}] !! CRISIS TRIGGERED !!")
        # Audio alarmowe (zawsze PL dla uwagi)
        st.markdown(f'<audio autoplay src="https://translate.google.com/translate_tts?ie=UTF-8&q={wynik_c}&tl=pl&client=tw-ob"></audio>', unsafe_allow_html=True)

with col_c2:
    st.subheader("💬 BASE CHAT (Simulated)")
    st.text_area("Live Data Stream:", value="[Base]: Connection Secure.\n[Base]: Monitoring your streak...\n[Base]: Ready for instructions.", height=120)

# --- TERMINAL LOGÓW ---
st.write("---")
st.markdown("### 📡 SYSTEM LOGS (Live History)")
log_display = "<br>".join(st.session_state.logs[-5:])
st.markdown(f'<div class="terminal-window">{log_display}</div>', unsafe_allow_html=True)

# --- SEKRETNY DOSTĘP PDF ---
st.write("---")
with st.expander("🔑 ENCRYPTED DATA SECTOR"):
    pass_key = st.text_input("Authorization Key", type="password")
    if pass_key == "RA2024":
        st.balloons()
        st.success("ACCESS GRANTED - SECURE FILES UNLOCKED")
        st.markdown("📂 [DOWNLOAD RA 8.5 DOCUMENTATION](https://example.com/your-file.pdf)")

# --- STOPKA ---
st.markdown("<p style='text-align: center; color: #333;'>RA 8.5 INFINITY | Language Revolution Protocol</p>", unsafe_allow_html=True)

```
