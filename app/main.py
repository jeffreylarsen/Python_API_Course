from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import auth, posts, users, votes, websocket, threeDeffect

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://www.google.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(votes.router)
app.include_router(websocket.router)
app.include_router(threeDeffect.router)

@app.get('/')
def root():
    return {"hello":"Hello, Internet!!"}