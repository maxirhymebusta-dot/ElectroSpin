import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="Periodic Master: Spin Quest", page_icon="🧪", layout="wide")

# 2. Sidebar Controls (Sound Toggle)
st.sidebar.title("🎮 Lab Controls")
st.session_state.mute = st.sidebar.toggle("Mute All Sounds", value=False)

# 3. Master Question Bank (20 Elements - Hidden Names)
if 'master_bank' not in st.session_state:
    st.session_state.master_bank = [
        {"name": "Hydrogen", "q": "Which element is the lightest gas with 1 proton?", "options": ["H", "He", "Li", "Be"], "ans": "H"},
        {"name": "Helium", "q": "Which Noble Gas has 2 protons and is used in balloons?", "options": ["H", "He", "Ne", "Ar"], "ans": "He"},
        {"name": "Lithium", "q": "Identify the Group 1 metal with Atomic Number 3.", "options": ["Li", "Na", "K", "Be"], "ans": "Li"},
        {"name": "Beryllium", "q": "Which element has 4 protons and 4 electrons?", "options": ["Li", "Be", "B", "Mg"], "ans": "Be"},
        {"name": "Boron", "q": "The metalloid with Atomic Number 5 used in glass.", "options": ["B", "C", "Si", "Al"], "ans": "B"},
        {"name": "Carbon", "q": "The core of organic chemistry with 6 protons.", "options": ["N", "O", "C", "P"], "ans": "C"},
        {"name": "Nitrogen", "q": "Which gas makes up 78% of the air (No. 7)?", "options": ["O", "N", "H", "Ar"], "ans": "N"},
        {"name": "Oxygen", "q": "Essential for respiration with Atomic Number 8.", "options": ["F", "N", "O", "C"], "ans": "O"},
        {"name": "Fluorine", "q": "The most reactive Halogen with 9 protons.", "options": ["Cl", "F", "Br", "I"], "ans": "F"},
        {"name": "Neon", "q": "Noble Gas No. 10 that glows orange-red.", "options": ["Ne", "Ar", "Kr", "He"], "ans": "Ne"},
        {"name": "Sodium", "q": "Atomic Number 11: Soft metal that explodes in water.", "options": ["Li", "K", "Na", "Mg"], "ans": "Na"},
        {"name": "Magnesium", "q": "Produces a bright white light when burned (No. 12).", "options": ["Al", "Mg", "Ca", "Na"], "ans": "Mg"},
        {"name": "Aluminum", "q": "The most abundant metal in Earth's crust (No. 13).", "options": ["Fe", "Sn", "Al", "Cu"], "ans": "Al"},
        {"name": "Silicon", "q": "The semi-conductor with 14 protons.", "options": ["C", "Ge", "Si", "As"], "ans": "Si"},
        {"name": "Phosphorus", "q": "Element No. 15 found in DNA and matchsticks.", "options": ["S", "N", "P", "K"], "ans": "P"},
        {"name": "Sulfur", "q": "Yellow non-metal (No. 16) with a rotten egg smell.", "options": ["P", "Cl", "S", "Se"], "ans": "S"},
        {"name": "Chlorine", "q": "The Halogen (No. 17) used in swimming pools.", "options": ["F", "Cl", "Br", "I"], "ans": "Cl"},
        {"id": 18, "name": "Argon", "q": "Noble Gas with Atomic Number 18.", "options": ["Ne", "He", "Ar", "Kr"], "ans": "Ar"},
        {"id": 19, "name": "Potassium", "q": "Group 1 metal (No. 19) found in bananas.", "options": ["Na", "K", "Li", "Rb"], "ans": "K"},
        {"id": 20, "name": "Calcium", "q": "Metal in bones and milk with 20 protons.", "options": ["Mg", "Ca", "Ba", "Sr"], "ans": "Ca"}
    ]

# 4. Custom CSS (Animated Background + Wheel Layout)
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}
.main-title { text-align: center; color: #00d2ff; font-size: 45px; font-weight: 800; text-shadow: 0 0 10px #00d2ff; }
.wheel-container { display: flex; justify-content: center; align-items: center; height: 380px; position: relative; }
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(
        #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%,
        #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%,
        #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%,
        #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%
    );
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 16px; pointer-events: none; }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 10px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 5. Audio Trigger Logic
def play_audio(url):
    if not st.session_state.mute:
        st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

# Continuous Ambient Background
if not st.session_state.mute:
    st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

# 6. Global Session State
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'answered_count' not in st.session_state: st.session_state.answered_count = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0
if 'session_pool' not in st.session_state: st.session_state.session_pool = st.session_state.master_bank.copy()

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-120px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 Periodic Master: Spin Quest</h1>', unsafe_allow_html=True)

# Instructions
with st.expander("📖 HOW TO PLAY"):
    st.write("1. Spin the wheel to select a random element challenge.")
    st.write("2. Analyze the chemical description carefully.")
    st.write("3. Select the correct Chemical Symbol to earn 10 points.")
    st.write("4. Complete 10 unique challenges to finish the level!")

if st.session_state.mode == "spin":
    st.write(f"### 📍 Progress: **{st.session_state.answered_count}/10** Questions Complete")
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN FOR A CHALLENGE", use_container_width=True):
        play_audio("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        
        # LOGIC: Pick a random element from the pool (Identity Hidden)
        target_q = random.choice(st.session_state.session_pool)
        st.session_state.current_q = target_q
        
        # LOGIC: Move wheel to a RANDOM slot (Disconnected from Atomic Number)
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Isolating Atomic Data...") as status:
            time.sleep(4)
            status.update(label=f"🎯 Target Locked at Slot {random_slot}!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.current_q
    st.subheader("🔍 Hidden Element Challenge")
    st.info(f"**Description:** {q['q']}")
    
    ans = st.radio("What is the Chemical Symbol for this element?", q['options'], index=None)
    
    if st.button("SUBMIT ANALYSIS"):
        if ans == q["ans"]:
            st.success(f"✅ CORRECT! This is **{q['name']}**.")
            play_audio("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 10
        else:
            st.error(f"❌ INCORRECT. This was **{q['name']}** ({q['ans']}).")
            play_audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        
        st.session_state.session_pool.remove(q)
        st.session_state.answered_count += 1
        time.sleep(2.5)
        
        if st.session_state.answered_count < 10:
            st.session_state.mode = "spin"
        else:
            st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.balloons()
    st.header("🏆 MASTER CHEMIST EVALUATION COMPLETE")
    st.metric("Final Proficiency Score", f"{st.session_state.score} / 100")
    if st.button("Start New Session"):
        st.session_state.answered_count = 0
        st.session_state.score = 0
        st.session_state.session_pool = st.session_state.master_bank.copy()
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div style="text-align:center; padding-top:40px; color:#aaa; font-style:italic;">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
