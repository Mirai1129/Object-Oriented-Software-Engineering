from sqlalchemy import Column, ForeignKey, Float, Date, String, DateTime, Integer
from sqlalchemy.orm import relationship

from ..database import Base


class ParticipationGrade(Base):
    __tablename__ = 'ParticipationGrade'

    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String(20), ForeignKey('Course.course_id'), nullable=False)
    student_id = Column(String(20), ForeignKey('Student.id'), nullable=False)
    grade = Column(Float, nullable=False)
    generated_date = Column(Date, nullable=False)
    modified_time = Column(DateTime, nullable=False)

    course = relationship("Course", back_populates="participation_grades")
    student = relationship("Student", back_populates="participation_grades")
