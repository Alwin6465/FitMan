import streamlit as st


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
    # WELCOME HEADER
    # ==================================================

    st.markdown(
        f"""
        <div class="fitman-header">
            <div class="fitman-title">
                👋 Welcome, {profile["name"]}
            </div>

            <div class="fitman-subtitle">
                Here's your personalized FitMan AI overview.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # DAILY OVERVIEW
    # ==================================================

    st.markdown(
        '<div class="section-title">Your Daily Overview</div>',
        unsafe_allow_html=True
    )

    food_count = len(
        st.session_state.food_entries
    )

    exercise_minutes = sum(
        item["duration"]
        for item in st.session_state.exercise_entries
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>💧 Hydration</h3>
                <p>
                    Stay hydrated throughout your day.
                </p>
                <h2>0 L</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

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
                    Exercise recorded today.
                </p>
                <h2>{exercise_minutes} min</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ==================================================
    # TODAY'S WORKOUT
    # ==================================================

    st.markdown(
        '<div class="section-title">💪 Today\'s Workout</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="dashboard-card">

            <p>
                <strong>📍 Location:</strong>
                {plan["workout_location"]}
            </p>

            <p>
                <strong>⏰ Preferred Time:</strong>
                {plan["preferred_time"]}
            </p>

            <p>
                <strong>⏱️ Duration:</strong>
                {plan["workout_time"]} minutes
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    for exercise in plan["workout"]:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <h3>🏋️ {exercise}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

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