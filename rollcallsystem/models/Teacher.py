from sqlalchemy import Column, String

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
