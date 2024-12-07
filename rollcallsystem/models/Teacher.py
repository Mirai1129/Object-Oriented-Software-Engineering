from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker

from .User import User


class Teacher(User):
    __tablename__ = 'Teacher'

    id = Column(String, primary_key=True)
    name = Column(String)

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
