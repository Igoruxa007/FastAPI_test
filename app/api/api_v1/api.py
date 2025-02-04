from __future__ import annotations

from fastapi import APIRouter

from app.api.api_v1.endpoints.auth import router
from app.api.api_v1.endpoints.user import api_router

users_router = APIRouter()
auth_router = APIRouter()

users_router.include_router(api_router, prefix='/users', tags=['users'])
auth_router.include_router(router, prefix='/auth', tags=['auth'])
