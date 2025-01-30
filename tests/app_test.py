from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base_class import Base
from app.dependencies import get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={
        'check_same_thread': False,
    },
)
TestingSessionLocal = sessionmaker(autoflush=False, bind=engine)


def ovverride_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = ovverride_get_db


client = TestClient(app)


@pytest.fixture(scope='module')
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_root_route(test_db):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}


def test_create(test_db):
    response = client.post('/cusers/4')
    response = client.post('/cusers/3')
    assert response.status_code == 200
    assert response.json() == {
        'first_name': 'first 3',
        'surname': 'surn 3',
        'is_superuser': False,
        'id': 3,
    }


def test_get(test_db):
    response = client.get('/users/3')
    assert response.status_code == 200
    assert response.json() == {
        'first_name': 'first 3',
        'surname': 'surn 3',
        'is_superuser': False,
        'id': 3,
    }


def test_get_multi(test_db):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {
        'results': [
            {
                'first_name': 'first 3',
                'surname': 'surn 3',
                'is_superuser': False,
                'id': 3,
            },
            {
                'first_name': 'first 4',
                'surname': 'surn 4',
                'is_superuser': False,
                'id': 4,
            },
        ],
    }


def test_delete(test_db):
    response = client.delete('/users/3')
    assert response.status_code == 200
    assert response.json() == {
        'first_name': 'first 3',
        'surname': 'surn 3',
        'is_superuser': False,
        'id': 3,
    }
