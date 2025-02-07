from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base_class import Base
from app.dependencies import get_current_user
from app.dependencies import get_db
from app.main import app
from app.models.user import User

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


def test_root_route():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}


def test_create(test_db):
    response = client.post('/api/v1/auth/signup', json={'first_name': 'Fourth', 'surname': 'Fourth_sur', 'email': '1@m.com', 'is_superuser': False, 'id': 4, 'password': '123'})
    response = client.post('/api/v1/auth/signup', json={'first_name': 'Third', 'surname': 'Third_sur', 'email': '2@m.com', 'is_superuser': False, 'id': 3, 'password': '123'})
    assert response.status_code == 200
    assert response.json() == {
        'first_name': 'Third',
        'surname': 'Third_sur',
        'is_superuser': False,
        'email': '2@m.com',
        'id': 3,
    }


def test_get():
    response = client.get('/api/v1/users/user/3')
    assert response.status_code == 200
    assert response.json() == {
        'first_name': 'Third',
        'surname': 'Third_sur',
        'is_superuser': False,
        'email': '2@m.com',
        'id': 3,
    }


def test_get_by_email():
    response = client.get('/api/v1/users/user_email/2@m.com')
    assert response.status_code == 200
    assert response.json() == {
        'first_name': 'Third',
        'surname': 'Third_sur',
        'is_superuser': False,
        'email': '2@m.com',
        'id': 3,
    }


def test_get_multi_unauth():
    response = client.get('/api/v1/users/users/')
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_login_incorrect():
    response = client.post(
        '/api/v1/auth/login', data={
            'grant_type': 'password', 'username': 11, 'password': 11, 'scope': '', 'client_id': 'string', 'client_secret': 'string',
        },
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect username or password'}


def test_get_multi_not_auth():
    response = client.get('/api/v1/users/users/')
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_get_own_page_false():
    response = client.get('/api/v1/auth/me')
    assert response.status_code == 401


def test_login_correct():
    response = client.post(
        '/api/v1/auth/login', data={
            'grant_type': 'password', 'username': '1@m.com', 'password': 123, 'scope': '', 'client_id': 'string', 'client_secret': 'string',
        },
    )
    assert response.status_code == 200


def test_get_multi_auth():
    def ovverride_get_current_user():
        return User(id=11, first_name='dsad', surname='sdfsd', email='12@m.com', is_superuser=True, hashed_password='sdfsdfsdfsdfs')
    app.dependency_overrides[get_current_user] = ovverride_get_current_user

    response = client.get('/api/v1/users/users/')
    assert response.status_code == 200
    assert response.json() == {
        'results': [
            {
                'first_name': 'Third',
                'surname': 'Third_sur',
                'is_superuser': False,
                'email': '2@m.com',
                'id': 3,
            },
            {
                'first_name': 'Fourth',
                'surname': 'Fourth_sur',
                'is_superuser': False,
                'email': '1@m.com',
                'id': 4,
            },
        ],
    }


def test_get_own_page_accept():
    response = client.get('/api/v1/auth/me')
    assert response.status_code == 200


def test_update():
    response = client.put('/api/v1/users/', json={'first_name': 'one', 'surname': 'two', 'email': '1@m.com', 'is_superuser': False})
    assert response.status_code == 201
    assert response.json() == {
        'first_name': 'one',
        'surname': 'two',
        'is_superuser': False,
        'email': '1@m.com',
        'id': 4,
    }


def test_fail_update():
    response = client.put('/api/v1/users/', json={'first_name': 'one', 'surname': 'two', 'email': '10@m.com', 'is_superuser': False})
    assert response.status_code == 400
    assert response.json() == {'detail': 'User with email: 10@m.com not found.'}


def test_delete():
    response = client.delete('/api/v1/users/users/4')
    assert response.status_code == 200
    assert response.json() == {
        'first_name': 'one',
        'surname': 'two',
        'is_superuser': False,
        'email': '1@m.com',
        'id': 4,
    }
