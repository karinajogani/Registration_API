from pydantic import BaseModel
from typing import Optional

class Entrypy(BaseModel):
    name : Optional[str]
    # id : int
    # owner2_id : int
    
    class Config:
        orm_mode = True
        
class EntryUpdate(BaseModel):
    name : Optional[str] = None