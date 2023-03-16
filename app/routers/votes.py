from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, Oauth2
from typing import List
from ..database import get_db

router = APIRouter(
     prefix="/votes",
     tags=["Votes"]
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(
        vote: schemas.Vote,
        db: Session = Depends(get_db),
        current_user: int = Depends(Oauth2.get_current_user)
    ):

    vote_query = db \
                .query(models.Vote) \
                .filter(
                    models.Vote.post_id == vote.post_id,
                    models.Vote.user_id == current_user.id
                )
    
    found_vote = vote_query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.id} has already voted on post: {vote.post_id}"
            )
        new_vote = models.Vote(post_id = vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"status": "Successfully added vote!"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote does not exist."
            )
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"status": "Successfully removed vote!"}

    # post = db.query(models.Votes).filter(models.Votes.post_id == vote.post_id).first()

    # if not post:
    #     raise HTTPException(
    #     status_code=status.HTTP_404_NOT_FOUND, 
    #     detail=f"Post: {vote.post_id} not found."
    #     )
        
    # vote_query = db \
    #     .query(models.Votes) \
    #     .filter(
    #         models.Votes.post_id == vote.post_id,
    #         models.Votes.user_id == current_user.id
    #     )
    
    # print(vote_query)
        
    # found_vote = vote_query.first()

    # print(found_vote)

    # if vote.dir == 1:
    #     if vote_query.first() != None:
    #         raise HTTPException(
    #             status_code=status.HTTP_208_ALREADY_REPORTED,
    #             detail=f"User: {current_user.id} has already voted on post: {vote.post_id}"
    #         )
    #     new_vote = models.Votes(post_id = vote.post_id, user_id = current_user.id)
    #     db.add(new_vote)
    #     db.commit()
    #     return {"status": "Successfully added vote!"}
    # else:
    #     #The code here to handle nonexisting votes, worked temporarilly
    #     #It is not working now for some reason.

    #     if vote_query.first() == None:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND, 
    #             detail=f"Post: {vote.post_id} not found."
    #         )

    #     vote_query.delete(synchronize_session=False)
    #     db.commit()
    #     return {"status": "Successfully removed vote!"}