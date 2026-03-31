import streamlit as st
import random
import time

# 1. Page Configuration & Integrated CSS (Background + Wheel + Text)
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

st.markdown("""
<style>
/* 1. Animated Chemistry Background */
@keyframes backgroundAnimation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
    background-size: 400% 400%;
    animation: backgroundAnimation 15s ease infinite;
}

/* 2. Glassmorphism UI Containers */
.stExpander, .instruction-box, .wheel-container, .stMarkdown {
    background: rgba(255, 255, 255, 0.03);
    border-radius: 15px;
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 15px;
}

/* 3. Spinning Wheel Design */
.wheel-container { display: flex; justify-content: center; align-items: center; height: 350px; position: relative; }
.wheel {
    width: 250px; height: 250px; border-radius: 50%; border: 8px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(#FF4136 0% 20%, #0074D9 20% 40%, #2ECC40 40% 60%, #FFDC00 60% 80%, #B10DC9 80% 100%);
    transition: transform 3s cubic-bezier(0.1, 0, 0, 1);
    z-index: 1;
    box-shadow: 0 0 30px rgba(0, 210, 255, 0.3);
}
.wheel-pointer { position: absolute; top: 15px; width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-top: 40px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 26px; pointer-events: none; }

/* 4. Text & Buttons */
h1, h2, h3, h4, p, li, label, [data-testid="stMarkdownContainer"] p { color: #e0e0e0 !important; }
.main-title { text-align: center; color: #00d2ff !important; font-size: 45px; font-weight: 800; text-shadow: 2px 2px 10px rgba(0, 210, 255, 0.5); }
.stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border: none; border-radius: 10px; font-weight: bold; width: 100%; }
.footer { text-align: center; padding: 40px; color: #aaa; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 2. Continuous Background Ambient Sound & Floating Icons
st.markdown("""
<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; opacity: 0.1; pointer-events: none;">
    <svg width="60" height="60" style="position: absolute; top: 15%; left: 10%;"><path d="M48 40V12H36V8H24V12H12V40C12 46.6 17.4 52 24 52H36C42.6 52 48 46.6 48 40Z" fill="#00d2ff"/></svg>
    <svg width="100" height="100" style="position: absolute; bottom: 15%; right: 10%;"><circle cx="50" cy="50" r="10" fill="#00d2ff"/><ellipse cx="50" cy="50" rx="40" ry="15" stroke="#00d2ff" stroke-width="3" fill="none" transform="rotate(45 50 50)"/></svg>
</div>
<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3" autoplay loop style="display:none"></audio>
""", unsafe_allow_html=True)

def play_sfx(url):
    st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

# 3. Categorized 8-Level Database
if 'levels_data' not in st.session_state:
    st.session_state.levels_data = {
        1: {"name": "Non-Metals (Gases)", "type": "Non-Metals", "data": [
            {"id": 1, "q": "Which element is the lightest, with Atomic Number 1?", "options": ["A) He", "B) H", "C) Li", "D) O"], "ans": "B) H"},
            {"id": 2, "q": "Atomic Number 2: Noble gas used in balloons?", "options": ["A) Ne", "B) Ar", "C) He", "D) H"], "ans": "C) He"},
            {"id": 3, "q": "Which gas makes up 78% of our atmosphere?", "options": ["A) O", "B) N", "C) C", "D) Ne"], "ans": "B) N"},
            {"id": 4, "q": "Atomic Number 8: Essential for breathing?", "options": ["A) C", "B) F", "C) O", "D) N"], "ans": "C) O"},
            {"id": 5, "q": "The core element of organic chemistry?", "options": ["A) N", "B) O", "C) C", "D) P"], "ans": "C) C"}
        ]},
        2: {"name": "The Reactive Metals", "type": "Groups 1 & 2", "data": [
            {"id": 1, "q": "Group 1 metal used in phone batteries?", "options": ["A) Na", "B) Li", "C) K", "D) Be"], "ans": "B) Li"},
            {"id": 2, "q": "Atomic Number 11: Explodes in water?", "options": ["A) Mg", "B) K", "C) Na", "D) Li"], "ans": "C) Na"},
            {"id": 3, "q": "Found in bananas, Atomic Number 19?", "options": ["A) Na", "B) Ca", "C) K", "D) Li"], "ans": "C) K"},
            {"id": 4, "q": "Atomic Number 12: Burns with bright white light?", "options": ["A) Ca", "B) Al", "C) Mg", "D) Zn"], "ans": "C) Mg"},
            {"id": 5, "q": "Essential for bone strength (No. 20)?", "options": ["A) Mg", "B) Ca", "C) Sr", "D) Ba"], "ans": "B) Ca"}
        ]}
        # Note: You can easily add levels 3-8 following this pattern
    }

# 4. State Management
if 'level' not in st.session_state: st.session_state.level = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'answered_ids' not in st.session_state: st.session_state.answered_ids = []
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

# --- GAME INTERFACE ---
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.markdown('<h1 class="main-title">🧪 Periodic Table: The Grand Quest</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">MSc Educational Assessment Tool</p>', unsafe_allow_html=True)

    with st.expander("📖 INSTRUCTIONS"):
        st.write("1. Spin the wheel to pick a question. 2. Select A-D. 3. Review facts to level up!")

    if st.session_state.mode == "spin":
        lvl = st.session_state.levels_data[st.session_state.level]
        st.write(f"### 📍 Level {st.session_state.level}: {lvl['name']} ({lvl['type']})")
        
        wheel_placeholder = st.empty()
        wheel_placeholder.markdown(render_wheel(st.session_state.rotation), unsafe_allow_html=True)
        
        if st.button("🚀 SPIN FOR A CHALLENGE"):
            play_sfx("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
            available = [q for q in lvl["data"] if q["id"] not in st.session_state.answered_ids]
            target_q = random.choice(available)
            st.session_state.current_q_data = target_q
            
            target_stop = -( (target_q['id'] - 1) * 72 + 36 )
            st.session_state.rotation += 1440 + (target_stop - (st.session_state.rotation % 360))
            wheel_placeholder.markdown(render_wheel(st.session_state.rotation), unsafe_allow_html=True)
            
            with st.status("Analyzing Atoms...") as status:
                time.sleep(3.2)
                status.update(label=f"🎯 Target Locked: Question {target_q['id']}!", state="complete")
            st.session_state.mode = "quiz"
            st.rerun()

    elif st.session_state.mode == "quiz":
        q = st.session_state.current_q_data
        st.subheader(f"🔍 Question {q['id']}")
        st.info(f"**CHALLENGE:** {q['q']}")
        ans = st.radio("Choose the correct option:", q["options"], index=None)
        
        if st.button("SUBMIT RESEARCH DATA"):
            if ans == q["ans"]:
                st.success("✅ Correct!")
                play_sfx("https://www.soundjay.com/buttons/sounds/button-3.mp3")
                st.session_state.score += 20
            else:
                st.error(f"❌ Incorrect. Answer was {q['ans']}")
                play_sfx("https://www.soundjay.com/buttons/sounds/button-10.mp3")
            
            st.session_state.answered_ids.append(q["id"])
            time.sleep(2)
            if len(st.session_state.answered_ids) < 5: st.session_state.mode = "spin"
            else: st.session_state.mode = "review"
            st.rerun()

    elif st.session_state.mode == "review":
        st.balloons()
        st.header(f"🏁 Level {st.session_state.level} Complete!")
        if st.button("Unlock Next Gate"):
            if st.session_state.level < len(st.session_state.levels_data):
                st.session_state.level += 1
                st.session_state.answered_ids = []
                st.session_state.mode = "spin"
            else: st.session_state.mode = "end"
            st.rerun()

    elif st.session_state.mode == "end":
        st.header("🏆 MASTER CHEMIST CERTIFIED")
        st.metric("Total Score", f"{st.session_state.score} / 400")
        if st.button("Restart Journey"):
            st.session_state.level = 1
            st.session_state.score = 0
            st.session_state.answered_ids = []
            st.session_state.mode = "spin"
            st.rerun()

    st.markdown(f'<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
    
