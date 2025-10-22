from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import Optional, List
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from pprint import pprint
from . import models,schemas, utils
from .database import engine,SessionLocal, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app=FastAPI()




@app.get("/posts", response_model= List[schemas.postResponse])
async def get_posts(db:Session=Depends(get_db)):

    posts= db.query(models.Post).all()
    return posts
        


@app.post("/posts",status_code=status.HTTP_201_CREATED, response_model=schemas.postResponse) #to change default status code just pass status code to decorator
async def create_post(post: schemas.PostCreate, db:Session=Depends(get_db)):


    # new_post=models.Post(title=post.title, content=post.content, published=post.published)
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # Refreshes to retrieve the newly created post including generated fields like id.
    return new_post


@app.get("/posts/{id}", response_model=schemas.postResponse)  
def get_post(id: int, response:Response, db:Session=Depends(get_db)):  


    post=db.query(models.Post).filter(models.Post.id==id).first()

    if not post:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    
    return post


@app.delete("/posts/{id}")
def delete_post(id:int, response:Response, db:Session=Depends(get_db)):


    post=db.query(models.Post).filter(models.Post.id==id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) # when we delete something fastApi dont expect to send anything




@app.put("/posts/{id}", response_model=schemas.postResponse)
def update_post(id: int, post_updates: schemas.PostCreate, db:Session=Depends(get_db)):


        post_query=db.query(models.Post).filter(models.Post.id==id)

        post=post_query.first()

        if post==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
        
        post_query.update(post_updates.dict(), synchronize_session=False)
        db.commit()
        return post_query.first()
         

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db:Session=Depends(get_db)):

    # hash the password
    hashed_password=utils.hash_password(user.password)
    user.password=hashed_password


    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users/{id}", response_model=schemas.UserResponse)
def get_user(id:int, db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} not found")
    return user

