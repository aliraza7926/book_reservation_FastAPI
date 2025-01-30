from pydantic import BaseModel
from schemas.user import User
from schemas.customer import Customer

class SignUp(BaseModel):
    user:User
    customer:Customer
    