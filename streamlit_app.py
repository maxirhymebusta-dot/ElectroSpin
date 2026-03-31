import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
enable_sounds = st.sidebar.toggle("Enable Laboratory Audio", value=True)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. 10-Level Database (Summary version - keep your full questions from previous steps!)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "The Non-Metals", "type": "Gas & Life Essentials", "data": [
            {"id": 1, "q": "Lightest element in the universe (1 proton)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"id": 2, "q": "Noble gas used in balloons (Atomic No. 2)?", "options": ["Ne", "Ar", "He", "H"], "ans": "He"},
            {"id": 3, "q": "Gas making up 78% of Earth's atmosphere?", "options": ["O", "N", "C", "Ar"], "ans": "N"},
            {"id": 4, "q": "Element essential for human respiration?", "options": ["C", "F", "O", "N"], "ans": "O"},
            {"id": 5, "q": "The primary basis of all organic chemistry?", "options": ["N", "O", "C", "P"], "ans": "C"}
        ]},
        # ... Levels 2-10 continue here ...
    }

# 4. BEAUTIFIED CSS (Animations + Neon Heading + Glassmorphism)
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes floatIcons { 0% {transform: translateY(0px) rotate(0deg);} 50% {transform: translateY(-20px) rotate(5deg);} 100% {transform: translateY(0px) rotate(0deg);} }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

/* Neon Heading */
.main-title {
    text-align: center;
    color: #00d2ff !important;
    font-size: 50px;
    font-weight: 800;
    text-shadow: 0 0 15px #00d2ff, 0 0 30px #3a7bd5;
    margin-bottom: 10px;
}

/* Glassmorphism Instruction Box */
.instruction-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 20px;
    margin-bottom: 25px;
    color: #e0e0e0;
}

.wheel-container { display: flex; justify-content: center; align-items: center; height: 380px; position: relative; }
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(from 0deg, #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
    box-shadow: 0 0 30px rgba(0, 210, 255, 0.2);
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 14px; pointer-events: none; }
.footer { text-align: center; padding: 40px; color: #888; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 5. ANIMATED BACKGROUND ELEMENTS (Floating SVGs)
st.markdown("""
<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; opacity: 0.15; pointer-events: none;">
    <svg width="80" height="80" style="position: absolute; top: 20%; left: 10%; animation: floatIcons 8s infinite;"><path d="M40 10 L10 50 Q10 60 20 60 L60 60 Q70 60 70 50 L40 10" fill="none" stroke="#00d2ff" stroke-width="2"/></svg>
    <svg width="60" height="60" style="position: absolute; bottom: 20%; right: 15%; animation: floatIcons 10s infinite reverse;"><circle cx="30" cy="30" r="20" fill="none" stroke="#00d2ff" stroke-width="2"/><circle cx="30" cy="30" r="5" fill="#00d2ff"/></svg>
</div>
""", unsafe_allow_html=True)

# 6. Audio Handler
def play_sound(url):
    if enable_sounds:
        st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

if enable_sounds:
    st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

# 7. Session State
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-120px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 PERIODIC MASTER: SPIN QUEST</h1>', unsafe_allow_html=True)

# RESTORED INSTRUCTIONS
st.markdown("""
<div class="instruction-box">
    <h3>📖 Laboratory Protocol (How to Play)</h3>
    <ul>
        <li><b>Spin the Wheel:</b> Click the button to land on a random chemical slot (1-20).</li>
        <li><b>Identify:</b> Use your knowledge of Atomic Numbers, Mass, and Groups to choose the correct symbol.</li>
        <li><b>Mastery:</b> Complete 5 trials per level. Review all correct facts at the end of each gate.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 GATE {st.session_state.level}: {lvl['name']}")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 INITIATE CHEMICAL SPIN", use_container_width=True):
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
    st.info(f"**Description:** {q['q']}")
    ans = st.radio("What is the Chemical Symbol?", q["options"], index=None)
    
    if st.button("SUBMIT DATA ANALYSIS", use_container_width=True):
        if ans == q["ans"]:
            st.success("✅ CORRECT! Atomic Data Verified.")
            play_sound("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT. Analysis points to: {q['ans']}")
            play_sound("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons()
    st.header(f"🏁 Level {st.session_state.level} Complete!")
    
    # SHOW CORRECT ANSWERS
    st.subheader("📊 Post-Lab Review (Correct Facts):")
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Question Review: {item['q'][:40]}..."):
            st.write(f"**Question:** {item['q']}")
            st.success(f"**Scientific Fact:** The correct symbol is {item['ans']}")

    if st.button("Proceed to Next Gate", use_container_width=True):
        if st.session_state.level < 10:
            st.session_state.level += 1
            st.session_state.q_idx = 0
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

# ... (End screen and footer remain same) ...
st.markdown('<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
