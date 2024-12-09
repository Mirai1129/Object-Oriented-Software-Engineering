from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from ..database import Base


class QuestionAndAnswerRecord(Base):
    __tablename__ = "QuestionAndAnswerRecord"

    id = Column(Integer, primary_key=True)
    student_id = Column(String(20), ForeignKey('Student.student_id'), nullable=False)
    course_id = Column(String(20), ForeignKey('Course.course_id'), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now)
    score = Column(Float, nullable=True)

    student = relationship("Student", back_populates="question_answer_records")
    course = relationship("Course", back_populates="question_answer_records")

    def add_score(self, score: float):
        self.score = score

    def edit_question_and_answer_record(self):
        pass
