from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import auth, posts, users, votes, shows, stories, websocket, threeDeffect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request


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
app.include_router(shows.router)
app.include_router(stories.router)
app.include_router(websocket.router)
app.include_router(threeDeffect.router)

@app.get('/')
def root():
    return {"hello":"Hello, Internet!!"}

templates = Jinja2Templates(directory="../Portfolio_Website")
app.mount("/", StaticFiles(directory="../Portfolio_Website"))

@app.get('/hello')
def serve_home(request: Request):
    return templates.TemplateResponse("index.html", context= {"request": request}) 