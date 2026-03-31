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

# 3. COMPLETE 10-LEVEL DATABASE (SS1 Curriculum)
QUIZ_DATA = {
    1: {"name": "The Non-Metals", "data": [
        {"id": 1, "q": "Lightest element (1 proton)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
        {"id": 2, "q": "Noble gas in balloons (No. 2)?", "options": ["Ne", "Ar", "He", "H"], "ans": "He"},
        {"id": 3, "q": "Gas making 78% of air?", "options": ["O", "N", "C", "Ar"], "ans": "N"},
        {"id": 4, "q": "Essential for respiration?", "options": ["C", "F", "O", "N"], "ans": "O"},
        {"id": 5, "q": "Core of organic chemistry?", "options": ["N", "O", "C", "P"], "ans": "C"}
    ]},
    2: {"name": "Reactive Metals", "data": [
        {"id": 1, "q": "Battery metal (Group 1)?", "options": ["Na", "Li", "K", "Be"], "ans": "Li"},
        {"id": 2, "q": "Explodes in water (No. 11)?", "options": ["Mg", "K", "Na", "Li"], "ans": "Na"},
        {"id": 3, "q": "Found in bananas (No. 19)?", "options": ["Na", "Ca", "K", "Li"], "ans": "K"},
        {"id": 4, "q": "White flame when burned (No. 12)?", "options": ["Ca", "Al", "Mg", "Zn"], "ans": "Mg"},
        {"id": 5, "q": "Essential for bones (No. 20)?", "options": ["Mg", "Ca", "Sr", "Ba"], "ans": "Ca"}
    ]},
    3: {"name": "Metalloid Bridge", "data": [
        {"id": 1, "q": "Main chip metalloid (No. 14)?", "options": ["Ge", "Si", "As", "B"], "ans": "Si"},
        {"id": 2, "q": "Used in rat poison (No. 33)?", "options": ["Sb", "As", "Te", "Po"], "ans": "As"},
        {"id": 3, "q": "Semiconductor in Group 14?", "options": ["C", "Si", "P", "Al"], "ans": "Si"},
        {"id": 4, "q": "Metalloid No. 5?", "options": ["B", "Al", "Si", "C"], "ans": "B"},
        {"id": 5, "q": "Infrared metalloid (No. 32)?", "options": ["Si", "Ge", "B", "Sb"], "ans": "Ge"}
    ]},
    4: {"name": "The Halogens", "data": [
        {"id": 1, "q": "Most electronegative element?", "options": ["Cl", "F", "O", "N"], "ans": "F"},
        {"id": 2, "q": "Used to disinfect pools?", "options": ["F", "Cl", "Br", "I"], "ans": "Cl"},
        {"id": 3, "q": "Only liquid non-metal?", "options": ["Hg", "Br", "Cl", "I"], "ans": "Br"},
        {"id": 4, "q": "Antiseptic halogen (No. 53)?", "options": ["Cl", "Br", "I", "At"], "ans": "I"},
        {"id": 5, "q": "Purple vapor sublimate?", "options": ["Br", "I", "Cl", "F"], "ans": "I"}
    ]},
    5: {"name": "Noble Gases", "data": [
        {"id": 1, "q": "Used in orange neon signs?", "options": ["Ar", "Kr", "Ne", "Xe"], "ans": "Ne"},
        {"id": 2, "q": "Most abundant noble gas in air?", "options": ["He", "Ne", "Ar", "Rn"], "ans": "Ar"},
        {"id": 3, "q": "Noble gas No. 36?", "options": ["Ar", "Kr", "Xe", "Rn"], "ans": "Kr"},
        {"id": 4, "q": "Radioactive noble gas?", "options": ["Xe", "Rn", "Kr", "Ar"], "ans": "Rn"},
        {"id": 5, "q": "High-speed flash gas?", "options": ["He", "Ar", "Ne", "Xe"], "ans": "Xe"}
    ]},
    6: {"name": "Transition Metals", "data": [
        {"id": 1, "q": "Symbol for Iron?", "options": ["F", "Fr", "Fe", "Ir"], "ans": "Fe"},
        {"id": 2, "q": "Wiring metal (No. 29)?", "options": ["Cu", "Zn", "Ni", "Co"], "ans": "Cu"},
        {"id": 3, "q": "Main component of steel?", "options": ["Cr", "Fe", "Mn", "Ni"], "ans": "Fe"},
        {"id": 4, "q": "Used to galvanize steel (No. 30)?", "options": ["Cd", "Zn", "Pb", "Sn"], "ans": "Zn"},
        {"id": 5, "q": "Metal in Emeralds (No. 24)?", "options": ["Cr", "V", "Mn", "Ti"], "ans": "Cr"}
    ]},
    7: {"name": "Precious Metals", "data": [
        {"id": 1, "q": "Symbol for Gold?", "options": ["Gd", "Go", "Au", "Ag"], "ans": "Au"},
        {"id": 2, "q": "Best electrical conductor?", "options": ["Au", "Ag", "Cu", "Al"], "ans": "Ag"},
        {"id": 3, "q": "Symbol for Platinum?", "options": ["Pd", "Pu", "Pt", "Pa"], "ans": "Pt"},
        {"id": 4, "q": "Atomic Number 47?", "options": ["Au", "Pt", "Ag", "Hg"], "ans": "Ag"},
        {"id": 5, "q": "Atomic Number of Gold?", "options": ["47", "78", "79", "80"], "ans": "79"}
    ]},
    8: {"name": "Post-Transition", "data": [
        {"id": 1, "q": "Symbol for Lead?", "options": ["Pd", "P", "Pb", "Li"], "ans": "Pb"},
        {"id": 2, "q": "Atomic Number 13?", "options": ["Mg", "Al", "Si", "Ga"], "ans": "Al"},
        {"id": 3, "q": "Symbol for Tin?", "options": ["Ti", "Tn", "Sn", "Sb"], "ans": "Sn"},
        {"id": 4, "q": "Metal in old paint?", "options": ["Hg", "Pb", "Cd", "Bi"], "ans": "Pb"},
        {"id": 5, "q": "Symbol for Bismuth?", "options": ["Bs", "Bi", "Bt", "Bm"], "ans": "Bi"}
    ]},
    9: {"name": "Periodic Trends", "data": [
        {"id": 1, "q": "Vertical columns are...?", "options": ["Periods", "Groups", "Blocks", "Shells"], "ans": "Groups"},
        {"id": 2, "q": "Horizontal rows are...?", "options": ["Groups", "Periods", "Families", "Orbits"], "ans": "Periods"},
        {"id": 3, "q": "How many periods total?", "options": ["5", "7", "8", "18"], "ans": "7"},
        {"id": 4, "q": "How many groups total?", "options": ["7", "10", "18", "32"], "ans": "18"},
        {"id": 5, "q": "L to R, Atomic No...?", "options": ["Decreases", "Increases", "Same", "Varies"], "ans": "Increases"}
    ]},
    10: {"name": "Heavy Elements", "data": [
        {"id": 1, "q": "Nuclear fuel (No. 92)?", "options": ["Th", "Pu", "U", "Ra"], "ans": "U"},
        {"id": 2, "q": "Symbol for Plutonium?", "options": ["Pl", "Pt", "Pu", "Po"], "ans": "Pu"},
        {"id": 3, "q": "Discovered by Curie (No. 88)?", "options": ["U", "Ra", "Th", "Rn"], "ans": "Ra"},
        {"id": 4, "q": "Symbol for Thorium?", "options": ["Th", "Tm", "Ti", "Tb"], "ans": "Th"},
        {"id": 5, "q": "Last natural element?", "options": ["U", "Np", "Pu", "Am"], "ans": "U"}
    ]}
}

# 4. BEAUTIFIED CSS (Nebula Background + Floating Particles + Glassmorphism)
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes float { 0% {transform: translateY(0px);} 50% {transform: translateY(-20px);} 100% {transform: translateY(0px);} }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

/* Floating Chemistry Particle Layer */
.stApp::before {
    content: "🧪 ⚛️ ⚗️ 🔬 🧪 ⚛️";
    position: fixed; top: 10%; left: 0; width: 100%; font-size: 60px; opacity: 0.1;
    display: flex; justify-content: space-around; pointer-events: none; animation: float 6s ease-in-out infinite;
}

.main-title { text-align: center; color: #00d2ff !important; font-size: 45px; font-weight: 800; text-shadow: 0 0 15px #00d2ff; }

/* Instruction Box (Glassmorphism) */
.instruction-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    border: 1px solid rgba(0, 210, 255, 0.3);
    margin-bottom: 25px;
    color: #e0e0e0;
}

/* Wheel Layout */
.wheel-container { display: flex; justify-content: center; align-items: center; height: 350px; position: relative; }
.wheel {
    width: 280px; height: 280px; border-radius: 50%; border: 8px solid #FFD700; position: relative; overflow: hidden;
    background: conic-gradient(from 0deg, #FF4136 0% 20%, #0074D9 20% 40%, #2ECC40 40% 60%, #FFDC00 60% 80%, #B10DC9 80% 100%);
    transition: transform 3.5s cubic-bezier(0.1, 0, 0, 1);
    box-shadow: 0 0 30px rgba(0, 210, 255, 0.2);
}
.wheel-pointer { position: absolute; top: 15px; width: 0; height: 0; border-left: 18px solid transparent; border-right: 18px solid transparent; border-top: 40px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 20px; pointer-events: none; }

h1, h2, h3, h4, p, li, label { color: #e0e0e0 !important; }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 10px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# 5. INITIALIZATION & RANDOMIZATION LOGIC
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'rotation' not in st.session_state: st.session_state.rotation = 0
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0

# Randomize Question Order for the Level
if 'shuffled_questions' not in st.session_state:
    pool = QUIZ_DATA[st.session_state.level]["data"]
    st.session_state.shuffled_questions = random.sample(pool, len(pool))

# 6. AUDIO HANDLER
def play_sfx(url):
    if enable_sounds: st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)
if enable_sounds: st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*72-36}deg) translateY(-100px) rotate(-{i*72-36}deg);">{i}</div>' for i in range(1, 6)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 PERIODIC MASTER: SPIN QUEST</h1>', unsafe_allow_html=True)

# INSTRUCTIONS (Restored)
st.markdown("""
<div class="instruction-box">
    <b>📖 LABORATORY INSTRUCTIONS:</b><br>
    1. Click <b>SPIN</b> to select a random question slot.<br>
    2. Analyze the challenge and select the correct chemical symbol.<br>
    3. Complete 5 spins to master the current gate and unlock the next!
</div>
""", unsafe_allow_html=True)

# Safety check for level key
if st.session_state.level not in QUIZ_DATA:
    st.session_state.level = 1
    st.rerun()

if st.session_state.mode == "spin":
    st.write(f"### 📍 GATE {st.session_state.level}: {QUIZ_DATA[st.session_state.level]['name']}")
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 INITIATE CHEMICAL SPIN"):
        play_sfx("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        # Use the ID of the next shuffled question to determine where the wheel stops
        target_q = st.session_state.shuffled_questions[st.session_state.q_idx]
        target_stop = -( (target_q['id'] - 1) * 72 + 36 )
        st.session_state.rotation += 1440 + (target_stop - (st.session_state.rotation % 360))
        
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Analyzing Atomic Structure...") as status:
            time.sleep(3.5)
            status.update(label=f"🎯 Target Locked: Slot {target_q['id']}!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.shuffled_questions[st.session_state.q_idx]
    st.info(f"**Challenge:** {q['q']}")
    ans = st.radio("Choose Symbol:", q["options"], index=None)
    
    if st.button("SUBMIT ANALYSIS"):
        if ans == q["ans"]:
            st.success("✅ CORRECT!"); play_sfx("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT. Correct Symbol was {q['ans']}"); play_sfx("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons(); st.header("🏁 Gate Mastered!")
    for item in st.session_state.shuffled_questions:
        with st.expander(f"Review: Question {item['id']}"):
            st.write(item['q']); st.success(f"Fact: {item['ans']}")
    
    if st.button("Proceed to Next Gate"):
        if st.session_state.level < 10:
            st.session_state.level += 1
            st.session_state.q_idx = 0
            del st.session_state.shuffled_questions
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST CERTIFIED"); st.metric("Final Score", f"{st.session_state.score} / 1000")
    if st.button("Restart Journey"):
        st.session_state.clear()
        st.rerun()

st.markdown('<div style="text-align:center; padding:40px; color:#888; font-style:italic;">Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
