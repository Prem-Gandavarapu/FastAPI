from fastapi import FastAPI, HTTPException
from Student import Student

app = FastAPI()

students = [
    Student(
        id=1,
        name="Prem",
        age=21,
        branch="CSE",
        cgpa=9.2,
        email="prem@gmail.com"
    ),
    Student(
        id=2,
        name="Nandha",
        age=22,
        branch="ECE",
        cgpa=8.4,
        email="nandha@gmail.com"
    ),
    Student(
        id=3,
        name="Geethika",
        age=20,
        branch="IT",
        cgpa=9.6,
        email="geethika@gmail.com"
    )
]


@app.get("/")
def greet():
    return {"message" : "Welcome to StudentManagement API"}

# GET ALL STUDENTS
@app.get("/students")
def get_students():
    return students


# GET STUDENT BY ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# CREATE STUDENT
@app.post("/students", status_code=201)
def create_student(student: Student):

    for s in students:
        if s.id == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

        if s.email.lower() == student.email.lower():
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    students.append(student)

    return {
        "message": "Student added successfully",
        "student": student
    }


# UPDATE STUDENT
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student.id == student_id:

            # Prevent duplicate email
            for s in students:
                if (
                    s.email.lower() == updated_student.email.lower()
                    and s.id != student_id
                ):
                    raise HTTPException(
                        status_code=400,
                        detail="Email already exists"
                    )

            # Keep URL id as the source of truth
            updated_student.id = student_id

            students[index] = updated_student

            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# DELETE STUDENT
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:

            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )