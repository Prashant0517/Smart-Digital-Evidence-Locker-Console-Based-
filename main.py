# main.py
# Main entry point of the project

from database import create_tables
from auth import login, create_default_admin
from evidence import add_evidence, view_evidence, verify_evidence
from logs import view_logs

def main():
    # Setup database and admin
    create_tables()
    create_default_admin()

    user = login()
    if not user:
        return

    user_id, role = user

    while True:
        print("\n1. Add Evidence")
        print("2. View Evidence")
        print("3. Verify Evidence")
        print("4. View Logs")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_evidence(user_id)

        elif choice == "2":
            view_evidence()

        elif choice == "3":
            verify_evidence(user_id)

        elif choice == "4":
            if role == "Admin":
                view_logs()
            else:
                print("Access denied! Admin only.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
