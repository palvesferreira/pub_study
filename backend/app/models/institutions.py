from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Institution(Base):
    __tablename__ = 'institutions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    titles = relationship("InvestmentTitle", back_populates="institution")