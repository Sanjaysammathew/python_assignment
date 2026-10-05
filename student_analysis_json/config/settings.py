import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _get_file_path(variable_name: str, default: str) -> str:
    file_path = Path(os.getenv(variable_name, default))
    if not file_path.is_absolute():
        file_path = BASE_DIR / file_path
    return str(file_path)


STUDENT_FILE: str = _get_file_path("STUDENT_FILE", "data/students.json")
MARKS_FILE: str = _get_file_path("MARKS_FILE", "data/marks.json")
subjects_string = os.getenv(
    "SUBJECTS",
    "Python,Java,DBMS,Maths"
)

subjects_list = subjects_string.split(",")

cleaned_subjects = []

for subject in subjects_list:
    subject = subject.strip()

    if subject:
        cleaned_subjects.append(subject)

SUBJECTS = tuple(cleaned_subjects)

MIN_MARK: int = int(os.getenv("MIN_MARK", "1"))
MAX_MARK: int = int(os.getenv("MAX_MARK", "100"))
PASSING_MARK: int = int(os.getenv("PASSING_MARK", "50"))
