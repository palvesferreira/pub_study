from datetime import datetime

from sqlalchemy import Column, Integer, String, Enum, Date, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base
from app.core.enums import TipoAtivo


class Ativo(Base):
    __tablename__ = "ativos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, index=True)
    tipo: Mapped[str] = mapped_column(Enum(TipoAtivo))
    data_compra: Mapped[datetime] = mapped_column(Date)
    preco_compra: Mapped[float] = mapped_column(Float)
    mercado: Mapped[str] = mapped_column(String)  # "primario" ou "secundario"
    cotacao_manual: Mapped[float] = mapped_column(Float, nullable=True)
