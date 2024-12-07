from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean, DateTime, String
from sqlalchemy.orm import relationship

from ..database import Base


class AttendanceRecord(Base):
    __tablename__ = 'AttendanceRecord'

    record_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('Course.course_id'))
    student_id = Column(String, ForeignKey('Student.id'))
    attendance_date = Column(Date)
    attendance_status = Column(Boolean)
    modified_time = Column(DateTime)

    student = relationship("Student", back_populates="attendance_records")
    course = relationship("Course", back_populates="attendance_records")

    def update_attendance_status(self, attendance_status: bool):
        """
        update attendance status

        Args:
            attendance_status (bool): new status
        """
        self.attendance_status = attendance_status
