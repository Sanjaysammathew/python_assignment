import csv
from pathlib import Path


def read_csv(file_path: str | Path) -> list[dict[str, str]]:
    path = Path(file_path)
    with path.open(mode="r") as csv_file:
        rows = csv.DictReader(csv_file)
        return [
            {
                key: value
                for key, value in row.items()
                if key is not None and value is not None
            }
            for row in rows
        ]


def write_csv(
    file_path: str | Path,
    rows: list[dict[str, str]],
    fieldnames: list[str],
) -> None:
    path = Path(file_path)
    with path.open(mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
