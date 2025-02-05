from __future__ import annotations

from collections.abc import MutableMapping
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Union

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm.session import Session

from app.core.security import verify_password
from app.models.user import User

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, list[str], list[int]],
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')


def authenticate(
        *,
        email: str,
        password: str,
        db: Session,
) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(*, sub: str) -> str:
    return _create_token(
        token_type='access_token',
        lifetime=timedelta(minutes=60),
        sub=sub,
    )


def _create_token(
        token_type: str,
        lifetime: timedelta,
        sub: str,
) -> str:
    payload : dict[str, str | datetime] = {}
    expire = datetime.now(timezone.utc) + lifetime
    payload['type'] = token_type
    payload['exp'] = expire
    payload['iat'] = datetime.now(timezone.utc)
    payload['sub'] = str(sub)

    encoded_jwt = jwt.encode(payload, '1111', algorithm='HS256')
    return encoded_jwt
