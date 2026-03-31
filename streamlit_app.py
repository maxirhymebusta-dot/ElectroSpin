import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sidebar Controls
st.sidebar.title("🎮 Lab Command Center")
enable_sounds = st.sidebar.toggle("Enable Laboratory Audio", value=True)
st.sidebar.info("Developed by Ukazim Chidinma Favour")

# 3. 10-Level Categorized Database (Complete Curriculum)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "The Non-Metals", "type": "Gas & Life Essentials", "data": [
            {"q": "Lightest element in the universe (1 proton)?", "options": ["H", "He", "Li", "O"], "ans": "H"},
            {"q": "Noble gas used in balloons (Atomic No. 2)?", "options": ["Ne", "Ar", "He", "H"], "ans": "He"},
            {"q": "Gas making up 78% of Earth's atmosphere?", "options": ["O", "N", "C", "Ar"], "ans": "N"},
            {"q": "Element essential for human respiration?", "options": ["C", "F", "O", "N"], "ans": "O"},
            {"q": "The primary basis of all organic chemistry?", "options": ["N", "O", "C", "P"], "ans": "C"}
        ]},
        2: {"name": "The Reactive Metals", "type": "Groups 1 & 2", "data": [
            {"q": "Group 1 metal used in phone batteries?", "options": ["Na", "Li", "K", "Be"], "ans": "Li"},
            {"q": "Atomic Number 11: Explodes in water?", "options": ["Mg", "K", "Na", "Li"], "ans": "Na"},
            {"q": "Found in bananas, Atomic Number 19?", "options": ["Na", "Ca", "K", "Li"], "ans": "K"},
            {"q": "Atomic Number 12: Burns with bright white light?", "options": ["Ca", "Al", "Mg", "Zn"], "ans": "Mg"},
            {"q": "Essential for bone strength (No. 20)?", "options": ["Mg", "Ca", "Sr", "Ba"], "ans": "Ca"}
        ]},
        3: {"name": "The Metalloid Bridge", "type": "The Staircase Elements", "data": [
            {"q": "Primary metalloid used in computer chips?", "options": ["Ge", "Si", "As", "B"], "ans": "Si"},
            {"q": "Metalloid with Atomic Number 5?", "options": ["B", "Al", "Si", "C"], "ans": "B"},
            {"q": "Which element is a semiconductor in Group 14?", "options": ["C", "Si", "P", "Al"], "ans": "Si"},
            {"q": "Element used in rat poison and semiconductors (No. 33)?", "options": ["Sb", "As", "Te", "Po"], "ans": "As"},
            {"q": "The metalloid often used in infrared devices (No. 32)?", "options": ["Si", "Ge", "B", "Sb"], "ans": "Ge"}
        ]},
        4: {"name": "The Halogens", "type": "Group 17 (Reactive Non-metals)", "data": [
            {"q": "Most electronegative element on the table?", "options": ["Cl", "F", "O", "N"], "ans": "F"},
            {"q": "Halogen used to disinfect swimming pools?", "options": ["F", "Cl", "Br", "I"], "ans": "Cl"},
            {"q": "Only non-metal element that is liquid at room temp?", "options": ["Hg", "Br", "Cl", "I"], "ans": "Br"},
            {"q": "Halogen used as an antiseptic in medicine (No. 53)?", "options": ["Cl", "Br", "I", "At"], "ans": "I"},
            {"q": "Which Halogen is a dark grey solid that sublimes to purple vapor?", "options": ["Br", "I", "Cl", "F"], "ans": "I"}
        ]},
        5: {"name": "The Noble Gases", "type": "Group 18 (Inert Gases)", "data": [
            {"q": "Which Noble Gas is used in orange-red neon signs?", "options": ["Ar", "Kr", "Ne", "Xe"], "ans": "Ne"},
            {"q": "The most abundant Noble Gas in Earth's atmosphere?", "options": ["He", "Ne", "Ar", "Rn"], "ans": "Ar"},
            {"q": "Noble Gas with Atomic Number 36?", "options": ["Ar", "Kr", "Xe", "Rn"], "ans": "Kr"},
            {"q": "Which Noble Gas is radioactive and can seep into basements?", "options": ["Xe", "Rn", "Kr", "Ar"], "ans": "Rn"},
            {"q": "Noble Gas used in high-speed photographic flashes?", "options": ["He", "Ar", "Ne", "Xe"], "ans": "Xe"}
        ]},
        6: {"name": "Transition Metals (Part A)", "type": "The D-Block Elements", "data": [
            {"q": "Which transition metal has the symbol Fe?", "options": ["F", "Fr", "Fe", "Ir"], "ans": "Fe"},
            {"q": "Metal with Atomic Number 29, used in wiring?", "options": ["Cu", "Zn", "Ni", "Co"], "ans": "Cu"},
            {"q": "The main component of steel?", "options": ["Cr", "Fe", "Mn", "Ni"], "ans": "Fe"},
            {"q": "Transition metal used in galvanizing steel (No. 30)?", "options": ["Cd", "Zn", "Pb", "Sn"], "ans": "Zn"},
            {"q": "Which metal gives emeralds their green color (No. 24)?", "options": ["Cr", "V", "Mn", "Ti"], "ans": "Cr"}
        ]},
        7: {"name": "The Precious Metals", "type": "Coinage & Jewelry Metals", "data": [
            {"q": "What is the chemical symbol for Gold?", "options": ["Gd", "Go", "Au", "Ag"], "ans": "Au"},
            {"q": "Which metal is the best conductor of electricity?", "options": ["Au", "Ag", "Cu", "Al"], "ans": "Ag"},
            {"q": "Metal with the symbol Pt, used in catalytic converters?", "options": ["Pd", "Pu", "Pt", "Pa"], "ans": "Pt"},
            {"q": "Atomic Number 47 belongs to which metal?", "options": ["Au", "Pt", "Ag", "Hg"], "ans": "Ag"},
            {"q": "What is the Atomic Number of Gold?", "options": ["47", "78", "79", "80"], "ans": "79"}
        ]},
        8: {"name": "Post-Transition Metals", "type": "The Poor Metals", "data": [
            {"q": "Which metal has the symbol Pb?", "options": ["Pd", "P", "Pb", "Li"], "ans": "Pb"},
            {"q": "Metal with Atomic Number 13?", "options": ["Mg", "Al", "Si", "Ga"], "ans": "Al"},
            {"q": "The symbol for Tin is?", "options": ["Ti", "Tn", "Sn", "Sb"], "ans": "Sn"},
            {"q": "Which heavy metal was historically used in pipes and paint?", "options": ["Hg", "Pb", "Cd", "Bi"], "ans": "Pb"},
            {"q": "What is the symbol for Bismuth?", "options": ["Bs", "Bi", "Bt", "Bm"], "ans": "Bi"}
        ]},
        9: {"name": "Periods & Trends", "type": "Periodic Table Navigation", "data": [
            {"q": "Elements in the same vertical column belong to the same...?", "options": ["Period", "Group", "Block", "Shell"], "ans": "Group"},
            {"q": "Elements in the same horizontal row belong to the same...?", "options": ["Group", "Period", "Family", "Orbit"], "ans": "Period"},
            {"q": "How many periods are in the standard periodic table?", "options": ["5", "7", "8", "18"], "ans": "7"},
            {"q": "How many groups are in the standard periodic table?", "options": ["7", "10", "18", "32"], "ans": "18"},
            {"q": "As you move left to right, Atomic Number generally...?", "options": ["Decreases", "Increases", "Stays Same", "Fluctuates"], "ans": "Increases"}
        ]},
        10: {"name": "The Heavy Elements", "type": "Lanthanides & Actinides", "data": [
            {"q": "Which radioactive element is used in nuclear power (No. 92)?", "options": ["Th", "Pu", "U", "Ra"], "ans": "U"},
            {"q": "What is the symbol for Plutonium?", "options": ["Pl", "Pt", "Pu", "Po"], "ans": "Pu"},
            {"q": "The element discovered by Marie Curie (No. 88)?", "options": ["U", "Ra", "Th", "Rn"], "ans": "Ra"},
            {"q": "The symbol for Thorium is?", "options": ["Th", "Tm", "Ti", "Tb"], "ans": "Th"},
            {"q": "Which element is the last natural element (No. 92)?", "options": ["U", "Np", "Pu", "Am"], "ans": "U"}
        ]}
    }

# 4. Custom CSS for Visual Design
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
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
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 10px; font-weight: bold; width: 100%; }
.footer { text-align: center; padding: 40px; color: #aaa; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 5. Audio Setup Logic
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

def get_wheel_html(rotation):
    nums = "".join([f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({i*18-9}deg) translateY(-120px) rotate(-{i*18-9}deg);">{i}</div>' for i in range(1, 21)])
    return f'<div class="wheel-container"><div class="wheel-pointer"></div><div class="wheel" style="transform: rotate({rotation}deg);">{nums}</div></div>'

# --- INTERFACE ---
st.markdown('<h1 class="main-title">🧪 Periodic Master: Spin Quest</h1>', unsafe_allow_html=True)

if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 Level {st.session_state.level}: {lvl['name']} ({lvl['type']})")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(get_wheel_html(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN FOR A CHALLENGE"):
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
    
    if st.button("SUBMIT ANALYSIS"):
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
    
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Review: {item['q'][:40]}..."):
            st.write(f"**Question:** {item['q']}")
            st.success(f"**Correct Symbol:** {item['ans']}")

    if st.button("Unlock Next Chemical Gate"):
        if st.session_state.level < 10:
            st.session_state.level += 1
            st.session_state.q_idx = 0
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST CERTIFIED")
    st.metric("Final Proficiency Score", f"{st.session_state.score} / 1000")
    if st.button("Restart Journey"):
        st.session_state.level = 1
        st.session_state.score = 0
        st.session_state.q_idx = 0
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
