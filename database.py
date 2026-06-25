import sqlite3
from datetime import datetime

DB_PATH = "data/interview.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_name TEXT,
        role TEXT,
        score REAL,
        feedback TEXT,
        interview_date TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_interview(candidate_name, role, score, feedback):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interviews
    (candidate_name, role, score, feedback, interview_date)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        candidate_name,
        role,
        score,
        feedback,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

def get_all_interviews():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interviews")
    data = cursor.fetchall()

    conn.close()

    return data