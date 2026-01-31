# Smart-Digital-Evidence-Locker-Console-Based-

Secure Digital Evidence Management System is a console-based application developed using Core Python and SQLite. The project is designed to securely store, manage, and verify digital evidence files such as documents, images, and reports by maintaining their integrity using cryptographic hashing.

Instead of storing actual files, the system stores file metadata and a SHA-256 hash of each evidence file in a database. This ensures that any unauthorized modification or tampering with the file can be easily detected by re-verifying the hash. The system also maintains a complete audit trail of user activities, ensuring accountability and traceability.

The application supports user authentication and role-based access control, where administrators can view system logs, and authorized users can add, view, and verify evidence. The project demonstrates the practical use of file handling, database operations, hashing, and secure system design using only core Python libraries.

This project is suitable for understanding real-world concepts related to data integrity, security, and database-driven applications, and can be further extended into GUI or web-based systems.

🛠 Technologies Used

Core Python

SQLite Database

hashlib (SHA-256 hashing)

File Handling & OS module

🎯 Key Features

Add evidence using file path

Generate and store secure file hash

Verify evidence integrity (tamper detection)

User authentication and roles

Database-based audit logging

Console-based menu-driven interface

