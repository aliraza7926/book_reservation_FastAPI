from fastapi import APIRouter,Depends
from schemas.user import UserCreate
from schemas.customer import Customer
from schemas.auth import SignUp
from sqlalchemy.orm import Session
from database.session import get_db
from services.user_service import UserService
from services.customer_service import CustomerService

# TODO: Add JWT
# TODO: Add authorization 
# TODO: Add OTP

router=APIRouter()

@router.post("/signup",response_model=SignUp)
def get_user(user_info:UserCreate,db:Session=Depends(get_db)):
    user_service=UserService(db)
    user=user_service.create_user(user_info)
    
    customer_service=CustomerService(db)
    customer=customer_service.create_customer(Customer(user_id=user.user_id))
    
    return SignUp(user=user,customer=customer)
