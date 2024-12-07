from datetime import datetime

from .Course import Course
from .Student import Student


class QuestionAndAnswerRecord:
    __tablename__ = "QuestionAndAnswerRecord"

    def __init__(self, record_id: int, student: Student, course: Course, date: datetime = datetime.now()):
        self.id: int = record_id
        self.student: Student = student
        self.course: Course = course
        self.date: datetime = date

    def add_score(self, score: float):
        pass

    def edit_question_and_answer_record(self):
        pass
