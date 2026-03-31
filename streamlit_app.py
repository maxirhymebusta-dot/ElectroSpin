import streamlit as st
import random
import time

# --- 1. PAGE SETUP & BRANDING ---
st.set_page_config(page_title="ElectroSpin: Master the Cell", page_icon="⚡", layout="centered")

# Custom CSS for a Professional Chemistry Lab Look
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f9; }
    .main-title { color: #003366; text-align: center; font-family: 'Arial Black'; font-size: 42px; margin-bottom: 0px; }
    .timer-box { font-size: 32px; font-weight: bold; color: #e74c3c; text-align: center; background: white; padding: 10px; border-radius: 15px; border: 3px solid #e74c3c; margin: 10px 0; }
    .score-display { font-size: 20px; color: #27ae60; font-weight: bold; text-align: center; }
    .lab-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 20px; }
    .wheel-zone { height: 120px; display: flex; align-items: center; justify-content: center; background: #2c3e50; color: #3498db; font-size: 24px; font-weight: bold; border-radius: 50% 50% 5px 5px; border-bottom: 5px solid #3498db; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GAME DATA (MSc Level Content) ---
if 'levels' not in st.session_state:
    st.session_state.levels = [
        {
            "id": 1,
            "mission": "Decompose Molten Lead(II) Bromide",
            "goal": "Collect Lead (Pb) at the Cathode",
            "solution": {"el": "Molten Lead(II) Bromide", "an": "Graphite", "ca": "Graphite"},
            "points": 100,
            "fact": "Pb²⁺ + 2e⁻ → Pb (Reduction at Cathode) | 2Br⁻ → Br₂ + 2e⁻ (Oxidation at Anode)"
        },
        {
            "id": 2,
            "mission": "Industrial Purification of Copper",
            "goal": "Transfer Copper from Impure to Pure electrode",
            "solution": {"el": "Copper(II) Sulfate", "an": "Impure Copper", "ca": "Pure Copper Strip"},
            "points": 200,
            "fact": "The Impure Anode dissolves into ions, which then plate onto the Pure Cathode."
        },
        {
            "id": 3,
            "mission": "Electroplating a Steel Medal with Gold",
            "goal": "Create a luxury finish on a base metal",
            "solution": {"el": "Gold Cyanide Solution", "an": "Pure Gold", "ca": "Steel Medal"},
            "points": 300,
            "fact": "The object to be plated MUST be the Cathode (-) to attract the positive metal ions."
        }
    ]

# --- 3. STATE INITIALIZATION ---
if 'current_level' not in st.session_state: st.session_state.current_level = 0
if 'total_score' not in st.session_state: st.session_state.total_score = 0
if 'spin_state' not in st.session_state: st.session_state.spin_state = "idle" # idle, spinning, done
if 'game_over' not in st.session_state: st.session_state.game_over = False

# --- 4. GAME HEADER ---
st.markdown("<h1 class='main-title'>⚡ ElectroSpin</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='score-display'>🏆 Total Lab Score: {st.session_state.total_score}</p>", unsafe_allow_html=True)

# --- 5. THE GAME LOOP ---
if not st.session_state.game_over:
    level_data = st.session_state.levels[st.session_state.current_level]
    
    st.markdown(f"### 🔬 Level {level_data['id']}: {level_data['mission']}")
    st.write(f"**Objective:** {level_data['goal']}")

    # --- PHASE 1: THE SPIN WHEEL ---
    if st.session_state.spin_state == "idle":
        st.info("The lab equipment is locked. Spin the wheel to select your materials!")
        if st.button("🎡 SPIN THE CHEMICAL WHEEL"):
            st.session_state.spin_state = "spinning"
            st.rerun()

    elif st.session_state.spin_state == "spinning":
        items = ["Gold Cyanide", "Graphite", "Lead Bromide", "Copper Sulfate", "Pure Gold", "Steel Medal", "Impure Copper"]
        wheel_placeholder = st.empty()
        for _ in range(10):
            pick = random.choice(items)
            wheel_placeholder.markdown(f"<div class='wheel-zone'>🌀 SPINNING...<br>{pick}</div>", unsafe_allow_html=True)
            time.sleep(0.15)
        st.session_state.spin_state = "done"
        st.rerun()

    # --- PHASE 2: THE 30s CHALLENGE ---
    elif st.session_state.spin_state == "done":
        # Sidebar timer to keep the main area clean
        timer_placeholder = st.empty()
        
        # UI for selection
        with st.container():
            st.markdown("<div class='lab-card'>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            with c1:
                u_el = st.selectbox("Electrolyte", ["Water", "Molten Lead(II) Bromide", "Copper(II) Sulfate", "Gold Cyanide Solution"])
            with c2:
                u_an = st.selectbox("Anode (+)", ["Graphite", "Impure Copper", "Pure Gold", "Platinum"])
            with c3:
                u_ca = st.selectbox("Cathode (-)", ["Graphite", "Pure Copper Strip", "Steel Medal", "Lead Rod"])
            
            submit = st.button("⚡ INITIATE ELECTROLYSIS")
            st.markdown("</div>", unsafe_allow_html=True)

        # The Countdown Logic
        # (Only runs if user hasn't submitted yet)
        if not submit:
            for t in range(30, -1, -1):
                timer_placeholder.markdown(f"<div class='timer-box'>⏳ {t}s</div>", unsafe_allow_html=True)
                time.sleep(1)
                if t == 0:
                    st.error("⏰ TIME EXPIRED! The electrolyte has solidified. Restarting level...")
                    time.sleep(2)
                    st.session_state.spin_state = "idle"
                    st.rerun()
        
        # Evaluation
        if submit:
            correct = level_data['solution']
            if u_el == correct['el'] and u_an == correct['an'] and u_ca == correct['ca']:
                st.balloons()
                st.session_state.total_score += level_data['points']
                st.success(f"✅ EXCELLENT! Level {level_data['id']} Complete.")
                st.markdown(f"**📚 Key Concept:** {level_data['fact']}")
                
                if st.session_state.current_level < len(st.session_state.levels) - 1:
                    if st.button("Proceed to Next Experiment ➡️"):
                        st.session_state.current_level += 1
                        st.session_state.spin_state = "idle"
                        st.rerun()
                else:
                    st.session_state.game_over = True
                    st.rerun()
            else:
                st.error("❌ Circuit Incomplete! Wrong components selected. Try spinning again.")
                if st.button("Retry Level"):
                    st.session_state.spin_state = "idle"
                    st.rerun()

# --- 6. GAME OVER SCREEN ---
else:
    st.balloons()
    st.markdown("<div class='lab-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("## 🎓 MSc Project Complete!")
    st.write(f"Congratulations, you have mastered the fundamentals of Electrolysis.")
    st.markdown(f"### Final Score: {st.session_state.total_score} Points")
    if st.button("Restart Journey"):
        st.session_state.current_level = 0
        st.session_state.total_score = 0
        st.session_state.spin_state = "idle"
        st.session_state.game_over = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
        
