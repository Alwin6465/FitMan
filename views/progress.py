import csv
from datetime import date, timedelta
from io import StringIO

import streamlit as st

from database import delete_entry, edit_entry, get_completions, get_entries, get_guided_workout_duration, get_guided_workout_sets
from planner import weekly_schedule


def show_progress():
    st.title("Progress")
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    entries = get_entries(monday, sunday)
    completed = get_completions(monday, sunday)
    plan = st.session_state.plan

    workouts, exercise, water = st.columns(3)
    planned = sum(workout is not None for workout in weekly_schedule(plan, monday).values()) if plan else 0
    workouts.metric("Workouts completed / planned", f"{len(completed)} / {planned}")
    minutes = sum(row["amount"] for row in entries if row["kind"] == "exercise")
    exercise.metric("Exercise this week", f"{minutes} min")
    water_ml = sum(row["amount"] for row in entries if row["kind"] == "water")
    water.metric("Water this week", f"{water_ml:,} mL")

    st.subheader("This week by day")
    chart_tabs = st.tabs(("Workouts", "Exercise", "Water"))
    days = [monday + timedelta(days=offset) for offset in range(7)]
    schedule = weekly_schedule(plan, monday) if plan else {}
    labels = [f"{index}. {day:%a}" for index, day in enumerate(days, 1)]

    with chart_tabs[0]:
        st.bar_chart({
            "Day": labels,
            "Planned": [int(bool(schedule.get(day))) for day in days],
            "Completed": [int(day.isoformat() in completed) for day in days],
        }, x="Day", y=["Planned", "Completed"], stack=False)

    for tab, kind, label in zip(
        chart_tabs[1:], ("exercise", "water"), ("Exercise (min)", "Water (mL)")
    ):
        daily_totals = dict.fromkeys(days, 0)
        for row in entries:
            if row["kind"] == kind:
                daily_totals[date.fromisoformat(row["day"])] += row["amount"]
        with tab:
            st.bar_chart(
                {"Day": labels, label: list(daily_totals.values())},
                x="Day", y=label,
            )

    st.subheader("Guided workout sets")
    workout_day = st.date_input("Workout date", value=today, max_value=today, key="guided_history_day")
    saved_sets = get_guided_workout_sets(workout_day)
    if saved_sets:
        duration = get_guided_workout_duration(workout_day)
        if duration is not None:
            minutes, seconds = divmod(duration, 60)
            st.caption(f"Session time (including rest): {minutes} min {seconds} sec")
        st.table([
            {"Exercise": item["exercise"], "Completed": f"{item['amount']} {item['measure'].lower()}", "Weight (kg)": item.get("weight_kg"), "Effort": item["rating"]}
            for item in saved_sets
        ])
    else:
        st.caption("No guided workout sets on this date.")

    st.subheader("Activity history")
    start = st.date_input("From", value=monday, max_value=today)
    end = st.date_input("Through", value=today, min_value=start, max_value=today, key=f"history_end_{start}")
    history = get_entries(start, end)
    if not history:
        st.info("No entries in this date range.")
        return
    units = {"food": "servings", "exercise": "minutes", "water": "mL"}
    export = StringIO(newline="")
    writer = csv.writer(export)
    writer.writerow(("Date", "Type", "Name", "Amount", "Unit"))
    for row in history:
        name = row["label"]
        # Keep user-entered names as text when opened in a spreadsheet.
        if name.lstrip().startswith(("=", "+", "-", "@")) or name.startswith(("\t", "\r", "\n")):
            name = "'" + name
        writer.writerow((row["day"], row["kind"], name, row["amount"], units[row["kind"]]))
    st.download_button(
        "Download activity CSV",
        data=export.getvalue().encode("utf-8-sig"),
        file_name=f"fitman-activity-{start}-to-{end}.csv",
        mime="text/csv",
        icon=":material/download:",
    )

    for row in history:
        entry_id = row["id"]
        unit = units[row["kind"]]
        with st.expander(f"{row['day']} · {row['label']} · {row['amount']} {unit}"):
            with st.form(f"activity_{entry_id}"):
                name = row["label"]
                if row["kind"] != "water":
                    name = st.text_input("Name", value=name)
                amount = st.number_input(f"Amount ({unit})", min_value=1, value=row["amount"])
                save, delete = st.columns(2)
                if save.form_submit_button("Save changes"):
                    if name.strip():
                        edit_entry(entry_id, name.strip(), amount)
                        st.rerun()
                    st.warning("Enter a name for the entry.")
                if delete.form_submit_button("Delete entry"):
                    delete_entry(entry_id)
                    st.rerun()
