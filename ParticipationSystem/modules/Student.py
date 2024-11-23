from typing import List

from .Course import Course
from .User import User

class Student(User):
    def __init__(self, account: str, password: str, student_id: int, name: str):
        super().__init__(account, password)
        self.id: int = student_id
        self.name: str = name
        self.courses: List[Course] = []  # 與課程的聚合關係

    def login(self):
        pass

    def view_question_and_answer_record(self):
        pass

    def enroll_course(self, course: 'Course'):
        self.courses.append(course)
