from sqlalchemy import Column, Integer, String, DateTime
from database.config import Base

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    dentist_id = Column(Integer)
    date = Column(DateTime)
    time = Column(String)
    status = Column(String, default = 'Booked')

    @classmethod
    def create(cls, session, patient_id, dentist_id, date, time):
        appointment = cls(patient_id=patient_id, dentist_id=dentist_id, date=date, time=str(time), status='Booked')
        session.add(appointment)
        session.commit()
        session.refresh(appointment)
        return appointment

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, appointment_id):
        return session.query(cls).filter(cls.id == appointment_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
