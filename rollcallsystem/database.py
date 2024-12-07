import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv(override=True)

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("ROLLCALL_DATABASE")

logger.info(f"Database Connection Details:")
logger.info(f"Username: {USERNAME}")
logger.info(f"Host: {HOST}")
logger.info(f"Port: {PORT}")
logger.info(f"Database: {DATABASE}")


def get_database_url():
    return f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"


try:
    url = get_database_url()
    engine = create_engine(url, echo=True)

    with engine.connect() as connection:
        logger.info("Database connection succeed")

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()

except Exception as e:
    logger.error(f"database connection is failed: {e}")
    raise


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
