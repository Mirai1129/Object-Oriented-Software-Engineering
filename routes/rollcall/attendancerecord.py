from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from rollcallsystem import get_db, Student, get_current_user

router = APIRouter()


@router.get("/getAttendance/{student_id}")
async def get_attendance(
        student_id: str,
        course_id: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
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
        attendance_records = student.get_attendance_record(db, course_id, start_date, end_date)
        return {"attendance_records": attendance_records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
