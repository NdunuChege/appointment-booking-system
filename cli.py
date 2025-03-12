import click
from database.config import SessionLocal, init_db
from models.patient import Patient
from models.dentist import Dentist
from models.appointment import Appointment

# Initialize the database at the start
init_db()

def create_patient():
    """Create a new patient."""
    session = SessionLocal()
    name = input("Enter patient name: ")
    contact_info = input("Enter patient email: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")

    try:
        Patient.create(session, name=name, contact_info=contact_info, age=age, gender=gender)
        print("Patient created successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_patients():
    """View all patients."""
    session = SessionLocal()
    patients = session.query(Patient).all()
    if patients:
        for patient in patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Email: {patient.contact_info}, Age: {patient.age}, Gender: {patient.gender}")
    else:
        print("No patients found.")

def delete_patient():
    """Delete a patient."""
    session = SessionLocal()
    patient_id = int(input("Enter patient ID to delete: "))
    patient = session.query(Patient).filter_by(id=patient_id).first()

    if patient:
        patient.delete(session)
        print("Patient deleted successfully!")
    else:
        print("Patient not found.")

def create_dentist():
    """Create a new dentist."""
    session = SessionLocal()
    name = input("Enter dentist name: ")
    specialty = input("Enter dentist specialty: ")
    contact_info = input("Enter dentist email: ")

    try:
        Dentist.create(session, name=name, specialty=specialty, contact_info=contact_info)
        print("Dentist created successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_dentists():
    """View all dentists."""
    session = SessionLocal()
    dentists = session.query(Dentist).all()
    if dentists:
        for dentist in dentists:
            print(f"ID: {dentist.id}, Name: {dentist.name}, Specialty: {dentist.specialty}, Email: {dentist.contact_info}")
    else:
        print("No dentists found.")

def delete_dentist():
    """Delete a dentist."""
    session = SessionLocal()
    dentist_id = int(input("Enter dentist ID to delete: "))
    dentist = session.query(Dentist).filter_by(id=dentist_id).first()

    if dentist:
        dentist.delete(session)
        print("Dentist deleted successfully!")
    else:
        print("Dentist not found.")

def create_appointment():
    """Create a new appointment."""
    session = SessionLocal()
    patient_id = int(input("Enter patient ID: "))
    dentist_id = int(input("Enter dentist ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM AM/PM): ")

    try:
        Appointment.create(session, patient_id=patient_id, dentist_id=dentist_id, date=date, time=time)
        print("Appointment created successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_appointments():
    """View all appointments."""
    session = SessionLocal()
    appointments = session.query(Appointment).all()
    if appointments:
        for appointment in appointments:
            print(f"ID: {appointment.id}, Patient ID: {appointment.patient_id}, Dentist ID: {appointment.dentist_id}, Date: {appointment.date}, Time: {appointment.time}, Status: {appointment.status}")
    else:
        print("No appointments found.")

def delete_appointment():
    """Delete an appointment."""
    session = SessionLocal()
    appointment_id = int(input("Enter appointment ID to delete: "))
    appointment = session.query(Appointment).filter_by(id=appointment_id).first()

    if appointment:
        appointment.delete(session)
        print("Appointment deleted successfully!")
    else:
        print("Appointment not found.")

def main_menu():
    """Interactive Main Menu for the CLI."""
    while True:
        print("\nDentist Appointment Manager")
        print("1. Add a Patient")
        print("2. View  Patients")
        print("3. Delete a Patient")
        print("4. Add a Dentist")
        print("5. View Dentists")
        print("6. Delete a Dentist")
        print("7. Add an Appointment")
        print("8. View Appointments")
        print("9. Delete an Appointment")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            create_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            delete_patient()
        elif choice == "4":
            create_dentist()
        elif choice == "5":
            view_dentists()
        elif choice == "6":
            delete_dentist()
        elif choice == "7":
            create_appointment()
        elif choice == "8":
            view_appointments()
        elif choice == "9":
            delete_appointment()
        elif choice == "0":
            print("Adios Muchacho!")
            break
        else:
            print("Please try again.")

if __name__ == "__main__":
    main_menu()
