from exceptions.student_exceptions import StudentAnalysisError
from config.settings import MARKS_FILE, STUDENT_FILE
from models.student import Student
from repositories.marks_repository import MarksRepository
from repositories.student_repository import StudentRepository
from services.student_analysis_service import StudentAnalysisService


def display_menu() -> None:
	print("       STUDENT ANALYSIS")
	print("1. Display Students")
	print("2. Analyze Student")
	print("3. Class Average")
	print("4. Highest Student")
	print("5. Lowest Student")
	print("6. Subject Analysis")
	print("7. Exit")


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


def main() -> None:
	student_repository = StudentRepository(STUDENT_FILE)
	marks_repository = MarksRepository(MARKS_FILE)
	analysis_service = StudentAnalysisService(student_repository, marks_repository)

	while True:
		display_menu()
		choice = input("Enter choice: ").strip()

		if choice == "7":
			print("Goodbye!")
			break

		try:
			if choice == "1":
				for student in analysis_service.get_all_students():
					print(f"{student.student_id} - {student.name} - {student.course}")
			elif choice == "2":
				student_id = input("Enter student ID: ").strip()
				display_student_analysis(analysis_service.analyze_student(student_id))
			elif choice == "3":
				print(f"Class Average: {analysis_service.get_class_average():.2f}")
			elif choice == "4":
				display_ranked_student(
					"Highest", analysis_service.get_highest_performing_student()
				)
			elif choice == "5":
				display_ranked_student(
					"Lowest", analysis_service.get_lowest_performing_student()
				)
			elif choice == "6":
				subject_averages, highest_subject = analysis_service.get_subject_analysis()
				for subject, average in subject_averages.items():
					print(f"{subject:<7}: {average:.2f}")
				print(f"\nHighest Subject Average: {highest_subject}")
			else:
				print("Invalid choice. Please enter a Correct ID")
		except (StudentAnalysisError, OSError, ValueError) as error:
			print(f"Error: {error}")


if __name__ == "__main__":
	main()
