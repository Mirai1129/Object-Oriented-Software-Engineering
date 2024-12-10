from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import relationship

from ..database import Base


class Course(Base):
    __tablename__ = "Course"
    course_id = Column(String, primary_key=True)
    teacher_id = Column(String, ForeignKey("Teacher.id"), nullable=False)
    name = Column(String, nullable=False)
    academic_year = Column(String, nullable=False)
    is_rollcall_opened = Column(TINYINT, nullable=False, default=False)

    attendance_records = relationship("AttendanceRecord", back_populates="course")
    course_enrollments = relationship("CourseEnrollment", back_populates="course")
