from sqlalchemy import Column, Integer, String
from database.config import Base
from models import Base

class Dentist(Base):
    __tablename__ = 'dentists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialty = Column(String)
    contact_info = Column(String)

    @classmethod
    def create(cls, session, name, specialty, contact_info):
        dentist = cls(name=name, specialty=specialty, contact_info=contact_info)
        session.add(dentist)
        session.commit()
        session.refresh(dentist)
        return dentist

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, dentist_id):
        return session.query(cls).filter(cls.id == dentist_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
