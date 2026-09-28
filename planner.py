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
