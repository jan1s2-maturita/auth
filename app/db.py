from .models.db_connect import Database
from .config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

db = Database(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT, db_name=DB_NAME)
