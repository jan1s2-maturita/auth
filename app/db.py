from .models.db_connect import Database
from .config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT)
