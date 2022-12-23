from fastapi import APIRouter, Depends, status, HTTPException
from app.entry.schemas import Entrypy, EntryUpdate
from app.entry.models import Entry
import datetime
from db_base.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

""" get method for getting the all entries"""
@router.get('/entries', status_code=200)
def get_all_entries(db: Session = Depends(get_db)):

    entries = db.query(Entry).all()

    return {"data": entries, "status": 200, "message": "Registration get successfully"}

""" get method for getting the particular 1 entry by id"""
@router.get('/entries/{entry_id}', status_code=status.HTTP_200_OK)
def get_an_entry(entry_id: str, db: Session = Depends(get_db)):

    entry = db.query(Entry).filter(Entry.id == entry_id).first()

    return {"data": entry, "status": 200, "message": "Registration retrive successfully"}

""" post method for create entries"""
@router.post('/entries', status_code=status.HTTP_201_CREATED)
def create_entry(payload: Entrypy, db: Session = Depends(get_db)):

    db_entry = db.query(Entry).filter(Entry.name == payload.name).first()

    if db_entry is not None:
        raise HTTPException(status_code=400, detail="Registration already exists")

    new_entry = Entry(
        name=payload.name,
        created_at = datetime.datetime.now(),
        competition_id = payload.competition_id,
        is_delete = False
    )

    db.add(new_entry)
    db.commit()

    return {"status": 200, "message": "Registration added successfully"}

"""put method for update an entry"""
@router.put('/entries/{entry_id}', status_code=status.HTTP_200_OK)
def update_an_entry(entry_id: str, entry: EntryUpdate, db: Session = Depends(get_db)):

    entry_to_update = db.query(Entry).filter(Entry.id == entry_id).first()

    if not entry_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    entry_to_update.updated_at = datetime.datetime.now()
    entry_update = entry.dict(exclude_unset=True)
    for key, value in entry_update.items():
        setattr(entry_to_update, key, value)

    db.commit()
    return {"status": 200, "message": "Registration update successfully"}
    # if entry.name != None:
    #     entry_to_update.name = entry.name
    # db.commit()
    # return {"status": 200, "message": "Registration update successfully"}

"""delete method for delete the entry"""
@router.delete('/entry/{entry_id}')
def delete_entry(entry_id: str, db: Session = Depends(get_db)):

    entry_to_delete = db.query(Entry).filter(Entry.id == entry_id).first()

    if entry_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registration delete successfully")

    db.delete(entry_to_delete)
    db.commit()

    return {"data": entry_to_delete, "status": 200, "message": "Registration delete successfully"}
