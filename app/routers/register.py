from ..db import db
from ..models.request import UserRegister
from fastapi import APIRouter, HTTPException
import re
router = APIRouter()

@router.post("/register")
def register(user: UserRegister):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user.email):
        raise HTTPException(status_code=400, detail="Invalid email")
    if len(user.password) < 4:
        raise HTTPException(status_code=400, detail="Password too short")
    db.add_user(email=user.email, password=user.password, username=user.username)
    return {"message": "User created"}

