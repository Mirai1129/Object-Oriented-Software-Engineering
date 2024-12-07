from sqlalchemy import Column, String

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
        print(db.query(Course).filter_by(teacher_id=self.id).all())
        return db.query(Course).filter_by(teacher_id=self.id).all()

    def manage_course(self):
        pass

    def manage_attendance_record(self):
        pass
