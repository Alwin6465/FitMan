import streamlit as st
from planner import create_plan


def saved_option(label, options, saved_value):
    index = options.index(saved_value) if saved_value in options else 0
    return st.selectbox(label, options, index=index)


def show_profile():

    profile = st.session_state.profile

    # ==================================================
    # BASIC INFORMATION
    # ==================================================

    st.subheader("Basic Information")

    name = st.text_input(
        "Name",
        value=profile.get("name", "")
    )

    age = st.number_input(
        "Age",
        min_value=13,
        max_value=100,
        value=profile.get("age", 18)
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=profile.get("height", 170)
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=30,
        max_value=300,
        value=profile.get("weight", 70)
    )

    gender = saved_option(
        "Gender",
        [
            "Male",
            "Female",
            "Other / Prefer not to say"
        ],
        profile.get("gender")
    )

    # ==================================================
    # FITNESS INFORMATION
    # ==================================================

    st.subheader("🏃 Fitness Information")

    activity = saved_option(
        "Activity Level",
        [
            "Low",
            "Moderate",
            "High"
        ],
        profile.get("activity")
    )

    experience = saved_option(
        "Workout Experience",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ],
        profile.get("experience")
    )

    goal = saved_option(
        "Main Goal",
        [
            "General Wellness",
            "Build Strength",
            "Improve Fitness",
            "Build Healthy Habits"
        ],
        profile.get("goal")
    )

    workout_location = saved_option(
        "Where do you usually work out?",
        [
            "Gym",
            "Home",
            "Outdoor"
        ],
        profile.get("workout_location")
    )

    workout_time = st.slider(
        "How much time do you have for a workout?",
        min_value=15,
        max_value=180,
        value=profile.get("workout_time", 45),
        step=15
    )

    preferred_time = saved_option(
        "Preferred Workout Time",
        [
            "Morning",
            "Afternoon",
            "Evening"
        ],
        profile.get("preferred_time")
    )

    plan_days = saved_option(
        "How many days per week would you like a plan for?",
        [
            2,
            3,
            5,
            7
        ],
        profile.get("plan_days")
    )

    # ==================================================
    # FOOD & RECOVERY
    # ==================================================

    st.subheader("🍎 Food & Recovery")

    diet = saved_option(
        "Diet Preference",
        [
            "No Restrictions",
            "Vegetarian",
            "Vegan",
            "High Protein",
            "Other"
        ],
        profile.get("diet")
    )

    bedtime = st.time_input(
        "Usual Bedtime",
        value=profile.get("bedtime", "now")
    )

    wake_time = st.time_input(
        "Usual Wake-up Time",
        value=profile.get("wake_time", "now")
    )

    # ==================================================
    # SAVE PROFILE
    # ==================================================

    if st.button(
        "🚀 Save Profile",
        type="primary",
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