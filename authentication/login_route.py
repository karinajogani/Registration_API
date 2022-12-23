from fastapi import APIRouter, Depends, status, HTTPException
from authentication.schemas import Userinfo
from authentication.models import Userauth
from db_base.database import get_db
from authentication.utils import verify_password, create_access_token, refresh_access_token
from sqlalchemy.orm import Session

router= APIRouter()

"""user login by post method"""
@router.post("/login")
def login_user(request: Userinfo, db: Session = Depends(get_db)):

    """check whether user name is present in database or not"""
    if not db.query(Userauth).filter(Userauth.name == request.name).count():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect name or password",
        )

    else:
        user = db.query(Userauth).filter(Userauth.name == request.name).first()
        user_password = user.password

        """compare login password with hash password"""
        if verify_password(request.password, user_password):
            access_token = create_access_token(user.name)
            refresh_token = refresh_access_token(user.name)

            """returning token"""
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
            }

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect name or password",
            )
