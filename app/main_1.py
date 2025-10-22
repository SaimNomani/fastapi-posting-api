from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from pprint import pprint

app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    # rating: Optional[int]=None

while True:
    try:
        conn=psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="postgress@123", cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Databaase connection was successfull")
        print("connection: ", conn)

        break

    except Exception as err:
        print("Databaase connection failed")
        print("error: ", err)
        time.sleep(2)

# saving posts in memory instead of DB
# my_posts=[]




@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    cursor.execute('''
        SELECT * FROM posts
    ''')

    posts=cursor.fetchall()
    pprint(posts)
    return {
        "message": "Your alll posts",
        "Posts":posts
        }

# ---function that takes a required JSON object from the request body,
#  turns it into a Python dictionary, and makes it available as body_data.
#
# ---Body(...) automatically converts the incoming JSON data from the request body into a Python dictionary
#  (or a Pydantic model, if you specify one).
# 
# @app.post("/createPost")
# async def create_post(body_data:dict=Body(...)):
#     return {"message":"Post successfully created",
#             "post":{ 
#                 "title":body_data["title"],
#                 "content":body_data["content"]
#             }}

# ---in Pydantic with FastAPI, you don’t need to use = Body(...) when the parameter is a Pydantic model.
#  ---FastAPI will automatically treat it as a request body.
# 
@app.post("/posts",status_code=status.HTTP_201_CREATED) #to change default status code just pass status code to decorator
async def create_post(post: Post):
    # print(type(new_post))
    # print(new_post)
    # print(new_post.dict())
    # post_dict=post.dict()
    # post_dict["id"]=1 if len(my_posts)==0 else my_posts[-1]["id"]+1
    # my_posts.append(post_dict)

    cursor.execute('''
        INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING *
        ''',(post.title, post.content, post.published))
    
    new_post=cursor.fetchone()

    conn.commit()

    pprint(new_post)
    return{
        "message":"Post successfully created",
        "Post":new_post

        }


@app.get("/posts/{id}")  
def get_post(id: int, response:Response):  
    # post = list(filter(lambda post: id == post["id"], my_posts))

    cursor.execute('''
        SELECT * FROM posts
        where id=%s
    ''',(str(id),))

    post=cursor.fetchone()

    if not post:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {
        #     "message": f"post with id: {id} not found"
        # }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    
    return {
        "post": post
    }


@app.delete("/posts/{id}")
def delete_post(id:int, response:Response):


    cursor.execute('''
        DELETE FROM posts WHERE id = %s RETURNING *
    ''', (str(id),))

    deleted_post=cursor.fetchone()
    
    conn.commit()

    pprint(deleted_post)


    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT) # when we delete something fastApi dont expect to send anything



    ########ANOTHER WAY TO DELETE#############
    # Find the index of the post
    # post_index = next((index for index, post in enumerate(my_posts) if post["id"] == id), None)

    # if post_index is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    
    # # Delete the post
    # deleted_post = my_posts.pop(post_index)

    # global my_posts
    # The keyword global is only needed when you reassign the entire variable, like this:
    # my_posts = [new list]  # <-- THIS is a reassignment.
    # But if you only modify the existing list, like .pop(), .append(), .remove(), .clear(), etc., you don't need global.

    # no_of_posts=len(my_posts)
    # my_posts=list(filter(lambda post: id!=post["id"], my_posts))
    # if len(my_posts)==no_of_posts:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    # else:
        # return Response(status_code=status.HTTP_204_NO_CONTENT) # when we delete something fastApi dont expect to send anything 
    


# PUT replaces the entire resource (full update).
# PATCH updates only specific fields (partial update).
# 
#Use PUT when you want to replace the whole object.
# Use PATCH when you want to modify only a part of the object.
# 
# For PUT, send the full object (all fields) in the request body (usually JSON).
# For PATCH, send only the fields you want to update in the request body (JSON).

# PUT request to update an entire post by id
@app.put("/posts/{id}")
def update_post(id: int, post_updates: Post):


        cursor.execute('''
        UPDATE posts SET title= %s, content= %s, published= %s WHERE id= %s RETURNING *
    ''', (post_updates.title, post_updates.content, post_updates.published, str(id)))
        
        updated_post=cursor.fetchone()
        pprint(updated_post)

        conn.commit()

        if updated_post==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
        return {
             "updated post": updated_post
         }

#     # Find the index of the post with matching id
#     post_index = next((index for index, post in enumerate(my_posts) if post["id"] == id), None)

#     # If post not found, raise 404 error
#     if post_index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     else:
#         # Convert incoming Post model to dictionary
#         post_dict = post_updates.dict()
#         # Keep the original id (do not allow user to change it)
#         post_dict["id"] = id
#         # Replace the old post completely with new data
#         my_posts[post_index] = post_dict
#         # Return the updated post
#         return {
#             "updated post": post_dict
#         }

# # PATCH request to update specific fields of a post by id
# @app.patch("/posts/{id}")
# def patch_post(id: int, post_updates: Post):
#     # Find the index of the post with matching id
#     post_index = next((index for index, post in enumerate(my_posts) if post["id"] == id), None)

#     # If post not found, raise 404 error
#     if post_index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     else:
#         # Convert incoming Post model to dictionary
#         post_dict = post_updates.dict(exclude_unset=True)  # ensures that fields not provided in the request retain their previous values (i.e., the default values or values that were already set before). These fields will be excluded from the update and will not be overwritten with the default values during the operation.
#         # Update the existing post, keeping the original id and other data intact
#         my_posts[post_index].update(post_dict)
#         # Return the updated post
#         return {
#             "updated post": my_posts[post_index]
#         }

 