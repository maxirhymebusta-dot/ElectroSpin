import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Master Pool: The First 20 Elements (Atomic Numbers 1-20)
# This pool will be used for ALL levels, picking 5 random ones each time.
if 'master_pool' not in st.session_state:
    st.session_state.master_pool = [
        {"id": 1, "name": "Hydrogen", "q": "Which element is the lightest, has Atomic Number 1, and only 1 electron?", "options": ["A) Helium", "B) Hydrogen", "C) Lithium", "D) Oxygen"], "ans": "B) Hydrogen"},
        {"id": 2, "name": "Helium", "q": "Which Noble Gas has an Atomic Number of 2 and is used in balloons?", "options": ["A) Neon", "B) Argon", "C) Helium", "D) Hydrogen"], "ans": "C) Helium"},
        {"id": 3, "name": "Lithium", "q": "Identify the Group 1 metal with Atomic Number 3, commonly used in batteries.", "options": ["A) Sodium", "B) Lithium", "C) Potassium", "D) Beryllium"], "ans": "B) Lithium"},
        {"id": 4, "name": "Beryllium", "q": "Which element has Atomic Number 4 and belongs to the Alkaline Earth Metals?", "options": ["A) Magnesium", "B) Calcium", "C) Beryllium", "D) Boron"], "ans": "C) Beryllium"},
        {"id": 5, "name": "Boron", "q": "This metalloid has Atomic Number 5 and is used in heat-resistant glass.", "options": ["A) Carbon", "B) Silicon", "C) Boron", "D) Aluminum"], "ans": "C) Boron"},
        {"id": 6, "name": "Carbon", "q": "Which element has Atomic Number 6 and is the basis of all organic life?", "options": ["A) Nitrogen", "B) Oxygen", "C) Carbon", "D) Phosphorus"], "ans": "C) Carbon"},
        {"id": 7, "name": "Nitrogen", "q": "Which gas makes up 78% of Earth's atmosphere and has Atomic Number 7?", "options": ["A) Oxygen", "B) Nitrogen", "C) Argon", "D) Neon"], "ans": "B) Nitrogen"},
        {"id": 8, "name": "Oxygen", "q": "What is the element with Atomic Number 8, essential for human respiration?", "options": ["A) Carbon", "B) Fluorine", "C) Oxygen", "D) Nitrogen"], "ans": "C) Oxygen"},
        {"id": 9, "name": "Fluorine", "q": "Identify the most electronegative element, which has Atomic Number 9.", "options": ["A) Chlorine", "B) Oxygen", "C) Fluorine", "D) Iodine"], "ans": "C) Fluorine"},
        {"id": 10, "name": "Neon", "ps": "Neon", "q": "Which Noble Gas has Atomic Number 10 and glows bright orange in signs?", "options": ["A) Argon", "B) Neon", "C) Krypton", "D) Xenon"], "ans": "B) Neon"},
        {"id": 11, "name": "Sodium", "q": "Which Group 1 metal (Atomic No. 11) reacts violently with water?", "options": ["A) Magnesium", "B) Potassium", "C) Sodium", "D) Lithium"], "ans": "C) Sodium"},
        {"id": 12, "name": "Magnesium", "q": "Which metal with Atomic Number 12 burns with a brilliant white light?", "options": ["A) Calcium", "B) Aluminum", "C) Magnesium", "D) Zinc"], "ans": "C) Magnesium"},
        {"id": 13, "name": "Aluminum", "q": "Identify the 'poor metal' with Atomic Number 13, used for foil and cans.", "options": ["A) Tin", "B) Lead", "C) Aluminum", "D) Silver"], "ans": "C) Aluminum"},
        {"id": 14, "name": "Silicon", "q": "Which metalloid has Atomic Number 14 and is used to make computer chips?", "options": ["A) Germanium", "B) Arsenic", "C) Silicon", "D) Carbon"], "ans": "C) Silicon"},
        {"id": 15, "name": "Phosphorus", "q": "Which element has Atomic Number 15 and is found in matchsticks and DNA?", "options": ["A) Sulfur", "B) Nitrogen", "C) Phosphorus", "D) Potassium"], "ans": "C) Phosphorus"},
        {"id": 16, "name": "Sulfur", "q": "Which yellow non-metal has Atomic Number 16 and a distinct 'rotten egg' smell?", "options": ["A) Phosphorus", "B) Chlorine", "C) Sulfur", "D) Selenium"], "ans": "C) Sulfur"},
        {"id": 17, "name": "Chlorine", "q": "Which Halogen (Atomic Number 17) is used to disinfect swimming pools?", "options": ["A) Fluorine", "B) Bromine", "C) Chlorine", "D) Iodine"], "ans": "C) Chlorine"},
        {"id": 18, "name": "Argon", "q": "Identify the Noble Gas with Atomic Number 18, the most abundant in air.", "options": ["A) Neon", "B) Helium", "C) Argon", "D) Radon"], "ans": "C) Argon"},
        {"id": 19, "name": "Potassium", "q": "Which Group 1 element (Atomic No. 19) is highly abundant in bananas?", "options": ["A) Sodium", "B) Calcium", "C) Potassium", "D) Lithium"], "ans": "C) Potassium"},
        {"id": 20, "name": "Calcium", "q": "Which element has Atomic Number 20 and is essential for strong bones?", "options": ["A) Magnesium", "B) Calcium", "C) Strontium", "D) Barium"], "ans": "B) Calcium"}
    ]

# 3. Custom CSS
st.markdown("""
<style>
@keyframes backgroundAnimation { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
.stApp { background: linear-gradient(-45deg, #1a1a2e, #16213e, #1a1a2e); background-size: 400% 400%; animation: backgroundAnimation 20s ease infinite; }
.stExpander, .instruction-box, .wheel-container { background: rgba(255, 255, 255, 0.05); border-radius: 16px; backdrop-filter: blur(5px); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; }
h1, h2, h3, h4, p, li, label, .stMarkdown { color: #e0e0e0 !important; }
.main-title { text-align: center; color: #4facfe !important; font-size: 45px; font-weight: 800; }
.subtitle { text-align: center; color: #b8c1ec !important; font-size: 18px; margin-bottom: 30px; }
.wheel-container { display: flex; justify-content: center; align-items: center; height: 350px; position: relative; }
.wheel {
    width: 250px; height: 250px; border-radius: 50%; border: 8px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(#FF4136 0% 20%, #0074D9 20% 40%, #2ECC40 40% 60%, #FFDC00 60% 80%, #B10DC9 80% 100%);
    transition: transform 3s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 15px; width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-top: 40px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 26px; }
.stButton>button { background: linear-gradient(45deg, #4facfe, #00f2fe); color: white; border-radius: 10px; font-weight: bold; width: 100%; }
.footer { text-align: center; padding: 40px; color: #b8c1ec; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 4. Global Session State
if 'level' not in st.session_state: st.session_state.level = 1
if 'total_score' not in st.session_state: st.session_state.total_score = 0
if 'level_scores' not in st.session_state: st.session_state.level_scores = {}
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'current_level_questions' not in st.session_state: st.session_state.current_level_questions = []
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0
if 'level_temp_score' not in st.session_state: st.session_state.level_temp_score = 0

def render_wheel(rotation_angle):
    return f"""
        <div class="wheel-container">
            <div class="wheel-pointer"></div>
            <div class="wheel" style="transform: rotate({rotation_angle}deg);">
                <div class="wheel-num" style="top:12%; left:55%; transform: rotate(36deg);">1</div>
                <div class="wheel-num" style="top:48%; left:75%; transform: rotate(108deg);">2</div>
                <div class="wheel-num" style="top:78%; left:40%; transform: rotate(180deg);">3</div>
                <div class="wheel-num" style="top:48%; left:10%; transform: rotate(252deg);">4</div>
                <div class="wheel-num" style="top:12%; left:25%; transform: rotate(324deg);">5</div>
            </div>
        </div>
    """

# --- MAIN UI ---
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.markdown('<h1 class="main-title">🧪 Periodic Table: The Grand Quest</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">MSc Chemistry Educational Assessment</p>', unsafe_allow_html=True)

    # Pick 5 random questions if a new level starts
    if not st.session_state.current_level_questions:
        st.session_state.current_level_questions = random.sample(st.session_state.master_pool, 5)

    if st.session_state.mode == "spin":
        st.write(f"### 📍 Level {st.session_state.level}: The First 20 Elements")
        st.write(f"Questions answered in this level: **{st.session_state.q_idx}/5**")
        wheel_placeholder = st.empty()
        wheel_placeholder.markdown(render_wheel(st.session_state.rotation), unsafe_allow_html=True)
        
        if st.button("🚀 SPIN FOR A CHALLENGE"):
            # Target Question is the next one in the random set of 5
            target_q_num = st.session_state.q_idx + 1
            target_stop = -( (target_q_num - 1) * 72 + 36 )
            st.session_state.rotation += 1440 + (target_stop - (st.session_state.rotation % 360))
            wheel_placeholder.markdown(render_wheel(st.session_state.rotation), unsafe_allow_html=True)
            with st.status("Picking an Element...") as status:
                time.sleep(3)
                status.update(label=f"🎯 Question {target_q_num} Locked!", state="complete")
            st.session_state.mode = "quiz"
            st.rerun()

    elif st.session_state.mode == "quiz":
        q = st.session_state.current_level_questions[st.session_state.q_idx]
        st.subheader(f"🔍 Question {st.session_state.q_idx + 1}")
        st.info(f"**CHALLENGE:** {q['q']}")
        ans = st.radio("Choose Answer:", q["options"], index=None)
        if st.button("SUBMIT"):
            if ans == q["ans"]:
                st.success("Correct!")
                st.session_state.level_temp_score += 20
                st.session_state.total_score += 20
            else:
                st.error(f"Incorrect. It was {q['ans']}")
            
            st.session_state.q_idx += 1
            time.sleep(2)
            if st.session_state.q_idx < 5: 
                st.session_state.mode = "spin"
            else: 
                st.session_state.level_scores[st.session_state.level] = st.session_state.level_temp_score
                st.session_state.mode = "review"
            st.rerun()

    elif st.session_state.mode == "review":
        st.header(f"🏁 Level {st.session_state.level} Complete: {st.session_state.level_temp_score}/100")
        for item in st.session_state.current_level_questions:
            with st.expander(f"Review: {item['name']}"):
                st.write(item['q'])
                st.success(f"Fact: {item['ans']}")
        
        if st.button("Unlock Next Level Gate" if st.session_state.level < 4 else "Final Evaluation"):
            if st.session_state.level < 4:
                st.session_state.level += 1
                st.session_state.q_idx = 0
                st.session_state.current_level_questions = [] # This triggers a new random 5 from the 20
                st.session_state.level_temp_score = 0
                st.session_state.mode = "spin"
                st.rerun()
            else:
                st.session_state.mode = "end"
                st.rerun()

    elif st.session_state.mode == "end":
        st.header("🏆 MASTER CHEMIST CERTIFIED")
        st.metric("Total Final Score", f"{st.session_state.total_score} / 400")
        for lvl, s in st.session_state.level_scores.items():
            st.write(f"Level {lvl}: {s}/100")
        if st.button("Restart Journey"):
            st.session_state.level = 1
            st.session_state.total_score = 0
            st.session_state.level_scores = {}
            st.session_state.q_idx = 0
            st.session_state.current_level_questions = []
            st.session_state.mode = "spin"
            st.rerun()

    st.markdown('<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
