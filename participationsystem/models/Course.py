from sqlalchemy import Integer, Column, ForeignKey, String


class Course:
    __tablename__ = "Course"

    course_id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('Teacher.teacher_id'))
    name = Column(String)
    year = Column(Integer)

    def edit_student_information(self):
        pass

    def edit_course_information(self):
        pass
