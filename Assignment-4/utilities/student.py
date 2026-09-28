from dataclasses import dataclass


@dataclass
class Student:
    student_id: str
    name: str
    age: int
    course: str
    email: str
    marks: list[float]

    @property
    def total(self) -> float:
        return sum(self.marks)

    @property
    def average(self) -> float:
        return self.total / len(self.marks) if self.marks else 0.0

    @property
    def grade(self) -> str:
        if self.average >= 90:
            return "A"
        if self.average >= 75:
            return "B"
        if self.average >= 60:
            return "C"
        return "D"

    def summary(self) -> str:
        return (
            f"{self.name} | Total: {self.total:.0f} | "
            f"Average: {self.average:.2f} | Grade: {self.grade}"
        )

    @staticmethod
    def is_valid_mark(mark: float) -> bool:
        return 0 <= mark <= 100