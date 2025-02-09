from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import time
from sqlalchemy.exc import OperationalError

load_dotenv()

MYSQL_URL = os.getenv("MYSQL_URL", "mysql://root:root@localhost/bookmarks")
MAX_RETRIES = 5
RETRY_DELAY = 5

def create_db_engine():
    retries = 0
    while retries < MAX_RETRIES:
        try:
            engine = create_engine(MYSQL_URL)
            # Verify the connection
            engine.connect()
            print("Database connection successful!")
            return engine
        except OperationalError as e:
            if retries < MAX_RETRIES - 1:
                retries += 1
                print(f"Database connection attempt {retries} failed. Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print("Failed to connect to the database after multiple attempts.")
                raise e

engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
