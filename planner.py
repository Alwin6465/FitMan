def create_plan(
    age,
    gender,
    activity,
    experience,
    goal,
    workout_location,
    workout_time,
    preferred_time,
    diet,
    bedtime,
    wake_time,
    plan_days
):

    # -------------------------
    # HOME WORKOUTS
    # -------------------------

    home_beginner = [
        "Warm-up",
        "Bodyweight Squats",
        "Wall Push-ups",
        "Glute Bridges",
        "Bird Dog",
        "Plank",
        "Stretching"
    ]

    home_intermediate = [
        "Warm-up",
        "Squats",
        "Push-ups",
        "Reverse Lunges",
        "Glute Bridges",
        "Plank",
        "Resistance Band Rows",
        "Stretching"
    ]

    home_advanced = [
        "Warm-up",
        "Squats",
        "Push-ups",
        "Lunges",
        "Dumbbell Exercises",
        "Resistance Band Exercises",
        "Plank",
        "Mobility",
        "Stretching"
    ]

    # -------------------------
    # GYM - MALE
    # -------------------------

    gym_male_beginner = [
        "Warm-up",
        "Treadmill Walking",
        "Leg Press",
        "Lat Pulldown",
        "Chest Press Machine",
        "Cable Row",
        "Light Dumbbell Exercises",
        "Stretching"
    ]

    gym_male_intermediate = [
        "Warm-up",
        "Treadmill or Bike",
        "Leg Press",
        "Lat Pulldown",
        "Chest Press",
        "Cable Row",
        "Dumbbell Bench Press",
        "Dumbbell Shoulder Press",
        "Core Exercises",
        "Stretching"
    ]

    gym_male_advanced = [
        "Warm-up",
        "Cardio",
        "Squat or Leg Press",
        "Lat Pulldown",
        "Chest Press",
        "Cable Row",
        "Dumbbell Exercises",
        "Cable Exercises",
        "Core Exercises",
        "Stretching"
    ]

    # -------------------------
    # GYM - FEMALE
    # -------------------------

    gym_female_beginner = [
        "Warm-up",
        "Treadmill Walking",
        "Leg Press",
        "Lat Pulldown",
        "Chest Press Machine",
        "Cable Row",
        "Light Dumbbell Exercises",
        "Stretching"
    ]

    gym_female_intermediate = [
        "Warm-up",
        "Treadmill or Bike",
        "Leg Press",
        "Lat Pulldown",
        "Chest Press",
        "Cable Row",
        "Dumbbell Exercises",
        "Hip and Glute Exercises",
        "Core Exercises",
        "Stretching"
    ]

    gym_female_advanced = [
        "Warm-up",
        "Cardio",
        "Squat or Leg Press",
        "Lat Pulldown",
        "Chest Press",
        "Cable Row",
        "Dumbbell Exercises",
        "Hip and Glute Exercises",
        "Cable Exercises",
        "Core Exercises",
        "Stretching"
    ]

    # -------------------------
    # GYM - OTHER
    # -------------------------

    gym_other_beginner = [
        "Warm-up",
        "Treadmill Walking",
        "Leg Press",
        "Lat Pulldown",
        "Chest Press Machine",
        "Cable Row",
        "Light Dumbbell Exercises",
        "Stretching"
    ]

    gym_other_intermediate = [
        "Warm-up",
        "Treadmill or Bike",
        "Leg Press",
        "Lat Pulldown",
        "Chest Press",
        "Cable Row",
        "Dumbbell Exercises",
        "Core Exercises",
        "Stretching"
    ]

    gym_other_advanced = [
        "Warm-up",
        "Cardio",
        "Squat or Leg Press",
        "Lat Pulldown",
        "Chest Press",
        "Cable Row",
        "Dumbbell Exercises",
        "Cable Exercises",
        "Core Exercises",
        "Stretching"
    ]

    # -------------------------
    # OUTDOOR WORKOUTS
    # -------------------------

    outdoor_beginner = [
        "Easy Walking",
        "Bodyweight Squats",
        "Bench Push-ups",
        "Walking Lunges",
        "Light Stretching"
    ]

    outdoor_intermediate = [
        "Brisk Walking",
        "Jogging",
        "Squats",
        "Walking Lunges",
        "Push-ups",
        "Plank",
        "Stretching"
    ]

    outdoor_advanced = [
        "Warm-up Walk",
        "Jogging",
        "Running",
        "Squats",
        "Lunges",
        "Push-ups",
        "Plank",
        "Mobility",
        "Stretching"
    ]

    # -------------------------
    # SELECT WORKOUT
    # -------------------------

    if workout_location == "Gym":

        if gender == "Male":

            if experience == "Beginner":
                base_workout = gym_male_beginner

            elif experience == "Intermediate":
                base_workout = gym_male_intermediate

            else:
                base_workout = gym_male_advanced

        elif gender == "Female":

            if experience == "Beginner":
                base_workout = gym_female_beginner

            elif experience == "Intermediate":
                base_workout = gym_female_intermediate

            else:
                base_workout = gym_female_advanced

        else:

            if experience == "Beginner":
                base_workout = gym_other_beginner

            elif experience == "Intermediate":
                base_workout = gym_other_intermediate

            else:
                base_workout = gym_other_advanced

    elif workout_location == "Home":

        if experience == "Beginner":
            base_workout = home_beginner

        elif experience == "Intermediate":
            base_workout = home_intermediate

        else:
            base_workout = home_advanced

    elif workout_location == "Outdoor":

        if experience == "Beginner":
            base_workout = outdoor_beginner

        elif experience == "Intermediate":
            base_workout = outdoor_intermediate

        else:
            base_workout = outdoor_advanced

    else:
        base_workout = home_beginner

    # -------------------------
    # GOAL RECOMMENDATION
    # -------------------------

    if goal == "General Wellness":

        goal_message = (
            "Focus on building consistent healthy habits, "
            "regular movement, balanced meals, and good recovery."
        )

    elif goal == "Build Strength":

        goal_message = (
            "Focus on gradually improving strength with "
            "controlled movements, proper technique, and "
            "consistent training."
        )

    elif goal == "Improve Fitness":

        goal_message = (
            "Focus on gradually improving your endurance, "
            "strength, mobility, and overall physical activity."
        )

    elif goal == "Build Healthy Habits":

        goal_message = (
            "Focus on consistency. Build a routine around "
            "movement, nutritious meals, hydration, and sleep."
        )

    else:

        goal_message = (
            "Focus on consistency and healthy daily habits."
        )

    # -------------------------
    # NUTRITION RECOMMENDATION
    # -------------------------

    if diet == "Vegetarian":

        food_message = (
            "Include a variety of vegetables, fruits, whole grains, "
            "beans, lentils, dairy or suitable alternatives, and "
            "other protein-rich foods."
        )

    elif diet == "Vegan":

        food_message = (
            "Build balanced meals around vegetables, fruits, "
            "whole grains, beans, lentils, nuts, seeds, and "
            "other plant-based protein sources."
        )

    elif diet == "High Protein":

        food_message = (
            "Include protein-rich foods throughout the day along "
            "with vegetables, fruits, whole grains, and healthy fats."
        )

    elif diet == "Other":

        food_message = (
            "Choose a variety of nutritious foods and try to include "
            "protein, fruits or vegetables, whole grains, and healthy "
            "fats across your meals."
        )

    else:

        food_message = (
            "Aim for balanced meals with vegetables or fruit, "
            "protein-rich foods, whole grains, and healthy fats."
        )

    # -------------------------
    # ACTIVITY RECOMMENDATION
    # -------------------------

    if activity == "Low":

        activity_message = (
            "Start with manageable amounts of movement and gradually "
            "build a consistent daily activity routine."
        )

    elif activity == "Moderate":

        activity_message = (
            "Keep your regular activity consistent and include a "
            "mix of strength, mobility, and cardiovascular activities."
        )

    else:

        activity_message = (
            "Balance active training with recovery, mobility work, "
            "and rest so your routine remains sustainable."
        )

    # -------------------------
    # WORKOUT TIME RECOMMENDATION
    # -------------------------

    time_message = (
        f"FitMan recommends a workout of about {workout_time} "
        f"minutes in the {preferred_time.lower()}."
    )

    # -------------------------
    # SLEEP & RECOVERY
    # -------------------------

    sleep_message = (
        f"Your current schedule is around {bedtime.strftime('%I:%M %p')} "
        f"to {wake_time.strftime('%I:%M %p')}. Try to keep your sleep "
        "schedule consistent and allow enough recovery between "
        "challenging activities."
    )

    # -------------------------
    # FINAL RECOMMENDATION
    # -------------------------

    recommendation = {
        "age": age,
        "gender": gender,
        "activity": activity,
        "experience": experience,
        "goal": goal,
        "workout_location": workout_location,
        "workout_time": workout_time,
        "preferred_time": preferred_time,
        "diet": diet,
        "bedtime": bedtime,
        "wake_time": wake_time,
        "plan_days": plan_days,

        "workout": base_workout,

        "goal_recommendation": goal_message,

        "food_recommendation": food_message,

        "activity_recommendation": activity_message,

        "time_recommendation": time_message,

        "sleep_recommendation": sleep_message
    }

    # THIS FIXES THE ERROR
    return recommendation

def plan_for_profile(profile):
    inputs = {key: value for key, value in profile.items() if key not in ("name", "height", "weight")}
    return create_plan(**inputs)


def weekly_schedule(plan, start):
    from datetime import timedelta

    training_days = {
        2: (0, 3),
        3: (0, 2, 4),
        5: (0, 1, 3, 4, 5),
        7: tuple(range(7)),
    }[plan["plan_days"]]
    exercises = plan["workout"]
    minutes = plan["workout_time"]
    slots = min(len(exercises), max(2, minutes // 8))
    schedule = {}
    for offset in range(7):
        day = start + timedelta(days=offset)
        if offset not in training_days:
            schedule[day] = None
            continue
        rotation = training_days.index(offset) % len(exercises)
        schedule[day] = {
            "minutes": minutes,
            "location": plan["workout_location"],
            "exercises": (exercises[rotation:] + exercises[:rotation])[:slots],
        }
    return schedule
