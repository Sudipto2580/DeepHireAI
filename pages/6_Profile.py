import streamlit as st
import pandas as pd

from utils.auth import get_user
from utils.supabase_db import get_all_candidates
from utils.theme import load_theme

load_theme()

if not st.session_state.get(
    "logged_in",
    False
):
    st.switch_page("app.py")

email = st.session_state.get(
    "user_email"
)

user = get_user(email)

history = get_all_candidates()

total = len(history)

best_score = 0

if history:

    df = pd.DataFrame(
        history,
        columns=[
            "ID",
            "Filename",
            "Score",
            "Semantic",
            "Skill",
            "Matched",
            "Missing"
        ]
    )

    best_score = round(
        pd.to_numeric(
            df["Score"],
            errors="coerce"
        ).max(),
        2
    )

st.markdown(
"""
# 👤 Professional Profile
"""
)

st.markdown(
f"""
<div style="
padding:25px;
border-radius:20px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.1);
">

<h2>{user["fullname"]}</h2>

<p>@{user["username"]}</p>

<p>📧 {user["email"]}</p>

<p>📱 {user["phone"]}</p>

</div>
""",
unsafe_allow_html=True
)

st.markdown("## 🌐 Social Profiles")

c1,c2 = st.columns(2)

with c1:

    st.info(
        f"🔗 LinkedIn\n\n{user['linkedin']}"
    )

    st.info(
        f"💻 GitHub\n\n{user['github']}"
    )

with c2:

    st.info(
        f"🌐 Portfolio\n\n{user['portfolio']}"
    )

    st.info(
        f"🐦 X / Twitter\n\n{user['twitter']}"
    )

st.info(
    f"📸 Instagram\n\n{user['instagram']}"
)

st.divider()

st.markdown("## 📊 Account Statistics")

col1,col2,col3 = st.columns(3)

col1.metric(
    "Total Analyses",
    total
)

col2.metric(
    "Best ATS",
    best_score
)

col3.metric(
    "Theme",
    user["theme"]
)

st.divider()

st.markdown(
f"""
### 🚀 Member Since

{user["created_at"]}
"""
)
