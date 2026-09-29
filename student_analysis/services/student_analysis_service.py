from models.marks import Marks
from models.student import Student
from repositories.marks_repository import MarksRepository
from repositories.student_repository import StudentRepository
from exceptions.student_exceptions import (
	StudentAnalysisError,
	StudentNotFoundError,
)


class StudentAnalysisService:
	def __init__(
		self,
		student_repository: StudentRepository,
		marks_repository: MarksRepository,
	) -> None:
		self.student_repository = student_repository
		self.marks_repository = marks_repository

	def get_all_students(self) -> list[Student]:
		return self.student_repository.get_all()

	def calculate_total(self, marks: Marks) -> float:
		return sum(self._get_subject_marks(marks).values())

	def calculate_average(self, marks: Marks) -> float:
		subject_marks = self._get_subject_marks(marks).values()
		return sum(subject_marks) / len(subject_marks)

	def calculate_highest_mark(self, marks: Marks) -> float:
		return max(self._get_subject_marks(marks).values())

	def calculate_lowest_mark(self, marks: Marks) -> float:
		return min(self._get_subject_marks(marks).values())

	def calculate_grade(self, average: float) -> str:
		if average >= 90:
			return "A+"
		if average >= 80:
			return "A"
		if average >= 70:
			return "B"
		if average >= 60:
			return "C"
		if average >= 50:
			return "D"
		return "F"

	def analyze_student(self, student_id: str) -> dict[str, str]:
		student = self.student_repository.get_by_id(student_id)
		if student is None:
			raise StudentNotFoundError(f"Student '{student_id}' was not found.")

		marks = self.marks_repository.get_by_student_id(student_id)
		if marks is None:
			raise StudentAnalysisError(f"No marks were found for student '{student_id}'.")

		subject_marks = self._get_subject_marks(marks)
		total = self.calculate_total(marks)
		average = self.calculate_average(marks)
		return {
			"student_id": student.student_id,
			"name": student.name,
			"age": str(student.age),
			"course": student.course,
			"email": student.email,
			"python": f"{subject_marks['Python']:g}",
			"java": f"{subject_marks['Java']:g}",
			"dbms": f"{subject_marks['DBMS']:g}",
			"maths": f"{subject_marks['Maths']:g}",
			"total": f"{total:g}",
			"average": f"{average:.2f}",
			"highest": f"{self.calculate_highest_mark(marks):g}",
			"lowest": f"{self.calculate_lowest_mark(marks):g}",
			"grade": self.calculate_grade(average),
		}

	def get_class_average(self) -> float:
		marks_list = self.marks_repository.get_all()
		if not marks_list:
			raise StudentAnalysisError("No marks are available for class analysis.")

		student_averages = [self.calculate_average(marks) for marks in marks_list]
		return sum(student_averages) / len(student_averages)

	def get_highest_performing_student(self) -> tuple[Student, float]:
		return max(self._get_ranked_students(), key=lambda result: result[1])

	def get_lowest_performing_student(self) -> tuple[Student, float]:
		return min(self._get_ranked_students(), key=lambda result: result[1])

	def get_subject_analysis(self) -> tuple[dict[str, float], str]:
		marks_list = self.marks_repository.get_all()
		if not marks_list:
			raise StudentAnalysisError("No marks are available for subject analysis.")

		subject_averages = {
			subject: sum(
				self._get_subject_marks(marks)[subject] for marks in marks_list
			)
			/ len(marks_list)
			for subject in ("Python", "Java", "DBMS", "Maths")
		}
		highest_subject = max(subject_averages.items(), key=lambda item: item[1])[0]
		return subject_averages, highest_subject

	def _get_ranked_students(self) -> list[tuple[Student, float]]:
		students_by_id = {
			student.student_id: student
			for student in self.student_repository.get_all()
		}
		ranked_students = [
			(students_by_id[marks.student_id], self.calculate_average(marks))
			for marks in self.marks_repository.get_all()
			if marks.student_id in students_by_id
		]
		if not ranked_students:
			raise StudentAnalysisError("No matching student marks are available.")
		return ranked_students

	@staticmethod
	def _get_subject_marks(marks: Marks) -> dict[str, float]:
		return {
			"Python": marks.python,
			"Java": marks.java,
			"DBMS": marks.dbms,
			"Maths": marks.maths,
		}
