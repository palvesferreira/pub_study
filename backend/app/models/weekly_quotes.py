from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class WeeklyQuote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('titles.id'))

    date = Column(Date)
    quantity = Column(Float)
    value = Column(Float)
    previous_value = Column(Float)
    gain = Column(Float)
    gain_percent = Column(Float)

    title = relationship("InvestmentTitle")
