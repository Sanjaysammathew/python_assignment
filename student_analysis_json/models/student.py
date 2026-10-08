from dataclasses import dataclass

from pydantic import BaseModel, Field, field_validator


@dataclass
class Student:
    student_id: str
    name: str
    age: int
    course: str
    email: str


class StudentSchema(BaseModel):
    student_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)
    course: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)

    @field_validator("name", "course")
    @classmethod
    def validate_name_and_course(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("Value cannot be blank.")
        return cleaned_value
