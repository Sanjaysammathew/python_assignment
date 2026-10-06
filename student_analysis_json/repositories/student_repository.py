import asyncio
from dataclasses import asdict
from pathlib import Path

from exceptions.student_exceptions import (
    InvalidStudentDataError,
    StudentAlreadyExistsError,
    StudentNotFoundError,
)
from models.student import Student
from utilities.json_utils import read_json, write_json


class StudentRepository:
    def __init__(self, file_path: str | Path) -> None:
        self._file_path = Path(file_path)

    async def get_all(self) -> list[Student]:
        rows = await asyncio.to_thread(read_json, self._file_path)
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

    async def get_by_id(self, student_id: str) -> Student | None:
        students = await self.get_all()
        return next(
            (student for student in students if student.student_id == student_id),
            None,
        )

    async def create(self, student: Student) -> None:
        file_exists = await asyncio.to_thread(self._file_path.exists)
        rows = (
            await asyncio.to_thread(read_json, self._file_path)
            if file_exists
            else []
        )
        if any(row.get("student_id") == student.student_id for row in rows):
            raise StudentAlreadyExistsError(
                f"Student '{student.student_id}' already exists."
            )
        rows.append(asdict(student))
        await asyncio.to_thread(write_json, self._file_path, rows)

    async def update(self, student_id: str, student: Student) -> None:
        rows = await asyncio.to_thread(read_json, self._file_path)
        for index, row in enumerate(rows):
            if row.get("student_id") == student_id:
                updated_student = asdict(student)
                updated_student["student_id"] = student_id
                rows[index] = updated_student
                await asyncio.to_thread(write_json, self._file_path, rows)
                return
        raise StudentNotFoundError(f"Student '{student_id}' was not found.")

    async def delete(self, student_id: str) -> None:
        rows = await asyncio.to_thread(read_json, self._file_path)
        remaining_rows = [
            row for row in rows if row.get("student_id") != student_id
        ]
        if len(remaining_rows) == len(rows):
            raise StudentNotFoundError(f"Student '{student_id}' was not found.")
        await asyncio.to_thread(write_json, self._file_path, remaining_rows)
