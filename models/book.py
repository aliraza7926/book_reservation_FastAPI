from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.association_tables import book_author

class Book(Base):
    __tablename__ = 'book'
    
    book_id = Column(Integer, primary_key=True)
    isbn = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.genre_id'))
    description = Column(Text)
    units = Column(Integer, default=0)
    
    # Relationships
    genre = relationship("Genre")
    authors = relationship("Author", secondary=book_author, back_populates="books")
    reservations = relationship("Reservation", back_populates="book")
