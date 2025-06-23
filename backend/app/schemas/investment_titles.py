from typing import List

from pydantic import BaseModel

# from .institutions import InstitutionBase
from .weekly_quotes import WeeklyQuoteResponse


class InvestmentTitleBase(BaseModel):
    code: str
    description: str
    type_title: str
    institution_id: int


class InvestmentTitleCreate(InvestmentTitleBase):
    pass


class InvestmentTitleResponse(InvestmentTitleBase):
    id: int
    institution: 'InstitutionBase'
    quotes: List[WeeklyQuoteResponse] = []

    class Config:
        from_attributes = True
