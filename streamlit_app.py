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

# 3. UPDATED SIMPLIFIED 10-LEVEL DATABASE (SS1 Friendly)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "Non-Metals", "type": "Gases", "data": [
            {"id": 1, "q": "Which element is the lightest gas in the universe and has Atomic Number 1?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"id": 2, "q": "Which Noble Gas has 2 protons and is used to make balloons float?", "options": ["Ne", "Ar", "He", "H"], "ans": "He"},
            {"id": 3, "q": "Which gas (Atomic No. 7) makes up 78% of the air we breathe?", "options": ["O", "N", "C", "Ar"], "ans": "N"},
            {"id": 4, "q": "Which element with Atomic Number 8 is essential for human breathing?", "options": ["C", "F", "O", "N"], "ans": "O"},
            {"id": 5, "q": "Which element (No. 6) is the core of all organic chemistry and life?", "options": ["N", "O", "C", "P"], "ans": "C"}
        ]},
        2: {"name": "Reactive Metals", "type": "Group 1 & 2", "data": [
            {"id": 1, "q": "Which Group 1 metal is used in phone batteries (Atomic No. 3)?", "options": ["Na", "Li", "K", "Be"], "ans": "Li"},
            {"id": 2, "q": "Which metal (No. 11) is so reactive that it explodes in water?", "options": ["Mg", "K", "Na", "Li"], "ans": "Na"},
            {"id": 3, "q": "Which metal (No. 19) is found in bananas and is highly reactive?", "options": ["Na", "Ca", "K", "Li"], "ans": "K"},
            {"id": 4, "q": "Which metal (No. 12) burns with a blinding white light in the lab?", "options": ["Ca", "Al", "Mg", "Zn"], "ans": "Mg"},
            {"id": 5, "q": "Which Group 2 metal (No. 20) is essential for strong bones and teeth?", "options": ["Mg", "Ca", "Sr", "Ba"], "ans": "Ca"}
        ]},
        3: {"name": "The Metalloids", "type": "Semiconductors", "data": [
            {"id": 1, "q": "Which metalloid (No. 14) is used to make computer chips?", "options": ["Ge", "Si", "As", "B"], "ans": "Si"},
            {"id": 2, "q": "Which metalloid (No. 5) is used in heat-resistant glassware?", "options": ["B", "Al", "Si", "C"], "ans": "B"},
            {"id": 3, "q": "Which Group 14 element is a semi-conductor (No. 14)?", "options": ["C", "Si", "P", "Al"], "ans": "Si"},
            {"id": 4, "q": "Which metalloid (No. 33) is famously used as a poison?", "options": ["Sb", "As", "Te", "Po"], "ans": "As"},
            {"id": 5, "q": "Which metalloid (No. 32) is used in infrared technology?", "options": ["Si", "Ge", "B", "Sb"], "ans": "Ge"}
        ]},
        4: {"name": "The Halogens", "type": "Group 17", "data": [
            {"id": 1, "q": "Which is the most reactive and electronegative element (No. 9)?", "options": ["Cl", "F", "O", "N"], "ans": "F"},
            {"id": 2, "q": "Which halogen (No. 17) is used to kill bacteria in swimming pools?", "options": ["F", "Cl", "Br", "I"], "ans": "Cl"},
            {"id": 3, "q": "Which element (No. 35) is the only non-metal liquid at room temp?", "options": ["Hg", "Br", "Cl", "I"], "ans": "Br"},
            {"id": 4, "q": "Which halogen (No. 53) is used as a brown antiseptic for wounds?", "options": ["Cl", "Br", "I", "At"], "ans": "I"},
            {"id": 5, "q": "Which solid halogen (No. 53) turns into purple gas when heated?", "options": ["Br", "I", "Cl", "F"], "ans": "I"}
        ]},
        5: {"name": "Noble Gases", "type": "Group 18", "data": [
            {"id": 1, "q": "Which Noble Gas (No. 10) is used in bright orange-red signs?", "options": ["Ar", "Kr", "Ne", "Xe"], "ans": "Ne"},
            {"id": 2, "q": "Which inert gas is the most abundant Noble Gas in the air?", "options": ["He", "Ne", "Ar", "Rn"], "ans": "Ar"},
            {"id": 3, "q": "Which Noble Gas has the Atomic Number 36?", "options": ["Ar", "Kr", "Xe", "Rn"], "ans": "Kr"},
            {"id": 4, "q": "Which radioactive gas (No. 86) can seep into basements?", "options": ["Xe", "Rn", "Kr", "Ar"], "ans": "Rn"},
            {"id": 5, "q": "Which gas (No. 54) is used in high-speed camera flashes?", "options": ["He", "Ar", "Ne", "Xe"], "ans": "Xe"}
        ]},
        6: {"name": "Transition Metals", "type": "Common Metals", "data": [
            {"id": 1, "q": "What is the chemical symbol for Iron (No. 26)?", "options": ["F", "Fr", "Fe", "Ir"], "ans": "Fe"},
            {"id": 2, "q": "Which reddish metal (No. 29) is used in electrical wiring?", "options": ["Cu", "Zn", "Ni", "Co"], "ans": "Cu"},
            {"id": 3, "q": "Which transition metal (No. 26) is the main ingredient in Steel?", "options": ["Cr", "Fe", "Mn", "Ni"], "ans": "Fe"},
            {"id": 4, "q": "Which metal (No. 30) is used to galvanize iron to prevent rust?", "options": ["Cd", "Zn", "Pb", "Sn"], "ans": "Zn"},
            {"id": 5, "q": "Which metal (No. 24) is used to make chrome plating on cars?", "options": ["Cr", "V", "Mn", "Ti"], "ans": "Cr"}
        ]},
        7: {"name": "Precious Metals", "type": "Jewelry", "data": [
            {"id": 1, "q": "What is the chemical symbol for Gold (No. 79)?", "options": ["Gd", "Go", "Au", "Ag"], "ans": "Au"},
            {"id": 2, "q": "Which metal (No. 47) is the best conductor of electricity?", "options": ["Au", "Ag", "Cu", "Al"], "ans": "Ag"},
            {"id": 3, "q": "Which precious metal (No. 78) is used in catalytic converters?", "options": ["Pd", "Pu", "Pt", "Pa"], "ans": "Pt"},
            {"id": 4, "q": "What is the symbol for Silver?", "options": ["Au", "Pt", "Ag", "Hg"], "ans": "Ag"},
            {"id": 5, "q": "What is the Atomic Number of Gold?", "options": ["47", "78", "79", "80"], "ans": "79"}
        ]},
        8: {"name": "Post-Transition", "type": "Heavy Metals", "data": [
            {"id": 1, "q": "What is the symbol for Lead (No. 82)?", "options": ["Pd", "P", "Pb", "Li"], "ans": "Pb"},
            {"id": 2, "q": "Which lightweight metal (No. 13) is used in foil and cans?", "options": ["Mg", "Al", "Si", "Ga"], "ans": "Al"},
            {"id": 3, "q": "What is the chemical symbol for Tin (No. 50)?", "options": ["Ti", "Tn", "Sn", "Sb"], "ans": "Sn"},
            {"id": 4, "q": "Which heavy metal (No. 82) was used in old pipes and paint?", "options": ["Hg", "Pb", "Cd", "Bi"], "ans": "Pb"},
            {"id": 5, "q": "What is the symbol for Bismuth (No. 83)?", "options": ["Bs", "Bi", "Bt", "Bm"], "ans": "Bi"}
        ]},
        9: {"name": "Trends", "type": "Navigation", "data": [
            {"id": 1, "q": "What do we call a vertical column in the periodic table?", "options": ["Period", "Group", "Block", "Shell"], "ans": "Group"},
            {"id": 2, "q": "What do we call a horizontal row in the periodic table?", "options": ["Group", "Period", "Family", "Orbit"], "ans": "Period"},
            {"id": 3, "q": "How many Periods are there in the standard table?", "options": ["5", "7", "8", "18"], "ans": "7"},
            {"id": 4, "q": "How many Groups are there in the standard table?", "options": ["7", "10", "18", "32"], "ans": "18"},
            {"id": 5, "q": "Moving from left to right, the Atomic Number usually...?", "options": ["Decreases", "Increases", "Stays Same", "Varies"], "ans": "Increases"}
        ]},
        10: {"name": "Heavy Elements", "type": "Actinides", "data": [
            {"id": 1, "q": "Which radioactive metal (No. 92) is used as nuclear fuel?", "options": ["Th", "Pu", "U", "Ra"], "ans": "U"},
            {"id": 2, "q": "What is the symbol for Plutonium (No. 94)?", "options": ["Pl", "Pt", "Pu", "Po"], "ans": "Pu"},
            {"id": 3, "q": "Which element (No. 88) was discovered by Marie Curie?", "options": ["U", "Ra", "Th", "Rn"], "ans": "Ra"},
            {"id": 4, "q": "What is the symbol for Thorium (No. 90)?", "options": ["Th", "Tm", "Ti", "Tb"], "ans": "Th"},
            {"id": 5, "q": "Which is the last naturally occurring element (No. 92)?", "options": ["U", "Np", "Pu", "Am"], "ans": "U"}
        ]}
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

# 5. INITIALIZATION & AUDIO
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

st.markdown("""
<div class="instruction-box">
    <b>📖 HOW TO PLAY:</b><br>
    1. Click <b>SPIN</b> to select a random question slot (1-20).<br>
    2. Analyze the challenge and select the correct chemical symbol.<br>
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
             
