from pydantic import BaseModel
from typing import Optional, List
# from competition.schemas import CompetitionPy

"""create schema for User Table"""
class Userpy(BaseModel):
    name : Optional[str]
    date_of_birth : Optional[str]
    gender : Optional[str]
    mail : Optional[str]

class User(Userpy):
    # id: int
    is_active: bool
    # competitions: List[CompetitionPy]

    class Config:
        orm_mode = True

"""create schema for update in User Table"""
class UserUpdate(BaseModel):
    name : Optional[str] = None
    date_of_birth : Optional[str] = None
    gender : Optional[str] = None
    mail : Optional[str] = None
