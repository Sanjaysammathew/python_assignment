from dataclasses import asdict
from pathlib import Path

from config.settings import PASSING_MARK
from exceptions.student_exceptions import (
	InvalidStudentDataError,
	StudentMarksNotFoundError,
)
from models.marks import Marks
from utilities.json_utils import read_json, write_json


class MarksRepository:
	def __init__(self, file_path: str | Path) -> None:
		self._file_path = Path(file_path)

	def get_all(self) -> list[Marks]:
		rows = read_json(self._file_path)
		return [
			Marks(
				student_id=row["student_id"],
				python=float(row["python"]),
				java=float(row["java"]),
				dbms=float(row["dbms"]),
				maths=float(row["maths"]),
			)
			for row in rows
		]

	def get_by_student_id(self, student_id: str) -> Marks | None:
		return next(
			(marks for marks in self.get_all() if marks.student_id == student_id),
			None,
		)

	def get_by_id(self, student_id: str) -> Marks | None:
		return self.get_by_student_id(student_id)

	def create(self, marks: Marks) -> None:
		rows = read_json(self._file_path) if self._file_path.exists() else []
		if any(row.get("student_id") == marks.student_id for row in rows):
			raise InvalidStudentDataError(
				f"Marks already exist for student '{marks.student_id}'."
			)
		rows.append(self._marks_to_json_row(marks))
		write_json(self._file_path, rows)

	def update(self, student_id: str, marks: Marks) -> None:
		rows = read_json(self._file_path)
		for index, row in enumerate(rows):
			if row.get("student_id") == student_id:
				updated_marks = asdict(marks)
				updated_marks["student_id"] = student_id
				rows[index] = self._marks_to_json_row(Marks(**updated_marks))
				write_json(self._file_path, rows)
				return
		raise StudentMarksNotFoundError(
			f"No marks were found for student '{student_id}'."
		)

	def delete(self, student_id: str) -> None:
		rows = read_json(self._file_path)
		remaining_rows = [
			row for row in rows if row.get("student_id") != student_id
		]
		if len(remaining_rows) == len(rows):
			raise StudentMarksNotFoundError(
				f"No marks were found for student '{student_id}'."
			)
		write_json(self._file_path, remaining_rows)

	@staticmethod
	def _marks_to_json_row(marks: Marks) -> dict[str, str | float]:
		subject_marks = (marks.python, marks.java, marks.dbms, marks.maths)
		average = sum(subject_marks) / len(subject_marks)
		if average >= 90:
			grade = "A+"
		elif average >= 80:
			grade = "A"
		elif average >= 70:
			grade = "B"
		elif average >= 60:
			grade = "C"
		elif average >= PASSING_MARK:
			grade = "D"
		else:
			grade = "F"
		return {
			"student_id": marks.student_id,
			"python": marks.python,
			"java": marks.java,
			"dbms": marks.dbms,
			"maths": marks.maths,
			"total": sum(subject_marks),
			"average": average,
			"grade": grade,
			"highest": max(subject_marks),
			"lowest": min(subject_marks),
		}
