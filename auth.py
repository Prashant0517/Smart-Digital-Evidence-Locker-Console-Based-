# auth.py
# This file handles user authentication

import sqlite3
from logs import add_log

def create_default_admin():
    conn = sqlite3.connect("evidence.db")
    cursor = conn.cursor()

    # Insert admin only if not exists
    cursor.execute("""
    INSERT OR IGNORE INTO users (username, password, role)
    VALUES ('admin', 'admin123', 'Admin')
    """)

    conn.commit()
    conn.close()


def login():
    conn = sqlite3.connect("evidence.db")
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check credentials
    cursor.execute(
        "SELECT user_id, role FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful!")
        add_log(user[0], "User logged in")
        return user  # returns (user_id, role)
    else:
        print("Invalid login!")
        return None
