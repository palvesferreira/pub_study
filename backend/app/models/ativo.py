from sqlalchemy import Column, Integer, String, Enum, Date, Float

from app.db.base_class import Base
from app.core.enums import TipoAtivo


class Ativo(Base):
    __tablename__ = "ativos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(Enum(TipoAtivo))
    data_compra = Column(Date)
    preco_compra = Column(Float)
    mercado = Column(String)  # "primario" ou "secundario"
    cotacao_manual = Column(Float, nullable=True)
