from typing import Union

from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Test", openapi_url="/openapi.json"
)

api_router = APIRouter()

@api_router.get("/", status_code=200)
def read_root() -> dict:
    return {"Hello": "World"}


@api_router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    return {"item_id": item_id, "q": q}

app.include_router(api_router)