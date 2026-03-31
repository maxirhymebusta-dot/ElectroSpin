import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
enable_sounds = st.sidebar.toggle("Enable Laboratory Audio", value=True)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. FULL 10-LEVEL DATABASE (Ensures all keys 1-10 exist to prevent KeyError)
RAW_DATA = {
    1: {"name": "The Non-Metals", "type": "Gas & Life Essentials", "data": [
        {"id": 1, "q": "Lightest element in the universe (1 proton)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
        {"id": 2, "q": "Noble gas used in balloons (Atomic No. 2)?", "options": ["Ne", "Ar", "He", "H"], "ans": "He"},
        {"id": 3, "q": "Gas making up 78% of Earth's atmosphere?", "options": ["O", "N", "C", "Ar"], "ans": "N"},
        {"id": 4, "q": "Element essential for human respiration?", "options": ["C", "F", "O", "N"], "ans": "O"},
        {"id": 5, "q": "The primary basis of all organic life?", "options": ["N", "O", "C", "P"], "ans": "C"}
    ]},
    2: {"name": "The Reactive Metals", "type": "Groups 1 & 2", "data": [
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
    4: {"name": "The Halogens", "type": "Group 17", "data": [
        {"id": 1, "q": "Most electronegative element?", "options": ["Cl", "F", "O", "N"], "ans": "F"},
        {"id": 2, "q": "Halogen used to disinfect pools?", "options": ["F", "Cl", "Br", "I"], "ans": "Cl"},
        {"id": 3, "q": "Only liquid non-metal at room temp?", "options": ["Hg", "Br", "Cl", "I"], "ans": "Br"},
        {"id": 4, "q": "Halogen used as an antiseptic (No. 53)?", "options": ["Cl", "Br", "I", "At"], "ans": "I"},
        {"id": 5, "q": "Solid Halogen that sublimes to purple?", "options": ["Br", "I", "Cl", "F"], "ans": "I"}
    ]},
    5: {"name": "The Noble Gases", "type": "Group 18", "data": [
        {"id": 1, "q": "Noble Gas used in orange neon signs?", "options": ["Ar", "Kr", "Ne", "Xe"], "ans": "Ne"},
        {"id": 2, "q": "Most abundant Noble Gas in air?", "options": ["He", "Ne", "Ar", "Rn"], "ans": "Ar"},
        {"id": 3, "q": "Noble Gas with Atomic Number 36?", "options": ["Ar", "Kr", "Xe", "Rn"], "ans": "Kr"},
        {"id": 4, "q": "Radioactive Noble Gas (basements)?", "options": ["Xe", "Rn", "Kr", "Ar"], "ans": "Rn"},
        {"id": 5, "q": "Used in high-speed flash photography?", "options": ["He", "Ar", "Ne", "Xe"], "ans": "Xe"}
    ]},
    6: {"name": "Transition Metals A", "type": "D-Block", "data": [
        {"id": 1, "q": "Transition metal with symbol Fe?", "options": ["F", "Fr", "Fe", "Ir"], "ans": "Fe"},
        {"id": 2, "q": "Used in electrical wiring (No. 29)?", "options": ["Cu", "Zn", "Ni", "Co"], "ans": "Cu"},
        {"id": 3, "q": "Main component of steel?", "options": ["Cr", "Fe", "Mn", "Ni"], "ans": "Fe"},
        {"id": 4, "q": "Used in galvanizing steel (No. 30)?", "options": ["Cd", "Zn", "Pb", "Sn"], "ans": "Zn"},
        {"id": 5, "q": "Gives emeralds green color (No. 24)?", "options": ["Cr", "V", "Mn", "Ti"], "ans": "Cr"}
    ]},
    7: {"name": "The Precious Metals", "type": "Coinage Metals", "data": [
        {"id": 1, "q": "Chemical symbol for Gold?", "options": ["Gd", "Go", "Au", "Ag"], "ans": "Au"},
        {"id": 2, "q": "Best conductor of electricity?", "options": ["Au", "Ag", "Cu", "Al"], "ans": "Ag"},
        {"id": 3, "q": "Used in catalytic converters (Pt)?", "options": ["Pd", "Pu", "Pt", "Pa"], "ans": "Pt"},
        {"id": 4, "q": "Atomic Number 47 (Silver)?", "options": ["Au", "Pt", "Ag", "Hg"], "ans": "Ag"},
        {"id": 5, "q": "Atomic Number of Gold?", "options": ["47", "78", "79", "80"], "ans": "79"}
    ]},
    8: {"name": "Post-Transition Metals", "type": "Poor Metals", "data": [
        {"id": 1, "q": "Metal with symbol Pb?", "options": ["Pd", "P", "Pb", "Li"], "ans": "Pb"},
        {"id": 2, "q": "Metal with Atomic Number 13?", "options": ["Mg", "Al", "Si", "Ga"], "ans": "Al"},
        {"id": 3, "q": "The symbol for Tin is?", "options": ["Ti", "Tn", "Sn", "Sb"], "ans": "Sn"},
        {"id": 4, "q": "Heavy metal used in old paint?", "options": ["Hg", "Pb", "Cd", "Bi"], "ans": "Pb"},
        {"id": 5, "q": "What is the symbol for Bismuth?", "options": ["Bs", "Bi", "Bt", "Bm"], "ans": "Bi"}
    ]},
    9: {"name": "Periods & Trends", "type": "Navigation", "data": [
        {"id": 1, "q": "A vertical column is a...?", "options": ["Period", "Group", "Block", "Shell"], "ans": "Group"},
        {"id": 2, "q": "A horizontal row is a...?", "options": ["Group", "Period", "Family", "Orbit"], "ans": "Period"},
        {"id": 3, "q": "How many periods are in the table?", "options": ["5", "7", "8", "18"], "ans": "7"},
        {"id": 4, "q": "How many groups are in the table?", "options": ["7", "10", "18", "32"], "ans": "18"},
        {"id": 5, "q": "As you move R to L, Atomic No...?", "options": ["Decreases", "Increases", "Same", "None"], "ans": "Decreases"}
    ]},
    10: {"name": "The Heavy Elements", "type": "Actinides", "data": [
        {"id": 1, "q": "Fuel in nuclear power (No. 92)?", "options": ["Th", "Pu", "U", "Ra"], "ans": "U"},
        {"id": 2, "q": "Symbol for Plutonium?", "options": ["Pl", "Pt", "Pu", "Po"], "ans": "Pu"},
        {"id": 3, "q": "Element discovered by Curie (No. 88)?", "options": ["U", "Ra", "Th", "Rn"], "ans": "Ra"},
        {"id": 4, "q": "Symbol for Thorium?", "options": ["Th", "Tm", "Ti", "Tb"], "ans": "Th"},
        {"id": 5, "q": "Last natural element (No. 92)?", "options": ["U", "Np", "Pu", "Am"], "ans": "U"}
    ]}
}

# 4. FIXED INITIALIZATION (Prevents KeyError)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = RAW_DATA

if 'level' not in st.session_state or st.session_state.level not in st.session_state.levels_data:
    st.session_state.level = 1

# 5. ALL ORIGINAL CSS (Background + Heading + Wheel)
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
.stApp { background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e); background-size: 400% 400%; animation: gradientBG 15s ease infinite; }
.main-title { text-align: center; color: #00d2ff !important; font-size: 45px; font-weight: 800; text-shadow: 0 0 15px #00d2ff; }
.wheel-container { display: flex; justify-content: center; align-items: center; height: 380px; position: relative; }
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700; position: relative; overflow: hidden;
    background: conic-gradient(from 0deg, #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%, #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%, #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%, #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%);
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 14px; pointer-events: none; }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 10px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# 6. ALL ORIGINAL SESSION STATE
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0

def play_audio(url):
    if enable_sounds: st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

if enable_sounds: st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-120px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- MAIN INTERFACE ---
st.markdown('<h1 class="main-title">🧪 Periodic Master: Spin Quest</h1>', unsafe_allow_html=True)

# Check for mode logic
if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 Level {st.session_state.level}: {lvl['name']}")
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    if st.button("🚀 SPIN FOR A CHALLENGE"):
        play_audio("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        random_slot = random.randint(1, 20)
        target_stop = -( (random_slot - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Analyzing Atomic Data...") as status:
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
            st.success("✅ CORRECT!"); play_audio("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.score += 20
        else:
            st.error(f"❌ INCORRECT!"); play_audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        st.session_state.q_idx += 1
        time.sleep(2)
        st.session_state.mode = "spin" if st.session_state.q_idx < 5 else "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons(); st.header("🏁 Level Results")
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Fact Check: {item['q'][:30]}..."):
            st.write(item['q']); st.success(f"Answer: {item['ans']}")
    if st.button("Next Level"):
        if st.session_state.level < 10:
            st.session_state.level += 1; st.session_state.q_idx = 0; st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST!"); st.metric("Score", f"{st.session_state.score} / 1000")
    if st.button("Restart"):
        st.session_state.level = 1; st.session_state.score = 0; st.session_state.q_idx = 0; st.session_state.mode = "spin"; st.rerun()

st.markdown('<div style="text-align:center; padding:40px; color:#888; font-style:italic;">Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
