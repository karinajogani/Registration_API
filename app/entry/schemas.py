from pydantic import BaseModel
from typing import Optional

class Entrypy(BaseModel):
    """create schema for Entry Table

    Args:
        BaseModel (_type_): _description_
    """
    name : Optional[str]
    competition_id : str

    class Config:
        orm_mode = True

class EntryUpdate(BaseModel):
    """create schema for update in Entry Table

    Args:
        BaseModel (_type_): _description_
    """
    name : Optional[str] = None
