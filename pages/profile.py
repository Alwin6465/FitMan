import streamlit as st
from planner import create_plan


def show_profile():

    st.header("👤 Your Profile")

    st.write(
        "Tell FitMan about yourself. Your information will be used "
        "to create personalized recommendations."
    )

    # ==================================================
    # BASIC INFORMATION
    # ==================================================

    st.subheader("Basic Information")

    name = st.text_input(
        "Name",
        value=st.session_state.profile.get("name", "")
    )

    age = st.number_input(
        "Age",
        min_value=13,
        max_value=100,
        value=st.session_state.profile.get("age", 18)
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=st.session_state.profile.get("height", 170)
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=30,
        max_value=300,
        value=st.session_state.profile.get("weight", 70)
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other / Prefer not to say"
        ]
    )

    # ==================================================
    # FITNESS INFORMATION
    # ==================================================

    st.subheader("🏃 Fitness Information")

    activity = st.selectbox(
        "Activity Level",
        [
            "Low",
            "Moderate",
            "High"
        ]
    )

    experience = st.selectbox(
        "Workout Experience",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    goal = st.selectbox(
        "Main Goal",
        [
            "General Wellness",
            "Build Strength",
            "Improve Fitness",
            "Build Healthy Habits"
        ]
    )

    workout_location = st.selectbox(
        "Where do you usually work out?",
        [
            "Gym",
            "Home",
            "Outdoor"
        ]
    )

    workout_time = st.slider(
        "How much time do you have for a workout?",
        min_value=15,
        max_value=180,
        value=45,
        step=15
    )

    preferred_time = st.selectbox(
        "Preferred Workout Time",
        [
            "Morning",
            "Afternoon",
            "Evening"
        ]
    )

    plan_days = st.selectbox(
        "How many days per week would you like a plan for?",
        [
            2,
            3,
            5,
            7
        ]
    )

    # ==================================================
    # FOOD & RECOVERY
    # ==================================================

    st.subheader("🍎 Food & Recovery")

    diet = st.selectbox(
        "Diet Preference",
        [
            "No Restrictions",
            "Vegetarian",
            "Vegan",
            "High Protein",
            "Other"
        ]
    )

    bedtime = st.time_input(
        "Usual Bedtime"
    )

    wake_time = st.time_input(
        "Usual Wake-up Time"
    )

    # ==================================================
    # SAVE PROFILE
    # ==================================================

    if st.button(
        "🚀 Save Profile",
        use_container_width=True
    ):

        if name.strip() == "":
            st.warning("Please enter your name.")

        else:

            st.session_state.profile = {
                "name": name,
                "age": age,
                "height": height,
                "weight": weight,
                "gender": gender,
                "activity": activity,
                "experience": experience,
                "goal": goal,
                "workout_location": workout_location,
                "workout_time": workout_time,
                "preferred_time": preferred_time,
                "plan_days": plan_days,
                "diet": diet,
                "bedtime": bedtime,
                "wake_time": wake_time
            }

            st.session_state.plan = create_plan(
                age=age,
                gender=gender,
                activity=activity,
                experience=experience,
                goal=goal,
                workout_location=workout_location,
                workout_time=workout_time,
                preferred_time=preferred_time,
                diet=diet,
                bedtime=bedtime,
                wake_time=wake_time,
                plan_days=plan_days
            )

            st.session_state.profile_saved = True

            st.success(
                "✅ Profile saved successfully!"
            )

    # ==================================================
    # SHOW PERSONALIZED PLAN
    # ==================================================

    if st.session_state.profile_saved:

        plan = st.session_state.plan

        st.divider()

        st.header(
            "🤖 Your Personalized FitMan Plan"
        )

        st.subheader(
            "🏋️ Recommended Workout"
        )

        for exercise in plan["workout"]:
            st.write(
                "•",
                exercise
            )

        st.subheader(
            "🎯 Goal Recommendation"
        )

        st.info(
            plan["goal_recommendation"]
        )

        st.subheader(
            "🍎 Nutrition Recommendation"
        )

        st.info(
            plan["food_recommendation"]
        )

        st.subheader(
            "🚶 Activity Recommendation"
        )

        st.info(
            plan["activity_recommendation"]
        )

        st.subheader(
            "⏱️ Workout Recommendation"
        )

        st.info(
            plan["time_recommendation"]
        )

        st.subheader(
            "😴 Sleep & Recovery"
        )

        st.info(
            plan["sleep_recommendation"]
        )