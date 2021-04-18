from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    email = Column(String, unique=True, index=True)
    phonenumber = Column(String, unique=True, index=True)
    premium = Column(Boolean, default=False)
    token = Column(String)
    
    contacts = relationship("Contact", back_populates="owner")
    
class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phonenumber = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="contacts")