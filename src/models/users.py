from datetime import datetime
from typing import Optional

from pydantic import EmailStr, validator, constr

from models.base import BaseModel


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    is_company: bool
    created_at: datetime
    updated_at: datetime


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password2: constr(min_length=8)
    is_company: bool = False

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password2' in values and v != values['password']:
            raise ValueError('Password do not match!')
        return v
