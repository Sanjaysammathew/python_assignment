from utilities.student import Student
from utilities.student_file import StudentFile


def main() -> None:

    # Create StudentFile object
    file: StudentFile = StudentFile(
        "data/students.csv",
        "data/student_records.csv"
    )

    while True:

        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Display Students")
        print("2. Add Student")
        print("3. Student Performance")
        print("4. File Details")
        print("5. Exit")

        choice: str = input("Enter your choice: ")

        if choice == "1":

            file.display_students()

        elif choice == "2":

            student_id: str = input("Student ID: ")

            marks: list[float] = []

            for i in range(1, 4):

                try:
                    mark: float = float(
                        input(f"Mark {i}: ")
                    )
                except ValueError:
                    print("Mark must be a number.")
                    break

                if not Student.is_valid_mark(mark):
                    print("Mark must be between 0 and 100.")
                    break

                marks.append(mark)

            else:

                sports: str = input("Sports: ")
                clubs: str = input("Clubs: ")

                file.append_student(
                    student_id,
                    marks,
                    sports,
                    clubs
                )

        elif choice == "3":

            records: list[dict[str, str]] = (
                file.read_records()
            )

            print("\nSTUDENT PERFORMANCE")

            for record in records:

                marks: list[float] = [
                    float(record["mark1"]),
                    float(record["mark2"]),
                    float(record["mark3"])
                ]

                student: Student = Student(
                    student_id=record["student_id"],
                    name="Student",
                    age=0,
                    course="",
                    email="",
                    marks=marks
                )

                print(
                    f"{student.student_id} | "
                    f"Total: {student.total:.0f} | "
                    f"Average: {student.average:.2f} | "
                    f"Grade: {student.grade}"
                )

        elif choice == "4":

            file.file_details()

        elif choice == "5":

            print("Program ended.")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()