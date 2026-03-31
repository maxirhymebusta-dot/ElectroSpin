import streamlit as st
import time

# --- 1. PAGE CONFIG & THEME ---
st.set_page_config(page_title="Electrolysis Tycoon", page_icon="🏭", layout="wide")

# Beautiful Laboratory Styling
st.markdown("""
    <style>
    .reportview-container { background: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    .job-card { background-color: #e3f2fd; padding: 20px; border-radius: 15px; border-left: 10px solid #1976d2; margin-bottom: 20px; }
    .status-text { font-family: 'Courier New', monospace; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if 'money' not in st.session_state: st.session_state.money = 500
if 'level' not in st.session_state: st.session_state.level = 1
if 'log' not in st.session_state: st.session_state.log = []

# --- 3. LEVEL DATABASE ---
jobs = {
    1: {
        "client": "Luxury Watches Inc.",
        "task": "Gold-plate 50 Stainless Steel watch bands.",
        "requirement": "Gold (Au)",
        "correct": {"el": "Gold Cyanide", "an": "Pure Gold", "ca": "Steel Bands"},
        "reward": 1000,
        "hint": "The object to be coated (Steel) must be the Negative Cathode!"
    },
    2: {
        "client": "Alu-Build Co.",
        "task": "Extract pure Aluminum from Bauxite ore.",
        "requirement": "Aluminum (Al)",
        "correct": {"el": "Molten Alumina in Cryolite", "an": "Graphite", "ca": "Graphite"},
        "reward": 2500,
        "hint": "Aluminum extraction requires a very high temperature and molten (liquid) ore."
    }
}

# --- 4. DASHBOARD ---
st.title("🏭 Electrolysis Tycoon: Lab Director")
col_stats1, col_stats2, col_stats3 = st.columns(3)
col_stats1.metric("Available Funds", f"${st.session_state.money}")
col_stats2.metric("Factory Level", f"LVL {st.session_state.level}")
col_stats3.metric("Successful Exports", len([x for x in st.session_state.log if "Success" in x]))

st.divider()

# --- 5. THE ACTIVE JOB ---
current_job = jobs[st.session_state.level]

st.markdown(f"""
<div class="job-card">
    <h3>📩 NEW CONTRACT: {current_job['client']}</h3>
    <p><b>Request:</b> {current_job['task']}</p>
    <p style="color: #1976d2;"><i>Hint: {current_job['hint']}</i></p>
</div>
""", unsafe_allow_html=True)

# --- 6. THE FACTORY FLOOR (Game Inputs) ---
st.subheader("🛠️ Setup Your Reaction Tank")
c1, c2, c3 = st.columns(3)

with c1:
    electrolyte = st.selectbox("1. Fill Tank With (Electrolyte):", 
        ["Distilled Water", "Gold Cyanide", "Molten Alumina in Cryolite", "Copper Sulfate"])

with c2:
    anode = st.selectbox("2. Install Anode (+):", 
        ["Graphite", "Pure Gold", "Iron Rod", "Platinum"])

with c3:
    cathode = st.selectbox("3. Install Cathode (-):", 
        ["Steel Bands", "Graphite", "Pure Aluminum Sheet", "Copper Strip"])

# --- 7. START THE MACHINE ---
if st.button("▶️ START PRODUCTION (30s Cycle)"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Check logic immediately but simulate time
    is_correct = (electrolyte == current_job['correct']['el'] and 
                  anode == current_job['correct']['an'] and 
                  cathode == current_job['correct']['ca'])
    
    # 30-Second Countdown Animation
    for percent in range(1, 101):
        time.sleep(0.3) # Total 30 seconds
        progress_bar.progress(percent)
        remaining = 30 - int(percent * 0.3)
        status_text.markdown(f"<p class='status-text'>⚡ Reacting... {remaining}s remaining</p>", unsafe_allow_html=True)
    
    if is_correct:
        st.balloons()
        st.success(f"📦 CONTRACT COMPLETE! You earned ${current_job['reward']}.")
        st.session_state.money += current_job['reward']
        st.session_state.log.append(f"Success: {current_job['client']}")
        
        if st.session_state.level < len(jobs):
            if st.button("Accept Next Contract"):
                st.session_state.level += 1
                st.rerun()
        else:
            st.write("🎉 You've completed all current industrial contracts!")
    else:
        st.error("💥 FACTORY ERROR: Wrong setup. The product was contaminated!")
        st.warning(f"Technical Reason: For {current_job['requirement']}, you needed {current_job['correct']['el']}.")
        st.session_state.money -= 200 # Penalty
        if st.button("Clean Up Lab & Retry"):
            st.rerun()

# --- 8. LAB LOGS ---
with st.expander("📋 View Factory Logs"):
    for entry in st.session_state.log:
        st.write(entry)
        
