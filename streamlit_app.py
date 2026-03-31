import streamlit as st
import time
import random

# --- 1. ADAPTIVE THEME & ADVENTURE UI ---
st.set_page_config(page_title="Ion Escape Room", page_icon="🏃‍♂️", layout="wide")

st.markdown("""
    <style>
    /* System Adaptive Glassmorphism */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #e94560;
    }
    .game-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
    }
    .timer-digital {
        font-family: 'Courier New', monospace;
        font-size: 50px;
        color: #00d4ff;
        text-shadow: 0 0 10px #00d4ff;
        text-align: center;
    }
    .ion-profile {
        background: #0f3460;
        padding: 15px;
        border-radius: 10px;
        border-bottom: 4px solid #e94560;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SS2 ION DATABASE ---
if 'level' not in st.session_state: st.session_state.level = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'game_state' not in st.session_state: st.session_state.game_state = "start"

levels = [
    {
        "ion": "Cu²⁺ (Copper Ion)",
        "location": "Aqueous Copper(II) Sulfate Solution",
        "rivals": "H⁺ (Hydrogen Ion)",
        "goal": "Reach the Cathode and become Copper Metal.",
        "options": ["Low Concentration / Carbon Electrode", "High Concentration / Copper Electrode", "Dilute / Platinum Electrode"],
        "correct": "High Concentration / Copper Electrode",
        "why": "Cu²⁺ is lower in the electrochemical series than H⁺, and using a Copper electrode (active) facilitates discharge!"
    },
    {
        "ion": "OH⁻ (Hydroxide Ion)",
        "location": "Dilute Sodium Chloride (Brine)",
        "rivals": "Cl⁻ (Chloride Ion)",
        "goal": "Reach the Anode and become Oxygen Gas.",
        "options": ["Very Concentrated Brine", "Dilute Brine / Graphite Electrode", "Molten NaCl"],
        "correct": "Dilute Brine / Graphite Electrode",
        "why": "In dilute solutions, OH⁻ is discharged in preference to Cl⁻ because it is higher in the series of anions."
    }
]

# --- 3. GAME SCREENS ---

if st.session_state.game_state == "start":
    st.markdown("<h1 style='text-align:center;'>🏃‍♂️ ION ESCAPE ROOM</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='game-card'>
    <h3>The Situation:</h3>
    <p>You are an <b>Ion</b> dissolved in a liquid. The battery has just been turned on! 
    You have <b>30 seconds</b> to navigate the chemical conditions and reach the electrode to be discharged.</p>
    <p>If you choose the wrong path, your rival ion will escape instead, and you stay trapped in the solution forever!</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("BEGIN ESCAPE"):
        st.session_state.game_state = "playing"
        st.rerun()

elif st.session_state.game_state == "playing":
    lvl = levels[st.session_state.level]
    
    col_info, col_timer = st.columns([2, 1])
    
    with col_info:
        st.markdown(f"""
        <div class='ion-profile'>
            <h2>Identity: {lvl['ion']}</h2>
            <p><b>Environment:</b> {lvl['location']}</p>
            <p><b>Rival Ion:</b> {lvl['rivals']}</p>
            <p><b>Mission:</b> {lvl['goal']}</p>
        </div>
        """, unsafe_allow_html=True)

    with col_timer:
        timer_place = st.empty()
    
    st.write("---")
    st.subheader("Choose your escape route:")
    choice = st.radio("Which lab conditions will allow YOU to be discharged?", lvl['options'])
    
    escape_btn = st.button("RUN TO THE ELECTRODE ⚡")

    # The 30s Countdown
    if not escape_btn:
        for t in range(30, -1, -1):
            timer_place.markdown(f"<div class='timer-digital'>{t}s</div>", unsafe_allow_html=True)
            time.sleep(1)
            if t == 0:
                st.error("⏰ THE POWER CUT OUT! You are trapped in the liquid.")
                if st.button("Restart Level"): st.rerun()
                st.stop()

    if escape_btn:
        if choice == lvl['correct']:
            st.balloons()
            st.success("🎉 ESCAPE SUCCESSFUL! You have been discharged.")
            st.info(f"<b>Chemistry Logic:</b> {lvl['why']}")
            st.session_state.score += 100
            
            if st.session_state.level < len(levels) - 1:
                if st.button("Next Level"):
                    st.session_state.level += 1
                    st.rerun()
            else:
                st.session_state.game_state = "won"
                st.rerun()
        else:
            st.error("❌ FAILED! Your rival was discharged instead. You remain an ion.")
            st.warning("Hint: Look at the Electrochemical Series. Which ion is easier to reduce/oxidize?")
            if st.button("Try Again"): st.rerun()

elif st.session_state.game_state == "won":
    st.markdown("<div class='game-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.title("🎓 MASTER OF IONS")
    st.write(f"You escaped every solution! Final Score: {st.session_state.score}")
    if st.button("Replay Game"):
        st.session_state.level = 0
        st.session_state.score = 0
        st.session_state.game_state = "start"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
