import streamlit as st
import random
import time

# 1. Page Configuration (Keep layout wide for modern feel)
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
enable_sounds = st.sidebar.toggle("Enable Laboratory Audio", value=True)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. Full 10-Level Database (Keep your full questions intact!)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "The Non-Metals", "type": "Gas & Life Essentials", "data": [
            {"id": 1, "q": "Lightest element in the universe (1 proton)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"id": 2, "q": "Noble gas used in balloons (Atomic No. 2)?", "options": ["Ne", "Ar", "He", "H"], "ans": "He"},
            {"id": 3, "q": "Gas making up 78% of Earth's atmosphere?", "options": ["O", "N", "C", "Ar"], "ans": "N"},
            {"id": 4, "q": "Element essential for human respiration?", "options": ["C", "F", "O", "N"], "ans": "O"},
            {"id": 5, "q": "The primary basis of all organic chemistry?", "options": ["N", "O", "C", "P"], "ans": "C"}
        ]},
        # ... Levels 2-10 continue here (keep your existing full data!) ...
    }

# 4. BEAUTIFIED GAME CSS (Deep Space Chemistry Theme)
st.markdown("""
<style>
/* A. Animated Deep Space Nebula Background */
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes floatingIcons { 0% {transform: translateY(0px) rotate(0deg);} 50% {transform: translateY(-20px) rotate(5deg);} 100% {transform: translateY(0px) rotate(0deg);} }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    position: relative;
    overflow: hidden;
}

/* B. Floating Chemistry Particle Layer (Beakers, Atoms, Molecules) */
.stApp::before {
    content: "🧪 ⚛️ ⚗️ 🔬 🧪 ⚛️";
    position: fixed;
    top: 10%; left: 0; width: 100%; height: 100%;
    font-size: 60px;
    opacity: 0.08;
    pointer-events: none;
    display: flex;
    justify-content: space-around;
    align-items: center;
    animation: floatingIcons 6s ease-in-out infinite;
}

/* C. Neon Styled Heading */
.main-title {
    text-align: center;
    color: #00d2ff !important;
    font-size: 50px;
    font-weight: 800;
    text-shadow: 0 0 15px #00d2ff, 0 0 30px #3a7bd5;
    margin-bottom: 20px;
}

/* D. Glassmorphism UI Containers (Blur effect for text clarity) */
.stExpander, .stMarkdown, .stStatus {
    background: rgba(255, 255, 255, 0.03);
    border-radius: 15px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 15px;
    margin-bottom: 20px;
}

/* E. Spinning Wheel Design */
.wheel-container { display: flex; justify-content: center; align-items: center; height: 380px; position: relative; }
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(from 0deg, #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
    box-shadow: 0 0 30px rgba(0, 210, 255, 0.2);
    z-index: 1;
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 14px; pointer-events: none; }

/* F. Text & Radio Buttons Styling */
h1, h2, h3, h4, p, li, label, [data-testid="stMarkdownContainer"] p { color: #e0e0e0 !important; }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 10px; font-weight: bold; }
.footer { text-align: center; padding: 40px; color: #888; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 5. Audio Setup (Keep from previous Step)
def play_sound(url):
    if enable_sounds:
        st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

if enable_sounds:
    st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

# 6. Session State Initialization
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0

# (Check if current level is valid in keys to prevent KeyError)
if st.session_state.level not in st.session_state.levels_data:
    st.session_state.level = 1

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-120px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 PERIODIC MASTER: SPIN QUEST</h1>', unsafe_allow_html=True)

if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 GATE {st.session_state.level}: {lvl['name']} ({lvl['type']})")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN FOR A CHALLENGE", use_container_width=True):
        play_sound("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Fetching Atomic Data...") as status:
            time.sleep(4)
            status.update(label=f"🎯 Target Locked at Slot {random_slot}!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.levels_data[st.session_state.level]["data"][st.session_state.q_idx]
    st.subheader("🔍 Hidden Element Challenge")
    st.info(f"**Challenge:** {q['q']}")
    ans = st.radio("Chemical Symbol?", q["options"], index=None)
    
    if st.button("SUBMIT DATA ANALYSIS", use_container_width=True):
        if ans == q["ans"]:
            st.success("✅ CORRECT! Atomic Data Verified.")
            play_sound("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT. Correct Symbol was: {q['ans']}")
            play_sound("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons()
    st.header(f"🏁 Level {st.session_state.level} Complete!")
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Review: Question {item['id']}"):
            st.write(item['q'])
            st.success(f"Fact: The correct symbol is {item['ans']}")
    
    if st.button("Unlock Next Chemical Gate", use_container_width=True):
        if st.session_state.level < len(st.session_state.levels_data):
            st.session_state.level += 1
            st.session_state.q_idx = 0
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

# ... (End screen and footer remain same) ...
st.markdown('<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
        
