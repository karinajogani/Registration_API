from pydantic import BaseModel

"""create schema for User signup"""
class Usersauth(BaseModel):
    id: int
    name: str
    password: str

"""create schema for signup response"""
class Displayuser(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

"""create schema for User login"""
class Userinfo(BaseModel):
    name: str
    password: str

    class Config:
        orm_mode = True
