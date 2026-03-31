import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
enable_sounds = st.sidebar.toggle("Enable Laboratory Audio", value=True)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. Full 10-Level Database (Ensuring all levels are defined)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "Non-Metals", "type": "SS1 Core", "data": [
            {"id": 1, "q": "Lightest element in the universe (1 proton)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"id": 2, "q": "Noble gas used in balloons (Atomic No. 2)?", "options": ["Ne", "Ar", "He", "H"], "ans": "He"},
            {"id": 3, "q": "Gas making up 78% of Earth's atmosphere?", "options": ["O", "N", "C", "Ar"], "ans": "N"},
            {"id": 4, "q": "Element essential for human respiration?", "options": ["C", "F", "O", "N"], "ans": "O"},
            {"id": 5, "q": "The primary basis of all organic chemistry?", "options": ["N", "O", "C", "P"], "ans": "C"}
        ]},
        2: {"name": "Reactive Metals", "type": "Groups 1 & 2", "data": [
            {"id": 1, "q": "Group 1 metal used in phone batteries?", "options": ["Na", "Li", "K", "Be"], "ans": "Li"},
            {"id": 2, "q": "Atomic Number 11: Explodes in water?", "options": ["Mg", "K", "Na", "Li"], "ans": "Na"},
            {"id": 3, "q": "Found in bananas, Atomic Number 19?", "options": ["Na", "Ca", "K", "Li"], "ans": "K"},
            {"id": 4, "q": "Atomic Number 12: Burns with bright white light?", "options": ["Ca", "Al", "Mg", "Zn"], "ans": "Mg"},
            {"id": 5, "q": "Essential for bone strength (No. 20)?", "options": ["Mg", "Ca", "Sr", "Ba"], "ans": "Ca"}
        ]},
        # Note: Add levels 3-10 here following the same format
    }

# 4. STABLE GAME CSS (Fixed Blank Screen Issue)
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes float { 0% {transform: translateY(0px);} 50% {transform: translateY(-20px);} 100% {transform: translateY(0px);} }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

/* Floating Particle Layer */
.stApp::before {
    content: "🧪 ⚛️ ⚗️ 🔬";
    position: fixed; top: 15%; left: 0; width: 100%; font-size: 50px; opacity: 0.1;
    display: flex; justify-content: space-around; pointer-events: none; animation: float 6s ease-in-out infinite;
}

.main-title { text-align: center; color: #00d2ff !important; font-size: 42px; font-weight: 800; text-shadow: 0 0 10px #00d2ff; }

/* Glassmorphism Containers */
.stExpander, .stMarkdown, .stStatus {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 15px !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.wheel-container { display: flex; justify-content: center; align-items: center; height: 350px; position: relative; }
.wheel {
    width: 280px; height: 280px; border-radius: 50%; border: 8px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(from 0deg, #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 15px; width: 0; height: 0; border-left: 18px solid transparent; border-right: 18px solid transparent; border-top: 40px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 14px; pointer-events: none; }
h1, h2, h3, h4, p, li, label { color: #e0e0e0 !important; }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 10px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# 5. Audio and Session State
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0

def play_sound(url):
    if enable_sounds:
        st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

if enable_sounds:
    st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-110px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 PERIODIC MASTER: SPIN QUEST</h1>', unsafe_allow_html=True)

if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 GATE {st.session_state.level}: {lvl['name']}")
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    if st.button("🚀 SPIN FOR A CHALLENGE"):
        play_sound("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Analyzing Elements...") as status:
            time.sleep(4)
            status.update(label=f"🎯 Target Locked!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.levels_data[st.session_state.level]["data"][st.session_state.q_idx]
    st.subheader("🔍 Hidden Element Challenge")
    st.info(f"**Description:** {q['q']}")
    ans = st.radio("Chemical Symbol?", q["options"], index=None)
    if st.button("SUBMIT"):
        if ans == q["ans"]:
            st.success("✅ CORRECT!"); play_sound("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT!"); play_sound("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons(); st.header("🏁 Level Mastery Complete!")
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Review: Question {item['id']}"):
            st.write(item['q']); st.success(f"Fact: {item['ans']}")
    if st.button("Next Chemical Gate"):
        if st.session_state.level < len(st.session_state.levels_data):
            st.session_state.level += 1; st.session_state.q_idx = 0; st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST CERTIFIED"); st.metric("Final Score", f"{st.session_state.score} / 1000")
    if st.button("Restart Journey"):
        st.session_state.level = 1; st.session_state.score = 0; st.session_state.q_idx = 0; st.session_state.mode = "spin"; st.rerun()

st.markdown('<div style="text-align:center; padding:40px; color:#888; font-style:italic;">Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
        
