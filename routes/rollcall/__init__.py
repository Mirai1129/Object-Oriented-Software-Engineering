from fastapi import APIRouter

from .attendancerecord import router as attendancerecord_router
from .course import router as teacher_router
from .rollcall import router as rollcall_router

router = APIRouter(prefix="/rollcall")

router.include_router(rollcall_router, prefix="", tags=["web"])
router.include_router(teacher_router, prefix="/course", tags=["rollcall"])
router.include_router(attendancerecord_router, prefix="/attendancerecord", tags=["rollcall"])
