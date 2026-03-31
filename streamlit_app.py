import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="Periodic Master: Spin Quest", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
st.session_state.mute = st.sidebar.toggle("Mute Laboratory Sounds", value=False)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. 8-Level Categorized Database
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "Atomic Fundamentals", "focus": "Atomic Number & Mass", "data": [
            {"q": "Which element has an Atomic Number of 6 and a Mass of 12.01?", "options": ["N", "C", "O", "B"], "ans": "C"},
            {"q": "Identify the element with exactly 8 protons in its nucleus.", "options": ["He", "O", "N", "F"], "ans": "O"},
            {"q": "Which element has the lowest Relative Atomic Mass (1.008)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"q": "Atomic Number 11 belongs to which reactive element?", "options": ["K", "Mg", "Na", "Li"], "ans": "Na"},
            {"q": "What is the mass of Helium to the nearest whole number?", "options": ["1", "2", "4", "8"], "ans": "4"}
        ]},
        2: {"name": "The Metal Gate", "focus": "Alkali & Alkaline Earth Metals", "data": [
            {"q": "Which Group 1 metal is found in bananas (No. 19)?", "options": ["Na", "K", "Li", "Rb"], "ans": "K"},
            {"q": "Which metal burns with a bright white flame (No. 12)?", "options": ["Ca", "Mg", "Al", "Be"], "ans": "Mg"},
            {"id": 20, "q": "Which Group 2 metal is essential for bone health?", "options": ["Mg", "Ca", "Ba", "Sr"], "ans": "Ca"},
            {"q": "Identify the Group 1 element used in rechargeable batteries.", "options": ["Li", "Na", "K", "Cs"], "ans": "Li"},
            {"q": "Which of these is NOT an Alkaline Earth Metal?", "options": ["Be", "Mg", "Ca", "Na"], "ans": "Na"}
        ]},
        3: {"name": "Non-Metal Territory", "focus": "Gases & Life Elements", "data": [
            {"q": "Which gas makes up the majority of Earth's atmosphere?", "options": ["O", "N", "H", "Ar"], "ans": "N"},
            {"q": "Which non-metal is a yellow solid with a strong smell?", "options": ["P", "S", "Cl", "Se"], "ans": "S"},
            {"q": "Which element is the primary component of diamonds?", "options": ["Si", "C", "B", "P"], "ans": "C"},
            {"q": "Which non-metal is found in matchsticks (No. 15)?", "options": ["S", "N", "P", "K"], "ans": "P"},
            {"q": "Which gas is essential for human aerobic respiration?", "options": ["CO2", "N", "O", "He"], "ans": "O"}
        ]},
        4: {"name": "The Metalloid Bridge", "focus": "Semi-Conductors", "data": [
            {"q": "Which metalloid is the primary material in computer chips?", "options": ["Ge", "Si", "As", "B"], "ans": "Si"},
            {"q": "Which metalloid has Atomic Number 5?", "options": ["B", "Al", "Si", "C"], "ans": "B"},
            {"q": "Identify the element that acts as both a metal and non-metal.", "options": ["Al", "Si", "S", "P"], "ans": "Si"},
            {"q": "Which element in Period 4 is a known metalloid?", "options": ["Ga", "Ge", "As", "Se"], "ans": "Ge"},
            {"q": "Metalloids are located along which feature of the table?", "options": ["Group 1", "The Staircase", "Period 7", "The Bottom"], "ans": "The Staircase"}
        ]}
        # Levels 5-8: Halogens, Noble Gases, Transition Metals, and Periods/Groups review
    }

# 4. Global CSS & Background
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
.stApp { background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e); background-size: 400% 400%; animation: gradientBG 15s ease infinite; }
.wheel-container { display: flex; justify-content: center; align-items: center; height: 380px; position: relative; }
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(#FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 16px; pointer-events: none; }
</style>
""", unsafe_allow_html=True)

# 5. Audio Setup
def play_audio(url):
    if not st.session_state.mute:
        st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

if not st.session_state.mute:
    st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

# 6. Session State
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-120px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 style="text-align:center; color:#00d2ff;">🧪 Periodic Master: Spin Quest</h1>', unsafe_allow_html=True)

if st.session_state.mode == "spin":
    lvl_data = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 Level {st.session_state.level}: {lvl_data['name']}")
    st.info(f"**Focus Area:** {lvl_data['focus']} | Questions: {st.session_state.q_idx}/5")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN FOR A CHALLENGE", use_container_width=True):
        play_audio("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        
        # Move wheel to a RANDOM slot (1-20)
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Fetching Chemical Data...") as status:
            time.sleep(4)
            status.update(label=f"🎯 Target Locked at Slot {random_slot}!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    lvl = st.session_state.levels_data[st.session_state.level]
    q = lvl["data"][st.session_state.q_idx]
    
    st.subheader(f"🔍 Level {st.session_state.level} Challenge")
    st.info(f"**Question:** {q['q']}")
    ans = st.radio("Select the correct Chemical Symbol/Value:", q['options'], index=None)
    
    if st.button("SUBMIT DATA"):
        if ans == q["ans"]:
            st.success("✅ CORRECT! Analysis Verified.")
            play_audio("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT. The correct answer was: {q['ans']}")
            play_audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        
        st.session_state.q_idx += 1
        time.sleep(2)
        
        if st.session_state.q_idx < 5:
            st.session_state.mode = "spin"
        else:
            st.session_state.mode = "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.header(f"🏁 Level {st.session_state.level} Results")
    st.metric("Score", f"{st.session_state.score} pts")
    if st.button("Proceed to Next Chemical Gate"):
        if st.session_state.level < 4:
            st.session_state.level += 1
            st.session_state.q_idx = 0
            st.session_state.mode = "spin"
        else:
            st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.balloons()
    st.header("🏆 MASTER CHEMIST CERTIFIED")
    st.metric("Final Total Score", f"{st.session_state.score} pts")
    if st.button("Restart Journey"):
        st.session_state.level = 1
        st.session_state.score = 0
        st.session_state.q_idx = 0
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div style="text-align:center; padding-top:40px; color:#aaa; font-style:italic;">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
        
