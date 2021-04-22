from animal_adoption import app, User
from flask import jsonify, request


@app.route('/', endpoint='', methods=['GET'])
def login():
    """
    Test basic routing
    :return:
    """
    hello = "Hello World"
    return hello


@app.route('/create-user', endpoint='create-user', methods=['POST'])
def create_user():
    """
    Create a new user with the provided credentials
    :return:
    """
    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        print('uri=/login error="Missing password parameter"')
        return jsonify({"msg": "Missing password parameter"}), 400

    new_user = User()
    result = new_user.create_user(username=username, password=password)
    if result:
        return jsonify(message='User {} creation successful'.format(username)), 200
    else:
        return jsonify(message='User {} creation failed'.format(username)), 500


@app.route('/login', endpoint='login', methods=['POST'])
def login():
    """
    Authenticate existing user
    :return:
    """
    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        print('uri=/login error="Missing password parameter"')
        return jsonify({"msg": "Missing password parameter"}), 400

    result = User.authenticate_user(username=username, password=password)
    if result:
        return jsonify(message='User {} authentication successful'.format(username)), 200
    else:
        return jsonify(message='Bad username or password'), 401
