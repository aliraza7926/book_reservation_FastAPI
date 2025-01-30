from pydantic import BaseModel
from datetime import datetime
from models.enums import SubscriptionTier


class Customer(BaseModel):
    user_id:int
    subscription_model:SubscriptionTier=SubscriptionTier.FREE
    subscription_end:datetime|None=None
    wallet_amount:int=0
    
    class Config:
        from_attributes = True
