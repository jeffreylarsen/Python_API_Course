from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional, List

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserRepsonse(BaseModel):
    id: int
    username: str
    email: str
    member: bool
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
    username: str
    email: EmailStr
    password: str
    member: bool

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


# class Show(BaseModel):
#     id: int
#     show_name: str
#     mos_active: bool
#     created_by: str
#     show_air_date: datetime
#     show_end_date: datetime

#     class Config:
#         orm_mode = True


class StoryBase(BaseModel):
    page_number: Optional[str]
    slug: Optional[str]
    segment: Optional[str]
    writer: Optional[str]
    editor: Optional[str]
    source: Optional[str]
    script: Optional[str]
    mos_objects: Optional[str]

class StoryCreate(StoryBase):
    pass

class ShowBase(BaseModel):
    show_name: str
    mos_active: bool
    show_air_date: datetime
    show_end_date: datetime

class ShowResponse(ShowBase):
    id: int
    created_by: str   

class ShowModel(ShowBase):
    id: int
    created_by: str

    class Config:
        orm_mode = True

class StoryModel(StoryBase):

    id: int
    created_by: str
    last_modified_by: str
    estimated_time: str
    show_id: int
    show: ShowModel

    class Config:
        orm_mode = True

class ShowCreate(ShowBase):
    pass








