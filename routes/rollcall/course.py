from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from rollcallsystem import get_current_user, Teacher
from rollcallsystem.database import get_db

router = APIRouter()


@router.get("/getTeacherCourse")
async def get_teacher_courses(
        current_user: Teacher = Depends(get_current_user),  # 驗證 Token 並取得使用者
        db: Session = Depends(get_db)
):
    """
    獲取指定教師的課程列表
    """
    # 確保當前使用者是有效的
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This is not a valid user!"
        )

    try:
        # 調用 get_courses 方法
        courses = current_user.get_courses(db)
        if not courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No courses found for this teacher"
            )
        return {"teacher_id": current_user.id, "courses": [course.name for course in courses]}
    except Exception as e:
        # 捕捉所有錯誤並返回
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )
