from fastapi import APIRouter, HTTPException
from ..dependencies import sign_data, get_timestamp
from ..models.db import User
from bcrypt import checkpw, gensalt, hashpw
from ..db import db
from ..models.request import UserLogin

router = APIRouter()

@router.post("/login")
def get_token(userLogin: UserLogin):
    user = db.get_user_by_creds(userLogin.username, userLogin.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    id = user.get_id()
    admin = user.get_is_admin()

    data = {"sub": id, "admin": admin, "exp": get_timestamp(7), "iat": get_timestamp()}
    return sign_data(data)
