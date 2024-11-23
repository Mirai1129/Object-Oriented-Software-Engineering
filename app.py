from flask import Flask

from ParticipationSystem import participation_blueprint
from RollcallSystem import rollcall_blueprint

app = Flask(__name__)
app.register_blueprint(rollcall_blueprint)
app.register_blueprint(participation_blueprint)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
