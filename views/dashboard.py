from datetime import date, timedelta

import streamlit as st

from database import add_entry, get_completions, get_entries, set_completion, undo_water
from planner import weekly_schedule
from views.guided_workout import show_guided_workout


def show_dashboard():

    if not st.session_state.profile_saved:

        st.markdown(
            """
            <div class="dashboard-card">
                <h2>👋 Welcome to FitMan AI</h2>
                <p>
                    Create your profile first and FitMan AI will build
                    your personalized wellness dashboard.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        return

    profile = st.session_state.profile
    plan = st.session_state.plan

    # ==================================================
    # DAILY OVERVIEW
    # ==================================================

    st.markdown(
        '<div class="section-title">Your Overview</div>',
        unsafe_allow_html=True
    )

    today = date.today()
    entries = get_entries(today, today)
    food_count = sum(row["kind"] == "food" for row in entries)
    exercise_minutes = sum(row["amount"] for row in entries if row["kind"] == "exercise")
    water_ml = sum(row["amount"] for row in entries if row["kind"] == "water")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Water today", f"{water_ml:,} mL")
        if st.button("Add 250 mL", type="primary"):
            add_entry("water", today, "Water", 250)
            st.rerun()
        if water_ml and st.button("Undo last glass"):
            undo_water(today)
            st.rerun()

    with col2:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <h3>🍎 Food</h3>
                <p>
                    Meals and food entries tracked.
                </p>
                <h2>{food_count}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <h3>🏃 Activity</h3>
                <p>
                    Exercise logged today.
                </p>
                <h2>{exercise_minutes} min</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    monday = today - timedelta(days=today.weekday())
    schedule = weekly_schedule(plan, monday)
    completed = get_completions(monday, monday + timedelta(days=6))
    session = schedule[today]

    st.subheader("Today's workout")
    if session is None:
        st.info("Rest day")
    else:
        st.write(f"{session['location']} · {session['minutes']} minutes · {plan['preferred_time']}")
        for exercise in session["exercises"]:
            st.write(f"• {exercise}")
        done = today.isoformat() in completed
        if st.button("Undo completion" if done else "Mark workout complete", type="primary"):
            set_completion(today, not done)
            st.rerun()

    if session is not None:
        show_guided_workout(today, session["exercises"], done)

    with st.expander("Weekly workout calendar", expanded=True):
        for day, workout in schedule.items():
            status = "Completed" if day.isoformat() in completed else "Training" if workout else "Rest"
            label = f"{day:%A, %b %d} · {status}"
            if workout:
                label += f" · {workout['minutes']} min · {workout['location']}"
            st.write(label)
            if workout:
                st.caption(" · ".join(workout["exercises"]))

    # ==================================================
    # RECOMMENDATIONS
    # ==================================================

    st.markdown(
        '<div class="section-title">✨ Your Recommendations</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <h3>🎯 Your Focus</h3>
                <p>
                    {plan["goal_recommendation"]}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="dashboard-card">
                <h3>🍎 Nutrition</h3>
                <p>
                    {plan["food_recommendation"]}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <h3>🚶 Daily Activity</h3>
                <p>
                    {plan["activity_recommendation"]}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="dashboard-card">
                <h3>😴 Recovery</h3>
                <p>
                    {plan["sleep_recommendation"]}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ==================================================
    # PROFILE SUMMARY
    # ==================================================

    st.markdown(
        '<div class="section-title">👤 Profile Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(
            f"**Age:** {profile['age']}"
        )

    with col2:
        st.write(
            f"**Activity:** {profile['activity']}"
        )

    with col3:
        st.write(
            f"**Experience:** {profile['experience']}"
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(
            f"**Workout:** {profile['workout_location']}"
        )

    with col2:
        st.write(
            f"**Diet:** {profile['diet']}"
        )

    with col3:
        st.write(
            f"**Preferred Time:** {profile['preferred_time']}"
        )