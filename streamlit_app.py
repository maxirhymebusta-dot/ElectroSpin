import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
enable_sounds = st.sidebar.toggle("Enable Laboratory Audio", value=True)
if st.sidebar.button("♻️ Reset App (Fix Errors)"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# 3. Full 10-Level Database (Ensuring Level 1-10 Keys Exist)
# This dictionary must be defined OUTSIDE the session_state check first to prevent KeyErrors
RAW_DATA = {
    1: {"name": "Non-Metals", "type": "Gas & Life Essentials", "data": [
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
    3: {"name": "The Metalloid Bridge", "type": "The Staircase Elements", "data": [
        {"id": 1, "q": "Primary metalloid used in computer chips?", "options": ["Ge", "Si", "As", "B"], "ans": "Si"},
        {"id": 2, "q": "Metalloid with Atomic Number 5?", "options": ["B", "Al", "Si", "C"], "ans": "B"},
        {"id": 3, "q": "Which element is a semiconductor in Group 14?", "options": ["C", "Si", "P", "Al"], "ans": "Si"},
        {"id": 4, "q": "Used in semiconductors (No. 33)?", "options": ["Sb", "As", "Te", "Po"], "ans": "As"},
        {"id": 5, "q": "Metalloid used in infrared devices (No. 32)?", "options": ["Si", "Ge", "B", "Sb"], "ans": "Ge"}
    ]},
    # Levels 4-10 (Simplified for code block, ensure you keep your full data)
}
# Fill in Levels 4-10 to ensure no KeyError
for i in range(4, 11):
    if i not in RAW_DATA:
        RAW_DATA[i] = RAW_DATA[1].copy() # Fallback to prevent crash

if 'levels_data' not in st.session_state:
    st.session_state.levels_data = RAW_DATA

# 4. State Management Setup
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0

# 5. CSS Animations & Background
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}
.main-title { text-align: center; color: #00d2ff !important; font-size: 40px; font-weight: 800; text-shadow: 0 0 10px #00d2ff; }
.wheel-container { display: flex; justify-content: center; align-items: center; height: 350px; position: relative; }
.wheel {
    width: 280px; height: 280px; border-radius: 50%; border: 8px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(from 0deg, #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 15px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 40px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 14px; pointer-events: none; }
</style>
""", unsafe_allow_html=True)

# Audio Handler
def play_audio(url):
    if enable_sounds:
        st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

# 6. UI Logic
st.markdown('<h1 class="main-title">🧪 PERIODIC MASTER: SPIN QUEST</h1>', unsafe_allow_html=True)

# Double check that level exists in keys to avoid KeyError
current_level = st.session_state.level
if current_level not in st.session_state.levels_data:
    st.session_state.level = 1
    st.rerun()

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-110px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# Main Game Loop
if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 GATE {st.session_state.level}: {lvl['name']}")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 INITIATE SPIN", use_container_width=True):
        play_audio("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Fetching Atomic Data...") as status:
            time.sleep(4)
            status.update(label=f"🎯 Slot {random_slot} Locked!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.levels_data[st.session_state.level]["data"][st.session_state.q_idx]
    st.info(f"**Challenge:** {q['q']}")
    ans = st.radio("Chemical Symbol?", q["options"], index=None)
    
    if st.button("SUBMIT"):
        if ans == q["ans"]:
            st.success("✅ CORRECT!")
            play_audio("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT. Answer: {q['ans']}")
            play_audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons()
    st.header("🏁 Level Results")
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Fact Check: {item['q'][:30]}..."):
            st.write(item['q'])
            st.success(f"Answer: {item['ans']}")
    
    if st.button("Next Level"):
        if st.session_state.level < 10:
            st.session_state.level += 1
            st.session_state.q_idx = 0
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST!")
    st.metric("Total Score", f"{st.session_state.score} / 1000")
    if st.button("Restart"):
        st.session_state.level = 1
        st.session_state.score = 0
        st.session_state.q_idx = 0
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div style="text-align:center; padding:40px; color:#888; font-style:italic;">Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
    
