from datetime import date

import streamlit as st

from database import add_entry, get_entries, get_meals, remove_meal, save_meal


MEALS = {
    "Breakfast": [
        ("Overnight oats with soy milk, berries, and nuts", {"vegan", "protein"}),
        ("Greek yogurt with fruit and seeds", {"vegetarian", "protein"}),
        ("Eggs with whole-grain toast and fruit", {"vegetarian", "protein"}),
    ],
    "Lunch": [
        ("Lentil and quinoa bowl with roasted vegetables", {"vegan", "protein"}),
        ("Grilled chicken and brown rice bowl", {"protein"}),
        ("Tomato and mozzarella sandwich", {"vegetarian"}),
    ],
    "Dinner": [
        ("Tofu and edamame stir-fry with rice", {"vegan", "protein"}),
        ("Salmon with potatoes and greens", {"protein"}),
        ("Chickpea and vegetable curry", {"vegan"}),
    ],
    "Snacks": [
        ("Apple slices with peanut butter", {"vegan"}),
        ("Roasted edamame", {"vegan", "protein"}),
        ("Cottage cheese and berries", {"vegetarian", "protein"}),
    ],
}


def show_food():
    st.title("Food & Nutrition")
    diet = st.session_state.profile.get("diet", "No Restrictions")
    food_style = st.selectbox(
        "Nutrition style", ("Balanced & Healthy", "Balanced + Flexible Choice Day")
    )
    st.subheader("Meal ideas")
    st.caption(f"Diet preference: {diet}")
    for category, suggestions in MEALS.items():
        with st.expander(category):
            for meal, tags in suggestions:
                matches = {
                    "Vegan": "vegan" in tags,
                    "Vegetarian": bool(tags & {"vegan", "vegetarian"}),
                    "High Protein": "protein" in tags,
                }
                if matches.get(diet, True):
                    st.write(f"• {meal}")

    if food_style == "Balanced + Flexible Choice Day":
        with st.expander("Flexible choice day"):
            st.write("Include a meal you enjoy alongside your regular meals.")
            st.text_input("What meal would you like to enjoy?")

    today = date.today()
    st.subheader("Log a meal")
    with st.form("meal_log", clear_on_submit=True):
        meal = st.text_input("Food or meal")
        quantity = st.number_input("Servings", min_value=1, value=1)
        favorite = st.checkbox("Save to favorites")
        if st.form_submit_button("Add food", type="primary"):
            if not meal.strip():
                st.warning("Enter a food or meal.")
            else:
                add_entry("food", today, meal.strip(), quantity)
                if favorite:
                    save_meal(meal.strip(), quantity)
                st.success("Meal logged.")

    favorites = get_meals()
    if favorites:
        st.subheader("Favorite meals")
        for index, row in enumerate(favorites):
            name, quantity = row["name"], row["quantity"]
            label, log, remove = st.columns([3, 2, 2])
            label.text(f"{name} · {quantity} servings")
            if log.button("Log meal", key=f"log_meal_{index}"):
                add_entry("food", today, name, quantity)
                st.rerun()
            if remove.button("Remove favorite", key=f"remove_meal_{index}"):
                remove_meal(name)
                st.rerun()

    st.subheader("Today's food")
    entries = [row for row in get_entries(today, today) if row["kind"] == "food"]
    if not entries:
        st.info("No food entries yet.")
    for row in entries:
        st.text(f"{row['label']} · {row['amount']} servings")
