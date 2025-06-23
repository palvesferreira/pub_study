from pydantic import BaseModel


# --- Base ---
class UserBase(BaseModel):
    username: str


# --- Create ---
class UserCreate(UserBase):
    password: str


# --- Response ---
class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True
