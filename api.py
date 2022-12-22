from fastapi import FastAPI
from app.user.routes import router as userRouter
from app.competition.routes import router as competitionRouter
from app.entry.routes import router as entryRouter
# async def method_name():
#     pass

app = FastAPI()

# @app.get("/")
# def news_scraper_home():
#     return {"Welcome to": "postgres with fastapi"}

app.include_router(userRouter, tags=["user"], prefix="/user")
app.include_router(competitionRouter, tags=["competition"], prefix="/competition")
app.include_router(entryRouter, tags=["entry"], prefix="/entry")
