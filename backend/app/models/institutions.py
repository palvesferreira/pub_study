from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Institution(Base):
    __tablename__ = 'institutions'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
