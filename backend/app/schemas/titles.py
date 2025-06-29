from pydantic import BaseModel


class TitleBase(BaseModel):
    code: str
    description: str
    type_title: str
    institution_id: int

class TitleCreate(TitleBase):
    pass

class Title(TitleBase):
    id: int
    class Config:
        orm_mode = True