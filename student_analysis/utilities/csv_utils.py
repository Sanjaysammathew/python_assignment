import csv
from pathlib import Path


def read_csv(file_path: str | Path) -> list[dict[str, str]]:
	path = Path(file_path)
	with path.open(mode="r", newline="", encoding="utf-8-sig") as csv_file:
		rows = csv.DictReader(csv_file)
		return [
			{
				key: value
				for key, value in row.items()
				if key is not None and value is not None
			}
			for row in rows
		]
