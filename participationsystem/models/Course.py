from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from ..database import Base


class Course(Base):
    __tablename__ = "Course"

    course_id = Column(String(20), primary_key=True)
    teacher_id = Column(String(20), ForeignKey('Teacher.id'), nullable=False)
    name = Column(String(100), nullable=False)
    semester = Column(String(20), nullable=False)

    teacher = relationship("Teacher", back_populates="courses")
    participation_grades = relationship("ParticipationGrade", back_populates="course")
