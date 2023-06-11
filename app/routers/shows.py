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
def get_my_posts(
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    posts = db.query(models.Show).all()
    print(posts)

    return posts

