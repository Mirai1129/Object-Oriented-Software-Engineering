from fastapi import APIRouter, Request

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="rollcallsystem/templates")


@router.get("/")
async def root():
    return {"message": "Hello participation."}


@router.get("/login")
async def login_page(request: Request):
    """
    show the login page
    """
    return templates.TemplateResponse("login.html", {"request": request})