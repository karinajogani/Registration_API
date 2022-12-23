from pydantic import BaseModel
from typing import Optional

"""create schema for Entry Table"""
class Entrypy(BaseModel):
    name : Optional[str]
    competition_id : str

    class Config:
        orm_mode = True

"""create schema for update in Entry Table"""
class EntryUpdate(BaseModel):
    name : Optional[str] = None
