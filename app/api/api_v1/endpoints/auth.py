from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from app import schemas
from app.core.auth import authenticate
from app.core.auth import create_access_token
from app.crud import user
from app.dependencies import get_current_user
from app.dependencies import get_db
from app.schemas.user import User
from app.schemas.user import UserCreate


router = APIRouter()


@router.post('/login')
def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    user = authenticate(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    return {
        'access_token': create_access_token(sub=user.id),
        'token_type': 'bearer',
    }


@router.post('/signup', response_model=schemas.user.User, status_code=200)
def create_user_signup(
    *,
    user_in: UserCreate,
    db: Session = Depends(get_db),
) -> dict:
    user_db = user.user_inst.get_by_email(db, email=user_in.email)
    if user_db:
        raise HTTPException(
            status_code=400,
            detail=f'User with email: {user_in.email} already exists.',
        )
    created_user = user.user_inst.create(db=db, obj_in=user_in)
    return created_user


@router.get('/me', response_model=User)
def read_user_me(current_user: User = Depends(get_current_user)) -> User:
    user = current_user
    return user
