import streamlit as st
import random
import time
from streamlit_player import st_player

# 1. Page Configuration
st.set_page_config(page_title="Periodic Master: Spin Quest", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
st.session_state.mute = st.sidebar.toggle("Mute All Sounds", value=False)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. Database (First 2 Levels for testing)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "Atomic Fundamentals", "data": [
            {"id": 1, "q": "Which element has an Atomic Number of 6?", "options": ["N", "C", "O", "B"], "ans": "C"},
            {"id": 2, "q": "Identify the element with 8 protons.", "options": ["He", "O", "N", "F"], "ans": "O"},
            {"id": 3, "q": "Lightest element (Mass 1.008)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"id": 4, "q": "Atomic Number 11?", "options": ["K", "Mg", "Na", "Li"], "ans": "Na"},
            {"id": 5, "q": "Mass of Helium (rounded)?", "options": ["1", "2", "4", "8"], "ans": "4"}
        ]},
        2: {"name": "The Metal Gate", "data": [
            {"id": 1, "q": "Found in bananas (No. 19)?", "options": ["Na", "K", "Li", "Rb"], "ans": "K"},
            {"id": 2, "q": "Bright white flame (No. 12)?", "options": ["Ca", "Mg", "Al", "Be"], "ans": "Mg"},
            {"id": 3, "q": "Bone health metal (No. 20)?", "options": ["Mg", "Ca", "Ba", "Sr"], "ans": "Ca"},
            {"id": 4, "q": "Battery metal (Group 1)?", "options": ["Li", "Na", "K", "Cs"], "ans": "Li"},
            {"id": 5, "q": "NOT an Alkaline Earth Metal?", "options": ["Be", "Mg", "Ca", "Na"], "ans": "Na"}
        ]}
    }

# 4. Custom CSS for Visuals
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
}
.main-title { text-align: center; color: #00d2ff !important; font-size: 45px; font-weight: 800; text-shadow: 0 0 10px rgba(0, 210, 255, 0.5); }
.wheel-container { display: flex; justify-content: center; align-items: center; height: 350px; position: relative; }
.wheel {
    width: 280px; height: 280px; border-radius: 50%; border: 8px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(#FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 3s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 15px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 40px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 18px; pointer-events: none; }
</style>
""", unsafe_allow_html=True)

# 5. Fixed Audio Section
if not st.session_state.mute:
    st_player("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", playing=True, volume=0.2, key="bg_music")

# 6. Session State
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-110px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 Periodic Master: Spin Quest</h1>', unsafe_allow_html=True)

with st.expander("📖 HOW TO PLAY"):
    st.write("1. Spin the wheel to get a question number. 2. Submit the correct chemical data. 3. Review facts to finish the level.")

if st.session_state.mode == "spin":
    st.write(f"### 📍 Level {st.session_state.level} | Progress: {st.session_state.q_idx}/5")
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN FOR A CHALLENGE", use_container_width=True):
        if not st.session_state.mute:
            st_player("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3", playing=True, key=f"spin_{time.time()}")
        
        # Disconnect slot from question logic
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Analyzing Elements...") as status:
            time.sleep(3)
            status.update(label=f"🎯 Landed on Slot {random_slot}!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.levels_data[st.session_state.level]["data"][st.session_state.q_idx]
    st.info(f"**Question:** {q['q']}")
    ans = st.radio("Choose the correct option:", q["options"], index=None)
    
    if st.button("SUBMIT DATA"):
        if ans == q["ans"]:
            st.success("✅ Correct!")
            if not st.session_state.mute:
                st_player("https://www.soundjay.com/buttons/sounds/button-3.mp3", playing=True, key=f"correct_{time.time()}")
            st.session_state.score += 20
        else:
            st.error(f"❌ Incorrect. Answer was {q['ans']}")
            if not st.session_state.mute:
                st_player("https://www.soundjay.com/buttons/sounds/button-10.mp3", playing=True, key=f"wrong_{time.time()}")
        
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.header(f"🏁 Level {st.session_state.level} Mastery!")
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Review: Question {item['id']}"):
            st.write(item['q'])
            st.success(f"Fact: {item['ans']}")
    
    if st.button("Proceed to Next Gate"):
        if st.session_state.level < 2:
            st.session_state.level += 1
            st.session_state.q_idx = 0
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.balloons()
    st.header("🏆 MASTER CHEMIST CERTIFIED")
    st.metric("Final Score", f"{st.session_state.score} / 200")
    if st.button("Restart Journey"):
        st.session_state.level = 1
        st.session_state.score = 0
        st.session_state.q_idx = 0
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div style="text-align:center; padding:40px; color:#aaa; font-style:italic;">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
    
