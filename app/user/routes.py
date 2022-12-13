from fastapi import APIRouter, status, HTTPException
from db_base.database import SessionLocal
from app.user.schemas import Userpy, UserUpdate
# from app.user.schemas import UserCreate
from app.user.models import User
import datetime

router = APIRouter()
db = SessionLocal()

@router.get('/users/', status_code=200)
def get_all_users():
    user = db.query(User).all()

    return {"data": user, "status": 200, "message": "Registration get successfully"}

@router.get('/users/{user_id}', status_code=status.HTTP_200_OK)
def get_an_user(user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    return {"data": user, "status": 200, "message": "Registration retrive successfully"}

@router.post('/users/', status_code=status.HTTP_201_CREATED)
def create_user(payload: Userpy):

    db_user = db.query(User).filter(User.name == payload.name).first()

    if db_user is not None:
        raise HTTPException(status_code=400, detail="Registration already exists")

    new_user = User(
        name=payload.name,
        date_of_birth = payload.date_of_birth,
        gender = payload.gender,
        mail = payload.mail,
        created_at = datetime.datetime.now(),
        # password = UserCreate.password + "notreallyhashed",
        is_delete = False
        # password =  payload.password
        # fake_hashed_password = User.password + "notreallyhashed"
    )

    db.add(new_user)
    db.commit()

    return {"status": 200, "message": "Registration added successfully"}

@router.patch('/users/{user_id}', status_code=status.HTTP_201_CREATED)
def update_an_user(user_id: int, user: UserUpdate):
    user_obj = db.query(User).filter(User.id == user_id).first()

    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    data_to_update = user.dict(exclude_unset=True)

    user_obj.update(data_to_update)

    user_obj.updated_at = datetime.datetime.now()

    # data_to_update = user.dict(exclude_unset=True)
    # for key, value in data_to_update.items():
    #     setattr(user_obj, key, value)

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

@router.delete('/user/{user_id}')
def delete_user(user_id: int):
    user_delete = db.query(User).filter(User.id == user_id).first()

    if user_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registration delete successfully")

    db.delete(user_delete)
    db.commit()

    return {"data": user_delete, "status": 200, "message": "Registration delete successfully"}
