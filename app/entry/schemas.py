from pydantic import BaseModel
from typing import Optional

class Entrypy(BaseModel):
    name : Optional[str]
    competition_id : str

    class Config:
        orm_mode = True

class EntryUpdate(BaseModel):
    name : Optional[str] = None
