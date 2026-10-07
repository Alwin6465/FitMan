import streamlit as st
from planner import create_plan
from pathlib import Path


# ==================================================
# PAGE SETUP
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

with open(css_file) as f:
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
# HEADER
# ==================================================

st.markdown(
    """
    <div class="fitman-header">
        <div class="fitman-title">💪 FitMan AI</div>
        <div class="fitman-subtitle">
            Your personal AI-powered fitness and wellness companion
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("💪 FitMan AI")

page = st.sidebar.selectbox(
    "Choose a page",
    [
        "Profile",
        "Dashboard",
        "Food",
        "Exercise"
    ]
)


# ==================================================
# PROFILE PAGE
# ==================================================

if page == "Profile":

    st.header("👤 Your Profile")

    st.write(
        "Tell FitMan about yourself. Your information will be used "
        "to create personalized recommendations."
    )

    # ----------------------------------------------
    # BASIC INFORMATION
    # ----------------------------------------------

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

    # ----------------------------------------------
    # FITNESS INFORMATION
    # ----------------------------------------------

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

    # ----------------------------------------------
    # FOOD & RECOVERY
    # ----------------------------------------------

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

    # ----------------------------------------------
    # SAVE PROFILE
    # ----------------------------------------------

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

    # ----------------------------------------------
    # PERSONALIZED PLAN
    # ----------------------------------------------

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


# ==================================================
# DASHBOARD PAGE
# ==================================================

elif page == "Dashboard":

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

    else:

        profile = st.session_state.profile
        plan = st.session_state.plan

        # ------------------------------------------
        # WELCOME HEADER
        # ------------------------------------------

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

        # ------------------------------------------
        # DAILY OVERVIEW
        # ------------------------------------------

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

        # ------------------------------------------
        # TODAY'S WORKOUT
        # ------------------------------------------

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

        # ------------------------------------------
        # RECOMMENDATIONS
        # ------------------------------------------

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

        # ------------------------------------------
        # PROFILE SUMMARY
        # ------------------------------------------

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


# ==================================================
# FOOD PAGE
# ==================================================

elif page == "Food":

    st.header("🍎 Food Tracker")

    st.write(
        "Keep track of meals and snacks you have logged."
    )

    food_name = st.text_input(
        "Food or Meal"
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    if st.button(
        "➕ Add Food",
        use_container_width=True
    ):

        if food_name.strip() == "":
            st.warning(
                "Please enter a food."
            )

        else:

            st.session_state.food_entries.append(
                {
                    "food": food_name,
                    "quantity": quantity
                }
            )

            st.success(
                f"Added {quantity} × {food_name}"
            )

    st.divider()

    st.subheader(
        "📋 Today's Food"
    )

    if len(st.session_state.food_entries) == 0:

        st.info(
            "No food entries yet."
        )

    else:

        for entry in st.session_state.food_entries:

            st.markdown(
                f"""
                <div class="dashboard-card">
                    🍎 {entry['quantity']} × {entry['food']}
                </div>
                """,
                unsafe_allow_html=True
            )


# ==================================================
# EXERCISE PAGE
# ==================================================

elif page == "Exercise":

    st.header("🏃 Exercise Tracker")

    st.write(
        "Record physical activities you complete."
    )

    exercise = st.selectbox(
        "Exercise",
        [
            "Walking",
            "Running",
            "Squats",
            "Push-ups",
            "Plank"
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

    st.divider()

    st.subheader(
        "📋 Today's Exercise"
    )

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
                    <p>{entry['duration']} minutes</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            total_minutes += entry["duration"]

        st.metric(
            "Total Exercise",
            f"{total_minutes} min"
        )