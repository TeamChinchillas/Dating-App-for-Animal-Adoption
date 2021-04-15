from animal_adoption import app, User
from flask import jsonify


@app.route('/', endpoint='', methods=['GET'])
def login():
    """
    Test basic routing
    :return:
    """
    hello = "Hello World"
    return hello


@app.route('/test-create-user', endpoint='test_create_user', methods=['GET'])
def create_user():
    """
    Test user creation and password hashing
    :return:
    """
    new_user = User()
    new_user.create_user('my_test', 'test123')
    print(new_user.authenticate_user('my_test', 'test123'))
    print(new_user.authenticate_user('my_test', 'test122'))

    return jsonify(message='success'), 200
