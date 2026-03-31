import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sidebar Controls (Sound Toggle)
st.sidebar.title("🎮 Lab Command Center")
enable_sounds = st.sidebar.toggle("Enable Laboratory Audio", value=True)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. 8-Level Categorized Database (Full Curriculum)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "The Non-Metals", "type": "Gas & Life Essentials", "data": [
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
        3: {"name": "Metalloids", "type": "The Staircase Elements", "data": [
            {"id": 1, "q": "Primary metalloid used in computer chips?", "options": ["Ge", "Si", "As", "B"], "ans": "Si"},
            {"id": 2, "q": "Metalloid with Atomic Number 5?", "options": ["B", "Al", "Si", "C"], "ans": "B"}
            # Add remaining level data here
        ]}
        # Levels 4-8 follow the same structure
    }

# 4. Custom CSS for Animated Background and UI
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes float { 0% {transform: translateY(0px);} 50% {transform: translateY(-15px);} 100% {transform: translateY(0px);} }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}
.stApp::after {
    content: "🧪 ⚛️ ⚗️ 🔬";
    position: fixed; top: 10%; left: 0; width: 100%; font-size: 60px; opacity: 0.05;
    display: flex; justify-content: space-around; pointer-events: none; animation: float 6s ease-in-out infinite;
}
.main-title { text-align: center; color: #00d2ff !important; font-size: 45px; font-weight: 800; text-shadow: 0 0 15px #00d2ff; }
.wheel-container { display: flex; justify-content: center; align-items: center; height: 380px; position: relative; }
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(from 0deg, #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 14px; pointer-events: none; }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 10px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 5. Audio Setup
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
if 'answered_ids' not in st.session_state: st.session_state.answered_ids = []

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-120px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 Periodic Master: Spin Quest</h1>', unsafe_allow_html=True)

with st.expander("📖 LABORATORY INSTRUCTIONS"):
    st.write("1. **Spin the Wheel**: Land on a random slot (1-20) to unlock a hidden chemical challenge.")
    st.write("2. **Analyze**: Read the properties provided and identify the correct Chemical Symbol.")
    st.write("3. **Master**: Complete 5 questions to view the level results and advance.")

if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 Level {st.session_state.level}: {lvl['name']} ({lvl['type']})")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN FOR A CHALLENGE", use_container_width=True):
        play_sound("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        
        # Disconnect slot number from Atomic Number for true randomness
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
    lvl = st.session_state.levels_data[st.session_state.level]
    q = lvl["data"][st.session_state.q_idx]
    st.subheader("🔍 Hidden Element Challenge")
    st.info(f"**Challenge:** {q['q']}")
    
    ans = st.radio("What is the Chemical Symbol?", q["options"], index=None)
    
    if st.button("SUBMIT ANALYSIS", use_container_width=True):
        if ans == q["ans"]:
            st.success("✅ CORRECT! Atomic Data Verified.")
            play_sound("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT. Data points to Symbol: {q['ans']}")
            play_sound("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons()
    st.header(f"🏁 Level {st.session_state.level} Complete!")
    st.subheader("📊 Scientific Review (Correct Answers):")
    
    # Review Table for pedagogical reinforcement
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Analysis: {item['q'][:40]}..."):
            st.write(f"**Question:** {item['q']}")
            st.success(f"**Correct Symbol:** {item['ans']}")

    if st.button("Unlock Next Chemical Gate", use_container_width=True):
        if st.session_state.level < len(st.session_state.levels_data):
            st.session_state.level += 1
            st.session_state.q_idx = 0
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST CERTIFIED")
    st.metric("Final Proficiency Score", f"{st.session_state.score} pts")
    if st.button("Restart Journey", use_container_width=True):
        st.session_state.level = 1
        st.session_state.score = 0
        st.session_state.q_idx = 0
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
    
