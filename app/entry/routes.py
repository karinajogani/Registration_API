from fastapi import APIRouter, status, HTTPException
from db_base.database import SessionLocal
from app.entry.schemas import Entrypy, EntryUpdate
from app.entry.models import Entry
import datetime

router = APIRouter()
db = SessionLocal()

@router.get('/entries', status_code=200)
def get_all_entries():
    """ get method for getting the all entries

    Returns:
        _type_: _description_
    """
    entries = db.query(Entry).all()

    return {"data": entries, "status": 200, "message": "Registration get successfully"}

@router.get('/entries/{entry_id}', status_code=status.HTTP_200_OK)
def get_an_entry(entry_id: str):
    """ get method for getting the particular 1 entry by id

    Args:
        entry_id (str): _description_

    Returns:
        _type_: _description_
    """
    entry = db.query(Entry).filter(Entry.id == entry_id).first()

    return {"data": entry, "status": 200, "message": "Registration retrive successfully"}

@router.post('/entries', status_code=status.HTTP_201_CREATED)
def create_entry(payload: Entrypy):
    """ post method for create entries

    Args:
        payload (Entrypy): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
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

@router.put('/entries/{entry_id}', status_code=status.HTTP_200_OK)
def update_an_entry(entry_id: str, entry: EntryUpdate):
    """put method for update an entry

    Args:
        entry_id (str): _description_
        entry (EntryUpdate): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
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

@router.delete('/entry/{entry_id}')
def delete_entry(entry_id: str):
    """delete method for delete the entry

    Args:
        entry_id (str): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    entry_to_delete = db.query(Entry).filter(Entry.id == entry_id).first()

    if entry_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registration delete successfully")

    db.delete(entry_to_delete)
    db.commit()

    return {"data": entry_to_delete, "status": 200, "message": "Registration delete successfully"}
