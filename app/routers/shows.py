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
        # db: Session = Depends(get_db),
        # current_user: int = Depends(Oauth2.get_current_user)
    ):

    # posts = db.query(models.Show).all()
    # print(posts)

    #return an array of shows with air and end dates from the database 
    return [
        {
            "id": 1,
            "show_name": "The Office",
            "show_air_time":"2023-06-11 16:02:27.934575",
            "show_end_time":"2023-06-11 17:02:27.934575"
        },
        {
            "id": 2,
            "show_name": "Parks and Rec",
            "show_air_time":"2023-06-11 17:02:27.934575",
            "show_end_time":"2023-06-11 18:02:27.934575"
        },
        {
            "id": 3,
            "show_name": "The Good Place",
            "show_air_time":"2023-06-11 18:02:27.934575",
            "show_end_time":"2023-06-11 19:02:27.934575"
        },{
            "id": 4,
            "show_name": "Brooklyn 99",
            "show_air_time":"2023-06-11 19:02:27.934575",
            "show_end_time":"2023-06-11 20:02:27.934575"
        }
    ]



# @router.get('/{show_id}', response_model=schemas.Show)
# def get_show_by_id(
#         show_id: int
#         db: Session = Depends(get_db),
#         current_user: int = Depends(Oauth2.get_current_user)
#     ):
#     # return a single show with air and end dates from the database
#     return {"id": 1, "show_name": "The Office", "show_air_time":""}
