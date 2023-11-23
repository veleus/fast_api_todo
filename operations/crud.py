from sqlalchemy.orm import Session
from dto.users import ItemBase
from models.database import User
from dto import users as User_new


def get_db(db: Session, user_id:str):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: User_new.ItemBase):
    exp = User(name=user.user_name)
    db.add(exp)
    db.commit()
    db.refresh(exp)
    return exp


def update_user(db: Session,id: int, user: User_new.ItemBase):
    existing_user = db.query(User).filter(User.id == id).first()
    existing_user.name = user.user_name
    db.commit()
    db.refresh(existing_user)
    return existing_user


def delete_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).delete()

