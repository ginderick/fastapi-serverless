from msilib import schema
from fastapi import APIRouter, Response
from starlette import status
from typing import List, Any

from app import schemas
from app.schemas import Post


router = APIRouter()

post_1 = Post()
post_1.title = "HELLO"
post_1.description = "hello"

post_2 = Post()
post_2.title = "HI"
post_2.description = "hi"

posts = [post_1, post_2]


@router.get("/", response_model=List[schemas.Post])
def read_posts() -> Any:
    """
    Retrieve items.
    """
    return posts

@router.post("/", response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
async def create_posts(post_in: schemas.PostCreate):
    """
    Create new post.
    """
    new_post = Post(title=post_in.title, description=post_in.description)
    posts.append(new_post)
    return new_post


@router.put("/{title}", status_code=status.HTTP_200_OK)
async def update_posts(title: str, description: str):
    for post in posts:
        if post.title == title:
            post.description = description
            return post

@router.delete("/{title}", response_model=schemas.Post)
async def delete_posts(title: str):

    for post in posts:
        if post.title == title:
            posts.remove(post)
            return post
    
    return Response(status_code=status.HTTP_400_BAD_REQUEST)