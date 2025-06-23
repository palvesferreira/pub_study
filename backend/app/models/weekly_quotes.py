from datetime import datetime

from sqlalchemy import Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class WeeklyQuote(Base):
    __tablename__ = 'quotes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title_id: Mapped[int] = mapped_column(Integer, ForeignKey('titles.id'))
    date: Mapped[datetime] = mapped_column(Date)
    quantity: Mapped[float] = mapped_column(Float)
    value: Mapped[float] = mapped_column(Float)
    previous_value: Mapped[float] = mapped_column(Float)
    gain: Mapped[float] = mapped_column(Float)
    gain_percent: Mapped[float] = mapped_column(Float)

    title = relationship("InvestmentTitle")
