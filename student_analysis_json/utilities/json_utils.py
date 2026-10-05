import json
from pathlib import Path
from typing import Any


def read_json(file_path: str | Path) -> list[dict[str, Any]]:
    path = Path(file_path)
    with path.open(mode="r", encoding="utf-8") as json_file:
        contents = json_file.read()
    if not contents.strip():
        return []

    rows = json.loads(contents)
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError(f"Expected a JSON array of objects in '{path}'.")
    return rows


def write_json(file_path: str | Path, rows: list[dict[str, Any]]) -> None:
    path = Path(file_path)
    with path.open(mode="w", encoding="utf-8") as json_file:
        json.dump(rows, json_file, indent=4)
        json_file.write("\n")
