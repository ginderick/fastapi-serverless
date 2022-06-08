from typing import Optional
from pydantic import BaseModel

# Shared properties
class PostBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Properties to receive on post creation
class PostCreate(PostBase):
    title: str

# Properties to receive on item update
class PostUpdate(PostBase):
    pass

# Properties to return to client
class Post(PostBase):
    pass