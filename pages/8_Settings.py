import streamlit as st

from utils.auth import get_user
from utils.theme import load_theme

load_theme()

if not st.session_state.get(
    "logged_in",
    False
    ):
    st.switch_page(
    "app.py"
    )

email = st.session_state.get(
"user_email"
)

user = get_user(email)

st.title(
"⚙ Settings"
)

tab1,tab2,tab3 = st.tabs(
[
"🎨 Appearance",
"👤 Account",
"👨‍💻 Developer"
]
)

# ------------------------

# APPEARANCE

# ------------------------

with tab1:

    theme = st.selectbox(
        "Theme",
        [
            "Dark",
            "Light",
            "Midnight Blue",
            "Corporate"
        ]
    )

    if st.button(
        "Save Theme"
    ):

        st.session_state.theme = theme

        st.success(
        f"{theme} Theme Applied"
    )


# ------------------------

# ACCOUNT

# ------------------------

with tab2:

    st.subheader(
    user["fullname"]
    )

    st.write(
    f"📧 {user['email']}"
    )

    st.write(
    f"📱 {user['phone']}"
    )

    st.write(
    f"🔗 {user['linkedin']}"
    )

    st.write(
    f"💻 {user['github']}"
    )

    st.write(
    f"🌐 {user['portfolio']}"
    )

    st.write(
    f"🐦 {user['twitter']}"
    )

    st.write(
    f"📷 {user['instagram']}"
    )


# ------------------------

# DEVELOPER

# ------------------------

with tab3:

    st.markdown(
    """
    ```

### 🚀 DeepHire AI v2.0

Developer:

Sudipto Bairagi

AI AND Machine Learning Engineer ASPIRANT

Department of Computer Science and Engineering

Dr B R Ambedkar NIT Jalandhar

Powered By:

• Gemini 2.5 Flash

• Sentence Transformers

• FAISS

• Streamlit
"""
)

st.divider()

email = st.session_state.get(
    "user_email",
    "Unknown"
)

st.divider()

if st.button(
    "🚪 Logout",
    use_container_width=True
):
    st.session_state.clear()
    st.switch_page("app.py")
    
    st.sidebar.markdown("---")


