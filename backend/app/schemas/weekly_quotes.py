from datetime import date

from pydantic import BaseModel


class WeeklyQuoteCreate(BaseModel):
    date: date
    quantity: float
    value: float
    previous_value: float
    gain: float
    gain_percent: float
    title_id: int


class WeeklyQuoteResponse(WeeklyQuoteCreate):
    id: int
    class Config:
        from_attributes = True
