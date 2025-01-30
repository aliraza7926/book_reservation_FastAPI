from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from models.base import Base
from models.enums import SubscriptionTier
from models.reservation import Reservation ## a fix for sqlalachemy mapper TODO:find a beter soultion later
class Customer(Base):
    __tablename__ = 'customer'
    
    user_id = Column(Integer, ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    subscription_model = Column(Enum(SubscriptionTier),nullable=False)
    subscription_end = Column(DateTime)
    wallet_amount = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User", back_populates="customer_profile")
    reservations = relationship("Reservation", back_populates="customer")
