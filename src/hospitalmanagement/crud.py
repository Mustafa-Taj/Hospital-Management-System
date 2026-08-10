from sqlalchemy.orm import Session
from . import models, schemas
# ================= DOCTOR CRUD =================
def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    new_doctor = models.Doctor(**doctor.model_dump())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor

def get_doctors(db: Session):
    return db.query(models.Doctor).all()

def get_doctor_by_id(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()

def delete_doctor(db: Session, doctor_id: int):
    doctor = get_doctor_by_id(db, doctor_id)
    if doctor:
        db.delete(doctor)
        db.commit()
        return True
    return False


# ================= PATIENT CRUD =================
def create_patient(db: Session, patient: schemas.PatientCreate):
    new_patient = models.Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

def get_patients(db: Session):
    return db.query(models.Patient).all()

def get_patient_by_id(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def delete_patient(db: Session, patient_id: int):
    patient = get_patient_by_id(db, patient_id)
    if patient:
        db.delete(patient)
        db.commit()
        return True
    return False


# ================= STAFF CRUD =================
def create_staff(db: Session, staff: schemas.StaffCreate):
    new_staff = models.Staff(**staff.model_dump())
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

def get_all_staff(db: Session):
    return db.query(models.Staff).all()

def get_staff_by_id(db: Session, staff_id: int):
    return db.query(models.Staff).filter(models.Staff.id == staff_id).first()

def delete_staff(db: Session, staff_id: int):
    staff_member = get_staff_by_id(db, staff_id)
    if staff_member:
        db.delete(staff_member)
        db.commit()
        return True
    return False






# ================= APPOINTMENT CRUD =================

def create_appointment(
    db: Session,
    appointment: schemas.AppointmentCreate
):
    new_appointment = models.Appointment(
        **appointment.model_dump()
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


def get_appointments(db: Session):
    return db.query(models.Appointment).all()


def get_appointment_by_id(
    db: Session,
    appointment_id: int
):
    return db.query(models.Appointment).filter(
        models.Appointment.id == appointment_id
    ).first()


def delete_appointment(
    db: Session,
    appointment_id: int
):
    appointment = get_appointment_by_id(
        db,
        appointment_id
    )

    if appointment:
        db.delete(appointment)
        db.commit()
        return True

    return False






#===================#


def delete_appointment(db: Session, appointment_id: int):
    appointment = (
        db.query(models.Appointment)
        .filter(models.Appointment.id == appointment_id)
        .first()
    )

    if appointment:
        db.delete(appointment)
        db.commit()
        return True

    return False












# ================= MEDICAL RECORD CRUD =================

def create_medical_record(
    db: Session,
    medical_record: schemas.MedicalRecordCreate
):
    new_record = models.MedicalRecord(
        **medical_record.model_dump()
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record


def get_medical_records(db: Session):
    return db.query(models.MedicalRecord).all()


def get_medical_record_by_id(
    db: Session,
    medical_record_id: int
):
    return db.query(models.MedicalRecord).filter(
        models.MedicalRecord.id == medical_record_id
    ).first()


def delete_medical_record(
    db: Session,
    medical_record_id: int
):
    medical_record = get_medical_record_by_id(
        db,
        medical_record_id
    )

    if medical_record:
        db.delete(medical_record)
        db.commit()
        return True

    return False