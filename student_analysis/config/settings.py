import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

def _get_file_path(variable_name: str, default: str) -> str:
	file_path = Path(os.getenv(variable_name, default))
	if not file_path.is_absolute():
		file_path = BASE_DIR / file_path
	return str(file_path)


STUDENT_FILE: str = _get_file_path("STUDENT_FILE", "data/students.csv")
MARKS_FILE: str = _get_file_path("MARKS_FILE", "data/marks.csv")
