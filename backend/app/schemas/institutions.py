from typing import List

from pydantic import BaseModel

# from .investment_titles import InvestmentTitleResponse


class InstitutionBase(BaseModel):
    name: str


class InstitutionCreate(InstitutionBase):
    pass


class InstitutionResponse(InstitutionBase):
    id: int
    titles: List['InvestmentTitleResponse'] = []

    class Config:
        from_attributes = True
