from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .User import User


class Student(User):
    __tablename__ = 'Student'

    id = Column(String, primary_key=True)
    name = Column(String)

    attendance_records = relationship("AttendanceRecord", back_populates="student")
    course_enrollments = relationship("CourseEnrollment", back_populates="student")

    __mapper_args__ = {
        'polymorphic_identity': 'student',
        'inherit_condition': id == User.account
    }

    def get_courses(self, db):
        """
        get Student's courses
        :param db:
        :return:
        """
        from .Course import Course
        return db.query(Course).filter_by(student_id=self.id).all()

    def view_attendance_record(self):
        """
        View attendance record

        Returns:
            list: Student attendance record
        """
        return self.attendance_records
