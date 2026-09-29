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
        return self.total / len(self.marks)

    @property
    def grade(self) -> str:
        if self.average >= 90:
            return "A"
        elif self.average >= 75:
            return "B"
        elif self.average >= 60:
            return "C"
        else:
            return "D"

    @property
    def highest_mark(self) -> float:
        return max(self.marks)

    @property
    def lowest_Mark(self) -> float:
        return min(self.marks)

    @staticmethod
    def is_valid_mark(mark: float) -> bool:
        return 0 <= mark <= 100
