from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base import Base

book_author = Table(
    'book_author',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('book.book_id', ondelete='CASCADE'), primary_key=True),
    Column('author_id', Integer, ForeignKey('author.user_id', ondelete='CASCADE'), primary_key=True)
)
