from __future__ import annotations

from typing import TypeVar

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.base_class import Base
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserUpdate


ModelType = TypeVar('ModelType', bound=Base)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_id(self, db: Session, user_id: int) -> ModelType | None:
        return db.query(User).filter(User.id == user_id).first()


user = CRUDUser(User)
