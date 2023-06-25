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

@router.get('/', response_model=List[schemas.ShowModel])
def get_all_shows(
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    posts = db.query(models.Show).all()
    # print(posts)
    
    return posts

@router.get('/{show_id}', response_model=List[schemas.StoryModel])
def get_show_by_id(
        show_id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    show = db.query(models.Show).filter(models.Show.id == show_id).first()
    # show = db.execute(f"SELECT FROM shows WHERE id = {show_id}").first()

    if not show:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Show with id: {show_id} was not found."
        )
    
    show_stories = db.execute(text(f"SELECT * FROM stories WHERE show_id = {show_id}")).all()

    return show_stories

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowModel)
def create_a_show(
        show: schemas.ShowCreate,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    new_show = models.Show(
        created_by=current_user.username,
        **show.dict()
    )

    db.add(new_show)
    db.commit()
    db.refresh(new_show)

    return new_show

    
    # print(show_stories)
    
@router.put('/{show_id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowModel)
def update_a_show(
        show_id: int,
        show: schemas.ShowCreate,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    show_to_update = db.query(models.Show).filter(models.Show.id == show_id).first()

    if not show_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Show with id: {show_id} was not found."
        )

    show_to_update.last_modified_by = current_user.username
    show_to_update.title = show.show_name

    db.commit()
    db.refresh(show_to_update)

    return show_to_update


@router.delete('/{show_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_a_show(
        show_id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    show_to_delete = db.query(models.Show).filter(models.Show.id == show_id).first()

    if not show_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Show with id: {show_id} was not found."
        )

    db.delete(show_to_delete)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
