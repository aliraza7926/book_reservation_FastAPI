from sqlalchemy.orm import Session
from schemas.user import UserCreate
from models.user import User

# TODO: Add more validation using sqlalachemy
# TODO: Add error handling for duplicate email,username,phone
# TODO: Add password hashing
class UserService:
    def __init__(self,db:Session):
        self.db=db
        
    
    def create_user(self,user_info:UserCreate):
        db_user=User(**user_info.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
        
        