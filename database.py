import json
import sqlite3
from contextlib import contextmanager
from datetime import time
from pathlib import Path


# ==================================================
# DATABASE LOCATION
# ==================================================

DATA_FOLDER = Path(__file__).resolve().parent / "data"
DATABASE_FILE = DATA_FOLDER / "fitman.db"


# ==================================================
# CONNECT TO DATABASE
# ==================================================

def get_connection():

    DATA_FOLDER.mkdir(exist_ok=True)

    connection = sqlite3.connect(
        DATABASE_FILE,
        check_same_thread=False
    )

    connection.row_factory = sqlite3.Row

    return connection


# ==================================================
# CREATE DATABASE TABLES
# ==================================================

def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    # ----------------------------------------------
    # USERS
    # ----------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,
            age INTEGER,
            height REAL,
            weight REAL,

            gender TEXT,
            activity TEXT,
            experience TEXT,
            goal TEXT,

            workout_location TEXT,
            workout_time INTEGER,
            preferred_time TEXT,

            plan_days INTEGER,
            diet TEXT,

            bedtime TEXT,
            wake_time TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # ----------------------------------------------
    # FOOD ENTRIES
    # ----------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS food_entries (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,
            food TEXT NOT NULL,
            quantity INTEGER,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id)
                REFERENCES users(id)
        )
        """
    )

    # ----------------------------------------------
    # EXERCISE ENTRIES
    # ----------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS exercise_entries (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,
            exercise TEXT NOT NULL,
            duration INTEGER,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id)
                REFERENCES users(id)
        )
        """
    )

    connection.commit()
    connection.close()


# ==================================================
# USER FUNCTIONS
# ==================================================

def create_user(profile):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (

            name,
            age,
            height,
            weight,
            gender,
            activity,
            experience,
            goal,
            workout_location,
            workout_time,
            preferred_time,
            plan_days,
            diet,
            bedtime,
            wake_time

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            profile["name"],
            profile["age"],
            profile["height"],
            profile["weight"],
            profile["gender"],
            profile["activity"],
            profile["experience"],
            profile["goal"],
            profile["workout_location"],
            profile["workout_time"],
            profile["preferred_time"],
            profile["plan_days"],
            profile["diet"],
            str(profile["bedtime"]),
            str(profile["wake_time"])
        )
    )

    user_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return user_id


def get_user(user_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    connection.close()

    return user


# ==================================================
# FOOD FUNCTIONS
# ==================================================

def add_food(user_id, food, quantity):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO food_entries (
            user_id,
            food,
            quantity
        )

        VALUES (?, ?, ?)
        """,
        (
            user_id,
            food,
            quantity
        )
    )

    connection.commit()
    connection.close()


def get_food_entries(user_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM food_entries
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    entries = cursor.fetchall()

    connection.close()

    return entries


# ==================================================
# EXERCISE FUNCTIONS
# ==================================================

def add_exercise(user_id, exercise, duration):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO exercise_entries (
            user_id,
            exercise,
            duration
        )

        VALUES (?, ?, ?)
        """,
        (
            user_id,
            exercise,
            duration
        )
    )

    connection.commit()
    connection.close()


def get_exercise_entries(user_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM exercise_entries
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    entries = cursor.fetchall()

    connection.close()

    return entries


# ==================================================
# INITIALIZE DATABASE
# ==================================================

initialize_database()

@contextmanager
def workspace_db():
    connection = get_connection()
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def initialize_workspace():
    with workspace_db() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS workspace_profile (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                payload TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS activity_log (
                id INTEGER PRIMARY KEY,
                kind TEXT NOT NULL CHECK (kind IN ('food', 'exercise', 'water')),
                day TEXT NOT NULL,
                label TEXT NOT NULL,
                amount INTEGER NOT NULL CHECK (amount > 0)
            );
            CREATE INDEX IF NOT EXISTS activity_log_day ON activity_log(day);
            CREATE TABLE IF NOT EXISTS workout_completion (
                day TEXT PRIMARY KEY
            );
            CREATE TABLE IF NOT EXISTS guided_workout (
                day TEXT PRIMARY KEY,
                feedback TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS guided_workout_sets (
                day TEXT PRIMARY KEY,
                sets TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS favorite_meals (
                name TEXT PRIMARY KEY COLLATE NOCASE,
                quantity INTEGER NOT NULL CHECK (quantity > 0)
            );
        """)


def save_profile(profile):
    payload = dict(profile)
    for field in ("bedtime", "wake_time"):
        payload[field] = profile[field].isoformat()
    with workspace_db() as db:
        db.execute("REPLACE INTO workspace_profile VALUES (1, ?)", (json.dumps(payload),))


def load_profile():
    with workspace_db() as db:
        row = db.execute("SELECT payload FROM workspace_profile WHERE id = 1").fetchone()
    if row is None:
        return {}
    profile = json.loads(row["payload"])
    for field in ("bedtime", "wake_time"):
        profile[field] = time.fromisoformat(profile[field])
    return profile


def add_entry(kind, day, label, amount):
    with workspace_db() as db:
        db.execute(
            "INSERT INTO activity_log(kind, day, label, amount) VALUES (?, ?, ?, ?)",
            (kind, day.isoformat(), label, amount),
        )


def get_entries(start, end):
    with workspace_db() as db:
        return db.execute(
            "SELECT * FROM activity_log WHERE day BETWEEN ? AND ? ORDER BY day DESC, id DESC",
            (start.isoformat(), end.isoformat()),
        ).fetchall()


def edit_entry(entry_id, label, amount):
    with workspace_db() as db:
        db.execute("UPDATE activity_log SET label = ?, amount = ? WHERE id = ?", (label, amount, entry_id))


def delete_entry(entry_id):
    with workspace_db() as db:
        db.execute("DELETE FROM activity_log WHERE id = ?", (entry_id,))


def undo_water(day):
    with workspace_db() as db:
        db.execute(
            """DELETE FROM activity_log WHERE id = (
                SELECT id FROM activity_log WHERE kind = 'water' AND day = ? ORDER BY id DESC LIMIT 1
            )""",
            (day.isoformat(),),
        )


def get_completions(start, end):
    with workspace_db() as db:
        return {row["day"] for row in db.execute(
            "SELECT day FROM workout_completion WHERE day BETWEEN ? AND ?",
            (start.isoformat(), end.isoformat()),
        )}


def set_completion(day, completed):
    with workspace_db() as db:
        if completed:
            db.execute("INSERT OR IGNORE INTO workout_completion VALUES (?)", (day.isoformat(),))
        else:
            db.execute("DELETE FROM workout_completion WHERE day = ?", (day.isoformat(),))


def save_meal(name, quantity):
    with workspace_db() as db:
        db.execute("REPLACE INTO favorite_meals VALUES (?, ?)", (name, quantity))


def get_meals():
    with workspace_db() as db:
        return db.execute("SELECT * FROM favorite_meals ORDER BY name").fetchall()


def remove_meal(name):
    with workspace_db() as db:
        db.execute("DELETE FROM favorite_meals WHERE name = ?", (name,))


def latest_workout_feedback(before):
    with workspace_db() as db:
        rows = db.execute(
            "SELECT feedback FROM guided_workout WHERE day < ? ORDER BY day",
            (before.isoformat(),),
        ).fetchall()
    feedback = {}
    for row in rows:
        feedback.update(json.loads(row["feedback"]))
    return feedback


def save_guided_workout(day, feedback, sets=()):
    with workspace_db() as db:
        db.execute(
            """INSERT INTO guided_workout VALUES (?, ?)
               ON CONFLICT(day) DO UPDATE SET feedback = excluded.feedback""",
            (day.isoformat(), json.dumps(feedback)),
        )
        if sets:
            db.execute(
                """INSERT INTO guided_workout_sets VALUES (?, ?)
                   ON CONFLICT(day) DO UPDATE SET sets = excluded.sets""",
                (day.isoformat(), json.dumps(sets)),
            )
        db.execute("INSERT OR IGNORE INTO workout_completion VALUES (?)", (day.isoformat(),))


def get_guided_workout_sets(day):
    with workspace_db() as db:
        row = db.execute(
            "SELECT sets FROM guided_workout_sets WHERE day = ?", (day.isoformat(),)
        ).fetchone()
    return json.loads(row["sets"]) if row else []
