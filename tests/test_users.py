import pytest
from app import schemas
from jose import JWTError, jwt
from app.config import settings

def test_create_user(client):
    response=client.post(
        "/users/",
        json={
            "email":"example123@gmail.com",
            "password":"example123"
        }
    )
    print(response.json())
    new_user=schemas.UserResponse(**response.json())
    assert new_user.email=="example123@gmail.com"
    assert response.status_code==201


def test_login(client, test_user):
    response=client.post(
        "/login",
        data={
            "username":test_user['email'],
            "password":test_user['password']
        }
    )
    assert response.status_code==200

    token=schemas.Token(**response.json())
    payload=jwt.decode(token.access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    id=payload.get("id")

    assert id==test_user['id']
    assert token.token_type=="Bearer token"

@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemail@gmail.com", "example123", 403),
    ("example123@gmail.com", "wrongpassword", 403),
    ("wrongemail@gmail.com", "wrongpassword", 403),
    (None, "example123", 422),
    ("example123@gmail.com", None, 422)
])
def test_incorrect_login(client, test_user, email, password, status_code):
    response=client.post(
        "/login",
        data={
            "username":email,
            "password":password
        }
    )
    assert response.status_code==status_code
    # assert response.json().get("detail")=="Invalid credentials"