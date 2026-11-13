from base64 import b64encode
from html import escape
from pathlib import Path

import streamlit as st

from database import initialize_workspace, load_profile
from planner import plan_for_profile
from views.progress import show_progress
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


@st.cache_resource
def prepare_storage():
    initialize_workspace()


prepare_storage()
if "profile" not in st.session_state:
    profile = load_profile()
    st.session_state.profile = profile
    st.session_state.profile_saved = bool(profile)
    st.session_state.plan = plan_for_profile(profile) if profile else None

pages = {
    "Profile": (show_profile, ":material/person:"),
    "Dashboard": (show_dashboard, ":material/dashboard:"),
    "Food": (show_food, ":material/restaurant:"),
    "Exercise": (show_exercise, ":material/fitness_center:"),
    "Progress": (show_progress, ":material/monitoring:"),
}
if "active_page" not in st.session_state:
    st.session_state.active_page = "Dashboard" if st.session_state.profile_saved else "Profile"

with st.sidebar:

    st.markdown(
        f'''<div class="fitman-brand">
            <img src="{image_data(LOGO, 'image/png')}" alt="">
            <span>FitMan <em>AI</em></span>
        </div>''',
        unsafe_allow_html=True,
    )

    st.caption("WORKSPACE")
    with st.container(key="fitman_navigation"):
        for label, (_, icon) in pages.items():
            active = label == st.session_state.active_page
            st.button(
                label,
                icon=icon,
                key=f"nav_{label}",
                type="primary" if active else "secondary",
                use_container_width=True,
                on_click=st.session_state.update,
                kwargs={"active_page": label},
            )

page = st.session_state.active_page
if page == "Profile":
    show_hero("Build your training plan", "Set your goals, training preferences, and recovery routine.")
elif page == "Dashboard":
    name = st.session_state.profile.get("name")
    title = f"Welcome, {name}" if name else "Dashboard"
    show_hero(title, "Your workout plan, hydration, and activity in one place.")

pages[page][0]()
