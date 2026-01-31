# evidence.py
# This file handles evidence operations

import sqlite3
import hashlib
import os
from datetime import datetime
from logs import add_log


def generate_hash(file_path):
    # Create SHA-256 hash of file
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


def add_evidence(user_id):
    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):
        print("File not found!")
        return

    file_name = os.path.basename(file_path)
    file_hash = generate_hash(file_path)
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("evidence.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO evidence (file_name, file_path, file_hash, uploaded_by, upload_time)
    VALUES (?, ?, ?, ?, ?)
    """, (file_name, file_path, file_hash, user_id, time_now))

    conn.commit()
    conn.close()

    add_log(user_id, f"Added evidence: {file_name}")
    print("Evidence added successfully!")


def view_evidence():
    conn = sqlite3.connect("evidence.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM evidence")
    records = cursor.fetchall()

    print("\n--- EVIDENCE LIST ---")
    for record in records:
        print(record)

    conn.close()


def verify_evidence(user_id):
    evidence_id = input("Enter evidence ID to verify: ")

    conn = sqlite3.connect("evidence.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT file_path, file_hash FROM evidence WHERE evidence_id=?",
        (evidence_id,)
    )

    record = cursor.fetchone()
    conn.close()

    if not record:
        print("Evidence not found!")
        return

    current_hash = generate_hash(record[0])

    if current_hash == record[1]:
        print("Evidence is SAFE. No tampering detected.")
        add_log(user_id, "Evidence verified successfully")
    else:
        print("WARNING! Evidence has been TAMPERED!")
        add_log(user_id, "Evidence tampering detected")
