from __future__ import annotations

from collections.abc import Sequence

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    surname: str
    is_superuser: bool


class User(UserBase):
    id: int

    class Config:
        orm_mod = True


class UserCreate(User):
    ...


class UserUpdate(User):
    ...


class UserMulti(BaseModel):
    results: Sequence[User]
