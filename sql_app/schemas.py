from typing import List, Optional

from pydantic import BaseModel


class ContactBase(BaseModel):
    name: str
    email: str
    phonenumber: str    


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    phonenumber: str


class UserCreate(UserBase):
    pass
    

class User(UserBase):   
    id: int
    token: str
    premium: bool
    
    contacts: List[Contact] = []
    
    class Config:
        orm_mode = True