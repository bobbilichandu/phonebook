from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_phonenumber(db: Session, phonenumber: str):
    return db.query(models.User).filter(models.User.phonenumber == phonenumber).first()

def create_user(db: Session, user:schemas.UserCreate):
    token = hash(user.email + user.phonenumber)
    db_user = models.User(email=user.email, phonenumber=user.phonenumber, name=user.name, token=token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_contacts(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).filter(models.User.id == user_id).offset(skip).limit(limit).all()

def create_user_contact(db: Session, contact: schemas.ContactCreate, user_id: int):
    db_item = models.Contact(**contact.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item