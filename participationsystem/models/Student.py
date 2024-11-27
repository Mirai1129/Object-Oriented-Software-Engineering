from typing import List

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .Course import Course
from .User import User

class Student(User):
    __tablename__ = "students"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    student_id = Column(Integer, unique=True)
    name = Column(String)

    # Relationship with courses can be added later
    courses = relationship("CourseModel", secondary="student_courses")

    __mapper_args__ = {
        "polymorphic_identity": "student"
    }


    def login(self):
        pass

    def view_question_and_answer_record(self):
        pass

    def enroll_course(self, course: 'Course'):
        self.courses.append(course)
