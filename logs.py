# logs.py
# This file handles logging user actions

import sqlite3
from datetime import datetime

def add_log(user_id, action):
    conn = sqlite3.connect("evidence.db")
    cursor = conn.cursor()

    # Get current date and time
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert log into logs table
    cursor.execute(
        "INSERT INTO logs (user_id, action, timestamp) VALUES (?, ?, ?)",
        (user_id, action, time_now)
    )

    conn.commit()
    conn.close()


def view_logs():
    conn = sqlite3.connect("evidence.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()

    print("\n--- AUDIT LOGS ---")
    for log in logs:
        print(log)

    conn.close()
