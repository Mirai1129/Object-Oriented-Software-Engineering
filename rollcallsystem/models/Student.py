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

    def get_attendance_record(self, db, course_id: str = None, start_date: str = None, end_date: str = None):
        """
        View attendance record, with optional filters for course, date range, and attendance status

        :param db: SQLAlchemy session
        :param course_id: Filter by course ID (optional)
        :param start_date: Filter by start date (optional)
        :param end_date: Filter by end date (optional)
        :return: List of attendance records matching the criteria
        """
        from .AttendanceRecord import AttendanceRecord
        query = db.query(AttendanceRecord).filter_by(student_id=self.id)

        # Add filters if provided
        if course_id:
            query = query.filter_by(course_id=course_id)
        if start_date:
            query = query.filter(AttendanceRecord.attendance_date >= start_date)
        if end_date:
            query = query.filter(AttendanceRecord.attendance_date <= end_date)

        return query.all()
