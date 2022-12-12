from fastapi import FastAPI
from app.user.routes import router as userRouter
from app.competition.routes import router as competitionRouter
from app.entry.routes import router as entryRouter

# from demo_backend.Models import user, competition, entry
# from fastapi.middleware.cors import CORSMiddleware


# app.user.Base.metadata.create_all(bind=engine)
# competition.Base.metadata.create_all(bind=engine)
# entry.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
def news_scraper_home():
    return {"Welcome to": "postgres with fastapi"}


app.include_router(userRouter, tags=["user"], prefix="/user")
app.include_router(competitionRouter, tags=["competition"], prefix="/competition")
app.include_router(entryRouter, tags=["entry"], prefix="/entry")