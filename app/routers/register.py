from ..db import db
from ..models.request import UserRegister
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/register")
def register(user: UserRegister):
    db.add_user(email=user.email, password=user.password, username=user.username)
    return {"message": "User created"}

