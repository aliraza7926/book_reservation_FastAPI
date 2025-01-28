from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core import config


# Create an engine using the connection string from config.py
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)


# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
