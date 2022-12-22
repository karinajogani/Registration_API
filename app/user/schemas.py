from pydantic import BaseModel
from typing import Optional, List
# from competition.schemas import CompetitionPy


class Userpy(BaseModel):
    """create schema for User Table

    Args:
        BaseModel (_type_): _description_
    """
    name : Optional[str]
    date_of_birth : Optional[str]
    gender : Optional[str]
    mail : Optional[str]

# class UserCreate(Userpy):
#     password: str

class User(Userpy):
    # id: int
    is_active: bool
    # competitions: List[CompetitionPy]

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    """create schema for update in User Table

    Args:
        BaseModel (_type_): _description_
    """
    name : Optional[str] = None
    date_of_birth : Optional[str] = None
    gender : Optional[str] = None
    mail : Optional[str] = None
