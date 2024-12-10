from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Session

from .User import User


class Teacher(User):
    __tablename__ = "Teacher"

    id = Column(String(20), primary_key=True)
    specialization = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'teacher',
        'inherit_condition': id == User.account
    }

    courses = relationship("Course", back_populates="teacher")

    def get_courses(self, db: Session, teacher_id: str):
        """
        Retrieve all courses taught by the specified teacher.

        Args:
            db (Session): The database session to perform queries.
            teacher_id (str): The ID of the teacher.

        Returns:
            List: A list of courses taught by the teacher. An empty list if no courses are found.
        """
        from .Course import Course

        try:
            courses = db.query(Course).filter(Course.teacher_id == teacher_id).all()

            if courses:
                return courses
            else:
                return []
        except Exception as e:
            raise Exception(f"Error querying courses: {e}")

    def add_student_participation_record(self,
                                         db: Session,
                                         course_id: str,
                                         student_id: str,
                                         grade: float):
        """
        Add a new participation record for a student in a specific course.

        Args:
            db (Session): The database session to interact with the database.
            course_id (str): The course ID where the record should be added.
            student_id (str): The ID of the student.
            grade (float): The grade of the student in the course.

        Returns:
            dict: A dictionary with a message indicating success or failure.
        """
        from .ParticipationGrade import ParticipationGrade

        try:
            modified_time = datetime.now()

            # Create a new participation record
            new_participation_grade = ParticipationGrade(
                course_id=course_id,
                student_id=student_id,
                grade=grade,
                generated_date=datetime.today(),
                modified_time=modified_time
            )

            db.add(new_participation_grade)
            db.commit()
            return {"message": "New participation record added"}

        except Exception as e:
            db.rollback()
            raise Exception(f"Error adding new participation record: {e}")

    def edit_student_participation_record(self,
                                          db: Session,
                                          grade_id: str,
                                          course_id: str,
                                          student_id: str,
                                          grade: float):
        """
        Edit an existing participation record for a student in a specific course.

        Args:
            db (Session): The database session to interact with the database.
            grade_id (str): The unique ID of the participation grade to be updated.
            course_id (str): The course ID where the participation record exists.
            student_id (str): The student ID whose participation record needs to be updated.
            grade (float): The new grade to be set for the student.

        Returns:
            dict: A dictionary with a message indicating success or failure.
        """
        from .ParticipationGrade import ParticipationGrade

        try:
            modified_time = datetime.now()

            participation_grade = db.query(ParticipationGrade).filter_by(
                grade_id=grade_id,
                course_id=course_id,
                student_id=student_id,
            ).first()

            if participation_grade:
                participation_grade.grade = grade
                participation_grade.modified_time = modified_time

                db.commit()
                return {"message": "Participation record updated"}
            else:
                return {"message": "No participation record found"}

        except Exception as e:
            db.rollback()
            raise Exception(f"Error updating participation record: {e}")
