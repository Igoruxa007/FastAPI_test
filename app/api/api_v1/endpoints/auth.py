from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm.session import Session

from app import schemas
from app.dependencies import get_db
from app.models.user import User

router = APIRouter()


@router.post('/signup', response_model=schemas.user.User, status_code=200)
def login(
    *,
    db: Session = Depends(get_db),
    user_in: schemas.UserCreate,
) -> Any:
    user = db.query(User).filter(User.email == user_in.email).first()
    return user
