from pydantic import BaseModel
from typing import Optional

class Competitionpy(BaseModel):
    name : Optional[str]
    url : Optional[str]

class CompetitionCreate(Competitionpy):
    pass

class CompetitionPy(Competitionpy):
    id: int
    owner_id : int

    class Config:
        orm_mode = True


class CompetitionUpdate(BaseModel):
    name : Optional[str] = None
    url : Optional[str] = None
