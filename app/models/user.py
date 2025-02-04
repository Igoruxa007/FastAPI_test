from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)
