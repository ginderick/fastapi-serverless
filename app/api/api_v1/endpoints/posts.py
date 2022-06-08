from fastapi import APIRouter, Response
from starlette import status


router = APIRouter()

posts = {}

@router.get("/")
async def get_posts():
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_posts(post: str, value: str):
    posts[post] = value
    return posts[post]

@router.put("/", status_code=status.HTTP_200_OK)
async def update_posts(post: str, value: str):
    posts[post] = value
    return posts[post]

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def update_posts(post: str):
    
    if post in posts:
        del posts[post]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_400_BAD_REQUEST)