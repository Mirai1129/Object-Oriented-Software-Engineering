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
        current_user: Student = Depends(get_current_user)  # 確認當前用戶是否為學生或教師
):
    """
    獲取學生的考勤記錄
    :param student_id: 學生ID
    :param course_id: 選填，課程ID（如果需要過濾）
    :param start_date: 選填，開始日期（如果需要過濾）
    :param end_date: 選填，結束日期（如果需要過濾）
    :param db: SQLAlchemy會話
    :param current_user: 驗證使用者身份（學生或教師）
    :return: 學生的考勤記錄
    """
    if current_user.id != student_id:
        raise HTTPException(status_code=403,
                            detail="You do not have permission to access this student's attendance records")

    # 從學生實體中調用 `get_attendance_record` 方法
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
        raise HTTPException(status_code=404, detail="This course's rollcall not opened")

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
        raise HTTPException(status_code=404, detail="This course's rollcall not opened")

    try:
        response = current_user.edit_attendance_record(db, course_id, student_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
