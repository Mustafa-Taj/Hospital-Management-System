
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# =========================
# STREAMLIT CONFIG
# =========================

st.set_page_config(
    page_title="Hospital Management",
    page_icon="🏥",
    layout="wide"
)


st.title("🏥 Hospital Management System")

st.sidebar.title("Menu")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Dashboard",
        "Doctors",
        "Patients",
        "Appointments",
        "Medical Records"
    ]
)


# =========================
# DASHBOARD
# =========================

if page == "Dashboard":

    st.header("🏥 Hospital Dashboard")

    # Get Doctors
    doctor_response = requests.get(
        "http://127.0.0.1:8000/doctor"
    )

    # Get Patients
    patient_response = requests.get(
        "http://127.0.0.1:8000/patient"
    )

    if doctor_response.status_code == 200:
        doctors = doctor_response.json()
        doctor_count = len(doctors)
    else:
        doctors = []
        doctor_count = 0

    if patient_response.status_code == 200:
        patients = patient_response.json()
        patient_count = len(patients)
    else:
        patients = []
        patient_count = 0

    # Dashboard cards
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "👨‍⚕️ Total Doctors",
            doctor_count
        )

    with col2:
        st.metric(
            "🧑‍🦽 Total Patients",
            patient_count
        )

    st.divider()

    st.subheader("📊 Hospital Overview")

    st.write(
        "Yahan hospital ke doctors aur patients ka summary "
        "show ho raha hai."
    )












    


# =========================
# DOCTORS
# =========================

elif page == "Doctors":

    st.header("👨‍⚕️ Doctors")

    # =========================
    # ADD DOCTOR
    # =========================

    with st.form("doctor_form"):

        st.subheader("➕ Add Doctor")

        name = st.text_input("Doctor Name")

        specialization = st.text_input(
            "Specialization"
        )

        email = st.text_input(
            "Email"
        )

        phone = st.text_input(
            "Phone"
        )

        salary = st.number_input(
            "Salary",
            min_value=0.0,
            step=1000.0
        )

        submit = st.form_submit_button(
            "Add Doctor"
        )

        if submit:

            doctor_data = {
                "name": name,
                "specialization": specialization,
                "email": email,
                "phone": phone,
                "salary": salary
            }

            response = requests.post(
                "http://127.0.0.1:8000/doctor",
                json=doctor_data
            )

            if response.status_code == 200:

                st.success(
                    "Doctor successfully add ho gaya! ✅"
                )

                st.rerun()

            else:

                st.error(
                    f"Doctor add nahi hua: {response.text}"
                )


    # =========================
    # DOCTORS LIST
    # =========================

    st.subheader("📋 Doctors List")

    response = requests.get(
        "http://127.0.0.1:8000/doctor"
    )

    if response.status_code == 200:

        doctors = response.json()

        if doctors:

            st.dataframe(
                doctors,
                width="stretch",
                hide_index=True
            )

        else:

            st.info(
                "Abhi koi doctor record nahi hai."
            )

    else:

        st.error(
            f"Doctors ka data nahi mil raha: {response.text}"
        )


    # =========================
    # DELETE DOCTOR
    # =========================

    st.subheader("🗑️ Delete Doctor")

    doctor_id = st.number_input(
        "Doctor ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Doctor"):

        response = requests.delete(
            f"http://127.0.0.1:8000/doctor/{doctor_id}"
        )

        if response.status_code == 200:

            st.success(
                "Doctor delete ho gaya! ✅"
            )

            st.rerun()

        else:

            st.error(
                f"Doctor delete nahi hua: {response.text}"
            )


# =========================
# PATIENTS
# =========================

elif page == "Patients":

    st.header("👨‍🦽 Patients")

    # =========================
    # ADD PATIENT
    # =========================

    with st.form("patient_form"):

        st.subheader("➕ Add Patient")

        name = st.text_input(
            "Patient Name"
        )

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            step=1
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

        disease = st.text_input(
            "Disease"
        )

        admission_date = st.date_input(
            "Admission Date"
        )

        doctor_id = st.number_input(
            "Doctor ID",
            min_value=1,
            step=1
        )

        submit = st.form_submit_button(
            "Add Patient"
        )

        if submit:

            patient_data = {
                "name": name,
                "age": age,
                "gender": gender,
                "disease": disease,
                "admission_date": str(admission_date),
                "doctor_id": doctor_id
            }

            response = requests.post(
                "http://127.0.0.1:8000/patient",
                json=patient_data
            )

            if response.status_code == 200:

                st.success(
                    "Patient successfully add ho gaya! ✅"
                )

                st.rerun()

            else:

                st.error(
                    f"Patient add nahi hua: {response.text}"
                )


    # =========================
    # PATIENTS LIST
    # =========================

    st.subheader("📋 Patients List")

    response = requests.get(
        "http://127.0.0.1:8000/patient"
    )

    if response.status_code == 200:

        patients = response.json()

        if patients:

            st.dataframe(
                patients,
                width="stretch",
                hide_index=True
            )

        else:

            st.info(
                "Abhi koi patient record nahi hai."
            )

    else:

        st.error(
            f"Patients ka data nahi mil raha: {response.text}"
        )


# =========================
# APPOINTMENTS
# =========================

elif page == "Appointments":

    st.header("📅 Appointments")


    # =========================
    # GET DOCTORS
    # =========================

    doctor_response = requests.get(
        "http://127.0.0.1:8000/doctor"
    )


    # =========================
    # GET PATIENTS
    # =========================

    patient_response = requests.get(
        "http://127.0.0.1:8000/patient"
    )


    if doctor_response.status_code == 200:

        doctors = doctor_response.json()

    else:

        doctors = []


    if patient_response.status_code == 200:

        patients = patient_response.json()

    else:

        patients = []


    # =========================
    # BOOK APPOINTMENT
    # =========================

    st.subheader("➕ Book New Appointment")


    if not doctors:

        st.warning(
            "Pehle kam az kam ek Doctor add karein."
        )


    elif not patients:

        st.warning(
            "Pehle kam az kam ek Patient add karein."
        )


    else:

        # Doctor selection

        doctor_options = {
            f"{doctor['name']} - {doctor['specialization']}":
            doctor["id"]
            for doctor in doctors
        }


        selected_doctor = st.selectbox(
            "👨‍⚕️ Select Doctor",
            list(doctor_options.keys()),
             key="medical_record_doctor"

        )


        doctor_id = doctor_options[
            selected_doctor
        ]


        # Patient selection

        patient_options = {
            f"{patient['name']} - ID {patient['id']}":
            patient["id"]
            for patient in patients
        }


        selected_patient = st.selectbox(
            "🧑 Select Patient",
            list(patient_options.keys()),
            key="medical_record_patient"

        )


        patient_id = patient_options[
            selected_patient
        ]


        # Appointment date

        appointment_date = st.date_input(
            "📅 Appointment Date"
        )


        # Appointment time

        appointment_time = st.time_input(
            "🕐 Appointment Time"
        )


        # Appointment status

        status = st.selectbox(
            "📌 Status",
            [
                "Scheduled",
                "Completed",
                "Cancelled",
            ],
             key="medical_record_status"

        )


        # Book button

        if st.button("📅 Book Appointment"):

            appointment_data = {

                "patient_id": patient_id,

                "doctor_id": doctor_id,

                "appointment_date":
                    str(appointment_date),

                "appointment_time":
                    str(appointment_time),

                "status": status
            }


            response = requests.post(
                "http://127.0.0.1:8000/appointment",
                json=appointment_data
            )


            if response.status_code == 200:

                st.success(
                    "Appointment successfully book ho gayi! ✅"
                )

                st.rerun()

            else:

                st.error(
                    f"Appointment book nahi hui: "
                    f"{response.text}"
                )


    # ==================================================
    # IMPORTANT:
    # Appointment List BOOK BUTTON ke andar nahi hai.
    # ==================================================

    st.divider()

    st.subheader("📋 Appointment List")


    response = requests.get(
        "http://127.0.0.1:8000/appointment"
    )


    appointments = []


    if response.status_code == 200:

        appointments = response.json()


        if appointments:

            # Doctor lookup

            doctor_lookup = {
                doctor["id"]: doctor["name"]
                for doctor in doctors
            }


            # Patient lookup

            patient_lookup = {
                patient["id"]: patient["name"]
                for patient in patients
            }


            # Display data

            appointment_display = []


            for appointment in appointments:

                appointment_display.append({

                    "Appointment ID":
                        appointment["id"],

                    "Patient":
                        patient_lookup.get(
                            appointment["patient_id"],
                            "Unknown"
                        ),

                    "Doctor":
                        doctor_lookup.get(
                            appointment["doctor_id"],
                            "Unknown"
                        ),

                    "Date":
                        appointment["appointment_date"],

                    "Time":
                        appointment["appointment_time"],

                    "Status":
                        appointment["status"]
                })


            st.dataframe(
                appointment_display,
                width="stretch",
                hide_index=True
            )


        else:

            st.info(
                "Abhi koi appointment nahi hai."
            )


    else:

        st.error(
            f"Appointments ka data nahi mil raha: "
            f"{response.text}"
        )


    # =========================
    # CANCEL APPOINTMENT
    # =========================

    st.divider()

    st.subheader("❌ Cancel Appointment")


    if appointments:

        appointment_ids = [
            appointment["id"]
            for appointment in appointments
        ]


        selected_appointment = st.selectbox(
            "Select Appointment ID",
            appointment_ids
        )


        if st.button(
            "❌ Cancel Appointment"
        ):

            response = requests.delete(
                f"http://127.0.0.1:8000/appointment/"
                f"{selected_appointment}"
            )


            if response.status_code == 200:

                st.success(
                    "Appointment cancel ho gayi! ✅"
                )

                st.rerun()


            else:

                st.error(
                    f"Appointment cancel nahi hui: "
                    f"{response.text}"
                )


    else:

        st.info(
            "Cancel karne ke liye koi appointment nahi hai."
        )


# =========================

    # -----------------------------------------------------
    # ADD MEDICAL RECORD
    # -----------------------------------------------------

    st.subheader("➕ Add Medical Record")

    if not doctors:

        st.warning(
            "Pehle kam az kam ek Doctor add karein."
        )

    elif not patients:

        st.warning(
            "Pehle kam az kam ek Patient add karein."
        )

    else:

        # Patient Selection
        patient_options = {
            f"{patient['name']} - ID {patient['id']}":
            patient["id"]
            for patient in patients
        }

        selected_patient = st.selectbox(
            "🧑 Select Patient",
            list(patient_options.keys())
        )

        patient_id = patient_options[
            selected_patient
        ]

        # Doctor Selection
        doctor_options = {
            f"{doctor['name']} - {doctor['specialization']}":
            doctor["id"]
            for doctor in doctors
        }

        selected_doctor = st.selectbox(
            "👨‍⚕️ Select Doctor",
            list(doctor_options.keys())
        )

        doctor_id = doctor_options[
            selected_doctor
        ]

        # Diagnosis
        diagnosis = st.text_input(
            "🩺 Diagnosis"
        )

        # Treatment
        treatment = st.text_area(
            "💊 Treatment"
        )

        # Record Date
        record_date = st.date_input(
            "📅 Record Date"
        )

        # Notes
        notes = st.text_area(
            "📝 Notes"
        )

        # Add Record
        if st.button("➕ Add Medical Record"):

            medical_record_data = {
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "diagnosis": diagnosis,
                "treatment": treatment,
                "record_date": str(record_date),
                "notes": notes
            }

            response = requests.post(
                f"{API_URL}/medical-record",
                json=medical_record_data
            )

            if response.status_code == 200:

                st.success(
                    "Medical Record successfully add ho gaya! ✅"
                )

                st.rerun()

            else:

                st.error(
                    f"Medical Record add nahi hua: "
                    f"{response.text}"
                )

    # -----------------------------------------------------
    # MEDICAL RECORD LIST
    # -----------------------------------------------------

    st.divider()

    st.subheader("📋 Medical Records List")

    response = requests.get(
        f"{API_URL}/medical-record"
    )

    if response.status_code == 200:

        medical_records = response.json()

        if medical_records:

            doctor_lookup = {
                doctor["id"]: doctor["name"]
                for doctor in doctors
            }

            patient_lookup = {
                patient["id"]: patient["name"]
                for patient in patients
            }

            medical_record_display = []

            for record in medical_records:

                medical_record_display.append(
                    {
                        "Record ID":
                            record["id"],

                        "Patient":
                            patient_lookup.get(
                                record["patient_id"],
                                "Unknown"
                            ),

                        "Doctor":
                            doctor_lookup.get(
                                record["doctor_id"],
                                "Unknown"
                            ),

                        "Diagnosis":
                            record["diagnosis"],

                        "Treatment":
                            record["treatment"],

                        "Record Date":
                            record["record_date"],

                        "Notes":
                            record["notes"]
                    }
                )

            st.dataframe(
                medical_record_display,
                width="stretch",
                hide_index=True
            )

        else:

            st.info(
                "Abhi koi Medical Record nahi hai."
            )

    else:

        st.error(
            f"Medical Records ka data nahi mil raha: "
            f"{response.text}"
        )

    # -----------------------------------------------------
    # DELETE MEDICAL RECORD
    # -----------------------------------------------------

    st.divider()

    st.subheader("🗑️ Delete Medical Record")

    if response.status_code == 200 and medical_records:

        medical_record_ids = [
            record["id"]
            for record in medical_records
        ]

        selected_record = st.selectbox(
            "Select Medical Record ID",
            medical_record_ids
        )

        if st.button("🗑️ Delete Medical Record"):

            delete_response = requests.delete(
                f"{API_URL}/medical-record/"
                f"{selected_record}"
            )

            if delete_response.status_code == 200:

                st.success(
                    "Medical Record delete ho gaya! ✅"
                )

                st.rerun()

            else:

                st.error(
                    f"Medical Record delete nahi hua: "
                    f"{delete_response.text}"
                )

    else:

        st.info(
            "Delete karne ke liye koi Medical Record nahi hai."
        )






elif page == "Medical Records":

    st.header("📋 Medical Records")

    # ================= GET DOCTORS =================

    doctor_response = requests.get(
        f"{API_URL}/doctor"
    )

    if doctor_response.status_code == 200:
        doctors = doctor_response.json()
    else:
        doctors = []

    # ================= GET PATIENTS =================

    patient_response = requests.get(
        f"{API_URL}/patient"
    )

    if patient_response.status_code == 200:
        patients = patient_response.json()
    else:
        patients = []

    # ================= ADD MEDICAL RECORD =================

    st.subheader("➕ Add Medical Record")

    if not patients:
        st.warning("Pehle Patient add karein.")

    elif not doctors:
        st.warning("Pehle Doctor add karein.")

    else:

        patient_options = {
            f"{patient['name']} - ID {patient['id']}":
            patient["id"]
            for patient in patients
        }

        selected_patient = st.selectbox(
            "🧑 Select Patient",
            list(patient_options.keys())
        )

        patient_id = patient_options[selected_patient]

        doctor_options = {
            f"{doctor['name']} - {doctor['specialization']}":
            doctor["id"]
            for doctor in doctors
        }

        selected_doctor = st.selectbox(
            "👨‍⚕️ Select Doctor",
            list(doctor_options.keys())
        )

        doctor_id = doctor_options[selected_doctor]

        diagnosis = st.text_input("Diagnosis")

        treatment = st.text_area("Treatment")

        record_date = st.date_input("Record Date")

        notes = st.text_area("Notes")

        if st.button("💾 Save Medical Record"):

            medical_record_data = {
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "diagnosis": diagnosis,
                "treatment": treatment,
                "record_date": str(record_date),
                "notes": notes
            }

            response = requests.post(
                f"{API_URL}/medical-record",
                json=medical_record_data
            )

            if response.status_code == 200:

                st.success(
                    "Medical Record successfully add ho gaya! ✅"
                )

                st.rerun()

            else:

                st.error(
                    f"Medical Record add nahi hua: {response.text}"
                )

    # ================= MEDICAL RECORD LIST =================

    st.divider()

    st.subheader("📋 Medical Records List")

    response = requests.get(
        f"{API_URL}/medical-record"
    )

    if response.status_code == 200:

        medical_records = response.json()

        if medical_records:

            doctor_lookup = {
                doctor["id"]: doctor["name"]
                for doctor in doctors
            }

            patient_lookup = {
                patient["id"]: patient["name"]
                for patient in patients
            }

            medical_record_display = []

            for record in medical_records:

                medical_record_display.append({
                    "Record ID": record["id"],
                    "Patient": patient_lookup.get(
                        record["patient_id"],
                        "Unknown"
                    ),
                    "Doctor": doctor_lookup.get(
                        record["doctor_id"],
                        "Unknown"
                    ),
                    "Diagnosis": record["diagnosis"],
                    "Treatment": record["treatment"],
                    "Date": record["record_date"],
                    "Notes": record["notes"]
                })

            st.dataframe(
                medical_record_display,
                width="stretch",
                hide_index=True
            )

        else:

            st.info(
                "Abhi koi Medical Record nahi hai."
            )

    else:

        st.error(
            f"Medical Records ka data nahi mil raha: {response.text}"
        )