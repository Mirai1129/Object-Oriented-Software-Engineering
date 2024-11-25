from typing import List

from .Student import Student


class Course:
    def __init__(self, course_id: int, name: str, year: int):
        self.id: int = course_id
        self.name: str = name
        self.year: int = year
        self.students: List[Student] = []  # 與學生的聚合關係

    def add_student(self, student: Student):
        self.students.append(student)

    def edit_student_information(self):
        pass

    def edit_course_information(self):
        pass
