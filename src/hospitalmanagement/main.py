from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .database import Base, engine, get_db
from . import schemas, crud


# =========================================================
# DATABASE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="Hospital Management System",
    description="Simple FastAPI Project for Hospital Management System Assignment"
)


# =========================================================
# HOME ROUTE
# =========================================================

@app.get("/")
def home():
    return {
        "message": "Hospital Management System API is Running"
    }


# =========================================================
# DOCTOR ROUTES
# =========================================================

@app.post(
    "/doctor",
    response_model=schemas.DoctorResponse
)
def add_doctor(
    doctor: schemas.DoctorCreate,
    db: Session = Depends(get_db)
):
    return crud.create_doctor(
        db=db,
        doctor=doctor
    )


@app.get(
    "/doctor",
    response_model=List[schemas.DoctorResponse]
)
def read_doctors(
    db: Session = Depends(get_db)
):
    return crud.get_doctors(db=db)


@app.get(
    "/doctor/{id}",
    response_model=schemas.DoctorResponse
)
def read_doctor(
    id: int,
    db: Session = Depends(get_db)
):
    doctor = crud.get_doctor_by_id(
        db=db,
        doctor_id=id
    )

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor


@app.delete("/doctor/{id}")
def remove_doctor(
    id: int,
    db: Session = Depends(get_db)
):
    success = crud.delete_doctor(
        db=db,
        doctor_id=id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return {
        "message": "Doctor deleted successfully"
    }


# =========================================================
# PATIENT ROUTES
# =========================================================

@app.post(
    "/patient",
    response_model=schemas.PatientResponse
)
def add_patient(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db)
):
    # Check if Doctor exists
    doctor = crud.get_doctor_by_id(
        db=db,
        doctor_id=patient.doctor_id
    )

    if not doctor:
        raise HTTPException(
            status_code=400,
            detail="Assigned Doctor ID does not exist"
        )

    return crud.create_patient(
        db=db,
        patient=patient
    )


@app.get(
    "/patient",
    response_model=List[schemas.PatientResponse]
)
def read_patients(
    db: Session = Depends(get_db)
):
    return crud.get_patients(db=db)


@app.get(
    "/patient/{id}",
    response_model=schemas.PatientResponse
)
def read_patient(
    id: int,
    db: Session = Depends(get_db)
):
    patient = crud.get_patient_by_id(
        db=db,
        patient_id=id
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@app.delete("/patient/{id}")
def remove_patient(
    id: int,
    db: Session = Depends(get_db)
):
    success = crud.delete_patient(
        db=db,
        patient_id=id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {
        "message": "Patient deleted successfully"
    }


# =========================================================
# STAFF ROUTES
# =========================================================

@app.post(
    "/staff",
    response_model=schemas.StaffResponse
)
def add_staff(
    staff: schemas.StaffCreate,
    db: Session = Depends(get_db)
):
    return crud.create_staff(
        db=db,
        staff=staff
    )


@app.get(
    "/staff",
    response_model=List[schemas.StaffResponse]
)
def read_staff(
    db: Session = Depends(get_db)
):
    return crud.get_all_staff(db=db)


@app.get(
    "/staff/{id}",
    response_model=schemas.StaffResponse
)
def read_staff_member(
    id: int,
    db: Session = Depends(get_db)
):
    staff_member = crud.get_staff_by_id(
        db=db,
        staff_id=id
    )

    if not staff_member:
        raise HTTPException(
            status_code=404,
            detail="Staff member not found"
        )

    return staff_member


@app.delete("/staff/{id}")
def remove_staff(
    id: int,
    db: Session = Depends(get_db)
):
    success = crud.delete_staff(
        db=db,
        staff_id=id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Staff member not found"
        )

    return {
        "message": "Staff member deleted successfully"
    }


# =========================================================
# APPOINTMENT ROUTES
# =========================================================

@app.post(
    "/appointment",
    response_model=schemas.AppointmentResponse
)
def add_appointment(
    appointment: schemas.AppointmentCreate,
    db: Session = Depends(get_db)
):
    # Check if Patient exists
    patient = crud.get_patient_by_id(
        db=db,
        patient_id=appointment.patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=400,
            detail="Patient ID does not exist"
        )

    # Check if Doctor exists
    doctor = crud.get_doctor_by_id(
        db=db,
        doctor_id=appointment.doctor_id
    )

    if not doctor:
        raise HTTPException(
            status_code=400,
            detail="Doctor ID does not exist"
        )

    return crud.create_appointment(
        db=db,
        appointment=appointment
    )


@app.get(
    "/appointment",
    response_model=List[schemas.AppointmentResponse]
)
def read_appointments(
    db: Session = Depends(get_db)
):
    return crud.get_appointments(db=db)


@app.get(
    "/appointment/{id}",
    response_model=schemas.AppointmentResponse
)
def read_appointment(
    id: int,
    db: Session = Depends(get_db)
):
    appointment = crud.get_appointment_by_id(
        db=db,
        appointment_id=id
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment


@app.delete("/appointment/{id}")
def remove_appointment(
    id: int,
    db: Session = Depends(get_db)
):
    success = crud.delete_appointment(
        db=db,
        appointment_id=id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return {
        "message": "Appointment cancelled successfully"
    }


# =========================================================
# MEDICAL RECORD ROUTES
# =========================================================

@app.post(
    "/medical-record",
    response_model=schemas.MedicalRecordResponse
)
def add_medical_record(
    medical_record: schemas.MedicalRecordCreate,
    db: Session = Depends(get_db)
):
    # Check if Patient exists
    patient = crud.get_patient_by_id(
        db=db,
        patient_id=medical_record.patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=400,
            detail="Patient ID does not exist"
        )

    # Check if Doctor exists
    doctor = crud.get_doctor_by_id(
        db=db,
        doctor_id=medical_record.doctor_id
    )

    if not doctor:
        raise HTTPException(
            status_code=400,
            detail="Doctor ID does not exist"
        )

    return crud.create_medical_record(
        db=db,
        medical_record=medical_record
    )


@app.get(
    "/medical-record",
    response_model=List[schemas.MedicalRecordResponse]
)
def read_medical_records(
    db: Session = Depends(get_db)
):
    return crud.get_medical_records(db=db)


@app.get(
    "/medical-record/{id}",
    response_model=schemas.MedicalRecordResponse
)
def read_medical_record(
    id: int,
    db: Session = Depends(get_db)
):
    medical_record = crud.get_medical_record_by_id(
        db=db,
        medical_record_id=id
    )

    if not medical_record:
        raise HTTPException(
            status_code=404,
            detail="Medical record not found"
        )

    return medical_record


@app.delete("/medical-record/{id}")
def remove_medical_record(
    id: int,
    db: Session = Depends(get_db)
):
    success = crud.delete_medical_record(
        db=db,
        medical_record_id=id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Medical record not found"
        )

    return {
        "message": "Medical record deleted successfully"
    }