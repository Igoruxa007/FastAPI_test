from __future__ import annotations

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str


class User(UserBase):
    id: int
    surname: str
    is_superuser: bool

    class Config:
        orm_mod = True
