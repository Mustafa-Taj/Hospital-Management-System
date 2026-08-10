from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Local PostgreSQL connection string
DATABASE_URL = "sqlite:///./hospital.db"
# SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# Session setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Model
Base = declarative_base()

# DB Dependency function for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()