from __future__ import annotations

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int

    class Config:
        orm_mod = True
