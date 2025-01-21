from __future__ import annotations

from fastapi import APIRouter
from fastapi import FastAPI


app = FastAPI(
    title='Test', openapi_url='/openapi.json',
)

api_router = APIRouter()


@api_router.get('/', status_code=200)
def read_root() -> dict:
    return {'Hello': 'World'}


@api_router.get('/users/{user_id}')
def read_user(user_id: int, q: str | None = None) -> dict:
    return {'item_id': user_id, 'q': q}


@api_router.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None) -> dict:
    return {'item_id': item_id, 'q': q}


app.include_router(api_router)
