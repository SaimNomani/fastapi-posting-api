import pytest
from fastapi.testclient import TestClient

from .database import TestingSessionLocal, engine
from app.main import app
from app.database import get_db, Base
from app.oauth2 import create_access_token
from app import models

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db]=override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data={
            "email":"example123@gmail.com",
            "password":"example123"
        }
    response=client.post(
        "/users/",
        json=user_data
    )
    assert response.status_code==201

    new_user=response.json()
    new_user['password']=user_data['password']
    return new_user



@pytest.fixture
def test_user2(client):
    user_data={
            "email":"example1234@gmail.com",
            "password":"example1234"
        }
    response=client.post(
        "/users/",
        json=user_data
    )
    assert response.status_code==201

    new_user=response.json()
    new_user['password']=user_data['password']
    return new_user



@pytest.fixture
def token(test_user):
    return create_access_token({
        "id": test_user['id'],
    })

@pytest.fixture
def authorized_client(client, token):
    client.headers={
        **client.headers,
        "Authorization":f"Bearer {token}"
    }
    return client


@pytest.fixture
def test_posts(test_user, test_user2, session):
    posts_data=[
        {
            "title":"first title",
            "content":"first content",
            "owner_id":test_user['id']
        },
        {
            "title":"second title",
            "content":"second content",
            "owner_id":test_user['id']
        },
        {
            "title":"third title",
            "content":"third content",
            "owner_id":test_user['id']
        },
        {
            "title":"fourth title",
            "content":"fourth content",
            "owner_id":test_user2['id']
        }
    ]



    post_models=list(map(lambda post: models.Post(**post), posts_data))
    session.add_all(post_models)
    session.commit()
    posts=session.query(models.Post).all()
    return posts
