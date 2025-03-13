from sqlalchemy import Column, Integer, String
from database.config import Base
from models import Base

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_info = Column(String)
    age = Column(Integer)
    gender = Column(String)

    @classmethod
    def create(cls, session, name, contact_info, age, gender):
        patient = cls(name=name, contact_info=contact_info, age=age, gender=gender)
        session.add(patient)
        session.commit()
        session.refresh(patient)
        return patient

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, patient_id):
        return session.query(cls).filter(cls.id == patient_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
