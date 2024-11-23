from .User import User


class Student(User):
    def __init__(self, account: str, password: str, student_id: int, name: str):
        super().__init__(account, password)
        self.id: int = student_id
        self.name: str = name

    def view_attendance_record(self):
        pass
