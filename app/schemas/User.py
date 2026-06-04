from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="The password must be at least 6 characters long")

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True