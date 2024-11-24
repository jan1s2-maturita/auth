from .models.db import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from bcrypt import hashpw, gensalt
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT
# database connection class - postgres
class Database:
    def __init__(self):
        self.engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
    def get_user_by_id(self, user_id):
        session = self.get_session()
        user = session.query(User).filter_by(id=user_id).first()
        session.close()
        return user
    def add_user(self, username, password, email):
        session = self.get_session()
        user = User(username=username, password=hashpw(password.encode('utf-8'), gensalt()), email=email)
        session.add(user)
        session.commit()
        session.close()
        return user
    def get_user_by_username(self, username) -> User:
        session = self.get_session()
        user = session.query(User).filter_by(username=username).first()
        session.close()
        return user
    def get_user_by_creds(self, username, password) -> User|None:
        session = self.get_session()
        user = session.query(User).filter_by(username=username).first()
        if user and user.verify_password(password):
            return user
        return None

def init_engine():
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    User.metadata.create_all(engine)
    return engine
def get_session():
    engine = init_engine()
    Session = sessionmaker(bind=engine)
    return Session()

def get_user_by_id(user_id):
    session = get_session()
    user = session.query(User).filter_by(id=user_id).first()
    session.close()
    return user

def add_user(username, password):
    session = get_session()
    user = User(username=username, password=hashpw(password.encode('utf-8'), gensalt()))
    session.add(user)
    session.commit()
    session.close()
    return user
def get_user_by_username(username) -> User:
    session = get_session()
    user = session.query(User).filter_by(username=username).first()
    session.close()
    return user
db = Database()
