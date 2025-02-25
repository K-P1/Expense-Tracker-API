# app/database.py
from sqlalchemy import create_engine, MetaData
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
#sqlalchemy.orm.declarative_base()
# Database URL (SQLite file named `database.db`)
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Create an engine for SQLite with check_same_thread set to False
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal class instance to create session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
metadata = MetaData()
