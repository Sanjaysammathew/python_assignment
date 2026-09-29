from pathlib import Path

from models.student import Student
from utilities.csv_utils import read_csv


class StudentRepository:
	def __init__(self, file_path: str | Path) -> None:
		self._file_path = Path(file_path)

	def get_all(self) -> list[Student]:
		rows = read_csv(self._file_path)
		return [
			Student(
				student_id=row["student_id"],
				name=row["name"],
				age=int(row["age"]),
				course=row["course"],
				email=row["email"],
			)
			for row in rows
		]

	def get_by_id(self, student_id: str) -> Student | None:
		return next(
			(student for student in self.get_all() if student.student_id == student_id),
			None,
		)
