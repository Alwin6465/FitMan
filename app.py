import streamlit as st
from pathlib import Path

from pages.profile import show_profile
from pages.dashboard import show_dashboard
from pages.food import show_food
from pages.exercise import show_exercise


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="FitMan AI",
    page_icon="💪",
    layout="wide"
)


# ==================================================
# LOAD CSS
# ==================================================

css_file = Path("frontend/styles/style.css")

if css_file.exists():
    with open(css_file, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# ==================================================
# SESSION STATE
# ==================================================

if "profile_saved" not in st.session_state:
    st.session_state.profile_saved = False

if "profile" not in st.session_state:
    st.session_state.profile = {}

if "plan" not in st.session_state:
    st.session_state.plan = None

if "food_entries" not in st.session_state:
    st.session_state.food_entries = []

if "exercise_entries" not in st.session_state:
    st.session_state.exercise_entries = []


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown(
        """
        # 💪 FitMan AI

        Your personal fitness and wellness companion.
        """
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "👤 Profile",
            "📊 Dashboard",
            "🍎 Food",
            "🏃 Exercise"
        ]
    )


# ==================================================
# PAGE ROUTING
# ==================================================

if page == "👤 Profile":

    show_profile()


elif page == "📊 Dashboard":

    show_dashboard()


elif page == "🍎 Food":

    show_food()


elif page == "🏃 Exercise":

    show_exercise()