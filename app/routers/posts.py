
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models, schemas, Oauth2
from typing import List, Optional
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get('/', response_model=List[schemas.PostModel])
def get_my_posts(
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    posts = db.query(models.Post).filter(models.User.id == current_user.id).all()

    return posts


@router.get('/all', response_model=List[schemas.PostVotesModel])
def get_all_posts(
        db: Session = Depends(get_db),
        # current_user: int = Depends(Oauth2.get_current_user),
        limit: int = 50,
        offset: int = 0,
        search: str = ""
    ):

    # posts = db \
    #         .query(models.Post) \
    #         .filter(
    #             # (models.Post.published == True and
    #             # models.owner == current_user.id) or
    #             models.Post.title.contains(search)
    #         ) \
    #         .limit(limit) \
    #         .offset(offset) \
    #         .all()
    
    posts = db \
            .query(models.Post, func.count(models.Vote.post_id).label("votes")) \
            .join(
                models.Vote, 
                models.Vote.post_id == models.Post.id,
                isouter=True
            ) \
            .group_by(models.Post.id) \
            .filter(
                # (models.Post.published == True and
                # models.User == current_user.id) or
                models.Post.title.contains(search)
            ) \
            .limit(limit) \
            .offset(offset) \
            .all()


    return posts

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PostModel)
def create_post(
        post: schemas.PostCreate, 
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    new_post = models.Post(owner_id=current_user.id, **post.dict())
    print(models.Post(owner_id=current_user.id, **post.dict()))
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get('/{id}', response_model=schemas.PostVotesModel)
def get_post(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    post = db \
            .query(models.Post, func.count(models.Vote.post_id).label("votes")) \
            .join(
                models.Vote, 
                models.Vote.post_id == models.Post.id,
                isouter=True
            ) \
            .group_by(models.Post.id) \
            .filter(models.Post.id == id) \
            .first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found."
        )
    
    return post

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found."
        )
    
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to delete another users' post."
        )
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}', response_model=schemas.PostModel)
def update_post(
        id: int,
        updated_post: schemas.PostCreate,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found."
        )
    
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to update another users' post."
        )

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
