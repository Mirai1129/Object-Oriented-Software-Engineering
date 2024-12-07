from fastapi import APIRouter

from .course import router as teacher_router
from .rollcall import router as rollcall_router

router = APIRouter(prefix="/rollcall")

router.include_router(rollcall_router, prefix="", tags=["rollcall"])
router.include_router(teacher_router, prefix="/course", tags=["course"])
