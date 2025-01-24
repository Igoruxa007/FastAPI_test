from __future__ import annotations

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str


class User(UserBase):
    id: int
    surname: str

    class Config:
        orm_mod = True


class UserCreate(User):
    ...


class UserUpdate(User):
    ...
