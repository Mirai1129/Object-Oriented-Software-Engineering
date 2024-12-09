from fastapi import APIRouter

from .participation import router as participation_router

router = APIRouter(prefix="/participation", tags=["participation"])

router.include_router(participation_router, prefix="", tags=["participation"])
