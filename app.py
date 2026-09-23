import streamlit as st

st.set_page_config(
    page_title="FitCoach AI",
    page_icon=":💪",
    layout="wide"
)

#Title
st.title("FitMan AI")
st.write("Welcome to FitMan AI, your personal fitness coach powered by AI! This app will help you create personalized workout plans and track your progress.")
st.divider()
# Sidebar
st.sidebar.title("FitMan AI")
st.sidebar.write("Navigation")

page = st.sidebar.selectbox("Select a page", ["Profile","Dashboard", "Food", "Exercise"])

#PROFILE PAGE

if page =="👤 Profile":
    st.header ("Create Your Profile")

    name = st.text_input ("Name")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=22
    )
    height= st.number_input(
        "Heaight (cm)",
        min_value= 50.0,
        max_value=300.0,
        value=170.0
    )

    activity= st.selectbox(
        "Activity Level",
        [
            "low",
            "Moderate",
            "High",
        ]
    )

    goal= st.selectbox(
        "Main Goal",
        [
            "Lose Weight",
            "Gain Muscle",
            "Maintain Weight",
        ]
    )
    if st.button("Save Profile"):

        if name == "":
            st.warning("Please enter your name.")

        else:
            st.success("Profile saved successfully!")
            st.write("### Your Information")

            st.write("Name:", name)
            st.write("Age:", age)
            st.write("Height:", height, "cm")
            st.write("Activity Level:", activity)
            st.write("Goal:", goal)

            #Dashboard Page
            

    elif page=="Dashboard":
        st.header("📊 Dashboard")
        st.write("Your daily wellness overview will appear here.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Water", "0 L")

    with col2:
        st.metric("Food Entries", "0")

    with col3:
        st.metric("Exercise", "0 min")

    st.divider()

    st.info(
        "Start by creating your profile and logging your meals "
        "and activities."
    )


# -------------------------
# FOOD PAGE
# -------------------------

elif page == "Food":

    st.header("🍎 Food Tracker")

    st.write("Log the food you eat throughout the day.")

    food = st.text_input("Food")

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    if st.button("Add Food"):

        if food == "":
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
