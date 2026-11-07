import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load variables from .env file into enviroment
load_dotenv()

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "051022")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5433")
DB_NAME = os.getenv("DB_NAME", "etl_db")

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def get_db_engine():
    """Creates and returns a SQLAlchemy engine for PostgreSQL."""
    return create_engine(DATABASE_URL)