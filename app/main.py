from __future__ import annotations

from fastapi import APIRouter
from fastapi import FastAPI

from app.db.base_class import engine
from app.models import user

app = FastAPI(
    title='Test', openapi_url='/openapi.json',
)

api_router = APIRouter()

user.Base.metadata.create_all(bind=engine)


@api_router.get('/', status_code=200)
def read_root() -> dict:
    return {'Hello': 'World'}


@api_router.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None) -> dict:
    return {'item_id': item_id, 'q': q}


app.include_router(api_router)
