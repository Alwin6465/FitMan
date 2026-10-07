import streamlit as st


def show_food():

    st.header("🍎 Food & Nutrition")

    st.write(
        "Build healthy eating habits with balanced meals and room "
        "for foods you enjoy."
    )

    # ==================================================
    # FOOD PREFERENCE
    # ==================================================

    st.subheader("🥗 Your Food Preference")

    food_style = st.selectbox(
        "Choose your nutrition style",
        [
            "Balanced & Healthy",
            "Balanced + Flexible Choice Day"
        ]
    )

    # ==================================================
    # HEALTHY FOOD SUGGESTIONS
    # ==================================================

    st.subheader("🌱 Healthy Food Ideas")

    healthy_foods = {
        "🍳 Breakfast": [
            "Eggs with whole-grain toast and fruit",
            "Oatmeal with fruit and yogurt",
            "Greek yogurt with berries and granola"
        ],

        "🥗 Lunch": [
            "Grilled chicken with rice and vegetables",
            "Turkey and vegetable whole-grain wrap",
            "Bean and vegetable bowl with rice"
        ],

        "🍎 Snack": [
            "Apple with peanut butter",
            "Yogurt with fruit",
            "Carrots with hummus",
            "Nuts and fruit"
        ],

        "🍗 Dinner": [
            "Chicken, potatoes, and vegetables",
            "Salmon with rice and vegetables",
            "Tofu and vegetable stir-fry with rice"
        ]
    }

    for meal, foods in healthy_foods.items():

        with st.expander(meal):

            for food in foods:
                st.write(f"• {food}")

    # ==================================================
    # FLEXIBLE CHOICE DAY
    # ==================================================

    if food_style == "Balanced + Flexible Choice Day":

        st.subheader("🍕 Flexible Choice Day")

        st.info(
            "Enjoy foods you like while keeping your overall eating "
            "pattern balanced. One flexible day can include foods such "
            "as pizza, burgers, fries, tacos, or other favorites."
        )

        favorite_food = st.text_input(
            "What's your favorite food?"
        )

        if favorite_food.strip():

            st.success(
                f"Today you can enjoy your favorite: {favorite_food} 😊"
            )

        st.write(
            "Tip: Keep regular meals, include nutritious foods during "
            "the day, and enjoy your favorite food without guilt."
        )

    # ==================================================
    # WATER
    # ==================================================

    st.subheader("💧 Hydration")

    st.write(
        "Keep water available throughout the day and drink regularly, "
        "especially when you are active."
    )

    # ==================================================
    # ADD FOOD
    # ==================================================

    st.subheader("📝 Log Your Food")

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

    # ==================================================
    # TODAY'S FOOD
    # ==================================================

    st.divider()

    st.subheader("📋 Today's Food")

    if len(st.session_state.food_entries) == 0:

        st.info(
            "No food entries yet."
        )

    else:

        for entry in st.session_state.food_entries:

            st.markdown(
                f"""
                <div class="dashboard-card">

                    <h3>🍎 {entry['food']}</h3>

                    <p>
                        Quantity: {entry['quantity']}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )