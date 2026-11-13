from base64 import b64encode
from html import escape
from pathlib import Path

import streamlit as st

from views.profile import show_profile
from views.dashboard import show_dashboard
from views.food import show_food
from views.exercise import show_exercise


ASSETS = Path(__file__).resolve().parent / "frontend"
LOGO = ASSETS / "images" / "fitman-logo.png"
HERO = ASSETS / "images" / "fitman-hero.webp"

st.set_page_config(page_title="FitMan AI", page_icon=str(LOGO), layout="wide")
st.markdown(
    f"<style>{(ASSETS / 'styles' / 'style.css').read_text(encoding='utf-8-sig')}</style>",
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def image_data(path, media_type):
    return f"data:{media_type};base64,{b64encode(path.read_bytes()).decode('ascii')}"


def show_hero(title, description):
    background = "linear-gradient(90deg, #101b16 0%, #101b1666 65%, #101b1626)"
    if HERO.is_file():
        background += f", url({image_data(HERO, 'image/webp')})"
    st.markdown(
        f'''<section class="fitman-hero" style="background-image: {background}">
            <div>
                <h1 class="fitman-title">{escape(title)}</h1>
                <p class="fitman-subtitle">{escape(description)}</p>
            </div>
        </section>''',
        unsafe_allow_html=True,
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
        f'''<div class="fitman-brand">
            <img src="{image_data(LOGO, 'image/png')}" alt="">
            <span>FitMan <em>AI</em></span>
        </div>''',
        unsafe_allow_html=True,
    )

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
    show_hero("Build your training plan", "Set your goals, training preferences, and recovery routine.")
    show_profile()


elif page == "📊 Dashboard":
    name = st.session_state.profile.get("name")
    title = f"Welcome, {name}" if name else "Dashboard"
    show_hero(title, "Your workout plan, hydration, and activity in one place.")
    show_dashboard()


elif page == "🍎 Food":

    show_food()


elif page == "🏃 Exercise":

    show_exercise()