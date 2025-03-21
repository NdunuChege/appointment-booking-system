import click
from database.config import SessionLocal, init_db # type: ignore
from models.patient import Patient # type: ignore
from models.dentist import Dentist # type: ignore
from models.appointment import Appointment # type: ignore


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


init_db()

@click.group()
def cli():
    """CLI for managing patients, dentists, and appointments."""
    pass


@cli.command()
def create_patient():
    
    session = SessionLocal()
    try:
        name = input("Enter patient name: ")
        contact_info = input("Enter patient email: ")
        age = int(input("Enter patient age: "))
        gender = input("Enter patient gender: ")

        Patient.create(session, name=name, contact_info=contact_info, age=age, gender=gender)
        click.echo("Patient created successfully!")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

@cli.command()
def view_patients():
    
    session = SessionLocal()
    try:
        patients = Patient.get_all(session)
        for patient in patients:
            click.echo(f"ID: {patient.id}, Name: {patient.name}, Email: {patient.contact_info}, Age: {patient.age}, Gender: {patient.gender}")
    finally:
        session.close()

@cli.command()
def delete_patient():
    
    session = SessionLocal()
    try:
        patient_id = int(input("Enter patient ID to delete: "))
        patient = Patient.find_by_id(session, patient_id)

        if patient:
            patient.delete(session)
            click.echo("Patient deleted successfully!")
        else:
            click.echo("Patient not found.")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()


@cli.command()
def create_dentist():
    
    session = SessionLocal()
    try:
        name = input("Enter dentist name: ")
        specialty = input("Enter dentist specialty: ")
        contact_info = input("Enter dentist email: ")

        Dentist.create(session, name=name, specialty=specialty, contact_info=contact_info)
        click.echo("Dentist created successfully!")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

@cli.command()
def view_dentists():
    
    session = SessionLocal()
    try:
        dentists = Dentist.get_all(session)
        for dentist in dentists:
            click.echo(f"ID: {dentist.id}, Name: {dentist.name}, Specialty: {dentist.specialty}, Email: {dentist.contact_info}")
    finally:
        session.close()

@cli.command()
def delete_dentist():
    
    session = SessionLocal()
    try:
        dentist_id = int(input("Enter dentist ID to delete: "))
        dentist = Dentist.find_by_id(session, dentist_id)

        if dentist:
            dentist.delete(session)
            click.echo("Dentist deleted successfully!")
        else:
            click.echo("Dentist not found.")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()


@cli.command()
def create_appointment():
    
    session = SessionLocal()
    try:
        patient_id = int(input("Enter patient ID: "))
        dentist_id = int(input("Enter dentist ID: "))
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM AM/PM): ")
        status = 'Booked'

        Appointment.create(session, patient_id=patient_id, dentist_id=dentist_id, date=date, time=time, status=status)
        click.echo("Your appointment was booked successfully!")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

@cli.command()
def view_appointments():
    
    session = SessionLocal()
    try:
        appointments = Appointment.get_all(session)
        for appointment in appointments:
            click.echo(f"ID: {appointment.id}, Patient ID: {appointment.patient_id}, Dentist ID: {appointment.dentist_id}, Date: {appointment.date}, Time: {appointment.time}, Status: {appointment.status}")
    finally:
        session.close()

@cli.command()
def delete_appointment():
    
    session = SessionLocal()
    try:
        appointment_id = int(input("Enter appointment ID to delete: "))
        appointment = Appointment.find_by_id(session, appointment_id)

        if appointment:
            appointment.delete(session)
            click.echo("Your appointment was deleted successfully!")
        else:
            click.echo("No such appointment.")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

from models import Base


if __name__ == "__main__":
    cli()
