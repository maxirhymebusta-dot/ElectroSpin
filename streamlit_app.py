import streamlit as st
import random
import time

# --- 1. PAGE SETUP & THEME ADAPTIVE STYLING ---
st.set_page_config(page_title="ElectroSpin: Master the Cell", page_icon="⚗️", layout="wide")

st.markdown("""
    <style>
    /* Adaptive Background & Text */
    :root {
        --bg-panel: rgba(255, 255, 255, 0.05);
        --accent: #00d4ff;
    }
    
    .main {
        background-image: radial-gradient(#2c3e50 0.5px, transparent 0.5px);
        background-size: 30px 30px;
    }

    /* Glassmorphism Effect for Lab Cards */
    .lab-card {
        background: var(--bg-panel);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 20px;
    }

    .instruction-step {
        background: #007bff22;
        padding: 10px;
        border-left: 4px solid #007bff;
        margin-bottom: 10px;
        border-radius: 5px;
    }

    .timer-text {
        font-family: 'Courier New', monospace;
        font-size: 40px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
    }

    /* Animation for the Spin Wheel */
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .spinning-icon {
        font-size: 50px;
        display: inline-block;
        animation: spin 1s infinite linear;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE SIMPLIFIED CONCEPT DATABASE ---
if 'levels' not in st.session_state:
    st.session_state.levels = [
        {
            "id": 1,
            "mission": "Making Shiny Jewelry (Silver Plating)",
            "goal": "Coating a Spoon with Silver",
            "hint": "The object you want to COAT goes at the Cathode (-). The metal you are USING to coat goes at the Anode (+).",
            "solution": {"el": "Silver Nitrate", "an": "Pure Silver", "ca": "Steel Spoon"},
            "explanation": "Silver ions (Ag⁺) swim to the spoon (Cathode) and turn into solid silver!",
            "points": 100
        },
        {
            "id": 2,
            "mission": "The Salt Splitter (Brine)",
            "goal": "Get Chlorine Gas from Salt Water",
            "hint": "Chlorine is a non-metal, so it's an Anion (-). Anions are attracted to the Anode (+).",
            "solution": {"el": "Concentrated NaCl (Brine)", "an": "Graphite", "ca": "Graphite"},
            "explanation": "Chloride ions lose electrons at the Anode to become Chlorine gas bubbles.",
            "points": 200
        }
    ]

# --- 3. SESSION STATES ---
if 'step' not in st.session_state: st.session_state.step = "instructions"
if 'current_level' not in st.session_state: st.session_state.current_level = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'wheel_spun' not in st.session_state: st.session_state.wheel_spun = False

# --- 4. GAME SCREENS ---

# SCREEN 1: INSTRUCTIONS
if st.session_state.step == "instructions":
    st.title("🧪 Welcome to ElectroSpin")
    st.markdown("### How to Play:")
    st.markdown("""
    <div class='instruction-step'>1. <b>Spin the Wheel:</b> Unlock the chemicals needed for the lab.</div>
    <div class='instruction-step'>2. <b>Assemble the Cell:</b> You have <b>30 seconds</b> to pick the right Electrolyte, Anode, and Cathode.</div>
    <div class='instruction-step'>3. <b>Apply Current:</b> Hit the button to see if your chemistry logic works!</div>
    <div class='instruction-step'>4. <b>Learn:</b> Check the 'Explanation' box to understand <i>why</i> it worked.</div>
    """, unsafe_allow_html=True)
    
    if st.button("I'M READY - START LAB"):
        st.session_state.step = "game"
        st.rerun()

# SCREEN 2: THE GAME
elif st.session_state.step == "game":
    level = st.session_state.levels[st.session_state.current_level]
    
    st.sidebar.metric("Lab Score", st.session_state.score)
    st.sidebar.write(f"**Level {level['id']}**")
    
    st.markdown(f"## 🔬 Mission: {level['mission']}")
    st.info(f"**Your Goal:** {level['goal']}")

    # Phase A: The Spin
    if not st.session_state.wheel_spun:
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        if st.button("🎡 SPIN FOR MATERIALS"):
            placeholder = st.empty()
            items = ["H₂O", "NaCl", "AgNO₃", "CuSO₄", "Pt", "Au"]
            for _ in range(10):
                placeholder.markdown(f"<div class='spinning-icon'>🌀</div><br>Searching: **{random.choice(items)}**", unsafe_allow_html=True)
                time.sleep(0.1)
            st.session_state.wheel_spun = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # Phase B: The Countdown & Setup
    else:
        # 30s Timer
        timer_place = st.empty()
        
        # UI
        st.markdown("<div class='lab-card'>", unsafe_allow_html=True)
        st.warning(f"**Teacher's Hint:** {level['hint']}")
        
        col1, col2, col3 = st.columns(3)
        with col1: el = st.selectbox("Electrolyte (Liquid)", ["Water", "Silver Nitrate", "Concentrated NaCl (Brine)", "Molten Lead Bromide"])
        with col2: an = st.selectbox("Anode (+ Terminal)", ["Graphite", "Pure Silver", "Platinum", "Impure Copper"])
        with col3: ca = st.selectbox("Cathode (- Terminal)", ["Graphite", "Steel Spoon", "Pure Copper Strip", "Aluminum"])
        
        submit = st.button("⚡ APPLY VOLTAGE")
        st.markdown("</div>", unsafe_allow_html=True)

        if not submit:
            for t in range(30, -1, -1):
                timer_place.markdown(f"<div class='timer-text'>{t}s</div>", unsafe_allow_html=True)
                time.sleep(1)
                if t == 0:
                    st.error("Time Out! The experiment failed.")
                    if st.button("Retry Level"): st.rerun()
                    st.stop()

        if submit:
            if el == level['solution']['el'] and an == level['solution']['an'] and ca == level['solution']['ca']:
                st.balloons()
                st.success(f"Success! +{level['points']} Points")
                st.markdown(f"**Why it worked:** {level['explanation']}")
                st.session_state.score += level['points']
                
                if st.session_state.current_level < len(st.session_state.levels) - 1:
                    if st.button("Next Level"):
                        st.session_state.current_level += 1
                        st.session_state.wheel_spun = False
                        st.rerun()
                else:
                    st.session_state.step = "win"
                    st.rerun()
            else:
                st.error("Wrong Setup! The ions are confused. Try again!")
                if st.button("Reset Level"):
                    st.session_state.wheel_spun = False
                    st.rerun()

# SCREEN 3: WIN
elif st.session_state.step == "win":
    st.title("🏆 Lab Certified!")
    st.write(f"Final Score: {st.session_state.score}")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2I4N2I4OWUzN2NlMzM4NTViM2E4MzU4Zjk3NjFlZTViMzE4MGM1NiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/3o72F8t9TDi2xVnxOE/giphy.gif")
    if st.button("Play Again"):
        st.session_state.step = "instructions"
        st.session_state.score = 0
        st.session_state.current_level = 0
        st.rerun()
        
