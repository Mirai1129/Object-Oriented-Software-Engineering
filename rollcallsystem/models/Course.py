from sqlalchemy import Column, Integer, ForeignKey, String

from .Student import Student
from .Teacher import Teacher
from ..database import Base


class Course(Base):
    __tablename__ = "Course"
    course_id = Column(String, primary_key=True, autoincrement=True)
    teacher_id = Column(String, ForeignKey("Teacher.TeacherID"), nullable=False)
    name = Column(String, nullable=False)
    academic_year = Column(Integer)

    def edit_student_information(self, student: Student):
        pass

    def edit_course_information(self, teacher: Teacher):
        pass