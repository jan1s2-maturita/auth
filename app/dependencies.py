import jwt
from .config import PRIVATE_KEY_PATH
from datetime import datetime, timedelta
import math


def sign_data(data):
    with open(PRIVATE_KEY_PATH, "rb") as private_key_file:
        private_key = private_key_file.read()
        return jwt.encode(data, private_key, algorithm='RS256')

def get_timestamp(days: int = 0) -> int:
    return math.floor(datetime.timestamp(datetime.now() + timedelta(days=days)))

