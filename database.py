# database.py
# This file handles database connection and table creation

import sqlite3

def get_connection():
    # Connect to SQLite database
    # If DB does not exist, it will be created automatically
    conn = sqlite3.connect("evidence.db")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Users table: stores login details
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # Evidence table: stores evidence details
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evidence (
        evidence_id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        file_path TEXT,
        file_hash TEXT,
        uploaded_by INTEGER,
        upload_time TEXT
    )
    """)

    # Logs table: stores activity logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()
