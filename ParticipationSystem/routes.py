from flask import Blueprint

participation_blueprint = Blueprint('participation_system', __name__, template_folder='templates')


@participation_blueprint.route('/participation')
def participation():
    return "ParticipationSystem"
