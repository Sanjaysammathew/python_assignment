from utilities.student import Student
from utilities.student_file import StudentFile


class StudentApp:
    def __init__(self, file: StudentFile) -> None:
        self.file = file

    def show_students(self) -> None:
        print("\nSTUDENT DETAILS")
        for s in self.file.read_students():
            print(f"{s.student_id} | {s.name} | {s.course}")

    def show_performance(self) -> None:
        print("\nSTUDENT PERFORMANCE")
        for s in self.file.read_students():
            print(s.summary())

    def show_class_summary(self) -> None:
        students = self.file.read_students()
        if not students:
            print("No students found.")
            return

        class_avg = sum(s.average for s in students) / len(students)
        top = max(students, key=lambda s: s.average)

        print("\nCLASS SUMMARY")
        print(f"Students: {len(students)}")
        print(f"Class Average: {class_avg:.2f}")
        print(f"Highest Student: {top.name} ({top.average:.2f})")

    def add_student(self) -> None:
        student_id = input("Student ID: ")
        try:
            marks = [float(input(f"Mark {i}: ")) for i in (1, 2, 3)]
        except ValueError:
            print("Marks must be numbers.")
            return

        if not all(Student.is_valid_mark(m) for m in marks):
            print("Marks must be between 0 and 100.")
            return

        sports = input("Sports: ")
        clubs = input("Club: ")
        self.file.add_record(student_id, marks, sports, clubs)
        print("Student added successfully.")

    def show_file_details(self) -> None:
        print("\nFILE DETAILS")
        print(self.file.details())

    def run(self) -> None:
        actions = {
            "1": self.show_students,
            "2": self.show_performance,
            "3": self.show_class_summary,
            "4": self.add_student,
            "5": self.show_file_details,
        }

        while True:
            print("\n===== STUDENT MANAGEMENT =====")
            print("1. Display Students")
            print("2. Student Performance")
            print("3. Class Summary")
            print("4. Append Student")
            print("5. File Details")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "6":
                print("Program ended.")
                break

            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice.")


def main() -> None:
    file = StudentFile("data/students.csv", "data/student_records.csv")
    StudentApp(file).run()


if __name__ == "__main__":
    main()