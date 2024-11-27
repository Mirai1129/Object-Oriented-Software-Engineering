import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# initialize
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("ROLLCALL_DATABASE")


def get_database_url():
    return f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"


# 創建引擎
url = get_database_url()
engine = create_engine(url)  # Only needed for SQLite

# 創建本地會話
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基礎模型
Base = declarative_base()


# 依賴注入：獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
