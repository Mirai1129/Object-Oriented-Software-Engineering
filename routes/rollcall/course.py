from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from rollcallsystem import get_current_user, Teacher
from rollcallsystem.database import get_db

router = APIRouter()


@router.get("/getTeacherCourse")
async def get_teacher_courses(
        current_user: Teacher = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    """
    Get the list of courses taught by the specified teacher.

    :param current_user: The teacher making the request, verified by token.
    :param db: SQLAlchemy database session.
    :return: A JSON object containing teacher ID and a list of course names.
    :raises HTTPException: If the teacher does not exist or there are no courses assigned.
    """
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This is not a valid user!"
        )

    try:
        courses = current_user.get_courses(db)
        if not courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No courses found for this teacher"
            )
        return {"teacher_id": current_user.id, "courses": [course.name for course in courses]}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@router.post("/addStudentToCourse")
async def add_student_to_course(
        course_id: str,
        student_id: str,
        semester: str,
        current_user: Teacher = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    """
    Add a student to the course enrollment.

    :param course_id: The ID of the course.
    :param student_id: The ID of the student to be enrolled.
    :param semester: The semester in which the student will be enrolled.
    :param current_user: The teacher making the request, verified by token.
    :param db: SQLAlchemy database session.
    :return: A response indicating whether the student was successfully added to the course.
    :raises HTTPException: If an error occurs during the process.
    """
    try:
        result = current_user.add_student_to_course_enrollment(db, course_id, student_id, semester)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/addNewCourse")
async def add_new_course_endpoint(
        course_data: dict,
        current_user: Teacher = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    """
    Add a new course. Only authorized teachers can add new courses.

    :param course_data: A dictionary containing course details such as course ID, name, and semester.
    :param current_user: The teacher making the request, verified by token.
    :param db: SQLAlchemy database session.
    :return: A response indicating whether the course was successfully added.
    :raises HTTPException: If an error occurs during the course creation.
    """
    try:
        response = current_user.add_new_course(db, course_data['course_id'], course_data['course_name'],
                                               course_data['semester'])
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/updateCourseStatus")
async def update_course_status(
        course_id: str,
        status: str,
        current_user: Teacher = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    try:
        result = current_user.update_course_status(db, course_id, status)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
