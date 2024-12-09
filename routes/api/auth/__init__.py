from fastapi import APIRouter

from .participationauth import router as participation_router
from .rollcallauth import router as rollcallauth_router

router = APIRouter(prefix="/api/auth", tags=["auth"])

router.include_router(participation_router, prefix="/participation", tags=["auth"])
router.include_router(rollcallauth_router, prefix="/rollcall", tags=["auth"])
