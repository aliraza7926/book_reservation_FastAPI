from sqlalchemy.orm import Session
from schemas.customer import Customer as CustomerSchema
from models.customer import Customer

class CustomerService:
    def __init__(self,db:Session):
        self.db=db
        
    
    def create_customer(self,customer:CustomerSchema):
        db_customer=Customer(**customer.model_dump())
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer
        