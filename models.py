from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    # Relationship with appointments
    appointments = relationship("Appointment", back_populates="patient")
    
    # ORM methods
    @staticmethod
    def create(session, **kwargs):
        patient = Patient(**kwargs)
        session.add(patient)
        session.commit()
        return patient

    def delete(self, session):
        session.delete(self)
        session.commit()


class Dentist(Base):
    __tablename__ = 'dentists'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)

    # Relationship with appointments
    appointments = relationship("Appointment", back_populates="dentist")
    
    # ORM methods
    @staticmethod
    def create(session, **kwargs):
        dentist = Dentist(**kwargs)
        session.add(dentist)
        session.commit()
        return dentist

    def delete(self, session):
        session.delete(self)
        session.commit()



class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    dentist_id = Column(Integer, ForeignKey('dentists.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(String, default='Scheduled')
    
    # Relationships
    patient = relationship("Patient", back_populates="appointments")
    dentist = relationship("Dentist", back_populates="appointments")
    
    # ORM methods
    @staticmethod
    def create(session, **kwargs):
        appointment = Appointment(**kwargs)
        session.add(appointment)
        session.commit()
        return appointment

    def delete(self, session):
        session.delete(self)
        session.commit()

engine = create_engine('sqlite:///dentist_appointments.db')  # Adjust for your DB
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)