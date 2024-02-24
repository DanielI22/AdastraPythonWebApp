from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://adastra-user:adastraPass@localhost/adastra-db")

def get_db_engine():
    engine = create_engine(DATABASE_URL)
    return engine