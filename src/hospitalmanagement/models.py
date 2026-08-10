# 






from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

from .database import Base


# =========================
# Doctor Table
# =========================
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    salary = Column(Float)

    # One Doctor -> Many Patients
    patients = relationship("Patient", back_populates="doctor")

    # One Doctor -> Many Appointments
    appointments = relationship("Appointment", back_populates="doctor")


# =========================
# Patient Table
# =========================
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    disease = Column(String)
    admission_date = Column(Date)

    # Foreign Key pointing to Doctor table
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    # Relationship back to Doctor
    doctor = relationship("Doctor", back_populates="patients")

    # One Patient -> Many Appointments
    appointments = relationship("Appointment", back_populates="patient")


# =========================
# Staff Table
# =========================
class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String)
    shift = Column(String)
    salary = Column(Float)



    #========================#




class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    doctor_id = Column(
        Integer,
        ForeignKey("doctors.id"),
        nullable=False
    )

    diagnosis = Column(String, nullable=False)
    treatment = Column(String, nullable=False)
    record_date = Column(Date, nullable=False)
    notes = Column(String)

    patient = relationship("Patient")
    doctor = relationship("Doctor")









# =========================
# Appointment Table
# =========================
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    # Patient Foreign Key
    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    # Doctor Foreign Key
    doctor_id = Column(
        Integer,
        ForeignKey("doctors.id"),
        nullable=False
    )

    # Appointment Date
    appointment_date = Column(Date, nullable=False)

    # Appointment Time
    appointment_time = Column(Time, nullable=False)

    # Appointment Status
    status = Column(String, default="Scheduled")

    # Relationships
    patient = relationship(
        "Patient",
        back_populates="appointments"
    )

    doctor = relationship(
        "Doctor",
        back_populates="appointments"
    )