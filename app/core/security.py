from __future__ import annotations

from passlib.context import CryptContext


PWD_CONTEXT = CryptContext(schemes=['bcrypt'])


def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)
