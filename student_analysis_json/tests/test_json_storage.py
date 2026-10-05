import json

import pytest

from exceptions.student_exceptions import StudentAlreadyExistsError
from models.marks import Marks
from models.student import Student
from repositories.marks_repository import MarksRepository
from repositories.student_repository import StudentRepository
from services.student_analysis_service import StudentAnalysisService
from utilities.json_utils import read_json, write_json


def test_json_utils_support_empty_files_and_missing_files(tmp_path):
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("", encoding="utf-8")
    missing_file = tmp_path / "missing.json"

    assert read_json(empty_file) == []
    with pytest.raises(FileNotFoundError):
        read_json(missing_file)


def test_student_repository_crud_preserves_unrelated_records(tmp_path):
    file_path = tmp_path / "students.json"
    first_student = Student("S001", "John", 20, "Course", "john@example.com")
    second_student = Student("S002", "Jane", 21, "Course", "jane@example.com")
    repository = StudentRepository(file_path)
    write_json(file_path, [first_student.__dict__])

    repository.create(second_student)
    with pytest.raises(StudentAlreadyExistsError):
        repository.create(first_student)
    repository.update(
        "S002",
        Student("S999", "Jane Updated", 22, "Course", "jane@example.com"),
    )

    assert repository.get_by_id("S001") == first_student
    assert repository.get_by_id("S002") == Student(
        "S002", "Jane Updated", 22, "Course", "jane@example.com"
    )

    repository.delete("S002")
    assert repository.get_all() == [first_student]


def test_marks_repository_crud_writes_json_records(tmp_path):
    file_path = tmp_path / "marks.json"
    repository = MarksRepository(file_path)
    first_marks = Marks("S001", 80, 70, 90, 60)
    second_marks = Marks("S002", 60, 70, 80, 90)

    repository.create(first_marks)
    repository.create(second_marks)
    repository.update("S002", Marks("S999", 70, 70, 70, 70))

    assert repository.get_by_id("S001") == first_marks
    assert repository.get_by_id("S002") == Marks("S002", 70, 70, 70, 70)
    stored_rows = json.loads(file_path.read_text(encoding="utf-8"))
    assert stored_rows[0]["total"] == 300
    assert stored_rows[0]["average"] == 75
    assert stored_rows[0]["grade"] == "B"

    repository.delete("S002")
    assert repository.get_all() == [first_marks]


def test_add_student_marks_updates_only_the_selected_json_record(tmp_path):
    student_file = tmp_path / "students.json"
    marks_file = tmp_path / "marks.json"
    student = Student("S001", "John", 20, "Course", "john@example.com")
    other_student = Student("S002", "Jane", 21, "Course", "jane@example.com")
    existing_marks = Marks("S001", 80, 70, 90, 60)
    other_marks = Marks("S002", 50, 60, 70, 80)
    write_json(student_file, [student.__dict__, other_student.__dict__])
    write_json(
        marks_file,
        [
            {
                "student_id": existing_marks.student_id,
                "python": existing_marks.python,
                "java": existing_marks.java,
                "dbms": existing_marks.dbms,
                "maths": existing_marks.maths,
                "total": 300,
                "average": 75,
                "grade": "B",
                "highest": 90,
                "lowest": 60,
            },
            {
                "student_id": other_marks.student_id,
                "python": other_marks.python,
                "java": other_marks.java,
                "dbms": other_marks.dbms,
                "maths": other_marks.maths,
                "total": 260,
                "average": 65,
                "grade": "C",
                "highest": 80,
                "lowest": 50,
            },
        ],
    )
    student_repository = StudentRepository(student_file)
    marks_repository = MarksRepository(marks_file)
    service = StudentAnalysisService(student_repository, marks_repository)

    assert service.add_student_marks("S001", 90, 80, 70, 60, marks_file) is True
    assert marks_repository.get_by_student_id("S001") == Marks("S001", 90, 80, 70, 60)
    assert marks_repository.get_by_student_id("S002") == other_marks
    assert len(json.loads(marks_file.read_text(encoding="utf-8"))) == 2


def test_repository_reads_existing_student_and_marks_json():
    from config.settings import MARKS_FILE, STUDENT_FILE

    students = StudentRepository(STUDENT_FILE).get_all()
    marks = MarksRepository(MARKS_FILE).get_all()

    assert len(students) == 5
    assert len(marks) == 5
    assert students[0].student_id == "S001"
    assert marks[0] == Marks("S001", 85, 78, 92, 88)


def test_analysis_operations_work_with_migrated_json_data():
    from config.settings import MARKS_FILE, STUDENT_FILE

    students = StudentRepository(STUDENT_FILE)
    marks = MarksRepository(MARKS_FILE)
    service = StudentAnalysisService(students, marks)

    assert len(service.get_all_students()) == 5
    assert service.analyze_student("S001")["total"] == "343"
    assert service.analyze_student("S001")["average"] == "85.75"
    assert service.get_subject_average("Python") == pytest.approx(72)
    assert service.get_highest_performing_student()[0].student_id == "S005"
    assert service.get_lowest_performing_student()[0].student_id == "S004"
    assert service.get_subject_analysis()[1] == "Maths"
    assert len(service.get_passing_students()) == 5
    assert service.has_failed_subject("S003") is False
