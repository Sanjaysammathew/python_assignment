from pathlib import Path

from models.marks import Marks
from utilities.csv_utils import read_csv


class MarksRepository:
	def __init__(self, file_path: str | Path) -> None:
		self._file_path = Path(file_path)

	def get_all(self) -> list[Marks]:
		rows = read_csv(self._file_path)
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
