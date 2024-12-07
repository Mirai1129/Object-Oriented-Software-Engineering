from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Session

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

    def get_attendance_record(self, db: Session, course_id: str = None, start_date: str = None, end_date: str = None):
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

    def update_attendance_record(self, db: Session, course_id: str, student_id: str):
        from .AttendanceRecord import AttendanceRecord

        try:
            attendance_date = datetime.today()
            attendance_status = True
            modified_time = datetime.now()

            attendance_record = AttendanceRecord(
                student_id=student_id,
                course_id=course_id,
                attendance_date=attendance_date,
                attendance_status=attendance_status,
                modified_time=modified_time
            )

            db.add(attendance_record)
            db.commit()
            return {"message": "New Attendance record updated."}
        except Exception as e:
            db.rollback()
            raise Exception(f"Error updating new attendance: {str(e)}")
