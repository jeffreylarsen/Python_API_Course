from fastapi import Response, status, HTTPException, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models, schemas, Oauth2
from typing import List, Optional

from ..database import get_db

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

#import Portfolio_Website index.


@router.get("/")
async def get():
    return {"message": "Hello World"}



#hello