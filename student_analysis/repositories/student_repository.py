from pathlib import Path

from exceptions.student_exceptions import InvalidStudentDataError
from models.student import Student
from utilities.csv_utils import read_csv


class StudentRepository:
    def __init__(self, file_path: str | Path) -> None:
        self._file_path = Path(file_path)

    def get_all(self) -> list[Student]:
        rows = read_csv(self._file_path)
        students = []
        for row in rows:
            try:
                age = int(row["age"])
            except (KeyError, ValueError) as error:
                student_id = row.get("student_id", "unknown")
                raise InvalidStudentDataError(
                    f"Invalid age for student '{student_id}'."
                ) from error

            students.append(
                Student(
                    student_id=row["student_id"],
                    name=row["name"],
                    age=age,
                    course=row["course"],
                    email=row["email"],
                )
            )
        return students

    def get_by_id(self, student_id: str) -> Student | None:
        return next(
            (student for student in self.get_all() if student.student_id == student_id),
            None,
        )
