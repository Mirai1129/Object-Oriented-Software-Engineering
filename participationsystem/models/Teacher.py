from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from ..database import Base


class Teacher(Base):
    __tablename__ = "Teacher"

    teacher_id = Column(String(20), primary_key=True)
    user_id = Column(String(50), ForeignKey('User.account'), nullable=False, unique=True)
    specialization = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False)

    user = relationship("User", back_populates="teachers")
    courses = relationship("Course", back_populates="teacher")

    # 可以新增及編輯學生發言加分分數，全權控制課堂發言紀錄

    def add_student_participation_record(self):
        from .Course import Course

    def manage_question_and_answer_record(self):
        pass
