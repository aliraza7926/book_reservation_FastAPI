from pydantic import BaseModel,EmailStr,Field
from models.enums import UserRole

# TODO: Add more validation using pydantic

class UserBase(BaseModel):
    username:str
    first_name:str
    last_name:str
    phone:str
    email:EmailStr
    role:UserRole=UserRole.CUSTOMER

class UserCreate(UserBase):
    password_hash:str
    

class User(UserBase):
    user_id:int

    class Config:
        from_attributes = True
    