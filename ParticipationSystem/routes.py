from flask import Blueprint, session, request

from .exceptions.LoginException import LoginException
from .models import Teacher, Student

participation_blueprint = Blueprint('participation_system', __name__, template_folder='templates')


user_database = {}

@participation_blueprint.route('/participation')
def participation():
    return "ParticipationSystem"


@participation_blueprint.route('/participation/login')
def login():
    userid = request.form['userid']
    password = request.form['password']

    user = check_user_login(userid, password)


    return "ParticipationSystemLogin"

def check_user_login(userid, password) -> Teacher | Student | None:
    if userid in user_database:
        user = user_database[userid]
        if user['password'] == password:
            if user['role'] == 'teacher':
                return Teacher(userid, password, user['id'], user['name'])
            if user['role'] == 'student':
                return Student(userid, password, user['id'], user['name'])
        return None
    raise LoginException
