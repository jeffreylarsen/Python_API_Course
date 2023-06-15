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
    print(db.query(models.Story))

#----------------------------

    # # WORKING!!
    stories = db.execute(text("SELECT * FROM stories")).all()
    # print(stories)
    
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Story with id: {id} not found."
        )
    
    return stories


@router.get('/{id}', response_model=List[schemas.Story])
def get_all_stories(
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):


    #NOT WORKING!!
    # stories = db.query(models.Story).all()
    print("hey look at me, I'm the shitty code that doesn't want to work")
    print(db.query(models.Story))

#----------------------------

    # # WORKING!!
    story = db.execute(text(f"SELECT * FROM stories WHERE id = {id}")).first()
    # print(stories)
    
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Story with id: {id} not found."
        )
    
    return story

