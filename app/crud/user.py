from __future__ import annotations

from typing import TypeVar

from sqlalchemy.orm import Session

from app.db.base_class import Base
from app.models import user


ModelType = TypeVar('ModelType', bound=Base)


def get_user(db: Session, user_id: int) -> ModelType | None:
    return db.query(user.User).filter(user.User.id == user_id).first()
