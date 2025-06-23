from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from core.security import hash_password

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    name = Column(String, unique=True)
    hashed_password = Column(String)

class InvestmentTitle(Base):
    __tablename__ = 'titles'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    description = Column(String)
    type_title = Column(String)
    institution_id = Column(Integer, ForeignKey('institutions.id'))
    institution = relationship("Institution")

class Institution(Base):
    __tablename__ = 'institutions'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class WeeklyQuote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    quantity = Column(Float)
    value = Column(Float)
    previous_value = Column(Float)
    gain = Column(Float)
    gain_percent = Column(Float)
    title_id = Column(Integer, ForeignKey('titles.id'))
    title = relationship("InvestmentTitle")