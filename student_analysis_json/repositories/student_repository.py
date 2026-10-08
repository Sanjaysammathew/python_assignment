import asyncio
import logging
from dataclasses import asdict
from pathlib import Path

from exceptions.student_exceptions import (
    InvalidStudentDataError,
    StudentAlreadyExistsError,
    StudentNotFoundError,
)
from models.student import Student, StudentSchema
from utilities.json_utils import read_json, write_json

logger = logging.getLogger(__name__)


class StudentRepository:
    def __init__(self, file_path: str | Path) -> None:
        self._file_path = Path(file_path)

    async def get_all(self) -> list[Student]:
        logger.info("Fetching all students from %s.", self._file_path)
        rows = await asyncio.to_thread(read_json, self._file_path)
        students = []
        for row in rows:
            try:
                age = int(row["age"])
            except (KeyError, ValueError) as error:
                student_id = row.get("student_id", "unknown")
                logger.error("Invalid age for student '%s'.", student_id)
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
        logger.info("Fetching student '%s'.", student_id)
        students = await self.get_all()
        return next(
            (student for student in students if student.student_id == student_id),
            None,
        )

    async def create(self, student: Student) -> None:
        StudentSchema.model_validate(asdict(student))
        file_exists = await asyncio.to_thread(self._file_path.exists)
        rows = (
            await asyncio.to_thread(read_json, self._file_path)
            if file_exists
            else []
        )
        if any(row.get("student_id") == student.student_id for row in rows):
            logger.warning("Student '%s' already exists.", student.student_id)
            raise StudentAlreadyExistsError(
                f"Student '{student.student_id}' already exists."
            )
        rows.append(asdict(student))
        await asyncio.to_thread(write_json, self._file_path, rows)

    async def update(self, student_id: str, student: Student) -> None:
        logger.info("Updating student '%s'.", student_id)
        StudentSchema.model_validate(asdict(student))
        rows = await asyncio.to_thread(read_json, self._file_path)
        for index, row in enumerate(rows):
            if row.get("student_id") == student_id:
                updated_student = asdict(student)
                updated_student["student_id"] = student_id
                rows[index] = updated_student
                await asyncio.to_thread(write_json, self._file_path, rows)
                return
        logger.error("Student '%s' was not found for update.", student_id)
        raise StudentNotFoundError(f"Student '{student_id}' was not found.")

    async def delete(self, student_id: str) -> None:
        logger.info("Deleting student '%s'.", student_id)
        rows = await asyncio.to_thread(read_json, self._file_path)
        remaining_rows = [
            row for row in rows if row.get("student_id") != student_id
        ]
        if len(remaining_rows) == len(rows):
            logger.error("Student '%s' was not found for deletion.", student_id)
            raise StudentNotFoundError(f"Student '{student_id}' was not found.")
        await asyncio.to_thread(write_json, self._file_path, remaining_rows)
