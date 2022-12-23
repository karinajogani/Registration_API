from fastapi import FastAPI
from app.user.routes import router as userRouter
from app.competition.routes import router as competitionRouter
from app.entry.routes import router as entryRouter
from authentication.signup_route import router as signupRouter
from authentication.login_route import router as loginRouter
# async def method_name():
#     pass

app = FastAPI()

# @app.get("/")
# def news_scraper_home():
#     return {"Welcome to": "postgres with fastapi"}

app.include_router(signupRouter, tags=["signup"], prefix="/signup")
app.include_router(loginRouter, tags=["login"], prefix="/login")
app.include_router(userRouter, tags=["user"], prefix="/user")
app.include_router(competitionRouter, tags=["competition"], prefix="/competition")
app.include_router(entryRouter, tags=["entry"], prefix="/entry")
