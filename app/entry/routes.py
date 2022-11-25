from fastapi import APIRouter, status, HTTPException
from db_base.database import SessionLocal
from app.entry.schemas import Entrypy
from app.entry.models import Entry
import datetime

router = APIRouter()
db = SessionLocal()

@router.get('/entries', status_code=200)
def get_all_entries():
    entries = db.query(Entry).all()
    
    return {"data": entries, "status": 200, "message": "Registration get successfully"}

@router.get('/entries/{entry_id}', status_code=status.HTTP_200_OK)
def get_an_entry(entry_id: int):
    entry = db.query(Entry).filter(Entry.id == entry_id).first()
    
    return {"data": entry, "status": 200, "message": "Registration retrive successfully"}

@router.post('/entries', status_code=status.HTTP_201_CREATED)
def create_entry(payload: Entrypy):
    
    db_entry = db.query(Entry).filter(Entry.name == payload.name).first()
    
    if db_entry is not None:
        raise HTTPException(status_code=400, detail="Registration already exists")
    
    new_entry = Entry(
        name=payload.name,
        created_at = datetime.datetime.now(),
        # owner2_id = payload.id,
        is_delete = False   
    )
    
    db.add(new_entry)
    db.commit()
    
    return {"status": 200, "message": "Registration added successfully"}

@router.put('/entries/{entry_id}', status_code=status.HTTP_200_OK)
def update_an_entry(entry_id: int, entry: Entrypy):
    
    entry_to_update = db.query(Entry).filter(Entry.id == entry_id).first()
    
    entry_to_update.updated_at = datetime.datetime.now()
    
    if entry.name != None:
        entry_to_update.name = entry.name
    
    db.commit()
    
    return {"status": 200, "message": "Registration update successfully"}

@router.delete('/entry/{entry_id}')
def delete_entry(entry_id: int):
    entry_to_delete = db.query(Entry).filter(Entry.id == entry_id).first()
    
    if entry_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registration delete successfully")        

    db.delete(entry_to_delete)
    db.commit()

    return {"data": entry_to_delete, "status": 200, "message": "Registration delete successfully"}        
 