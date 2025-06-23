from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class InvestmentTitle(Base):
    __tablename__ = 'titles'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    description = Column(String)
    type_title = Column(String)  # Ex: CRA, LCA, Ações...
    institution_id = Column(Integer, ForeignKey('institutions.id'))
    institution = relationship("Institution")
