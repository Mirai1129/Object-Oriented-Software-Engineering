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


@router.post("/addStudentToCourse")
async def add_student_to_course(
        course_id: str,
        student_id: str,
        semester: str,
        current_user: Teacher = Depends(get_current_user),  # 驗證 Token 並取得教師身份
        db: Session = Depends(get_db)
):
    """
    將學生加入課程的選課記錄
    """
    try:
        result = current_user.add_student_to_course_enrollment(db, course_id, student_id, semester)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/addNewCourse")
async def add_new_course_endpoint(
        course_data: dict,
        current_user: Teacher = Depends(get_current_user),  # 驗證 Token 並取得教師身份
        db: Session = Depends(get_db)
):
    """
    新增課程，只有授權的教師可以新增課程
    """
    try:
        # 確認教師是否有權限新增課程（例如檢查教師身份或角色）
        # 如果需要額外檢查，可以加上額外的邏輯來驗證教師身份

        # 呼叫新增課程的邏輯
        response = current_user.add_new_course(db, course_data['course_id'], course_data['course_name'],
                                               course_data['semester'])
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
