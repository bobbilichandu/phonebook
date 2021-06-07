import time
from random import randint

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
    token = hash(user.email + user.phonenumber + str(time.time()) + str(randint(0,1000000)))
    db_user = models.User(email=user.email, phonenumber=user.phonenumber, name=user.name, token=token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_contacts(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).filter(models.Contact.owner_id == user_id).offset(skip).limit(limit).all()

def create_user_contact(db: Session, contact: schemas.ContactCreate, user_id: int):
    db_contact = models.Contact(**contact.dict(), owner_id=user_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def contact_check(db: Session, user_id: int, contact_mail: str, contact_phonenumber: str):
    db_contact = db.query(models.Contact).filter(models.Contact.owner_id == user_id).filter(models.Contact.email == contact_mail).filter(models.Contact.phonenumber == contact_phonenumber).first()
    if db_contact is not None:
        return True
    else:
        return False
        

def update_user_email(db: Session, user_id: int, mail: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    db_user.email = mail
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_phonenumber(db: Session, user_id: int, phone_number: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    db_user.phonenumber = phone_number
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    skip = 0
    limit = 100
    try:
        db_contacts = db.query(models.Contact).filter(models.Contact.owner_id == user_id).offset(skip).limit(limit).all()
        for db_contact in db_contacts:
            db.delete(db_contact)
        db.delete(db_user)
        db.commit()
        return True
    except:
        return False
    
def update_contact_email(db: Session, user_id: int, email: str, mail: str):
    db_contact = db.query(models.Contact).filter(models.Contact.owner_id == user_id and models.Contact.email == email).first()
    db_contact.email = mail
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact_phonenumber(db: Session, user_id: int, phonenumber: str, newphonenumber: str):
    db_contact = db.query(models.Contact).filter(models.Contact.owner_id == user_id and models.Contact.phonenumber == phonenumber).first()
    db_contact.phonenumber = newphonenumber
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, user_id: int, contact_param: str):
    db_contact = db.query(models.Contact).filter(models.Contact.owner_id == user_id 
                                                 and (models.Contact.phonenumber == contact_param 
                                                      or models.Contact.email == contact_param)).first()
    if db_contact is None:
        return False
    print(db_contact.email)
    try:
        db.delete(db_contact)
        db.commit()
        return True
    except:
        return False
    
def update_user_premium_status(db: Session, user_id: int):
    try:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if db_user is None:
            return False
        db_user.premium = True
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return True
    except Exception as e:
        print(e)