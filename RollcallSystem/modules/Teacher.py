from .User import User


class Teacher(User):
    def __init__(self, account: str, password: str, teacher_id: int, name: str):
        super().__init__(account, password)
        self.id: int = teacher_id
        self.name: str = name

    def login(self):
        pass

    def manage_course(self):
        pass

    def manage_attendance_record(self):
        pass
