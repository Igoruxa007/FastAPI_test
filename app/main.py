from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.crud import user
from app.dependencies import get_db
from app.schemas.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserMulti


app = FastAPI(
    title='Test', openapi_url='/openapi.json',
)

api_router = APIRouter()


@api_router.get('/', status_code=200)
def read_root() -> dict:
    return {'Hello': 'World'}


@api_router.get('/users/', response_model=UserMulti)
def read_users(db: Session = Depends(get_db)) -> dict:
    results = user.user_inst.get_multi(db=db)
    return {'results': results}


@api_router.get('/users/{user_id}', response_model=User)
def read_user(user_id: int, q: str | None = None, db: Session = Depends(get_db)) -> User | None:
    return user.user_inst.get(db=db, id=user_id)


@api_router.post('/cusers/{user_id}', response_model=User)
def create_user(db: Session = Depends(get_db)) -> dict:
    user_name = {'first_name': 'first6', 'id': 7, 'surname': 'surn6', 'is_superuser': False}
    return user.user_inst.create(db=db, obj_in=UserCreate.model_validate(user_name))


@api_router.delete('/users/{user_id}', response_model=User)
def delete_user(user_id: int, q: str | None = None, db: Session = Depends(get_db)) -> User | None:
    return user.user_inst.remove(db=db, id=user_id)


app.include_router(api_router)
