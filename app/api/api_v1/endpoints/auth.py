from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm.session import Session

from app import schemas
from app.crud import user
from app.dependencies import get_db
from app.schemas.user import UserCreate


router = APIRouter()


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
