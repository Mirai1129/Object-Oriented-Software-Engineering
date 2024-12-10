from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .User import User


class Student(User):
    __tablename__ = "Student"

    id = Column(String(20), primary_key=True)
    name = Column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'student',
        'inherit_condition': id == User.account
    }

    participation_grades = relationship("ParticipationGrade", back_populates="student")
