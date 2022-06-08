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

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_posts(id: str, value: str):
    posts[id] = value
    return posts[id]

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_posts(id: str, value: str):
    posts[id] = value
    return posts[id]

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_posts(id: str):
    
    if id in posts:
        del posts[id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_400_BAD_REQUEST)