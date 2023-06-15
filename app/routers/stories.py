from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func, text
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


    #NOT WORKING!!
    # stories = db.query(models.Story).all()
    print("hey look at me, I'm the shitty code that doesn't want to work")
    print(db.query(models.Story).all())

#----------------------------

    # # WORKING!!
    stories = db.execute(text("SELECT * FROM stories")).all()
    # print(stories)
    
    return stories

