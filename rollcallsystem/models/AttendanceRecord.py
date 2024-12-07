from sqlalchemy import Column, Integer, ForeignKey, Date, DateTime, String
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship

from ..database import Base


class AttendanceRecord(Base):
    __tablename__ = 'AttendanceRecord'

    record_id = Column(Integer, primary_key=True)
    course_id = Column(String, ForeignKey('Course.course_id'))
    student_id = Column(String, ForeignKey('Student.id'))
    attendance_date = Column(Date, nullable=False)
    attendance_status = Column(TINYINT, nullable=False)
    modified_time = Column(DateTime, nullable=False)

    student = relationship("Student", back_populates="attendance_records")
    course = relationship("Course", back_populates="attendance_records")
