from fastapi import APIRouter

from .participation import router as participation_router
from .participationrecord import router as participation_record_router

router = APIRouter(prefix="/participation", tags=["participation"])

router.include_router(participation_router, prefix="", tags=["web"])
router.include_router(participation_record_router, prefix="", tags=["participation"])
