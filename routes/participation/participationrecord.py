from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from participationsystem import get_db, get_current_user, Teacher

router = APIRouter()


@router.get("/getCourses")
def get_courses(
        db: Session = Depends(get_db),
        current_user: Teacher = Depends(get_current_user)
):
    """
    Get courses taught by the current teacher.

    Args:
        db: SQLAlchemy session dependency for database interaction.
        current_user: The current logged-in teacher object.

    Returns:
        A list of courses taught by the current teacher or an empty list if no courses are found.
    """
    try:
        # Check if current_user is valid
        if not current_user:
            return {"detail": "User not found"}

        teacher_id = current_user.id
        course = current_user.get_courses(db, teacher_id)

        if not course:
            return {"courses": []}
        else:
            return {"courses": course}
    except Exception as e:
        raise Exception(f"Error to get courses: {e}")


@router.get("/getCourses/{teacher_id}")
def get_courses_by_teacher_id(
        teacher_id: str,
        db: Session = Depends(get_db),
        current_user: Teacher = Depends(get_current_user)
):
    """
    Get courses taught by a specific teacher based on teacher_id.

    Args:
        teacher_id: The teacher's unique identifier.
        db: SQLAlchemy session dependency for database interaction.
        current_user: The current logged-in teacher object.

    Returns:
        A list of courses taught by the teacher with the given teacher_id or an empty list if no courses are found.
    """
    try:
        course = current_user.get_courses(db, teacher_id)
        if not course:
            return {"courses": []}
        else:
            return {"courses": course}
    except Exception as e:
        raise Exception(f"Error to get courses: {e}")


@router.get("/addStudentParticipationRecord")
def add_student_participation_record(
        course_id: str,
        student_id: str,
        teacher_id: str,
        grade: float,
        db: Session = Depends(get_db),
        current_user: Teacher = Depends(get_current_user)
):
    """
    Add a student's participation record to a course, including their grade.

    Args:
        course_id: The unique identifier of the course.
        student_id: The unique identifier of the student.
        teacher_id: The unique identifier of the teacher adding the participation record.
        grade: The grade of the student for the participation.
        db: SQLAlchemy session dependency for database interaction.
        current_user: The current logged-in teacher object.

    Returns:
        A success message if the participation record was added or an error message if any issue occurred.

    Raises:
        HTTPException: If the current teacher is not authorized to add the participation record.
    """
    try:
        if str(current_user.id) != teacher_id:
            raise HTTPException(status_code=403, detail="Unauthorized to add participation record")

        result = current_user.add_student_participation_record(
            db=db,
            course_id=course_id,
            student_id=student_id,
            grade=grade
        )

        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/editStudentParticipationRecord")
def edit_student_participation_record(
        grade_id: str,
        course_id: str,
        student_id: str,
        grade: float,
        db: Session = Depends(get_db),
        current_user: Teacher = Depends(get_current_user)
):
    """
    Edit an existing student's participation record, updating the grade.

    Args:
        grade_id: The unique identifier of the grade record to be edited.
        course_id: The unique identifier of the course.
        student_id: The unique identifier of the student.
        grade: The new grade for the student.
        db: SQLAlchemy session dependency for database interaction.
        current_user: The current logged-in teacher object.

    Returns:
        A success message if the participation record was updated or an error message if any issue occurred.
    """
    try:
        result = current_user.edit_student_participation_record(
            db=db,
            grade_id=grade_id,
            course_id=course_id,
            student_id=student_id,
            grade=grade
        )

        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
