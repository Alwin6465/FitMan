from datetime import date

import streamlit as st

from database import add_entry, get_entries


def show_exercise():

    st.title("Exercise Tracker")

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
        type="primary",
        use_container_width=True
    ):

        add_entry("exercise", date.today(), exercise, duration)
        st.success(f"Added {exercise} for {duration} minutes.")

    st.divider()
    st.subheader("Today's exercise")
    today = date.today()
    entries = [row for row in get_entries(today, today) if row["kind"] == "exercise"]
    if not entries:
        st.info("No exercise entries yet.")
    else:
        for row in entries:
            st.text(f"{row['label']} · {row['amount']} min")
        st.metric("Total exercise today", f"{sum(row['amount'] for row in entries)} min")
