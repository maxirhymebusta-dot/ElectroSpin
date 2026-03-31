import streamlit as st
import time
import random

# --- 1. SETTING THE SCENE (Cyber-Chemistry Theme) ---
st.set_page_config(page_title="Ionic Pulse", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #050505; color: #00ffcc; }
    .pulse-container {
        border: 2px solid #00ffcc;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        background: rgba(0, 255, 204, 0.05);
        box-shadow: 0 0 20px #00ffcc;
    }
    .ion-float { font-size: 50px; font-weight: bold; text-shadow: 0 0 10px #fff; }
    .timer-bar { font-size: 60px; font-family: 'Orbitron', sans-serif; color: #ff0055; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE SOUND ENGINE (Embedded HTML5) ---
def play_sound(type):
    if type == "success":
        # High pitch beep
        st.components.v1.html("""
            <audio autoplay><source src="https://actions.google.com/sounds/v1/foley/beeps_short_high.ogg" type="audio/ogg"></audio>
        """, height=0)
    elif type == "fail":
        # Low buzz
        st.components.v1.html("""
            <audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>
        """, height=0)

# --- 3. GAME STATE ---
if 'score' not in st.session_state: st.session_state.score = 0
if 'health' not in st.session_state: st.session_state.health = 100
if 'playing' not in st.session_state: st.session_state.playing = False

# --- 4. GAME HEADER ---
st.title("⚡ IONIC PULSE: SS2 DEFENDER")
col1, col2 = st.columns(2)
col1.metric("CURRENT FLOW (HEALTH)", f"{st.session_state.health}%")
col2.metric("VOLTAGE SCORE", st.session_state.score)

# --- 5. THE GAMEPLAY LOOP ---
if not st.session_state.playing:
    st.markdown("""
    <div class='pulse-container'>
        <h2>INSTRUCTIONS</h2>
        <p>1. An Ion will appear at the center of the tank.</p>
        <p>2. You have <b>5 seconds</b> per ion to decide which electrode it belongs to.</p>
        <p>3. If you miss or choose wrong, the circuit breaks!</p>
        <p><i>(Turn your volume UP for game sounds)</i></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🔌 PLUG IN & START"):
        st.session_state.playing = True
        st.rerun()

else:
    # Randomly pick an Ion from SS2 Curriculum
    ion_list = [
        {"name": "Cu²⁺", "type": "Cation", "target": "Cathode (-)", "fact": "Copper ions are reduced to metal."},
        {"name": "Cl⁻", "type": "Anion", "target": "Anode (+)", "fact": "Chloride ions are oxidized to gas."},
        {"name": "H⁺", "type": "Cation", "target": "Cathode (-)", "fact": "Hydrogen ions form gas bubbles."},
        {"name": "SO₄²⁻", "type": "Anion", "target": "Stay in Solution", "fact": "Sulfate ions are usually not discharged in dilute soln."}
    ]
    
    current_ion = random.choice(ion_list)
    
    st.markdown(f"<div class='pulse-container'><div class='ion-float'>{current_ion['name']}</div></div>", unsafe_allow_html=True)
    
    # 30-Second Overall Session Timer (Visual Countdown)
    timer_place = st.empty()
    
    st.write("### WHERE DOES THIS ION GO?")
    c1, c2, c3 = st.columns(3)
    
    # Action Buttons
    btn_anode = c1.button("ANODE (+)")
    btn_sol = c2.button("STAY IN SOLUTION")
    btn_cath = c3.button("CATHODE (-)")

    # Check Logic
    user_choice = None
    if btn_anode: user_choice = "Anode (+)"
    if btn_sol: user_choice = "Stay in Solution"
    if btn_cath: user_choice = "Cathode (-)"

    if user_choice:
        if user_choice == current_ion['target']:
            st.session_state.score += 10
            play_sound("success")
            st.success(f"CORRECT! {current_ion['fact']}")
            time.sleep(1)
            st.rerun()
        else:
            st.session_state.health -= 20
            play_sound("fail")
            st.error("CIRCUIT BREACH! Wrong Electrode.")
            time.sleep(1)
            if st.session_state.health <= 0:
                st.session_state.playing = False
                st.session_state.health = 100
                st.write("💀 LAB BLACKOUT. GAME OVER.")
            st.rerun()

    # Automatic Timeout for the specific ion
    for t in range(5, 0, -1):
        timer_place.markdown(f"<div class='timer-bar'>⚡ {t}</div>", unsafe_allow_html=True)
        time.sleep(0.5) # Fast paced
    
    # If no choice made
    st.session_state.health -= 10
    play_sound("fail")
    st.rerun()
    
