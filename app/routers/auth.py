

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import oauth2, schemas, database, models, utils
from sqlalchemy.orm import Session



router=APIRouter()

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db:Session= Depends(database.get_db)):
# This is a dependency class to collect the username and password as form data for an OAuth2 password flow.
# The OAuth2 specification dictates that for a password flow the data should be collected using form data (instead of JSON) and that it should have the specific fields username and password.
# All the initialization parameters are extracted from the request.

# def login(user_credentials: schemas.UserLogin, db:Session= Depends(database.get_db)):

    if not user_credentials.username or not user_credentials.password:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Username and password are required")

    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    return {
        "access_token": oauth2.create_access_token({"id": user.id}),
        "token_type": "Bearer token"
    }