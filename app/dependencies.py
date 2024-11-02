import jwt
from .config import private_key
from datetime import datetime, timedelta
import math

# TODO
def get_id(email: str) -> int:
    return 1

# TODO
def get_admin(id: int) -> bool:
    return True

def sign_data(data):
    return jwt.encode(data, private_key, algorithm='RS256')

def get_timestamp(days: int = 0) -> int:
    return math.floor(datetime.timestamp(datetime.now() + timedelta(days=days)))

