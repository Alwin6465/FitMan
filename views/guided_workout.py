from math import ceil
from time import monotonic

import streamlit as st

from database import latest_workout_feedback, save_guided_workout


CUES = {
    "Bodyweight Squats": "Keep your feet planted and sit back toward a chair.",
    "Squats": "Keep your feet planted and move through a range you can control.",
    "Wall Push-ups": "Keep your body in a straight line and move slowly toward the wall.",
    "Push-ups": "Keep your hips in line with your shoulders. Use a wall if you need an easier option.",
    "Glute Bridges": "Press through your heels and lift your hips without arching your lower back.",
    "Plank": "Keep your ribs over your hips and breathe steadily.",
    "Warm-up": "Start with easy movement and gradually increase your pace.",
    "Stretching": "Move gently into each stretch and breathe steadily.",
}


@st.fragment(run_every=1)
def show_rest_timer(run):
    seconds = max(0, ceil(run["rest_until"] - monotonic()))
    if seconds:
        st.metric("Rest remaining", f"{seconds // 60}:{seconds % 60:02d}")
    else:
        st.success("Rest complete")
    if st.button("Skip rest" if seconds else "Continue workout"):
        run["rest_until"] = 0
        st.rerun()


def show_guided_workout(day, exercises, completed):
    run = st.session_state.get("guided_workout")
    if run and run["day"] != day:
        del st.session_state.guided_workout
        run = None
    if completed or not exercises:
        if run is not None:
            del st.session_state.guided_workout
        if st.session_state.pop("guided_workout_finished", None) == day:
            st.success("Workout complete. Your feedback was saved.")
        return

    if run is None:
        if st.button("Start guided workout", type="primary", icon=":material/play_arrow:"):
            st.session_state.guided_workout = {
                "day": day,
                "exercises": tuple(exercises),
                "feedback": {},
                "index": 0,
                "sets": [],
                "rest_until": 0,
                "previous": latest_workout_feedback(day),
            }
            st.rerun()
        return

    sets = run.setdefault("sets", [])
    index = run["index"]
    total = len(run["exercises"])
    with st.container(border=True):
        st.subheader("Guided workout")
        st.progress(index / total, text=f"{index} of {total} exercise steps finished")
        if run.get("rest_until", 0):
            show_rest_timer(run)
        elif index == total:
            if not run["feedback"]:
                st.info("All exercises were skipped.")
            else:
                st.write(f"{len(sets)} sets logged. Finish to save your session.")
                if st.button("Finish guided workout", type="primary"):
                    save_guided_workout(day, run["feedback"], sets)
                    del st.session_state.guided_workout
                    st.session_state.guided_workout_finished = day
                    st.rerun()
        else:
            exercise = run["exercises"][index]
            st.markdown(f"**{index + 1}. {exercise}**")
            st.caption(CUES.get(exercise, "Use a familiar variation and keep your movement controlled."))
            previous = run["previous"].get(exercise)
            if previous == "Too hard":
                st.info("Last time this felt too hard. Try an easier variation or reduce the effort today.")
            elif previous == "About right":
                st.info("Last time this felt about right. Repeat the effort if you feel ready.")
            elif previous == "Too easy":
                st.info("Last time this felt easy. If your form feels steady, try one small increase in effort.")
            logged = sum(item["step"] == index for item in sets)
            st.write(f"{logged} sets logged for this exercise")
            with st.form(f"guided_step_{index}_{logged}"):
                measure = st.selectbox("Track by", ("Reps", "Seconds"))
                amount = st.number_input("Reps or seconds completed", min_value=1, value=10)
                rating = st.radio(
                    "How did this set feel?",
                    ("Too easy", "About right", "Too hard"),
                    index=None,
                    horizontal=True,
                )
                rest = st.selectbox("Rest after logging", (0, 30, 60, 90, 120), index=2,
                                    format_func=lambda value: f"{value} seconds" if value else "No timer")
                if st.form_submit_button("Log set", type="primary"):
                    if rating is None:
                        st.warning("Choose how the set felt before logging it.")
                    else:
                        sets.append({
                            "step": index, "exercise": exercise, "measure": measure,
                            "amount": amount, "rating": rating,
                        })
                        run["feedback"][exercise] = rating
                        run["rest_until"] = monotonic() + rest if rest else 0
                        st.rerun()
            if st.button("Next exercise" if logged else "Skip exercise"):
                run["index"] += 1
                st.rerun()

        if st.button("End without saving"):
            del st.session_state.guided_workout
            st.rerun()
