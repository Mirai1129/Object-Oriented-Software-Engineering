from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from rollcallsystem import get_db, Student, get_current_user, Course, Teacher

router = APIRouter()


@router.get("/getAttendance/{student_id}")
async def get_attendance(
        student_id: str,
        course_id: str = None,
        start_date: date = None,
        end_date: date = None,
        db: Session = Depends(get_db),
        current_user: Student = Depends(get_current_user)
):
    """
    Get attendance records for a specific student.

    Args:
        student_id: The student's unique ID.
        course_id: Optional, the course ID to filter attendance by.
        start_date: Optional, the start date to filter attendance records.
        end_date: Optional, the end date to filter attendance records.
        db: SQLAlchemy session dependency for database interaction.
        current_user: The current logged-in student object.

    Returns:
        A list of attendance records for the student, filtered by the provided parameters.

    Raises:
        HTTPException: If the current user does not have permission to access the student's attendance records.
    """
    if current_user.id != student_id:
        raise HTTPException(status_code=403,
                            detail="You do not have permission to access this student's attendance records")

    student = db.query(Student).filter_by(id=student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    try:
        attendance_records = current_user.get_attendance_record(db, course_id, start_date, end_date)
        return {"attendance_records": attendance_records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/updateAttendance/{course_id}/{student_id}")
async def update_attendance(
        course_id: str,
        student_id: str,
        db: Session = Depends(get_db),
        current_user: Student = Depends(get_current_user)
):
    """
    Update attendance record for a student in a specific course.

    Args:
        course_id: The unique identifier of the course.
        student_id: The unique identifier of the student.
        db: SQLAlchemy session dependency for database interaction.
        current_user: The current logged-in student object.

    Returns:
        A response indicating the success of the update.

    Raises:
        HTTPException: If the current user is not authorized or if any errors occur during the update.
    """
    if current_user.id != student_id:
        raise HTTPException(status_code=403,
                            detail="You do not have permission to access this student's attendance records")

    course = db.query(Course).filter_by(course_id=course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    student = db.query(Student).filter_by(id=student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if not course.is_rollcall_opened:
        raise HTTPException(status_code=404, detail="This course's rollcall has not been opened")

    try:
        response = current_user.update_attendance_record(db, course_id, student_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/getAttendance/{course_id}/{student_id}")
async def get_attendance(
        course_id: str,
        student_id: str,
        db: Session = Depends(get_db),
        current_user: Teacher = Depends(get_current_user)
):
    """
    Get attendance records for a specific student in a specific course by a teacher.

    Args:
        course_id: The unique identifier of the course.
        student_id: The unique identifier of the student.
        db: SQLAlchemy session dependency for database interaction.
        current_user: The current logged-in teacher object.

    Returns:
        A list of attendance records for the student in the specified course.

    Raises:
        HTTPException: If the teacher or student is not found.
    """
    teacher = db.query(Teacher).filter_by(id=current_user.id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    response = current_user.get_attendance_records(db, course_id, student_id)
    return response


@router.put("/editAttendance/{course_id}/{student_id}")
async def update_attendance(
        course_id: str,
        student_id: str,
        db: Session = Depends(get_db),
        current_user: Teacher = Depends(get_current_user)
):
    """
    Edit the attendance record for a student in a specific course by a teacher.

    Args:
        course_id: The unique identifier of the course.
        student_id: The unique identifier of the student.
        db: SQLAlchemy session dependency for database interaction.
        current_user: The current logged-in teacher object.

    Returns:
        A response indicating the success of the update.

    Raises:
        HTTPException: If the teacher is not authorized or if any errors occur during the update.
    """
    if current_user.id != student_id:
        raise HTTPException(status_code=403,
                            detail="You do not have permission to access this student's attendance records")

    course = db.query(Course).filter_by(course_id=course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    teacher = db.query(Teacher).filter_by(id=student_id).first()

    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    if not course.is_rollcall_opened:
        raise HTTPException(status_code=404, detail="This course's rollcall has not been opened")

    try:
        response = current_user.edit_attendance_record(db, course_id, student_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
