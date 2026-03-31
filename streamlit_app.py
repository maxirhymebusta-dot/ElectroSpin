import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MSc Periodic Master", page_icon="🧪", layout="wide")

# 2. Sound Control Sidebar
st.sidebar.title("🎮 Game Controls")
bg_music = st.sidebar.checkbox("Enable Background Music", value=True)
sfx_enabled = st.sidebar.checkbox("Enable Sound Effects", value=True)

# 3. Custom CSS (Animated Background + 20-Segment Wheel)
st.markdown("""
<style>
@keyframes gradientBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes float { 0% {transform: translateY(0px);} 50% {transform: translateY(-20px);} 100% {transform: translateY(0px);} }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

/* Chemistry Background Elements */
.stApp::after {
    content: "🧪 ⚛️ ⚗️ 🔬 🧪 ⚛️";
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    font-size: 50px; opacity: 0.05; pointer-events: none;
    display: flex; justify-content: space-around; align-items: center;
    animation: float 6s ease-in-out infinite;
}

.main-title { text-align: center; color: #00d2ff; font-size: 45px; font-weight: 800; text-shadow: 2px 2px 10px #00d2ff; }
.wheel-container { display: flex; justify-content: center; align-items: center; height: 400px; position: relative; }

/* 20-Segment Wheel CSS */
.wheel {
    width: 300px; height: 300px; border-radius: 50%; border: 10px solid #FFD700;
    position: relative; overflow: hidden;
    background: conic-gradient(
        #FF4136 0% 5%, #0074D9 5% 10%, #2ECC40 10% 15%, #FFDC00 15% 20%, #B10DC9 20% 25%,
        #FF851B 25% 30%, #7FDBFF 30% 35%, #3D9970 35% 40%, #F012BE 40% 45%, #AAAAAA 45% 50%,
        #FF4136 50% 55%, #0074D9 55% 60%, #2ECC40 60% 65%, #FFDC00 65% 70%, #B10DC9 70% 75%,
        #FF851B 75% 80%, #7FDBFF 80% 85%, #3D9970 85% 90%, #F012BE 90% 95%, #AAAAAA 95% 100%
    );
    transition: transform 4s cubic-bezier(0.1, 0, 0, 1);
}
.wheel-pointer { position: absolute; top: 20px; width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 45px solid #FFD700; z-index: 10; }
.wheel-num { position: absolute; font-weight: bold; color: white; font-size: 20px; pointer-events: none; }
.footer { text-align: center; padding: 40px; color: #aaa; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 4. Sound Handler
if bg_music:
    st.markdown('<audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" autoplay loop style="display:none"></audio>', unsafe_allow_html=True)

def play_sfx(url):
    if sfx_enabled:
        st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

# 5. Question Database (20 Elements for the Bank)
# Each level will pull from this pool of 20
level_bank = [
    {"id": 1, "name": "Hydrogen", "q": "Atomic Number 1: Lightest element?", "options": ["A) He", "B) H", "C) Li", "D) O"], "ans": "B) H"},
    {"id": 2, "name": "Helium", "q": "Atomic Number 2: Noble gas in balloons?", "options": ["A) Ne", "B) Ar", "C) He", "D) H"], "ans": "C) He"},
    {"id": 3, "name": "Lithium", "q": "Atomic Number 3: Group 1 battery metal?", "options": ["A) Na", "B) Li", "C) K", "D) Be"], "ans": "B) Li"},
    {"id": 4, "name": "Beryllium", "q": "Atomic Number 4: Alkaline earth metal?", "options": ["A) Mg", "B) Ca", "C) Be", "D) B"], "ans": "C) Be"},
    {"id": 5, "name": "Boron", "q": "Atomic Number 5: Used in pyrex glass?", "options": ["A) C", "B) Si", "C) B", "D) Al"], "ans": "C) B"},
    {"id": 6, "name": "Carbon", "q": "Atomic Number 6: Basis of organic life?", "options": ["A) N", "B) O", "C) C", "D) P"], "ans": "C) C"},
    {"id": 7, "name": "Nitrogen", "q": "Atomic Number 7: 78% of air?", "options": ["A) O", "B) N", "C) C", "D) Ne"], "ans": "B) N"},
    {"id": 8, "name": "Oxygen", "q": "Atomic Number 8: Essential for breathing?", "options": ["A) C", "B) F", "C) O", "D) N"], "ans": "C) O"},
    {"id": 9, "name": "Fluorine", "q": "Atomic Number 9: Most reactive non-metal?", "options": ["A) Cl", "B) O", "C) F", "D) I"], "ans": "C) F"},
    {"id": 10, "name": "Neon", "q": "Atomic Number 10: Orange glow signs?", "options": ["A) Ar", "B) Ne", "C) Kr", "D) Xe"], "ans": "B) Neon"},
    {"id": 11, "name": "Sodium", "q": "Atomic Number 11: Soft metal, explodes in water?", "options": ["A) Mg", "B) K", "C) Na", "D) Li"], "ans": "C) Na"},
    {"id": 12, "name": "Magnesium", "q": "Atomic Number 12: Burns bright white?", "options": ["A) Ca", "B) Al", "C) Mg", "D) Zn"], "ans": "C) Mg"},
    {"id": 13, "name": "Aluminum", "q": "Atomic Number 13: Cans and foil?", "options": ["A) Tin", "B) Pb", "C) Al", "D) Ag"], "ans": "C) Al"},
    {"id": 14, "name": "Silicon", "q": "Atomic Number 14: Computer chips?", "options": ["A) Ge", "B) As", "C) Si", "D) C"], "ans": "C) Si"},
    {"id": 15, "name": "Phosphorus", "q": "Atomic Number 15: Found in matchsticks?", "options": ["A) S", "B) N", "C) P", "D) K"], "ans": "C) P"},
    {"id": 16, "name": "Sulfur", "q": "Atomic Number 16: Yellow smell?", "options": ["A) P", "B) Cl", "C) S", "D) Se"], "ans": "C) S"},
    {"id": 17, "name": "Chlorine", "q": "Atomic Number 17: Disinfects pools?", "options": ["A) F", "B) Br", "C) Cl", "D) I"], "ans": "C) Cl"},
    {"id": 18, "name": "Argon", "q": "Atomic Number 18: Found in lightbulbs?", "options": ["A) Ne", "B) He", "C) Ar", "D) Rn"], "ans": "C) Ar"},
    {"id": 19, "name": "Potassium", "q": "Atomic Number 19: Abundant in bananas?", "options": ["A) Na", "B) Ca", "C) K", "D) Li"], "ans": "C) K"},
    {"id": 20, "name": "Calcium", "q": "Atomic Number 20: Strong bones and milk?", "options": ["A) Mg", "B) Ca", "C) Sr", "D) Ba"], "ans": "B) Ca"},
]

# 6. Global Session State
if 'level' not in st.session_state: st.session_state.level = 1
if 'total_score' not in st.session_state: st.session_state.total_score = 0
if 'mode' not in st.session_state: st.session_state.mode = "spin"
if 'answered_count' not in st.session_state: st.session_state.answered_count = 0
if 'rotation' not in st.session_state: st.session_state.rotation = 0
if 'session_pool' not in st.session_state: st.session_state.session_pool = level_bank.copy()

def render_wheel(rotation_angle):
    # 20-segment numbers
    nums_html = ""
    for i in range(1, 21):
        angle = (i - 1) * 18 + 9
        nums_html += f'<div class="wheel-num" style="top:50%; left:50%; transform: translate(-50%, -50%) rotate({angle}deg) translateY(-120px) rotate(-{angle}deg);">{i}</div>'
    
    return f"""
        <div class="wheel-container">
            <div class="wheel-pointer"></div>
            <div class="wheel" style="transform: rotate({rotation_angle}deg);">
                {nums_html}
            </div>
        </div>
    """

# --- GAME INTERFACE ---
st.markdown('<h1 class="main-title">🧪 Periodic Master: Spin Quest</h1>', unsafe_allow_html=True)

if st.session_state.mode == "spin":
    st.write(f"### 📍 Level {st.session_state.level} | Questions Completed: **{st.session_state.answered_count}/10**")
    
    wheel_placeholder = st.empty()
    wheel_placeholder.markdown(render_wheel(st.session_state.rotation), unsafe_allow_html=True)
    
    if st.button("🚀 SPIN THE WHEEL", use_container_width=True):
        # Pick random question from current pool
        target_q = random.choice(st.session_state.session_pool)
        st.session_state.current_q = target_q
        
        # Calculate rotation (360/20 = 18 degrees per slice)
        # Land in center of slice: -( (ID-1)*18 + 9 )
        target_stop = -( (target_q['id'] - 1) * 18 + 9 )
        st.session_state.rotation += 1800 + (target_stop - (st.session_state.rotation % 360))
        
        play_sfx("https://www.soundjay.com/misc/sounds/spinning-wheel-1.mp3")
        wheel_placeholder.markdown(render_wheel(st.session_state.rotation), unsafe_allow_html=True)
        
        with st.status("Selecting from the 20-Element Bank...") as status:
            time.sleep(4)
            status.update(label=f"🎯 Target Locked: Element {target_q['id']}!", state="complete")
        
        st.session_state.mode = "quiz"
        st.rerun()

elif st.session_state.mode == "quiz":
    q = st.session_state.current_q
    st.subheader(f"🔍 Challenge: {q['name']}")
    st.info(f"**Question:** {q['q']}")
    ans = st.radio("Choose the correct answer:", q["options"], index=None)
    
    if st.button("SUBMIT DATA"):
        if ans == q["ans"]:
            st.success("✅ Correct! +10 Points")
            play_sfx("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            st.session_state.total_score += 10
        else:
            st.error(f"❌ Incorrect. The answer was {q['ans']}")
            play_sfx("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        
        # Remove used question from pool so it doesn't repeat
        st.session_state.session_pool.remove(q)
        st.session_state.answered_count += 1
        
        time.sleep(2)
        if st.session_state.answered_count < 10:
            st.session_state.mode = "spin"
        else:
            st.session_state.mode = "end"
        st.rerun()

elif st.session_state.mode == "end":
    st.balloons()
    st.header("🏆 Quest Complete!")
    st.metric("Total Final Score", f"{st.session_state.total_score} / 100")
    if st.button("Restart New Session"):
        st.session_state.answered_count = 0
        st.session_state.total_score = 0
        st.session_state.session_pool = level_bank.copy()
        st.session_state.mode = "spin"
        st.rerun()

st.markdown('<div class="footer">Game Developed by Ukazim Chidinma Favour</div>', unsafe_allow_html=True)
        
