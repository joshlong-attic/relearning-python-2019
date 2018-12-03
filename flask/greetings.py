from flask import *
import jsonpickle

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/users/<username>')
def get_user_profile(username):
    return jsonpickle.encode(Profile(username))


@app.route('/users/<username>/validation')
def is_account_valid(username):
    def reply(v, s):
        return app.response_class(response=json.dumps({'valid': v}), status=s, mimetype='application/json')

    if username == 'josh':
        return reply(True, 200)

    return reply(False, 302)


class Profile(object):
    def __init__(self, name):
        self.name = name
