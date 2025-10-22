from typing import Optional, Literal
from pydantic import BaseModel, EmailStr
from datetime import datetime

class BasePost(BaseModel):
    title:str
    content:str
    published:bool=True
    # rating: Optional[int]=None


class PostCreate(BasePost):
    pass

class UserResponse(BaseModel):
    id:int
    created_at: datetime
    email: EmailStr

    class Config:
        orm_mode=True


class postResponse(BasePost):
    id:int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True

# By default, Pydantic models only work with standard Python dict-like data. 
# However, SQLAlchemy returns ORM objects (instances of classes, not plain dicts). orm_mode = True tells Pydantic:
# “Treat non-dict objects (like SQLAlchemy ORM instances) as if they were dicts when accessing fields.”

class PostWithVotesResponse(BaseModel):
    Post: postResponse
    votes: int


class BaseUser(BaseModel):
    email:EmailStr
    password:str



class UserCreate(BaseUser):
    pass


# UserCreate is used to handle incoming JSON data from client requests, 
# which FastAPI automatically parses into a Python dictionary, so it doesn’t need orm_mode. 
# On the other hand, UserResponse is used to return data from the database, 
# which typically comes as a SQLAlchemy ORM object. Since Pydantic models expect dictionaries by default, 
# setting orm_mode = True in UserResponse allows it to read and serialize ORM objects correctly for the response.

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]=None

class Vote(BaseModel):
    post_id: int
    dir: Literal[0,1]  # 0 means delete vote, 1 means add vote