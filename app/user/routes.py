from fastapi import APIRouter, Depends, status, HTTPException
from app.user.schemas import Userpy, UserUpdate
from app.user.models import User
import datetime
from db_base.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

"""get method for getting the all users"""
@router.get('/users/', status_code=200)
def get_all_users(db: Session = Depends(get_db)):

    user = db.query(User).all()

    return {"data": user, "status": 200, "message": "Registration get successfully"}

"""get method for getting particular 1 user by id"""
@router.get('/users/{user_id}', status_code=status.HTTP_200_OK)
def get_an_user(user_id: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    return {"data": user, "status": 200, "message": "Registration retrive successfully"}

"""post method for create user"""
@router.post('/users/', status_code=status.HTTP_201_CREATED)
def create_user(payload: Userpy, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.name == payload.name).first()

    if db_user is not None:
        raise HTTPException(status_code=400, detail="Registration already exists")

    new_user = User(
        name=payload.name,
        date_of_birth = payload.date_of_birth,
        gender = payload.gender,
        mail = payload.mail,
        created_at = datetime.datetime.now(),
        is_delete = False
    )

    db.add(new_user)
    db.commit()

    return {"status": 200, "message": "Registration added successfully"}

"""patch method for update user"""
@router.patch('/users/{user_id}', status_code=status.HTTP_201_CREATED)
def update_an_user(user_id: str, user: UserUpdate, db: Session = Depends(get_db)):

    user_obj = db.query(User).filter(User.id == user_id).first()

    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # data_to_update = user.dict(exclude_unset=True)

    # user_obj.update(data_to_update)

    user_obj.updated_at = datetime.datetime.now()

    data_to_update = user.dict(exclude_unset=True)
    for key, value in data_to_update.items():
        setattr(user_obj, key, value)

    db.commit()
    return {"status": 200, "message": "Registration update successfully"}

    # if user.name != None:
    #     user_update.name = user.name

    # if user.date_of_birth != None:
    #     user_update.date_of_birth = user.date_of_birth

    # if user.gender != None:
    #     user_update.gender = user.gender

    # if user.mail != None:
    #     user_update.mail = user.mail

    # db.commit()

    # return {"status": 200, "message": "Registration update successfully"}

"""delete method for delete the user"""
@router.delete('/user/{user_id}')
def delete_user(user_id: str, db: Session = Depends(get_db)):

    user_delete = db.query(User).filter(User.id == user_id).first()

    if user_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registration delete successfully")

    db.delete(user_delete)
    db.commit()

    return {"data": user_delete, "status": 200, "message": "Registration delete successfully"}
