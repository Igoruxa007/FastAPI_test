from __future__ import annotations

from collections.abc import Generator

from fastapi import Depends
from fastapi import HTTPException
from jose import jwt
from jose import JWTError
from sqlalchemy.orm.session import Session

from app.core.auth import oauth2_scheme
from app.crud.user import user_inst
from app.db.base_class import SessionLocal
from app.models.user import User
from app.schemas.token import TokenData


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme),
) -> User:
    credentials_exeption = HTTPException(status_code=401, detail='Could not validate credentials')
    try:
        payload = jwt.decode(
            token=token,
            key='1111',
            algorithms='HS256',
            options={'verify_aud': False},
        )
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exeption
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exeption

    user = user_inst.get(db=db, id=token_data.username)
    if user is None:
        raise credentials_exeption
    return user
