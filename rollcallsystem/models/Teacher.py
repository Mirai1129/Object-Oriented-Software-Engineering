from datetime import datetime, date

from sqlalchemy import Column, String
from sqlalchemy.orm import Session

from .User import User


class Teacher(User):
    __tablename__ = 'Teacher'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'teacher',
        'inherit_condition': id == User.account
    }

    def get_courses(self, db):
        """
        Get the courses taught by the teacher.

        Args:
            db (Session): The database session to query courses.

        Returns:
            list: A list of courses assigned to the teacher.
        """
        from .Course import Course
        return db.query(Course).filter_by(teacher_id=self.id).all()

    def add_student_to_course_enrollment(self, db, course_id: str, student_id: str, semester: str):
        """
        Add a student to a course enrollment record.

        Args:
            db (Session): The database session to query the database.
            course_id (str): The course ID.
            student_id (str): The student ID.
            semester (str): The semester information.

        Returns:
            dict: A message indicating the result of the operation.
        """
        from .CourseEnrollment import CourseEnrollment

        try:
            is_existing_enrollment = db.query(CourseEnrollment).filter_by(
                course_id=course_id,
                student_id=student_id,
                semester=semester
            ).first()

            if is_existing_enrollment:
                return {"message": "The student is already enrolled in this course for the given semester."}

            enrollment = CourseEnrollment(
                course_id=course_id,
                student_id=student_id,
                semester=semester
            )
            db.add(enrollment)
            db.commit()
            return {"message": "Student successfully added to course enrollment."}
        except Exception as e:
            db.rollback()
            raise Exception(f"Error adding student to course enrollment: {str(e)}")

    def add_new_course(self, db, course_id: str, course_name: str, semester: str):
        """
        Add a new course.

        Args:
            db (Session): The database session to query the database.
            course_id (str): The course ID.
            course_name (str): The name of the course.
            semester (str): The semester information.

        Returns:
            dict: A message indicating the result of the operation.
        """
        from .Course import Course

        try:
            is_existing_course = db.query(Course).filter_by(course_id=course_id).first()

            if is_existing_course:
                return {"message": "Course with this ID already exists."}

            new_course = Course(
                course_id=course_id,
                name=course_name,
                teacher_id=self.id,
                academic_year=semester
            )

            db.add(new_course)
            db.commit()
            return {"message": "New course successfully added."}

        except Exception as e:
            db.rollback()
            raise Exception(f"Error adding new course: {str(e)}")

    def get_attendance_records(self, db: Session, course_id: str, student_id: str):
        """
        Get the attendance records for a specific student in a specific course.

        Args:
            db (Session): The database session to query the database.
            course_id (str): The course ID.
            student_id (str): The student ID.

        Returns:
            list: A list of attendance records for the given student in the course.
        """
        from .AttendanceRecord import AttendanceRecord

        try:
            attendance_record = db.query(AttendanceRecord).filter_by(course_id=course_id, student_id=student_id).all()
            if attendance_record:
                return attendance_record
        except Exception as e:
            db.rollback()
            raise Exception(f"Error getting attendance records: {str(e)}")

    def edit_attendance_record(self,
                               db: Session,
                               course_id: str,
                               student_id: str,
                               attendance_date: date = None,
                               attendance_status: bool = None
                               ):
        """
        Edit or create an attendance record for a student in a course.

        Args:
            db (Session): The database session to query the database.
            course_id (str): The course ID.
            student_id (str): The student ID.
            attendance_date (date, optional): The date of the attendance. Defaults to None.
            attendance_status (bool, optional): The attendance status (True for present, False for absent). Defaults to None.

        Returns:
            dict: A message indicating the result of the operation.
        """
        from .AttendanceRecord import AttendanceRecord

        try:
            modified_time = datetime.now()

            attendance_record = db.query(AttendanceRecord).filter_by(
                student_id=student_id, course_id=course_id, attendance_date=attendance_date
            ).first()

            if attendance_record:
                attendance_record.attendance_status = attendance_status
                attendance_record.modified_time = modified_time
                db.commit()
                return {"message": "Attendance record updated."}
            else:
                attendance_record = AttendanceRecord(
                    student_id=student_id,
                    course_id=course_id,
                    attendance_date=datetime.today(),
                    attendance_status=attendance_status,
                    modified_time=modified_time
                )
                db.add(attendance_record)
                db.commit()
                return {"message": "New Attendance record created."}

        except Exception as e:
            db.rollback()
            raise Exception(f"Error updating attendance record: {str(e)}")
