from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from ..database import Base


class Department(Base):
    __tablename__ = 'Department'

    dept_num = Column(String(20), primary_key=True)
    dept_name = Column(String(100), nullable=False)

    # Relationship
    students = relationship("Student", back_populates="department")
