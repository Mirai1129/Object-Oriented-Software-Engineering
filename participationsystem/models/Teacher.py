from sqlalchemy import Column, Integer, ForeignKey, String

from .User import User


class Teacher(User):
    class TeacherModel(User):
        __tablename__ = "teachers"

        id = Column(Integer, ForeignKey('users.id'), primary_key=True)
        teacher_id = Column(Integer, unique=True)
        name = Column(String)

        __mapper_args__ = {
            "polymorphic_identity": "teacher"
        }

    def login(self):
        pass

    def manage_course(self):
        pass

    def manage_question_and_answer_record(self):
        pass
