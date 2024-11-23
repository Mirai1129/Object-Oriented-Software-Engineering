from flask import Blueprint

rollcall_blueprint = Blueprint('rollcall_system', __name__, template_folder='templates')


@rollcall_blueprint.route('/rollcall')
def rollcall():
    return "RollcallSystem"
