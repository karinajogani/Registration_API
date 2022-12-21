from pydantic import BaseModel
from typing import Optional

class Competitionpy(BaseModel):
    name : Optional[str]
    url : Optional[str]
    user_id : str

    class Config:
        orm_mode = True

# class CompetitionCreate(Competitionpy):
#     pass

# class CompetitionPy(Competitionpy):
#     # id: str
#     user_id : str


class CompetitionUpdate(BaseModel):
    name : Optional[str] = None
    url : Optional[str] = None
