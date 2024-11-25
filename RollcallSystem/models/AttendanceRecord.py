from .Student import Student


class AttendanceRecord:
    def __init__(self, student: Student, attendance_status: int):
        self.student: Student = student
        self.status: int = attendance_status

    def update_attendance_status(self, attendance_status: int):
        pass
