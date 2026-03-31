import streamlit as st
import random
import time
from streamlit_player import st_player

# 1. Page Configuration
st.set_page_config(page_title="Periodic Quest: Science Unveiled", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
st.session_state.mute = st.sidebar.toggle("Mute All Sounds", value=False)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. 8-Level Categorized Database
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "Atomic Fundamentals", "focus": "Atomic Number & Mass", "data": [
            {"id": 1, "q": "Which element has an Atomic Number of 6 and a Mass of 12.01?", "options": ["N", "C", "O", "B"], "ans": "C"},
            {"id": 2, "q": "Identify the element with exactly 8 protons in its nucleus.", "options": ["He", "O", "N", "F"], "ans": "O"},
            {"id": 3, "q": "Which element has the lowest Relative Atomic Mass (1.008)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"id": 4, "q": "Atomic Number 11 belongs to which reactive element?", "options": ["K", "Mg", "Na", "Li"], "ans": "Na"},
            {"id": 5, "q": "What is the mass of Helium to the nearest whole number?", "options": ["1", "2", "4", "8"], "ans": "4"}
        ]},
        2: {"name": "The Metal Gate", "focus": "Alkali & Alkaline Earth Metals", "data": [
            {"id": 1, "q": "Which Group 1 metal is found in bananas (No. 19)?", "options": ["Na", "K", "Li", "Rb"], "ans": "K"},
            {"id": 2, "q": "Which metal burns with a bright white flame (No. 12)?", "options": ["Ca", "Mg", "Al", "Be"], "ans": "Mg"},
            {"id": 3, "q": "Which Group 2 metal is essential for bone health?", "options": ["Mg", "Ca", "Ba", "Sr"], "ans": "Ca"},
            {"id": 4, "q": "Identify the Group 1 element used in rechargeable batteries.", "options": ["Li", "Na", "K", "Cs"], "ans": "Li"},
            {"id": 5, "q": "Which of these is NOT an Alkaline Earth Metal?", "options": ["Be", "Mg", "Ca", "Na"], "ans": "Na"}
        ]}
    }

# 4. Custom CSS for Visual Design and Dynamic Background
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes particleRotate { from { transform: rotate(0deg) translate(20px) rotate(0deg); } to { transform: rotate(360deg) translate(20px) rotate(-360deg); } }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
    overflow: hidden;
}

/* Glassmorphism Containers */
[data-testid="stVerticalBlock"] > div:has(div.instruction-box),
[data-testid="stVerticalBlock"] > div:has(div.wheel-container),
.stExpander {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 20px;
    margin-bottom: 20px;
}

h1, h2, h3, h4, p, li, label, [data-testid="stMarkdownContainer"] p {
    color: #e0e0e0 !important;
}

.main-title {
    text-align: center;
    color: #00d2ff !important;
    font-size: 45px;
    font-weight: 800;
    text-shadow: 0 0 10px rgba(0, 210, 255, 0.5);
}

.wheel-container { display: flex; justify-content: center; align-items: center; height: 380px; position: relative; }
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(#FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 3s cubic-bezier(0.1, 0, 0, 1);
    z-index: 1;
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 26px; pointer-events: none; }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border: none; border-radius: 10px; font-weight: bold; width: 100%; }
.footer { text-align: center; padding: 40px; color: #aaa; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 5. Continuous Audio & Animated Chemical Icons
if not st.session_state.mute:
    st_player("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", playing=True, looping=True, volume=0.2, config={"display": "none"})

st.markdown("""
<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; opacity: 0.1; pointer-events: none;">
    <svg width="60" height="60" viewBox="0 0 60 60" style="position: absolute; top: 10%; left: 5%; animation: particleRotate 10s linear infinite;">
        <path d="M48 40V12H36V8H24V12H12V40C12 46.6 17.4 52 24 52H36C42.6 52 48 46.6 48 40ZM28 12H32V40C32 42.2 30.2 44 28 44H20C17.8 44 16 42.2 16 40V12H20V20H24V12H28Z" fill="#b8c1ec"/>
    </svg>
    <svg width="80" height="80" viewBox="0 0 100 100" style="position: absolute; top: 15%; right: 10%; animation: particleRotate 15s linear infinite;">
        <circle cx="20" cy="50" r="15" stroke="#b8c1ec" stroke-width="3" fill="none"/>
        <circle cx="80" cy="50" r="15" stroke="#b8c1ec" stroke-width="3" fill="none"/>
        <line x1="35" y1="50" x2="65" y2="50" stroke="#b8c1ec" stroke-width="3"/>
    </svg>
    <svg width="100" height="100" viewBox="0 0 100 100" style="position: absolute; bottom: 15%; left: 10%; animation: particleRotate 20s linear infinite;">
        <circle cx="50" cy="50" r="10" fill="#b8c1ec"/>
        <ellipse cx="50" cy="50" rx="40" ry="15" stroke="#b8c1ec" stroke-width="3" fill="none" transform="rotate(45 50 50)"/>
    </svg>
</div>
""", unsafe_allow_html=True)

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
st.markdown('<h1 class="main-title">🧪 Periodic Master: Spin Quest</h1>', unsafe_allow_html=True)

# instructions
with st.expander("📖 HOW TO PLAY"):
    st.markdown("""
    <div class="instruction-box">
    1. Spin the wheel to pick a random scientific challenge.
    2. Analyze the chemical prompt and select the best answer (A-D).
    3. Review the correct facts to advance to the next gate.
    </div>
    """, unsafe_allow_html=True)

if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 Level {st.session_state.level}: {lvl['name']}")
    st.info(f"Progress: **{st.session_state.q_idx}/5** Questions Complete")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN FOR A CHALLENGE", use_container_width=True):
        st_player("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3", playing=True)
        # Randomize slot landing (1-20), separate from atomic number
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Analyzing Elements...") as status:
            time.sleep(3.2)
            status.update(label=f"🎯 Landed on Slot {random_slot}!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.levels_data[st.session_state.level]["data"][st.session_state.q_idx]
    st.subheader(f"🔍 Challenge: Question {st.session_state.q_idx + 1}")
    st.info(f"**Description:** {q['q']}")
    ans = st.radio("Choose the correct option:", q["options"], index=None)
    
    if st.button("SUBMIT DATA"):
        if ans == q["ans"]:
            st.success("✅ Correct!")
            st_player("https://www.soundjay.com/buttons/sounds/button-3.mp3", playing=True)
            st.session_state.score += 20
        else:
            st.error(f"❌ Incorrect. Answer was {q['ans']}")
            st_player("https://www.soundjay.com/buttons/sounds/button-10.mp3", playing=True)
        
        st.session_state.q_idx += 1
        time.sleep(2)
        if st.session_state.q_idx < 5: st.session_state.mode = "spin"
        else: st.session_state.mode = "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons()
    st.header(f"🏁 Level {st.session_state.level} Mastery Achieved!")
    
    # Review with all correct answers
    review_list = st.session_state.levels_data[st.session_state.level]["data"]
    for item in review_list:
        with st.expander(f"Question {item['id']} Review"):
            st.markdown(f"**Question:** {item['q']}")
            st.success(f"**Correct Fact:** {item['ans']}")

    st.write(f"### Current Total Score: {st.session_state.score}")
    
    if st.button("Proceed to Next Chemical Gate", use_container_width=True):
        if st.session_state.level < len(st.session_state.levels_data):
            st.session_state.level += 1
            st.session_state.q_idx = 0
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST CERTIFIED")
    st.metric("Final Proficiency Score", f"{st.session_state.score} / 200")
    if st.button("Restart New session", use_container_width=True):
        st.session_state.level = 1
        st.session_state.score = 0
        st.session_state.q_idx = 0
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
    
