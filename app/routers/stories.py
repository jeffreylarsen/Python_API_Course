from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func, text
from sqlalchemy.orm import Session
from .. import models, schemas, Oauth2
from typing import List, Optional
from ..database import get_db
from ..utils import calculate_reading_time

router = APIRouter(
    prefix="/stories",
    tags=["Stories"]
)

@router.get('/', response_model=List[schemas.StoryModel])
def get_all_stories(
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    stories = db.execute(text("SELECT * FROM stories")).all()
    # print(stories)

    return stories


@router.get('/{id}', response_model=List[schemas.StoryModel])
def get_a_story(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    story = db.execute(text(f"SELECT * FROM stories WHERE id = {id}")).first()
    # print(stories)
    
    if not story:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Story with id: {id} not found."
        )
    
    return story

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.StoryModel)
def create_a_story(
        story: schemas.StoryCreate,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    new_story = models.Story(
        created_by=current_user.username,
        last_modified_by=current_user.username,
        estimated_time=calculate_reading_time(story.script, 100),
        **story.dict()
    )
    print(story.dict())
    db.add(new_story)
    db.commit()
    db.refresh(new_story)

    return new_story

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_a_story(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    story_query = db.query(models.Story).filter(models.Story.id == id)

    story = story_query.first()

    if story == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Story with id: {id} was not found."
        )
    
    if story.created_by != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"You are not authorized to delete this story."
        )

    story_query.delete(synchronize_session=False)
    db.commit()

    return story


