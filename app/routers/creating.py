from fastapi import APIRouter, HTTPException
from ..dependencies import sign_data, get_id, get_admin, get_timestamp
from ..models.user import User

router = APIRouter()

@router.post("/token")
def get_token(user: User):
    if not check_password(user.email, user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    id = get_id(user.email)
    admin = get_admin(id)

    data = {"sub": id, "admin": admin, "exp": get_timestamp(7), "iat": get_timestamp()}
    return sign_data(data)

# TODO
def check_password(email: str, password: str):
    return True
