from __future__ import annotations

import uvicorn
from fastapi import APIRouter
from fastapi import FastAPI

from app.api.api_v1.api import auth_router
from app.api.api_v1.api import users_router


app = FastAPI(
    title='Test', openapi_url='/openapi.json',
)


api_router = APIRouter()


@api_router.get('/', status_code=200)
def read_root() -> dict:
    return {'Hello': 'World'}


app.include_router(api_router)
app.include_router(users_router, prefix='/api/v1')
app.include_router(auth_router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
