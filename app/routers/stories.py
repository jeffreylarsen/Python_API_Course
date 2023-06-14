from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models, schemas, Oauth2
from typing import List, Optional
from ..database import get_db

router = APIRouter(
    prefix="/stories",
    tags=["Stories"]
)

@router.get('/', response_model=List[schemas.Story])
def get_all_stories(
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    if db:
        print("Well the database is getting accessed, here look...")
        print(db)
    else:
        print("the database is fucked up")

    print(db.query(models.Story))
    print(db.query(models.Story).all())
    stories = db.query(models.Story).all()
    
    return stories

