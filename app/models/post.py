from pydantic import BaseModel

class Post(BaseModel):
    title: str
    description: str