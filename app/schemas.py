from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserRepsonse(BaseModel):
    id: int
    email: str
    created: datetime

    class Config:
        orm_mode = True

class PostModel(PostBase):
    id: int
    created: datetime
    owner_id: int
    owner: UserRepsonse

    class Config:
        orm_mode = True

class PostVotesModel(BaseModel):
    Post: PostModel
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)