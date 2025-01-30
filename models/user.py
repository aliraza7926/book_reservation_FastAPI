from sqlalchemy import Column, Integer, Text, Enum
from sqlalchemy.orm import relationship
from models.base import Base
from models.enums import UserRole
from models.customer import Customer ## a fix for sqlalachemy mapper TODO:find a beter soultion later
class User(Base):
    __tablename__ = 'user'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    phone = Column(Text, unique=True, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    
    # Relationships
    author_profile = relationship("Author", back_populates="user", uselist=False)
    customer_profile = relationship("Customer", back_populates="user", uselist=False)
