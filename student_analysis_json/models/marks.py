from dataclasses import dataclass

from pydantic import BaseModel, Field, field_validator


@dataclass
class Marks:
    student_id: str
    python: float
    java: float
    dbms: float
    maths: float


class MarksSchema(BaseModel):
    student_id: str = Field(..., min_length=1)
    python: float = Field(..., ge=1, le=100)
    java: float = Field(..., ge=1, le=100)
    dbms: float = Field(..., ge=1, le=100)
    maths: float = Field(..., ge=1, le=100)

    @field_validator("student_id")
    @classmethod
    def validate_student_id(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("student_id cannot be blank.")
        return cleaned_value
