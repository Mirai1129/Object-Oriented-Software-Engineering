from .Student import Student
from .Teacher import Teacher


class Course:
    def __init__(self, course_id: int, course_name: str, academic_year: int):
        self.id: int = course_id
        self.name: str = course_name
        self.academic_year: int = academic_year

    def edit_student_information(self, student: Student):
        pass

    def edit_course_information(self, teacher: Teacher):
        pass
