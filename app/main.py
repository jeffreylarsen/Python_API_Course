from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, posts, users, votes, shows, stories, threeDeffect, portfolio

app = FastAPI()


origins = ["*"]

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
app.include_router(threeDeffect.router)
app.include_router(portfolio.router)

# @app.get('/')
# def root():
#     return {"hello":"Hello, Internet!!"}



from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app.mount("/static", StaticFiles(directory="app/Portfolio_Website/images"), name="static")

templates = Jinja2Templates(directory="app/Portfolio_Website")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

