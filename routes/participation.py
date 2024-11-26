from fastapi import APIRouter

from ParticipationSystem.exceptions.LoginException import LoginException
from ParticipationSystem.models import Teacher, Student


router = APIRouter(prefix="/participation")
db = {}

@router.get("/")
async def root():
    return {"message": "Hello participation."}


def check_user_login(userid, password) -> Teacher | Student | None:
    if userid in db:
        user = db[userid]
        if user['password'] == password:
            if user['role'] == 'teacher':
                return Teacher(userid, password, user['id'], user['name'])
            if user['role'] == 'student':
                return Student(userid, password, user['id'], user['name'])
        raise LoginException(message="Userid or password is wrong.")
    raise LoginException(message=f"{userid} does not exist.")
