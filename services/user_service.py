from sqlalchemy.orm import Session
from schemas.user import UserCreate
from models.user import User
from fastapi import HTTPException,status

# TODO: Add more validation using sqlalachemy
# TODO: Add password hashing
class UserService:
    def __init__(self,db:Session):
        self.db=db
        
    
    def create_user(self,user_info:UserCreate):
        existing_email=self.db.query(User).filter(User.email==user_info.email).first()
        if existing_email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"A user with this email: {user_info.email} exist")
        
        existing_username=self.db.query(User).filter(User.username==user_info.username).first()
        if existing_username:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"A user with this username: {user_info.username} exist")
        
        existing_Phone=self.db.query(User).filter(User.phone==user_info.phone).first()
        if existing_Phone:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"A user with this phone number: {user_info.phone} exist")
        
        db_user=User(**user_info.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
        
        