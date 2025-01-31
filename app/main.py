from __future__ import annotations

import uvicorn
from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud import user
from app.dependencies import get_db
from app.schemas.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserMulti
from app.schemas.user import UserUpdate


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
def create_user(user_id: int, db: Session = Depends(get_db)) -> dict:
    user_name = {
        'first_name': f'first {user_id}', 'id': user_id,
        'surname': f'surn {user_id}', 'is_superuser': False,
    }
    return user.user_inst.create(db=db, obj_in=UserCreate.model_validate(user_name))


@api_router.put('/', status_code=201, response_model=User)
def update_recipe(
    *,
    recipe_in: UserUpdate,
    db: Session = Depends(get_db),
) -> dict:
    recipe = user.user_inst.get(db, id=recipe_in.id)
    if not recipe:
        raise HTTPException(
            status_code=400, detail=f'Recipe with ID: {recipe_in.id} not found.',
        )
    updated_recipe = user.user_inst.update(db=db, db_obj=recipe, obj_in=recipe_in)
    db.commit()
    return updated_recipe


@api_router.delete('/users/{user_id}', response_model=User)
def delete_user(user_id: int, q: str | None = None, db: Session = Depends(get_db)) -> User | None:
    return user.user_inst.remove(db=db, id=user_id)


app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
