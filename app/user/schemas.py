from pydantic import BaseModel
from typing import Optional, List
# from competition.schemas import CompetitionPy


class Userpy(BaseModel):
    name : Optional[str]
    date_of_birth : Optional[str]
    gender : Optional[str]
    mail : Optional[str]
    
# class UserCreate(Userpy):
#     password: str

class User(Userpy):
    id: int
    is_active: bool
    # competitions: List[CompetitionPy]
    
    class Config:
        orm_mode = True
        
class UserUpdate(BaseModel):
    # name : Optional[str] = None
    # date_of_birth : Optional[str] = None
    # gender : Optional[str] = None
    # mail : Optional[str] = None
    
    def update(self):
        self.name : Optional[str] = None
        self.date_of_birth : Optional[str] = None
        self.gender : Optional[str] = None
        self.mail : Optional[str] = None
        # for key, value in UserUpdate.items():
        #     setattr(self, key, value)
        
obj=UserUpdate()
