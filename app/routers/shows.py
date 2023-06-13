from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models, schemas, Oauth2
from typing import List, Optional
from ..database import get_db

router = APIRouter(
    prefix="/shows",
    tags=["Shows"]
)

@router.get('/', response_model=List[schemas.Show])
def get_all_shows(
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    posts = db.query(models.Show).all()
    # print(posts)

    #return an array of shows with air and end dates from the database 
    
    return posts
    
    # return [
    #     {
    #         "id": 1,
    #         "show_name": "The Office",
    #         "show_air_time":"2023-05-24T15:53:39.169735+00:00",
    #         "show_end_time":"2023-05-24T15:53:39.169735+00:00"
    #     },
    #     {
    #         "id": 2,
    #         "show_name": "Parks and Rec",
    #         "show_air_time":"2023-05-24T15:53:39.169735+00:00",
    #         "show_end_time":"2023-05-24T15:53:39.169735+00:00"
    #     },
    #     {
    #         "id": 3,
    #         "show_name": "The Good Place",
    #         "show_air_time":"2023-05-24T15:53:39.169735+00:00",
    #         "show_end_time":"2023-05-24T15:53:39.169735+00:00"
    #     },{
    #         "id": 4,
    #         "show_name": "Brooklyn 99",
    #         "show_air_time":"2023-05-24T15:53:39.169735+00:00",
    #         "show_end_time":"2023-05-24T15:53:39.169735+00:00"
    #     }
    # ]



@router.get('/{show_id}', response_model=List[schemas.Story])
def get_show_by_id(
        show_id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    show_stories = db.query(models.Story).filter(models.Show.id == show_id).all()
    print(show_stories)
    
    return show_stories
