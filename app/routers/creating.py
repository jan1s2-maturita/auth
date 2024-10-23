from fastapi import APIRouter, HTTPException


def get_token(email: str, password: str):
