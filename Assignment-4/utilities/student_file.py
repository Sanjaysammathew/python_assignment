import csv
from pathlib import Path


class StudentFile:

    def __init__(self, primary_path: str, records_path: str) -> None:
        self.primary_path = Path(primary_path)
        self.records_path = Path(records_path)

    def read_students(self) -> list[dict[str, str]]:
        with self.primary_path.open(newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def read_records(self) -> list[dict[str, str]]:
        with self.records_path.open(newline="") as file:
            reader = csv.DictReader(file)

            return list(reader)

    def display_students(self) -> None:
        students = self.read_students()
        print("\nSTUDENT DETAILS")

        for student in students:
            print(student["student_id"], "|", student["name"], "|", student["course"])

    def append_student(
        self, student_id: str, marks: list[float], sports: str, clubs: str
    ) -> None:

        with self.records_path.open("a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, marks[0], marks[1], marks[2], sports, clubs])
        print("Student added successfully.")

    def file_details(self) -> None:
        print("\nFILE DETAILS")
        print(f"Primary: {self.primary_path}")
        print(f"Primary exists: " f"{self.primary_path.exists()}")
        print(f"Records: {self.records_path}")
        print(f"Records exists: " f"{self.records_path.exists()}")
