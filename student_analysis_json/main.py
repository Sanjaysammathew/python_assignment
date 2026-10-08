import asyncio

from config.logging_config import configure_logging
from exceptions.student_exceptions import (
    InvalidStudentDataError,
    NoMarksAvailableError,
    StudentAlreadyExistsError,
    StudentMarksNotFoundError,
    StudentNotFoundError,
)
from config.settings import MARKS_FILE, PASSING_MARK, STUDENT_FILE
from models.student import Student
from repositories.marks_repository import MarksRepository
from repositories.student_repository import StudentRepository
from services.student_analysis_service import StudentAnalysisService


def display_menu() -> None:
    print("       STUDENT ANALYSIS")
    print("1. Display Students")
    print("2. Analyze Student")
    print("3. Subject Average")
    print("4. Highest Student")
    print("5. Lowest Student")
    print("6. Subject Analysis")
    print("7. Display Passing Students")
    print("8. Check Failed Subject")
    print("9. Add Student Marks")
    print("10. Exit")


def display_student_analysis(report: dict[str, str]) -> None:
    print("\nStudent Analysis")
    print(f"ID       : {report['student_id']}")
    print(f"Name     : {report['name']}")
    print(f"Age      : {report['age']}")
    print(f"Course   : {report['course']}")
    print(f"Email    : {report['email']}")
    print()
    print(f"Python   : {report['python']}")
    print(f"Java     : {report['java']}")
    print(f"DBMS     : {report['dbms']}")
    print(f"Maths    : {report['maths']}")
    print()
    print(f"Total    : {report['total']}")
    print(f"Average  : {report['average']}")
    print(f"Highest  : {report['highest']}")
    print(f"Lowest   : {report['lowest']}")
    print(f"Grade    : {report['grade']}")


def display_ranked_student(label: str, result: tuple[Student, float]) -> None:
    student, average = result
    print(f"\n{label} Student")
    print(f"Name      : {student.name}")
    print(f"Student ID: {student.student_id}")
    print(f"Average   : {average:.2f}")


async def main() -> None:
    configure_logging()
    student_repository = StudentRepository(STUDENT_FILE)
    marks_repository = MarksRepository(MARKS_FILE)
    analysis_service = StudentAnalysisService(student_repository, marks_repository)

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "10":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                for student in await analysis_service.get_all_students():
                    print(f"{student.student_id} - {student.name} - {student.course}")
            elif choice == "2":
                print("Task 1 started")
                student_id = input("Enter student ID: ").strip()
                report = await analysis_service.analyze_student(student_id)
                display_student_analysis(report)
                print("Task 1 completed")
            elif choice == "3":
                subject = input("Enter subject: ").strip()
                average = await analysis_service.get_subject_average(subject)
                if average is None:
                    print(f"Subject '{subject}' not found.")
                else:
                    print(f"\nSubject: {subject}\nAverage: {average:.2f}")
            elif choice == "4":
                display_ranked_student(
                    "Highest", await analysis_service.get_highest_performing_student()
                )
            elif choice == "5":
                display_ranked_student(
                    "Lowest", await analysis_service.get_lowest_performing_student()
                )
            elif choice == "6":
                subject_averages, highest_subject = (
                    await analysis_service.get_subject_analysis()
                )
                for subject, average in subject_averages.items():
                    print(f"{subject:<7}: {average:.2f}")
                print(f"\nHighest Subject Average: {highest_subject}")
            elif choice == "7":
                for student in await analysis_service.get_passing_students():
                    print(f"{student.student_id} - {student.name}")
            elif choice == "8":
                student_id = input("Enter student ID: ").strip()
                if await analysis_service.has_failed_subject(student_id):
                    print(
                        f"Student {student_id} has a subject mark below {PASSING_MARK}."
                    )
                else:
                    print(f"Student {student_id} has passed every subject.")
            elif choice == "9":
                student_id = input("Enter student ID: ").strip()
                if await student_repository.get_by_id(student_id) is None:
                    raise StudentNotFoundError("Student not found.")

                existing_marks = await marks_repository.get_by_student_id(student_id)
                if existing_marks is not None:
                    print("Existing marks found.")
                    print("Updating marks...")

                python_mark = float(input("Enter Python mark: "))
                java_mark = float(input("Enter Java mark: "))
                dbms_mark = float(input("Enter DBMS mark: "))
                maths_mark = float(input("Enter Maths mark: "))
                was_updated = await analysis_service.add_student_marks(
                    student_id,
                    python_mark,
                    java_mark,
                    dbms_mark,
                    maths_mark,
                    MARKS_FILE,
                )
                if was_updated:
                    print("Marks updated successfully.")
                else:
                    print("Marks saved successfully.")
            else:
                print("Invalid choice. Please enter a Correct ID")
        except StudentNotFoundError as error:
            print(f"Error: {error}")
        except StudentAlreadyExistsError as error:
            print(f"Error: {error}")
        except StudentMarksNotFoundError as error:
            print(f"Error: {error}")
        except NoMarksAvailableError as error:
            print(f"Error: {error}")
        except InvalidStudentDataError as error:
            print(f"Error: {error}")
        except (OSError, ValueError) as error:
            print(f"Error: {error}")
        finally:
            print("Program is executed")


if __name__ == "__main__":
    asyncio.run(main())
