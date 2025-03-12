import click
from database.config import session, init_db
from models.patient import Patient
from models.dentist import Dentist
from models.appointment import Appointment

@click.group()
def cli():
    """CLI for managing the application."""
    pass

@cli.command()
def create_patient():
    """Create a new patient."""
    session = SessionLocal()
    name = input("Enter name: ")
    contact_info = input("Enter email: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")

    try:
        Patient.create(session, name=name, contact_info=contact_info, age=age, gender=gender)
        print("Patient created successfully!")
    except Exception as e:
        print(f"Error: {e}")

@cli.command()
def view_patients():
    """View all patients."""
    session = SessionLocal()
    patients = Patient.get_all(session)
    for patient in patients:
        print(f"ID: {patient.id}, Name: {patient.name}, Email: {patient.contact_info}")

if __name__ == "__main__":
    init_db()
    cli()
