from fastapi import APIRouter, Response, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette import status
from typing import List, Any

from app import models
from app.schemas import Post

import motor.motor_asyncio


router = APIRouter()

post_1 = Post()
post_1.title = "HELLO"
post_1.description = "hello"

post_2 = Post()
post_2.title = "HI"
post_2.description = "hi"

posts = [post_1, post_2]

MONGODB_URL ="change_this_url"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.posts
collection = db.posts

@router.get("/", response_model=List[models.Post])
def read_posts() -> Any:
    """
    Retrieve items.
    """
    return posts

@router.post("/", response_model=models.Post)
async def create_posts(post: models.Post = Body(...)):
    """
    Create new post.
    """
    post_json = jsonable_encoder(post)

    new_post = await collection.insert_one(post_json)
    
    created_post = await collection.find_one(
        {"_id": new_post.inserted_id})
    
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_post)


@router.put("/{title}", status_code=status.HTTP_200_OK)
async def update_posts(title: str, description: str):
    """
    Update a post.
    """
    for post in posts:
        if post.title == title:
            post.description = description
            return post

@router.delete("/{title}", response_model=models.Post)
async def delete_posts(title: str):
    """
    Delete a post.
    """
    for post in posts:
        if post.title == title:
            posts.remove(post)
            return post
    
    return Response(status_code=status.HTTP_400_BAD_REQUEST)