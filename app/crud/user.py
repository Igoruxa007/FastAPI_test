from __future__ import annotations

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    ...


user_inst = CRUDUser(User)
