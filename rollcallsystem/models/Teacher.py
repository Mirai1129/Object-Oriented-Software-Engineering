from sqlalchemy import Column, String

from .User import User


class Teacher(User):
    __tablename__ = 'Teacher'

    id = Column(String, primary_key=True)
    password = Column(String)
    name = Column(String)

    def login(self):
        pass

    def manage_course(self):
        pass

    def manage_attendance_record(self):
        pass
