from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class AttendanceRecord(Base):
    __tablename__ = 'AttendanceRecord'

    record_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('Course.id'))
    student_id = Column(Integer, ForeignKey('Student.id'))
    attendance_date = Column(Date)
    attendance_status = Column(Boolean)
    modified_time = Column(DateTime)

    # add relationship with other object
    student = relationship("Student", back_populates="attendance_records")
    course = relationship("Course", back_populates="attendance_records")

    def update_attendance_status(self, attendance_status: bool):
        """
        更新出席狀態

        Args:
            attendance_status (bool): 新的出席狀態
        """
        self.attendance_status = attendance_status
