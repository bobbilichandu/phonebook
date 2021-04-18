from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

phonebook = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@phonebook.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = crud.get_user_by_phonenumber(db, phonenumber=user.phonenumber)
    if db_user:
        raise HTTPException(status_code=400, detail="Phone Number already registered")
    return crud.create_user(db=db, user=user)

@phonebook.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@phonebook.get("/users/{user_id}/addcontact/", response_model=schemas.Contact)
def create_contact_for_user(
    user_id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)
):
    return crud.create_user_contact(db=db, contact=contact, user_id=user_id)

@phonebook.get("/users/{user_id}/contacts", response_model=List[schemas.Contact])
def get_contacts_of_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_contacts(db=db, user_id=user_id)