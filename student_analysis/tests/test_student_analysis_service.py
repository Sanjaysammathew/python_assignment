import pytest


from models.marks import Marks
from services.student_analysis_service import StudentAnalysisService


class EmptyStudentRepository:

    def get_by_id(self, student_id):
        return None


@pytest.fixture
def service():
    # Calculation methods don't use the repositories, so None is fine.
    return StudentAnalysisService(None, None)


@pytest.fixture
def marks():
    # Marks(student_id, python, java, dbms, maths)
    return Marks("S001", 80, 70, 90, 60)


def test_calculate_total(service, marks):
    assert service.calculate_total(marks) == 300


def test_calculate_average(service, marks):
    assert service.calculate_average(marks) == 75


def test_highest_and_lowest(service, marks):
    assert service.calculate_highest_mark(marks) == 90
    assert service.calculate_lowest_mark(marks) == 60


@pytest.mark.parametrize(
    "average, expected_grade",
    [
        (95, "A+"),
        (85, "A"),
        (75, "B"),
        (65, "C"),
        (55, "D"),
        (30, "F"),
    ],
)
def test_calculate_grade(service, average, expected_grade):
    assert service.calculate_grade(average) == expected_grade


