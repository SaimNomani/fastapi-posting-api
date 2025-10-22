from fastapi import Response,HTTPException, Depends, status, APIRouter
from typing import Optional
from httpx import post
from ..database import engine, SessionLocal, get_db
from .. import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List 
from .. import oauth2


router=APIRouter()

@router.get("/", response_model= List[schemas.PostWithVotesResponse])
async def get_posts(db:Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user),
                    limit:int=10, skip:int=0, search: Optional[str]=""):


    # logged in user can only see his own posts
    # posts= db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()

    # posts with no votes
    # posts= db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    # posts with votes
    posts_with_votes=db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Post.id==models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(
            models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts_with_votes
        


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.postResponse) #to change default status code just pass status code to decorator
async def create_post(post: schemas.PostCreate, db:Session=Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):


    # new_post=models.Post(title=post.title, content=post.content, published=post.published)
    new_post=models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # Refreshes to retrieve the newly created post including generated fields like id.
    return new_post


@router.get("/{id}", response_model=schemas.PostWithVotesResponse)  
def get_post(id: int, response:Response, db:Session=Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):  


    # post=db.query(models.Post).filter(models.Post.id==id).first()

    post_with_votes=db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Post.id==models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(
            models.Post.id==id).first()

    if not post_with_votes:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")

# loggedin user can only see his own post by id
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")


    return post_with_votes


@router.delete("/{id}")
def delete_post(id:int, response:Response, db:Session=Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):


    post_query=db.query(models.Post).filter(models.Post.id==id)

    post=post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

# loggedin user can only delete his own post
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) # when we delete something fastApi dont expect to send anything




@router.put("/{id}", response_model=schemas.postResponse)
def update_post(id: int, post_updates: schemas.PostCreate, db:Session=Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):


        post_query=db.query(models.Post).filter(models.Post.id==id)

        post=post_query.first()

        if post==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
        
        # loggedin user can only update his own post
        if post.owner_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

        
        post_query.update(post_updates.dict(), synchronize_session=False)
        db.commit()
        return post_query.first()
