from .models.db import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from bcrypt import hashpw, gensalt
def init_engine():
    engine = create_engine('sqlite:///db.sqlite')
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
