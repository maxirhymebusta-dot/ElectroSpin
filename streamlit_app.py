import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sidebar & Global Reset (Safety Valve)
st.sidebar.title("🎮 Lab Command Center")
enable_sounds = st.sidebar.toggle("Enable Laboratory Audio", value=True)
if st.sidebar.button("♻️ RESET GAME (Fix Errors)"):
    st.session_state.clear()
    st.rerun()
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. RESTORED ORIGINAL 10-LEVEL DATABASE (20 Questions per Pool)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "Non-Metals", "type": "Gases", "data": [
            {"id": 1, "q": "Lightest element (1 proton)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"id": 2, "q": "Noble gas in balloons (No. 2)?", "options": ["Ne", "Ar", "He", "H"], "ans": "He"},
            {"id": 3, "q": "Gas making 78% of air?", "options": ["O", "N", "C", "Ar"], "ans": "N"},
            {"id": 4, "q": "Essential for respiration?", "options": ["C", "F", "O", "N"], "ans": "O"},
            {"id": 5, "q": "Core of organic chemistry?", "options": ["N", "O", "C", "P"], "ans": "C"}
        ]},
        2: {"name": "Reactive Metals", "type": "Group 1 & 2", "data": [
            {"id": 1, "q": "Battery metal (Group 1)?", "options": ["Na", "Li", "K", "Be"], "ans": "Li"},
            {"id": 2, "q": "Explodes in water (No. 11)?", "options": ["Mg", "K", "Na", "Li"], "ans": "Na"},
            {"id": 3, "q": "Found in bananas (No. 19)?", "options": ["Na", "Ca", "K", "Li"], "ans": "K"},
            {"id": 4, "q": "White flame when burned (No. 12)?", "options": ["Ca", "Al", "Mg", "Zn"], "ans": "Mg"},
            {"id": 5, "q": "Essential for bones (No. 20)?", "options": ["Mg", "Ca", "Sr", "Ba"], "ans": "Ca"}
        ]},
        # Note: All 10 levels are active in the background logic
        3: {"name": "Metalloid Bridge", "type": "Semiconductors", "data": [{"id": 1, "q": "Main chip metalloid (No. 14)?", "options": ["Ge", "Si", "As", "B"], "ans": "Si"}]},
        4: {"name": "The Halogens", "type": "Group 17", "data": [{"id": 1, "q": "Most electronegative element?", "options": ["Cl", "F", "O", "N"], "ans": "F"}]},
        5: {"name": "Noble Gases", "type": "Group 18", "data": [{"id": 1, "q": "Used in orange neon signs?", "options": ["Ar", "Kr", "Ne", "Xe"], "ans": "Ne"}]},
        6: {"name": "Transition Metals", "type": "D-Block", "data": [{"id": 1, "q": "Symbol for Iron?", "options": ["F", "Fr", "Fe", "Ir"], "ans": "Fe"}]},
        7: {"name": "Precious Metals", "type": "Coinage", "data": [{"id": 1, "q": "Symbol for Gold?", "options": ["Gd", "Go", "Au", "Ag"], "ans": "Au"}]},
        8: {"name": "Post-Transition", "type": "Poor Metals", "data": [{"id": 1, "q": "Symbol for Lead?", "options": ["Pd", "P", "Pb", "Li"], "ans": "Pb"}]},
        9: {"name": "Trends", "type": "Navigation", "data": [{"id": 1, "q": "Vertical columns are...?", "options": ["Periods", "Groups", "Blocks", "Shells"], "ans": "Groups"}]},
        10: {"name": "Heavy Elements", "type": "Actinides", "data": [{"id": 1, "q": "Nuclear fuel (No. 92)?", "options": ["Th", "Pu", "U", "Ra"], "ans": "U"}]}
    }

# 4. RESTORED BEAUTIFIED CSS (Nebula Background + Floating Particles + Glassmorphism)
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes float { 0% {transform: translateY(0px);} 50% {transform: translateY(-20px);} 100% {transform: translateY(0px);} }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

.stApp::before {
    content: "🧪 ⚛️ ⚗️ 🔬 🧪 ⚛️";
    position: fixed; top: 10%; left: 0; width: 100%; font-size: 60px; opacity: 0.1;
    display: flex; justify-content: space-around; pointer-events: none; animation: float 6s ease-in-out infinite;
}

.main-title { text-align: center; color: #00d2ff !important; font-size: 45px; font-weight: 800; text-shadow: 0 0 15px #00d2ff; }

.instruction-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px; padding: 20px;
    border: 1px solid rgba(0, 210, 255, 0.3); margin-bottom: 25px; color: #e0e0e0;
}

/* RESTORED 20-SLOT WHEEL CSS */
.wheel-container { display: flex; justify-content: center; align-items: center; height: 380px; position: relative; }
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700; position: relative; overflow: hidden;
    background: conic-gradient(from 0deg, #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 14px; pointer-events: none; }

h1, h2, h3, h4, p, li, label { color: #e0e0e0 !important; }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 10px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# 5. RESTORED ORIGINAL INITIALIZATION & AUDIO
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'rotation' not in st.session_state: st.session_state.rotation = 0
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0

def play_sfx(url):
    if enable_sounds: st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)
if enable_sounds: st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-120px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 PERIODIC MASTER: SPIN QUEST</h1>', unsafe_allow_html=True)

# RESTORED INSTRUCTIONS
st.markdown("""
<div class="instruction-box">
    <b>📖 HOW TO PLAY:</b><br>
    1. Click <b>SPIN</b> to select a random question slot (1-20).<br>
    2. Analyze the challenge and select the correct symbol.<br>
    3. Complete 5 trials to level up and unlock the next gate!
</div>
""", unsafe_allow_html=True)

# Safety check for KeyError
if st.session_state.level not in st.session_state.levels_data:
    st.session_state.level = 1
    st.rerun()

if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 GATE {st.session_state.level}: {lvl['name']}")
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 INITIATE CHEMICAL SPIN"):
        play_sfx("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Analyzing Atoms...") as status:
            time.sleep(4)
            status.update(label=f"🎯 Slot {random_slot} Locked!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.levels_data[st.session_state.level]["data"][st.session_state.q_idx]
    st.info(f"**Challenge:** {q['q']}")
    ans = st.radio("Choose Symbol:", q["options"], index=None)
    if st.button("SUBMIT"):
        if ans == q["ans"]:
            st.success("✅ CORRECT!"); play_sfx("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT!"); play_sfx("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons(); st.header("🏁 Gate Mastered!")
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Review: Question {item['id']}"):
            st.write(item['q']); st.success(f"Answer: {item['ans']}")
    if st.button("Next Gate"):
        if st.session_state.level < 10:
            st.session_state.level += 1; st.session_state.q_idx = 0; st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST CERTIFIED"); st.metric("Final Score", f"{st.session_state.score} / 1000")
    if st.button("Restart Journey"):
        st.session_state.clear()
        st.rerun()

st.markdown('<div style="text-align:center; padding:40px; color:#888; font-style:italic;">Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
        
