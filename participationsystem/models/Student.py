from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from ..database import Base


class Student(Base):
    __tablename__ = "Student"

    student_id = Column(String(20), primary_key=True)
    user_id = Column(String(50), ForeignKey('User.account'), nullable=False, unique=True)
    name = Column(String(50), nullable=False)

    user = relationship("User", back_populates="students")
    participation_grades = relationship("ParticipationGrade", back_populates="student")
    question_answer_records = relationship("QuestionAndAnswerRecord", back_populates="student")

    def login(self):
        pass

    def view_question_and_answer_record(self):
        pass

    def enroll_course(self, course):
        pass
