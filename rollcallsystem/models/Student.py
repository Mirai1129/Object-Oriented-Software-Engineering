from sqlalchemy import Column, String

from .User import User


class Student(User):
    __tablename__ = 'student'

    id = Column(String, primary_key=True)
    name = Column(String)

    def __init__(self, id: str, name: str, account: str, password: str):
        super().__init__(account=account, password=password)
        self.id = id
        self.name = name

    def view_attendance_record(self):
        pass
