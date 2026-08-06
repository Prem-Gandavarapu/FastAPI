from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Patient Model
class Patient(BaseModel):
    id: int
    name: str
    age: int
    disease: str

patients = [
    Patient(
        id=1,
        name="Prem Kishore",
        age=21,
        disease="Fever"
    ),
    Patient(
        id=2,
        name="Rahul Sharma",
        age=35,
        disease="Diabetes"
    ),
    Patient(
        id=3,
        name="Ananya Reddy",
        age=27,
        disease="Migraine"
    ),
    Patient(
        id=4,
        name="Suresh Kumar",
        age=42,
        disease="Hypertension"
    ),
    Patient(
        id=5,
        name="Priya Singh",
        age=30,
        disease="Asthma"
    )
]

@app.get("/")
def welcome_msg():
    return {"message": "Welcome to Patients Log API"}

@app.get("/patients")
def get_all_patients():
    return patients

@app.get("/patients/{id}")
def get_patient_by_id(id: int):
    for patient in patients:
        if patient.id == id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@app.post("/patients")
def add_patient(patient: Patient):
    for p in patients:
        if p.id == patient.id:
            raise HTTPException(
                status_code=409,
                detail=f"Patient with ID {patient.id} already exists."
            )

    patients.append(patient)
    return {
        "message": "Patient added successfully",
        "patient": patient
    }


@app.delete("/patients/{id}")
def delete_record(id: int):
    for p in patients:
        if p.id == id:
            patients.remove(p)
            return {"message": "Successfully deleted"}

    raise HTTPException(status_code=404, detail="Patient not found")