from pydantic import BaseModel, EmailStr
from datetime import date, time


# =========================
# DOCTOR SCHEMAS
# =========================

class DoctorBase(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    phone: str
    salary: float


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True


# =========================
# PATIENT SCHEMAS
# =========================

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    disease: str
    admission_date: date
    doctor_id: int


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True


# =========================
# STAFF SCHEMAS
# =========================

class StaffBase(BaseModel):
    name: str
    role: str
    shift: str
    salary: float


class StaffCreate(StaffBase):
    pass


class StaffResponse(StaffBase):
    id: int

    class Config:
        from_attributes = True


# =========================
# APPOINTMENT SCHEMAS
# =========================

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time
    status: str = "Scheduled"


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        from_attributes = True


# =========================
# MEDICAL RECORD SCHEMAS
# =========================

class MedicalRecordBase(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str
    treatment: str
    record_date: date
    notes: str | None = None


class MedicalRecordCreate(MedicalRecordBase):
    pass


class MedicalRecordResponse(MedicalRecordBase):
    id: int

    class Config:
        from_attributes = True