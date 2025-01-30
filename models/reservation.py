from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.base import Base

class Reservation(Base):
    __tablename__ = 'reservation'
    
    reservation_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.user_id', ondelete='CASCADE'))
    book_id = Column(Integer, ForeignKey('book.book_id', ondelete='CASCADE'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)  # Admin can update this
    price = Column(Integer, nullable=False)
    
    # Relationships
    customer = relationship("Customer", back_populates="reservations")
    book = relationship("Book", back_populates="reservations")
