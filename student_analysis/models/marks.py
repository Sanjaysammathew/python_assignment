from dataclasses import dataclass


@dataclass
class Marks:
	student_id: str
	python: float
	java: float
	dbms: float
	maths: float
