import streamlit as st

# ============================================================
#  Page Configuration
# ============================================================
st.set_page_config(
    page_title="Dhikr Counter | اللهم صلي على محمد",
    page_icon="📿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ============================================================
#  Custom CSS for a beautiful, centered layout
# ============================================================
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        }
        .dhikr-text {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #FFD700;
            margin: 20px 0 10px 0;
            line-height: 1.6;
            direction: rtl;
        }
        .count-number {
            text-align: center;
            font-size: 120px;
            font-weight: bold;
            color: #FFFFFF;
            margin: 10px 0;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
        }
        .goal-text {
            text-align: center;
            font-size: 18px;
            color: #A0D8EF;
            margin-bottom: 25px;
        }
        .footer-text {
            text-align: center;
            font-size: 14px;
            color: #888888;
            margin-top: 40px;
        }
        /* Style the buttons */
        div.stButton > button {
            font-size: 20px;
            font-weight: bold;
            border-radius: 12px;
            padding: 15px 0;
            transition: transform 0.1s ease;
        }
        div.stButton > button:hover {
            transform: scale(1.03);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
#  Session State Initialization
# ============================================================
if "count" not in st.session_state:
    st.session_state.count = 0
if "target" not in st.session_state:
    st.session_state.target = 100

# ============================================================
#  Header
# ============================================================
st.markdown('<div class="dhikr-text">اللهم صلي على محمد</div>', unsafe_allow_html=True)

# ============================================================
#  Count Display
# ============================================================
st.markdown(f'<div class="count-number">{st.session_state.count}</div>', unsafe_allow_html=True)

# Progress toward target
if st.session_state.target > 0:
    progress = min(st.session_state.count / st.session_state.target, 1.0)
    st.progress(progress)
    st.markdown(
        f'<div class="goal-text">Target: {st.session_state.target} '
        f'({st.session_state.count}/{st.session_state.target})</div>',
        unsafe_allow_html=True,
    )

# ============================================================
#  Action Buttons
# ============================================================
col1, col2 = st.columns([3, 1])

with col1:
    if st.button("📿 Count", use_container_width=True, type="primary"):
        st.session_state.count += 1

with col2:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.count = 0

# ============================================================
#  Target Setting
# ============================================================
with st.expander("⚙️ Settings"):
    new_target = st.number_input(
        "Set your target (0 to disable):",
        min_value=0,
        max_value=100000,
        value=st.session_state.target,
        step=10,
    )
    if new_target != st.session_state.target:
        st.session_state.target = new_target
        st.rerun()

# ============================================================
#  Auto-Reminder When Goal Reached
# ============================================================
if (
    st.session_state.target > 0
    and st.session_state.count == st.session_state.target
):
    st.success(f"🎉 ماشاء الله! You reached {st.session_state.target} repetitions!")
    st.balloons()

# ============================================================
#  Footer
# ============================================================
st.markdown(
    '<div class="footer-text">May Allah accept your dhikr 🤲</div>',
    unsafe_allow_html=True,
)
streamlit
