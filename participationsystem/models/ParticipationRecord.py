from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Date, String

from ..database import Base


class ParticipationRecord(Base):
    __tablename__ = 'ParticipationRecord'

    student_id = Column(String(20), ForeignKey('Student.student_id'), primary_key=True, nullable=False)
    grade_id = Column(String(20), ForeignKey('ParticipationGrade.grade_id'), primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    modified_time = Column(DateTime, default=datetime.now)
