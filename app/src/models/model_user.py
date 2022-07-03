import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, constr, validator


# For data representation
class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    is_company: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


# For data obtaining from user
class UserInput(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password_confirm: str
    is_company: bool = False

    @validator("password_confirm")
    def password_match(cls, value, values):
        if "password" in values and value != values["password"]:
            raise ValueError("paswords don't match")
        else:
            return value
