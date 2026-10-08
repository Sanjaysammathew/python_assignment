import asyncio
import logging
from functools import reduce
from pathlib import Path

from config.logging_config import configure_logging
from config.settings import MAX_MARK, MIN_MARK, PASSING_MARK, SUBJECTS
from models.marks import Marks, MarksSchema
from models.student import Student
from repositories.marks_repository import MarksRepository
from repositories.student_repository import StudentRepository
from exceptions.student_exceptions import (
    InvalidStudentDataError,
    NoMarksAvailableError,
    StudentMarksNotFoundError,
    StudentNotFoundError,
)

configure_logging()
logger = logging.getLogger(__name__)


class StudentAnalysisService:
    def __init__(
        self,
        student_repository: StudentRepository,
        marks_repository: MarksRepository,
    ) -> None:
        self.student_repository = student_repository
        self.marks_repository = marks_repository

    async def get_all_students(self) -> list[Student]:
        logger.info("Fetching all students.")
        return await self.student_repository.get_all()

    def calculate_total(self, marks: Marks) -> float:
        subject_values = self._get_subject_marks(marks).values()
        return float(
            reduce(lambda total, value: total + value, subject_values, 0.0)
        )

    def calculate_total_async(self, marks: Marks) -> float:
        return self.calculate_total(marks)

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
        if average >= PASSING_MARK:
            return "D"
        return "F"

    async def analyze_student(self, student_id: str) -> dict[str, str]:
        logger.info("Reading student data for student '%s'.", student_id)
        student = await self.student_repository.get_by_id(student_id)
        if student is None:
            logger.warning("Student '%s' was not found.", student_id)
            raise StudentNotFoundError(f"Student '{student_id}' was not found.")

        marks = await self.marks_repository.get_by_student_id(student_id)
        if marks is None:
            logger.warning("No marks were found for student '%s'.", student_id)
            raise StudentMarksNotFoundError(
                f"No marks were found for student '{student_id}'."
            )

        logger.info("Student data retrieved successfully for '%s'.", student_id)
        subject_marks = self._get_subject_marks(marks)
        total = self.calculate_total(marks)
        average = self.calculate_average(marks)
        report = {
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
        logger.info("Calculation completed for student '%s'.", student_id)
        return report

    async def get_subject_average(self, subject: str) -> float | None:
        logger.info("Fetching average for subject '%s'.", subject)
        selected_subject = next(
            (
                configured_subject
                for configured_subject in SUBJECTS
                if configured_subject.casefold() == subject.strip().casefold()
            ),
            None,
        )
        if selected_subject is None:
            logger.warning("Subject '%s' was not found.", subject)
            return None

        marks_list = await self.marks_repository.get_all()
        if not marks_list:
            logger.error("No marks are available for subject analysis.")
            raise NoMarksAvailableError("No marks are available for subject analysis.")

        subject_marks = map(
            lambda marks: self._get_subject_marks(marks)[selected_subject], marks_list
        )
        return sum(subject_marks) / len(marks_list)

    async def get_highest_performing_student(self) -> tuple[Student, float]:
        ranked_students = await self._get_ranked_students()
        logger.info("Finding the highest-performing student.")
        return max(ranked_students, key=lambda result: result[1])

    async def get_lowest_performing_student(self) -> tuple[Student, float]:
        ranked_students = await self._get_ranked_students()
        logger.info("Finding the lowest-performing student.")
        return min(ranked_students, key=lambda result: result[1])

    async def get_subject_analysis(self) -> tuple[dict[str, float], str]:
        marks_list = await self.marks_repository.get_all()
        if not marks_list:
            logger.error("No marks are available for subject analysis.")
            raise NoMarksAvailableError("No marks are available for subject analysis.")

        subject_averages = {
            subject: sum(
                self._get_subject_marks(marks)[subject] for marks in marks_list
            )
            / len(marks_list)
            for subject in SUBJECTS
        }
        highest_subject = max(subject_averages.items(), key=lambda item: item[1])[0]
        return subject_averages, highest_subject

    async def get_passing_students(self) -> list[Student]:
        logger.info("Finding all students who passed.")
        passing_results = filter(
            lambda result: result[1] >= PASSING_MARK,
            await self._get_ranked_students(),
        )
        return list(map(lambda result: result[0], passing_results))

    async def has_failed_subject(self, student_id: str) -> bool:
        marks = await self.marks_repository.get_by_student_id(student_id)
        if marks is None:
            raise StudentMarksNotFoundError(
                f"No marks were found for student '{student_id}'."
            )
        return any(
            mark < PASSING_MARK for mark in self._get_subject_marks(marks).values()
        )

    async def add_student_marks(
        self,
        student_id: str,
        python: float,
        java: float,
        dbms: float,
        maths: float,
        file_path: str | Path,
    ) -> bool:
        logger.info("Adding or updating marks for student '%s'.", student_id)
        if await self.student_repository.get_by_id(student_id) is None:
            logger.warning("Student '%s' was not found during mark update.", student_id)
            raise StudentNotFoundError("Student not found.")

        marks_list = await self.marks_repository.get_all()
        is_update = any(marks.student_id == student_id for marks in marks_list)

        payload = MarksSchema(
            student_id=student_id,
            python=python,
            java=java,
            dbms=dbms,
            maths=maths,
        )
        new_marks = Marks(
            student_id=payload.student_id,
            python=payload.python,
            java=payload.java,
            dbms=payload.dbms,
            maths=payload.maths,
        )
        invalid_marks = [
            mark
            for mark in self._get_subject_marks(new_marks).values()
            if not MIN_MARK <= mark <= MAX_MARK
        ]
        if invalid_marks:
            logger.error(
                "Attempted mark %s is outside the allowed range for student '%s'.",
                invalid_marks[0],
                student_id,
            )
            raise InvalidStudentDataError(
                f"Mark {invalid_marks[0]:g} is outside the allowed range. "
                f"Mark must be between {MIN_MARK} and {MAX_MARK}."
            )

        rows = [
            self._marks_to_json_row(marks)
            for marks in marks_list
            if marks.student_id != student_id
        ]
        rows.append(self._marks_to_json_row(new_marks))
        await self.marks_repository.save_all(rows, file_path)
        return is_update

    def _marks_to_json_row(self, marks: Marks) -> dict[str, str | float]:
        average = self.calculate_average(marks)
        return {
            "student_id": marks.student_id,
            "python": marks.python,
            "java": marks.java,
            "dbms": marks.dbms,
            "maths": marks.maths,
            "total": self.calculate_total(marks),
            "average": average,
            "grade": self.calculate_grade(average),
            "highest": self.calculate_highest_mark(marks),
            "lowest": self.calculate_lowest_mark(marks),
        }

    async def _get_ranked_students(self) -> list[tuple[Student, float]]:
        students, marks_list = await asyncio.gather(
            self.student_repository.get_all(),
            self.marks_repository.get_all(),
        )
        students_by_id = {
            student.student_id: student for student in students
        }
        ranked_students = [
            (students_by_id[marks.student_id], self.calculate_average(marks))
            for marks in marks_list
            if marks.student_id in students_by_id
        ]
        if not ranked_students:
            raise NoMarksAvailableError("No matching student marks are available.")
        return ranked_students

    @staticmethod
    def _get_subject_marks(marks: Marks) -> dict[str, float]:
        return {
            "Python": marks.python,
            "Java": marks.java,
            "DBMS": marks.dbms,
            "Maths": marks.maths,
        }
