import streamlit as st
import time

# --- 1. THEME & SYSTEM ADAPTIVE UI ---
st.set_page_config(page_title="SS2 Electrolysis Lab", page_icon="🧪", layout="wide")

st.markdown("""
    <style>
    /* Adapts to Light/Dark Mode automatically */
    .main { padding: 2rem; }
    .stAlert { border-radius: 12px; }
    .lab-header { 
        background: linear-gradient(90deg, #2e7d32, #1b5e20); 
        color: white; 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center;
        margin-bottom: 25px;
    }
    .timer-display {
        font-size: 45px;
        font-family: 'Courier New', Courier, monospace;
        color: #d32f2f;
        text-align: center;
        font-weight: bold;
    }
    .equation-box {
        background-color: rgba(0,0,0,0.05);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SS2 CURRICULUM DATABASE ---
if 'level' not in st.session_state: st.session_state.level = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "instructions"

curriculum_tasks = [
    {
        "title": "Task 1: Electrolysis of Molten Lead(II) Bromide",
        "description": "Demonstrate the decomposition of a molten binary compound.",
        "correct": {"el": "Molten PbBr₂", "an": "Graphite", "ca": "Graphite"},
        "result": "Lead metal at Cathode, Red-brown Bromine gas at Anode.",
        "equation": "Cathode: Pb²⁺ + 2e⁻ → Pb(l)  |  Anode: 2Br⁻ → Br₂(g) + 2e⁻",
        "points": 50
    },
    {
        "title": "Task 2: Electrolysis of Acidified Water",
        "description": "Using a Hoffmann Voltameter to produce Hydrogen and Oxygen.",
        "correct": {"el": "Dilute H₂SO₄", "an": "Platinum", "ca": "Platinum"},
        "result": "Hydrogen (2 volumes) at Cathode, Oxygen (1 volume) at Anode.",
        "equation": "At Cathode: 4H⁺ + 4e⁻ → 2H₂(g)  |  At Anode: 4OH⁻ → 2H₂O + O₂ + 4e⁻",
        "points": 100
    },
    {
        "title": "Task 3: Electro-refining of Copper",
        "description": "Purifying a sample of impure copper using active electrodes.",
        "correct": {"el": "CuSO₄ solution", "an": "Impure Copper", "ca": "Pure Copper"},
        "result": "The impure anode dissolves; pure copper coats the cathode.",
        "equation": "Anode: Cu(s, impure) → Cu²⁺ + 2e⁻  |  Cathode: Cu²⁺ + 2e⁻ → Cu(s, pure)",
        "points": 150
    }
]

# --- 3. GAME SCREENS ---

# SCREEN A: INSTRUCTIONS
if st.session_state.mode == "instructions":
    st.markdown("<div class='lab-header'><h1>🧪 SS2 Chemistry: Electrolysis Practical</h1></div>", unsafe_allow_html=True)
    st.info("### 📖 How to play:")
    st.write("1. **Analyze the Experiment:** Read the curriculum task provided.")
    st.write("2. **Spin & Select:** Choose the correct electrolyte and electrodes.")
    st.write("3. **30s Timer:** You must initiate the reaction before the lab timer runs out.")
    st.write("4. **Collect Results:** Correct setups earn points and show the chemical equations.")
    
    if st.button("Enter the Lab"):
        st.session_state.mode = "game"
        st.rerun()

# SCREEN B: THE LAB (GAME)
elif st.session_state.mode == "game":
    task = curriculum_tasks[st.session_state.level]
    
    st.markdown(f"## {task['title']}")
    st.write(f"**Objective:** {task['description']}")
    st.divider()

    col_setup, col_timer = st.columns([3, 1])

    with col_setup:
        st.subheader("🛠️ Lab Setup")
        c1, c2, c3 = st.columns(3)
        with c1:
            u_el = st.selectbox("Select Electrolyte", ["Molten PbBr₂", "Dilute H₂SO₄", "CuSO₄ solution", "Brine (NaCl)"])
        with c2:
            u_an = st.selectbox("Select Anode (+)", ["Graphite", "Platinum", "Impure Copper", "Iron"])
        with c3:
            u_ca = st.selectbox("Select Cathode (-)", ["Graphite", "Platinum", "Pure Copper", "Steel Rod"])
        
        run_btn = st.button("⚡ Start Electrolysis")

    with col_timer:
        timer_placeholder = st.empty()
        if not run_btn:
            for t in range(30, -1, -1):
                timer_placeholder.markdown(f"<div class='timer-display'>{t}s</div>", unsafe_allow_html=True)
                time.sleep(1)
                if t == 0:
                    st.error("⏰ LAB TIMEOUT! The experiment failed.")
                    if st.button("Reset Lab"): st.rerun()
                    st.stop()

    if run_btn:
        st.markdown("---")
        if u_el == task['correct']['el'] and u_an == task['correct']['an'] and u_ca == task['correct']['ca']:
            st.balloons()
            st.success(f"🎊 Practical Successful! You earned {task['points']} points.")
            st.session_state.score += task['points']
            
            st.markdown("### 📊 Practical Observation")
            st.write(task['result'])
            
            st.markdown("### 📝 Chemical Equations (Half-Reactions)")
            st.markdown(f"<div class='equation-box'><code>{task['equation']}</code></div>", unsafe_allow_html=True)
            
            if st.session_state.level < len(curriculum_tasks) - 1:
                if st.button("Next Experiment"):
                    st.session_state.level += 1
                    st.rerun()
            else:
                st.session_state.mode = "finish"
                st.rerun()
        else:
            st.error("❌ Experiment Failed! Your setup does not match standard lab procedure.")
            st.warning("Check your choice of electrodes. Remember: Inert electrodes (Graphite/Platinum) are used for simple decomposition!")
            if st.button("Try Setup Again"):
                st.rerun()

# SCREEN C: FINISH
elif st.session_state.mode == "finish":
    st.title("🎓 Lab Practical Certified")
    st.write(f"Excellent work! You have completed the SS2 Electrolysis Curriculum.")
    st.metric("Final Lab Score", f"{st.session_state.score} pts")
    if st.button("Restart Curriculum"):
        st.session_state.level = 0
        st.session_state.score = 0
        st.session_state.mode = "instructions"
        st.rerun()

