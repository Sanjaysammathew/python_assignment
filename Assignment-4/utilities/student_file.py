import csv
from pathlib import Path

from utilities.student import Student


class StudentFile:
    def __init__(self, primary_path: str, records_path: str) -> None:
        self.primary_path = Path(primary_path)
        self.records_path = Path(records_path)

    def _read_csv(self, path: Path) -> list[dict[str, str]]:
        with path.open(newline="") as file:
            return list(csv.DictReader(file))

    def read_students(self) -> list[Student]:
        primary = self._read_csv(self.primary_path)
        records = {row["student_id"]: row for row in self._read_csv(self.records_path)}

        students: list[Student] = []
        for row in primary:
            record = records.get(row["student_id"], {})
            marks = [float(record.get(key, 0) or 0) for key in ("mark1", "mark2", "mark3")]
            students.append(
                Student(
                    student_id=row["student_id"],
                    name=row["name"],
                    age=int(row["age"]),
                    course=row["course"],
                    email=row["email"],
                    marks=marks,
                )
            )
        return students

    def add_record(
        self, student_id: str, marks: list[float], sports: str, clubs: str
    ) -> None:
        with self.records_path.open("a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, *marks, sports, clubs])

    def details(self) -> str:
        return (
            f"Primary: {self.primary_path} (exists: {self.primary_path.exists()})\n"
            f"Records: {self.records_path} (exists: {self.records_path.exists()})"
        )