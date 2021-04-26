import datetime
from animal_adoption import app, User, UserDetail
from flask import jsonify, make_response, redirect, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, set_access_cookies
)


app.config['JWT_SECRET_KEY'] = 'JofJtRHKzQmFRXGI4v60'
JWT_TOKEN_LOCATION = ['cookies']
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=1800)
JWT_COOKIE_NAME = "ACCESS-COOKIE"
jwt = JWTManager(app)


@app.route('/', endpoint='', methods=['GET'])
def login():
    """
    Test basic routing
    :return:
    """
    hello = "Hello World"
    return hello


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
        access_token = create_access_token(identity=User.get_id_by_username(username))
        response = make_response(redirect('/', 200))
        set_access_cookies(response, access_token)
        return response
    else:
        return jsonify(message='Bad username or password'), 401


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


@app.route('/create-user-with-details', endpoint='create_user_with_details', methods=['POST'])
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
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    user_type = request.json.get('user_type', None)

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        print('uri=/login error="Missing password parameter"')
        return jsonify({"msg": "Missing password parameter"}), 400
    if not first_name:
        print('uri=/login error="Missing first name parameter"')
        return jsonify({"msg": "Missing first name parameter"}), 400
    if not last_name:
        print('uri=/login error="Missing last name parameter"')
        return jsonify({"msg": "Missing last name parameter"}), 400
    if not user_type:
        print('uri=/login error="Missing user type parameter"')
        return jsonify({"msg": "Missing user type parameter"}), 400

    new_user = User()
    create_user_result = new_user.create_user(username=username, password=password)

    existing_user_detail = UserDetail.get_user_detail(username)

    if not existing_user_detail:
        new_user_detail = UserDetail()
        create_user_detail_result = new_user_detail.create_user_detail(
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type
        )

        if create_user_result and create_user_detail_result:
            return jsonify(message='User account and details for {} created successfully'.format(username)), 200
    else:
        return jsonify(message='User account and details for {} failed'.format(username)), 500


@app.route('/get-user-details', endpoint='get-user-details', methods=['GET'])
@jwt_required(locations='cookies')
def get_user_details():
    """
    Get details for a specified user
    :return:
    """
    current_user = get_jwt_identity()

    if not current_user:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400

    username = User.get_username_by_id(current_user)
    result = UserDetail.get_printable_user_detail(username)

    if result:
        return jsonify(message=result), 200
    else:
        return jsonify(message='User {} not found'.format(username)), 500


@app.route('/create-user-details', endpoint='create-user-details', methods=['POST'])
@jwt_required(locations='cookies')
def create_user_details():
    """
    Create user details for new user
    :return:
    """
    current_user = get_jwt_identity()

    if not current_user:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400

    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = User.get_username_by_id(current_user)
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    user_type = request.json.get('user_type', None)

    if not username:
        print('uri=/login error="User {} not found"'.format(username))
        return jsonify({"msg": "User {} not found".format(username)}), 400
    if not first_name:
        print('uri=/login error="Missing first name parameter"')
        return jsonify({"msg": "Missing first name parameter"}), 400
    if not last_name:
        print('uri=/login error="Missing last name parameter"')
        return jsonify({"msg": "Missing last name parameter"}), 400
    if not user_type:
        print('uri=/login error="Missing user type parameter"')
        return jsonify({"msg": "Missing user type parameter"}), 400

    existing_user_detail = UserDetail.get_user_detail(username)

    if not existing_user_detail:
        new_user_detail = UserDetail()
        result = new_user_detail.create_user_detail(
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type
        )
        if result:
            return jsonify(message='User details for {} created successfully'.format(username)), 200
    else:
        return jsonify(message='User details for {} failed'.format(username)), 500


@app.route('/update-user-details', endpoint='update-user-details', methods=['POST'])
@jwt_required(locations='cookies')
def update_user_details():
    """
    Update details for user that does exist
    :return:
    """
    current_user = get_jwt_identity()

    if not current_user:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400

    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = User.get_username_by_id(current_user)
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400
    if not first_name:
        print('uri=/login error="Missing first name parameter"')
        return jsonify({"msg": "Missing first name parameter"}), 400
    if not last_name:
        print('uri=/login error="Missing last name parameter"')
        return jsonify({"msg": "Missing last name parameter"}), 400

    if UserDetail.get_user_detail(username):
        result = UserDetail.update_user_detail(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
    else:
        return jsonify(message='User {} does not exist'.format(username)), 500

    if result:
        return jsonify(message='User {} detail update successful'.format(username)), 200
    else:
        return jsonify(message='User {} detail update failed'.format(username)), 500


@app.route('/get-user-dispositions', endpoint='get-user-dispositions', methods=['GET'])
@jwt_required(locations='cookies')
def get_user_dispositions():
    """
    Get dispositions for a specified user
    :return:
    """
    current_user = get_jwt_identity()

    if not current_user:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400

    result = UserDetail.get_user_dispositions(User.get_username_by_id(current_user))

    if result:
        return jsonify(message=result), 200
    else:
        return jsonify(message='User {} not found'.format(current_user)), 500


@app.route('/update-user-dispositions', endpoint='update-user-dispositions', methods=['POST'])
@jwt_required(locations='cookies')
def update_user_dispositions():
    """
    Update dispositions for a specific user
    :return:
    """
    current_user = get_jwt_identity()

    if not current_user:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400

    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = User.get_username_by_id(current_user)
    dispositions = request.json.get('dispositions', None)

    if not dispositions:
        print('uri=/login error="Missing dispositions parameter"')
        return jsonify({"msg": "Missing dispositions parameter"}), 400

    if UserDetail.get_user_detail(username):
        result = UserDetail.update_user_dispositions(
            username=username,
            dispositions=dispositions
        )
    else:
        return jsonify(message='User {} does not exist'.format(username)), 500

    if result:
        return jsonify(message='Dispositions for user {} updated successfully'.format(username)), 200
    else:
        return jsonify(message='User {} detail update failed'.format(username)), 500


@app.route('/get-shelters', endpoint='get_shelter', methods=['POST'])
def get_shelters():
    """
    Return a list of shelters
    :return:
    """
    pass


@app.route('/assign-user-to-shelter', endpoint='assign_user_to_shelter', methods=['POST'])
@jwt_required(locations='cookies')
def assign_user_to_shelter():
    """

    :return:
    """
    current_user = get_jwt_identity()

    if not current_user:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400

    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = User.get_username_by_id(current_user)
    shelter = request.json.get('shelter', None)
