from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class InvestmentTitle(Base):
    __tablename__ = 'titles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String)
    type_title: Mapped[str] = mapped_column(String)  # Ex: CRA, LCA, Ações...
    institution_id: Mapped[int] = mapped_column(Integer, ForeignKey('institutions.id'))

    # Relacionamentos
    institution = relationship("Institution")
    quotes = relationship("WeeklyQuote", back_populates="title")