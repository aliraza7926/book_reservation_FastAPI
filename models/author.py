from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.association_tables import book_author

class Author(Base):
    __tablename__ = 'author'
    
    user_id = Column(Integer, ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    city_id = Column(Integer, ForeignKey('city.city_id', ondelete='SET NULL'))
    goodreads_link = Column(Text)
    bank_account = Column(Text)
    
    # Relationships
    user = relationship("User", back_populates="author_profile")
    books = relationship("Book", secondary=book_author, back_populates="authors")
