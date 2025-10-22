from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

from . import schemas, database, models
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from .config import settings

SECRET_KEY=settings.SECRET_KEY
ALGORITHM=settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES=settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data:dict):
    to_encode=data.copy()

    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    print(to_encode)

    encoded_jwt= jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload=jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id:str=str(payload.get("id"))
        if id is None:
            raise credentials_exception
        
        token_data=schemas.TokenData(id=id)
        return token_data

    except JWTError:
        raise credentials_exception
    

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str=Depends(oauth2_scheme), db:Session=Depends(database.get_db)):
    credentials_exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                         detail="could not validate credential", 
                                         headers={"www-Authenticate": "Bearer"})
    
    token_data= verify_access_token(token, credentials_exception)
    user=db.query(models.User).filter(models.User.id==token_data.id).first()

    return user



