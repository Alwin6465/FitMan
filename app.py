import streamlit as st

st.set_page_config(
    page_title="FitMan AI",
    page_icon="💪",
    layout="wide"
)

# -------------------------
# TITLE
# -------------------------

st.title("FitMan AI")

st.write(
    "Welcome to FitMan AI, your personal fitness coach powered by AI! "
    "This app will help you create personalized workout plans and track your progress."
)

st.divider()


# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("FitMan AI")
st.sidebar.write("Navigation")

page = st.sidebar.selectbox(
    "Select a page",
    ["Profile", "Dashboard", "Food", "Exercise"]
)


# -------------------------
# PROFILE PAGE
# -------------------------

if page == "Profile":

    st.header("👤 Create Your Profile")

    st.write(
        "Tell FitMan about yourself so we can create "
        "a personalized wellness plan."
    )

    st.divider()

    st.subheader("Basic Information")

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=13,
        max_value=100,
        value=18
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=170.0
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=300.0,
        value=70.0
    )

    st.divider()

    st.subheader("Fitness Information")

    activity = st.selectbox(
        "Activity Level",
        ["Low", "Moderate", "High"]
    )

    experience = st.selectbox(
        "Fitness Experience",
        ["Beginner", "Intermediate", "Advanced"]
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

    st.divider()

    st.subheader("Workout Preferences")

    workout_location = st.selectbox(
        "Where do you normally exercise?",
        ["Gym", "Home", "Outdoor"]
    )

    workout_time = st.slider(
        "Available workout time (minutes)",
        min_value=15,
        max_value=120,
        value=45,
        step=15
    )

    preferred_time = st.selectbox(
        "Preferred workout time",
        ["Morning", "Afternoon", "Evening"]
    )

    st.divider()

    st.subheader("Food Preferences")

    diet = st.selectbox(
        "Food Preference",
        [
            "No Restrictions",
            "Vegetarian",
            "Vegan",
            "High Protein",
            "Other"
        ]
    )

    st.divider()

    st.subheader("Sleep Schedule")

    col1, col2 = st.columns(2)

    with col1:
        bedtime = st.time_input("Typical Bedtime")

    with col2:
        wake_time = st.time_input("Typical Wake-up Time")

    st.divider()

    if st.button("🚀 Save Profile", use_container_width=True):

        if name.strip() == "":
            st.warning("Please enter your name.")

        else:
            st.success("Profile saved successfully!")

            st.write("### Your Information")

            st.write("**Name:**", name)
            st.write("**Age:**", age)
            st.write("**Height:**", height, "cm")
            st.write("**Weight:**", weight, "kg")
            st.write("**Activity Level:**", activity)
            st.write("**Fitness Experience:**", experience)
            st.write("**Goal:**", goal)
            st.write("**Workout Location:**", workout_location)
            st.write("**Workout Time:**", workout_time, "minutes")
            st.write("**Preferred Workout Time:**", preferred_time)
            st.write("**Food Preference:**", diet)
            st.write("**Bedtime:**", bedtime)
            st.write("**Wake-up Time:**", wake_time)


# -------------------------
# DASHBOARD PAGE
# -------------------------

elif page == "Dashboard":

    st.header("📊 Dashboard")

    st.write(
        "Your daily wellness overview will appear here."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💧 Water", "0 L")

    with col2:
        st.metric("🍎 Food Entries", "0")

    with col3:
        st.metric("🏃 Exercise", "0 min")

    st.divider()

    st.info(
        "Start by creating your profile and logging "
        "your meals and activities."
    )


# -------------------------
# FOOD PAGE
# -------------------------

elif page == "Food":

    st.header("🍎 Food Tracker")

    st.write(
        "Log the food you eat throughout the day."
    )

    food = st.text_input("Food")

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    if st.button("Add Food"):

        if food.strip() == "":
            st.warning("Please enter a food.")

        else:
            st.success(
                f"Added {quantity} × {food}"
            )


# -------------------------
# EXERCISE PAGE
# -------------------------

elif page == "Exercise":

    st.header("🏃 Exercise Tracker")

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
        value=10
    )

    if st.button("Add Exercise"):

        st.success(
            f"Added {duration} minutes of {exercise}."
        )