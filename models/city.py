from sqlalchemy import Column, Integer, Text
from models.base import Base

class City(Base):
    __tablename__ = 'city'
    
    city_id = Column(Integer, primary_key=True)
    city_name = Column(Text, unique=True, nullable=False)
