from services.path_manager import (
    get_primary_path,
    get_secondary_path,
    path_details
)

from services.reader import display_students

from services.writer import (
    append_student,
    search_student,
    update_student
)

def main():

    primary_path = get_primary_path()
    secondary_path = get_secondary_path()

    while True:

        print("\n")
        print(" STUDENT MANAGEMENT SYSTEM")

        print("1. Display Students")
        print("2. Append Details")
        print("3. Search Details")
        print("4. Update Details")
        print("5. Path Details")
        print("6. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            display_students(primary_path)

        elif choice == "2":
            append_student(primary_path,secondary_path)

        elif choice == "3":
            search_student(secondary_path)

        elif choice == "4":
            update_student(secondary_path)

        elif choice == "5":
            path_details()

        elif choice == "6":
            print("Exit")
            break

        else:
            print("Error: Invalid choice.")


main()