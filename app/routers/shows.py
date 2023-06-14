from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func, text
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
    
    return posts

@router.get('/{show_id}', response_model=List[schemas.Story])
def get_show_by_id(
        show_id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    show_stories = db.query(models.Story).filter(show_id == models.Show.id).all()
    print(show_stories)
    
    return show_stories
