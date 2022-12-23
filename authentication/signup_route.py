from fastapi import APIRouter, Depends, Request
from authentication.schemas import Usersauth, Displayuser
from db_base.database import get_db
from sqlalchemy.orm import Session
from authentication.models import Userauth
from authentication.utils import password_hash, JWTBearer, decodeJWT

router = APIRouter()

"""secure router for total users"""
@router.get("/alluser",dependencies=[Depends(JWTBearer())])
def alluser(request: Request, db:Session = Depends(get_db)):

    access_token = request.headers["Authorization"][7:]
    decoded = decodeJWT(access_token)
    print(decoded)
    db_users = db.query(Userauth).all()

    return db_users


"""user signup by post method"""
@router.post("/user_signup", response_model=Displayuser)
def signupp(resquest: Usersauth, db: Session = Depends(get_db)):

    """convert plain password to hash password"""
    newuser = Userauth(id=resquest.id, name=resquest.name, password=password_hash(resquest.password))
    db.add(newuser)
    db.commit()
    db.refresh(newuser)

    return newuser
