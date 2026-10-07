import streamlit as st


def show_exercise():

    st.header("🏃 Exercise Tracker")

    st.write(
        "Record your physical activities and keep track of your "
        "daily movement."
    )

    # ==================================================
    # ADD EXERCISE
    # ==================================================

    st.subheader("➕ Add Exercise")

    exercise = st.selectbox(
        "Exercise",
        [
            "Walking",
            "Running",
            "Cycling",
            "Squats",
            "Push-ups",
            "Plank",
            "Yoga",
            "Stretching",
            "Other"
        ]
    )

    duration = st.number_input(
        "Duration (minutes)",
        min_value=1,
        max_value=300,
        value=30
    )

    if st.button(
        "➕ Add Exercise",
        use_container_width=True
    ):

        st.session_state.exercise_entries.append(
            {
                "exercise": exercise,
                "duration": duration
            }
        )

        st.success(
            f"Added {exercise} for {duration} minutes."
        )

    # ==================================================
    # TODAY'S EXERCISE
    # ==================================================

    st.divider()

    st.subheader("📋 Today's Exercise")

    if len(st.session_state.exercise_entries) == 0:

        st.info(
            "No exercise entries yet."
        )

    else:

        total_minutes = 0

        for entry in st.session_state.exercise_entries:

            st.markdown(
                f"""
                <div class="dashboard-card">

                    <h3>🏃 {entry['exercise']}</h3>

                    <p>
                        Duration: {entry['duration']} minutes
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            total_minutes += entry["duration"]

        # ==================================================
        # TOTAL ACTIVITY
        # ==================================================

        st.metric(
            "Total Exercise Today",
            f"{total_minutes} min"
        )