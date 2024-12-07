from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from ..database import Base


class CourseEnrollment(Base):
    __tablename__ = 'CourseEnrollment'

    id = Column(Integer, primary_key=True)
    course_id = Column(String, ForeignKey('Course.course_id'))
    student_id = Column(String, ForeignKey('Student.id'))
    semester = Column(String)

    student = relationship("Student", back_populates="course_enrollments")
    course = relationship("Course", back_populates="course_enrollments")
