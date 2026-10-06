import asyncio
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

	async def get_all(self) -> list[Marks]:
		rows = await asyncio.to_thread(read_json, self._file_path)
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

	async def get_by_student_id(self, student_id: str) -> Marks | None:
		marks_list = await self.get_all()
		return next(
			(marks for marks in marks_list if marks.student_id == student_id),
			None,
		)

	async def get_by_id(self, student_id: str) -> Marks | None:
		return await self.get_by_student_id(student_id)

	async def create(self, marks: Marks) -> None:
		file_exists = await asyncio.to_thread(self._file_path.exists)
		rows = (
			await asyncio.to_thread(read_json, self._file_path)
			if file_exists
			else []
		)
		if any(row.get("student_id") == marks.student_id for row in rows):
			raise InvalidStudentDataError(
				f"Marks already exist for student '{marks.student_id}'."
			)
		rows.append(self._marks_to_json_row(marks))
		await asyncio.to_thread(write_json, self._file_path, rows)

	async def update(self, student_id: str, marks: Marks) -> None:
		rows = await asyncio.to_thread(read_json, self._file_path)
		for index, row in enumerate(rows):
			if row.get("student_id") == student_id:
				updated_marks = asdict(marks)
				updated_marks["student_id"] = student_id
				rows[index] = self._marks_to_json_row(Marks(**updated_marks))
				await asyncio.to_thread(write_json, self._file_path, rows)
				return
		raise StudentMarksNotFoundError(
			f"No marks were found for student '{student_id}'."
		)

	async def delete(self, student_id: str) -> None:
		rows = await asyncio.to_thread(read_json, self._file_path)
		remaining_rows = [
			row for row in rows if row.get("student_id") != student_id
		]
		if len(remaining_rows) == len(rows):
			raise StudentMarksNotFoundError(
				f"No marks were found for student '{student_id}'."
			)
		await asyncio.to_thread(write_json, self._file_path, remaining_rows)

	async def save_all(
		self,
		rows: list[dict[str, str | float]],
		file_path: str | Path | None = None,
	) -> None:
		target_path = Path(file_path) if file_path is not None else self._file_path
		await asyncio.to_thread(write_json, target_path, rows)

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
