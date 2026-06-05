import streamlit as st

from utils.auth import login, signup
from utils.database import create_database

st.set_page_config(
    page_title="DeepHire AI",
    page_icon="🚀",
    layout="wide"
)

create_database()

# ---------------------------
# SESSION
# ---------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

# ---------------------------
# HIDE SIDEBAR BEFORE LOGIN
# ---------------------------

if not st.session_state.logged_in:

    st.markdown(
    """
    <style>
    [data-testid="stSidebar"]{
        display:none;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

# ---------------------------
# LOAD CSS
# ---------------------------

css_file = (
    "assets/styles.css"
    if st.session_state.theme == "Dark"
    else "assets/light.css"
)

with open(css_file) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------------------
# ALREADY LOGGED IN
# ---------------------------

if st.session_state.logged_in:

    st.switch_page(
        "pages/1_Dashboard.py"
    )

# ---------------------------
# HERO
# ---------------------------

st.markdown(
"""
<h3 style='
text-align:center;
color:#cbd5e1;
'>
Enterprise Recruitment Intelligence Platform
</h3>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------
# MAIN LAYOUT
# ---------------------------

left, right = st.columns([1.2, 1])

# =====================================================
# LEFT SIDE
# =====================================================

with left:

    st.markdown(
    """
    ### 🚀 AI Recruitment Platform

    AI ATS Screening • Resume Intelligence • AI Recruiter • AI Interviewer
    """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.info("📄 ATS Screening")
        st.info("🤖 AI Recruiter")

    with c2:
        st.info("🎤 AI Interviewer")
        st.info("📊 Analytics")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
    """
    ### Why DeepHire AI?

    ✅ ATS Resume Screening

    ✅ Candidate Ranking

    ✅ Resume Intelligence

    ✅ Gemini AI Assistant

    ✅ AI Recruiter

    ✅ AI Interview Agent

    ✅ Analytics Dashboard

    ✅ Cloud Database
    """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "Resumes",
            "1000+"
        )

    with m2:
        st.metric(
            "Accuracy",
            "95%"
        )

    with m3:
        st.metric(
            "AI Model",
            "Gemini"
        )

# =====================================================
# RIGHT SIDE
# =====================================================

with right:

    st.markdown(
    """
    <div style="
    padding:25px;
    border-radius:20px;
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.1);
    ">
    """,
    unsafe_allow_html=True
    )

    login_tab, signup_tab = st.tabs(
        ["🔐 Login", "📝 Sign Up"]
    )

    # =================================================
    # LOGIN
    # =================================================

    with login_tab:

        st.subheader(
            "Welcome Back"
        )

        login_email = st.text_input(
            "Email",
            key="login_email"
        )

        login_password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            user = login(
                login_email,
                login_password
            )

            if user:

                st.session_state.logged_in = True

                st.session_state.user_email = (
                    login_email
                )

                st.success(
                    "Login Successful"
                )

                st.switch_page(
                    "pages/1_Dashboard.py"
                )

            else:

                st.error(
                    "Invalid Credentials"
                )

        st.divider()

        st.button(
            "🔵 Continue with Google",
            use_container_width=True,
            disabled=True
        )

        st.button(
            "💼 Continue with LinkedIn",
            use_container_width=True,
            disabled=True
        )

    # =================================================
    # SIGNUP
    # =================================================

    with signup_tab:

        st.subheader(
            "Create Account"
        )

        fullname = st.text_input(
            "Full Name"
        )

        username = st.text_input(
            "Username"
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        phone = st.text_input(
            "Phone"
        )

        linkedin = st.text_input(
            "LinkedIn"
        )

        github = st.text_input(
            "GitHub"
        )

        portfolio = st.text_input(
            "Portfolio"
        )

        twitter = st.text_input(
            "X / Twitter"
        )

        instagram = st.text_input(
            "Instagram"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            success = signup(
                fullname,
                username,
                email,
                password,
                phone,
                linkedin,
                github,
                portfolio,
                twitter,
                instagram
            )

            if success:

                st.session_state.logged_in = True

                st.session_state.user_email = email

                st.success(
                    "Account Created Successfully"
                )

                st.balloons()

                st.switch_page(
                    "pages/1_Dashboard.py"
                )

            else:

                st.error(
                    "Account already exists"
                )


st.markdown("<br><br>", unsafe_allow_html=True)

st.caption(
    "DeepHire AI • Powered by Gemini 2.5 Flash • Developed by Sudipto Bairagi / NIT Jalandhar"
)