from sqlalchemy import Column, String

from .User import User


class Teacher(User):
    __tablename__ = 'Teacher'

    # Add an explicit foreign key to link to the User table
    teacher_id = Column(String, primary_key=True)
    name = Column(String)

    # Configure the inheritance
    __mapper_args__ = {
        'polymorphic_identity': 'teacher',
        'inherit_condition': teacher_id == User.account
    }

    def manage_course(self):
        pass

    def manage_attendance_record(self):
        pass
