from services.path_manager import (
    get_primary_path,
    get_secondary_path
)

from services.reader import display_students

from services.writer import (
    read_students,
    append_students,
    search_student,
)


def main():

    primary_path = get_primary_path()
    secondary_path = get_secondary_path()

    while True:

        print("\n")
        print("=" * 40)
        print("     STUDENT MANAGEMENT SYSTEM")
        print("=" * 40)

        print("1. Display Students")
        print("2. Append Student")
        print("3. Search Student")
        print("4. Exit")

        print("=" * 40)

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                display_students(primary_path)

            elif choice == "2":

                append_students(secondary_path)

            elif choice == "3":

                search_student(secondary_path)

            elif choice == "4":

                print("Thank you!")
                break

            else:

                print("Error: Invalid choice.")

        except Exception as e:

            print("Error:", e)


if __name__ == "__main__":
    main()