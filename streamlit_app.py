import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Categorized Curriculum Data (The 8 Levels of Chemistry)
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "The Non-Metals", "type": "Non-Metals", "desc": "Period 1 & 2 Essentials.", "data": [
            {"id": 1, "q": "Atomic Number 1: Lightest element in the universe?", "options": ["A) He", "B) H", "C) Li", "D) O"], "ans": "B) H"},
            {"id": 2, "q": "Atomic Number 2: Unreactive gas used in balloons?", "options": ["A) Ne", "B) Ar", "C) He", "D) H"], "ans": "C) He"},
            {"id": 3, "q": "Atomic Number 7: Makes up 78% of the air?", "options": ["A) O", "B) N", "C) C", "D) Ne"], "ans": "B) N"},
            {"id": 4, "q": "Atomic Number 8: Essential for respiration?", "options": ["A) C", "B) F", "C) O", "D) N"], "ans": "C) O"},
            {"id": 5, "q": "Atomic Number 6: The basis of all organic life?", "options": ["A) N", "B) O", "C) C", "D) P"], "ans": "C) C"}
        ]},
        2: {"name": "Reactive Metals", "type": "Group 1 & 2", "desc": "Alkali and Alkaline Earth metals.", "data": [
            {"id": 1, "q": "Atomic Number 3: Used in rechargeable batteries?", "options": ["A) Na", "B) Li", "C) K", "D) Be"], "ans": "B) Li"},
            {"id": 2, "q": "Atomic Number 11: Explodes in water, found in salt?", "options": ["A) Mg", "B) K", "C) Na", "D) Li"], "ans": "C) Na"},
            {"id": 3, "q": "Atomic Number 19: Found in bananas, Group 1?", "options": ["A) Na", "B) Ca", "C) K", "D) Li"], "ans": "C) K"},
            {"id": 4, "q": "Atomic Number 12: Burns with bright white light?", "options": ["A) Ca", "B) Al", "C) Mg", "D) Zn"], "ans": "C) Mg"},
            {"id": 5, "q": "Atomic Number 20: Essential for bones and teeth?", "options": ["A) Mg", "B) Ca", "C) Sr", "D) Ba"], "ans": "B) Ca"}
        ]},
        3: {"name": "Metalloids & Poor Metals", "type": "Groups 13 & 14", "desc": "Elements with mixed properties.", "data": [
            {"id": 1, "q": "Atomic Number 5: Used in heat-resistant glass?", "options": ["A) C", "B) Si", "C) B", "D) Al"], "ans": "C) B"},
            {"id": 2, "q": "Atomic Number 14: Basis of computer chips?", "options": ["A) Ge", "B) As", "C) Si", "D) C"], "ans": "C) Si"},
            {"id": 3, "q": "Atomic Number 13: Lightweight metal used in foil?", "options": ["A) Sn", "B) Pb", "C) Al", "D) Ag"], "ans": "C) Al"},
            {"id": 4, "q": "Atomic Number 4: High-melting point Group 2 metal?", "options": ["A) Mg", "B) Ca", "C) Be", "D) B"], "ans": "C) Be"},
            {"id": 5, "q": "Which is the metalloid in Period 3?", "options": ["A) Al", "B) P", "C) Si", "D) S"], "ans": "C) Si"}
        ]},
        4: {"name": "Halogens & Noble Gases", "type": "Groups 17 & 18", "desc": "Inert and reactive non-metals.", "data": [
            {"id": 1, "q": "Atomic Number 9: Most reactive non-metal?", "options": ["A) Cl", "B) O", "C) F", "D) I"], "ans": "C) F"},
            {"id": 2, "q": "Atomic Number 17: Used to clean pools?", "options": ["A) F", "B) Br", "C) Cl", "D) I"], "ans": "C) Cl"},
            {"id": 3, "q": "Atomic Number 10: Used in orange neon signs?", "options": ["A) Ar", "B) Ne", "C) Kr", "D) Xe"], "ans": "B) Ne"},
            {"id": 4, "q": "Atomic Number 18: Most abundant Noble Gas?", "options": ["A) Ne", "B) He", "C) Ar", "D) Rn"], "ans": "C) Ar"},
            {"id": 5, "q": "Which group does Fluorine belong to?", "options": ["A) Group 1", "B) Group 18", "C) Group 17", "D) Group 16"], "ans": "C) Group 17"}
        ]}
        # (Levels 5-8 follow the same structure)
    }

# 3. Custom CSS (Background + Spinning Wheel Logic)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}
@keyframes gradient { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }

.wheel-container { display: flex; justify-content: center; align-items: center; height: 350px; position: relative; }
.wheel {
    width: 250px; height: 250px; border-radius: 50%; border: 8px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(#FF4136 0% 20%, #0074D9 20% 40%, #2ECC40 40% 60%, #FFDC00 60% 80%, #B10DC9 80% 100%);
    transition: transform 3s cubic-bezier(0.1, 0, 0, 1);
    z-index: 1;
}
.wheel-pointer { position: absolute; top: 15px; width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-top: 40px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 26px; pointer-events: none; }
.stButton>button { background: linear-gradient(45deg, #4facfe, #00f2fe); color: white; border-radius: 10px; font-weight: bold; }
.footer { text-align: center; padding: 40px; color: #aaa; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 4. Session State
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'level_scores' not in st.session_state: st.session_state.level_scores = {}
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'answered_ids' not in st.session_state: st.session_state.answered_ids = []
if 'current_q_data' not in st.session_state: st.session_state.current_q_data = None
if 'rotation' not in st.session_state: st.session_state.rotation = 0

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
st.markdown('<h1 style="text-align:center; color:#00d2ff;">🧪 Periodic Table: The Grand Quest</h1>', unsafe_allow_html=True)

if st.session_state.mode == "spin":
    lvl = st.session_state.levels_data[st.session_state.level]
    st.write(f"### 📍 Level {st.session_state.level}: {lvl['name']}")
    st.info(f"**Classification:** {lvl['type']} | **Progress:** {len(st.session_state.answered_ids)}/5")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(render_wheel(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN FOR A CHALLENGE", use_container_width=True):
        available = [q for q in lvl["data"] if q["id"] not in st.session_state.answered_ids]
        target_q = random.choice(available)
        st.session_state.current_q_data = target_q
        
        target_stop = -( (target_q['id'] - 1) * 72 + 36 )
        st.session_state.rotation += 1440 + (target_stop - (st.session_state.rotation % 360))
        
        wheel_placeholder.markdown(render_wheel(st.session_state.rotation), unsafe_allow_html=True)
        with st.status("Analyzing Elements...") as status:
            time.sleep(3.2)
            status.update(label=f"🎯 Target Locked: Question {target_q['id']}!", state="complete")
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.current_q_data
    st.subheader(f"🔍 Question {q['id']}")
    st.write(f"**CHALLENGE:** {q['q']}")
    ans = st.radio("Choose the correct option:", q["options"], index=None)
    if st.button("SUBMIT DATA", use_container_width=True):
        if ans == q["ans"]:
            st.success("✅ Correct!")
            st.session_state.score += 20
        else:
            st.error(f"❌ Incorrect! The fact is {q['ans']}")
        
        st.session_state.answered_ids.append(q["id"])
        time.sleep(2)
        if len(st.session_state.answered_ids) < 5: st.session_state.mode = "spin"
        else: st.session_state.mode = "review"
        st.rerun()

elif st.session_state.mode == "review":
    st.balloons()
    st.header(f"🏁 Gate {st.session_state.level} Mastery Achieved!")
    st.subheader("Performance Review:")
    for item in st.session_state.levels_data[st.session_state.level]["data"]:
        with st.expander(f"Analysis: {item['q'][:30]}..."):
            st.write(item['q'])
            st.success(f"Scientific Fact: {item['ans']}")
    
    if st.button("Proceed to Next Gate", use_container_width=True):
        if st.session_state.level < 4:
            st.session_state.level += 1
            st.session_state.answered_ids = []
            st.session_state.mode = "spin"
        else: st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.header("🏆 MASTER CHEMIST CERTIFIED")
    st.metric("Final Score", f"{st.session_state.score} / 400")
    if st.button("Restart Journey", use_container_width=True):
        st.session_state.level = 1
        st.session_state.score = 0
        st.session_state.answered_ids = []
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
    
