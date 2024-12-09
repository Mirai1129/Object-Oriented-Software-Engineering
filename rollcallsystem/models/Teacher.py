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
        獲取教師所負責的課程
        """
        from .Course import Course
        return db.query(Course).filter_by(teacher_id=self.id).all()

    def add_student_to_course_enrollment(self, db, course_id: str, student_id: str, semester: str):
        """
        將學生加入課程選課記錄
        :param db: SQLAlchemy Session
        :param course_id: 課程ID
        :param student_id: 學生ID
        :param semester: 學期資訊
        """
        from .CourseEnrollment import CourseEnrollment

        try:
            # 檢查是否已存在相同的選課記錄
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
            db.add(enrollment)  # 新增實體到資料庫會話
            db.commit()  # 提交變更
            return {"message": "Student successfully added to course enrollment."}
        except Exception as e:
            db.rollback()  # 發生錯誤時回滾變更
            raise Exception(f"Error adding student to course enrollment: {str(e)}")

    def add_new_course(self, db, course_id: str, course_name: str, semester: str):
        """
        新增課程
        :param db: SQLAlchemy Session
        :param course_id: 課程ID
        :param course_name: 課程名稱
        :param semester: 學期資訊
        """
        from .Course import Course  # 匯入課程模型

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
            db.rollback()  # 發生錯誤時回滾變更
            raise Exception(f"Error adding new course: {str(e)}")

    def get_attendance_records(self, db: Session, course_id: str, student_id: str):
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
        from .AttendanceRecord import AttendanceRecord

        try:
            modified_time = datetime.now()

            # 查詢是否已經存在該學生和該課程的出勤紀錄
            attendance_record = db.query(AttendanceRecord).filter_by(
                student_id=student_id, course_id=course_id, attendance_date=attendance_date
            ).first()

            # 如果已經有紀錄，則進行更新
            if attendance_record:
                attendance_record.attendance_status = attendance_status
                attendance_record.modified_time = modified_time
                db.commit()
                return {"message": "Attendance record updated."}
            else:
                # 如果該紀錄不存在，則新增一條
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
