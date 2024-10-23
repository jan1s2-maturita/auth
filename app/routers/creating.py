from fastapi import APIRouter, HTTPException
from .checking import check_password

def get_token(email: str, password: str):
    if not check_password(email, password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
