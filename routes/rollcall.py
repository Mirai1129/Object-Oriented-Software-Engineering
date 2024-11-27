from fastapi import APIRouter

router = APIRouter(prefix="/rollcall")

@router.get("/")
async def root():
    return {"message": "Hello rollcall."}

@router.post("/login")
async def login():
    return {"message": "Hello rollcall."}
