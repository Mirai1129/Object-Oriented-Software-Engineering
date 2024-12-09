from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "User"

    account = Column(String(50), primary_key=True)
    password = Column(String(255), nullable=False)
    role = Column(Integer, nullable=False)

    students = relationship("Student", back_populates="user")
    teachers = relationship("Teacher", back_populates="user")
