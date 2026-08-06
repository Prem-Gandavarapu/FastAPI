from pydantic import BaseModel, EmailStr, Field

class Student(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=100)
    branch: str = Field(..., min_length=2, max_length=30)
    cgpa: float = Field(..., ge=0.0, le=10.0)
    email: EmailStr