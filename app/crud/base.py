from __future__ import annotations

from typing import Generic
from typing import TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base


ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()
