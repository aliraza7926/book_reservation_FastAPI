from sqlalchemy import create_engine
from core import config


# Create an engine using the connection string from config.py
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
