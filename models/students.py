from pydantic import BaseModel, Field
from typing import Optional


class Address(BaseModel):
    city: str = Field(..., description="City name", min_length=1)
    country: str = Field(..., description="Country name", min_length=1)


class Student(BaseModel):
    name: str = Field(..., description="Student name", min_length=1)
    age: int = Field(..., description="Student age", ge=1)
    address: Address = Field(..., description="Student address")


class UpdateStudent(BaseModel):
    name: Optional[str] = Field(None, description="Student name", min_length=1)
    age: Optional[int] = Field(None, description="Student age", ge=1)
    address: Optional[Address] = Field(None, description="Student address")
