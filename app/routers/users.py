from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, Oauth2
from typing import List
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserRepsonse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.email == user.email, models.User.username == user.username)
    existing_user = user_query.first()

    if existing_user == None:
            user.password = utils.hash(user.password)
            new_user = models.User(**user.dict())

            db.add(new_user)
            db.commit()
            db.refresh(new_user)
    else:
        return Response(status_code=status.HTTP_418_IM_A_TEAPOT)

    return new_user
    
@router.get('/', response_model=List[schemas.UserRepsonse])
def get_users(db: Session = Depends(get_db)):

    users = db.query(models.User).all()
    print(db.query(models.User))
    return users

@router.get('/{id}', response_model=schemas.UserRepsonse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    print(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} not found."
        )
    return user
