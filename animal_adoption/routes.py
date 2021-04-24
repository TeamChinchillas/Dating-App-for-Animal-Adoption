from animal_adoption import app, User, UserDetail
from flask import jsonify, request


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
        return jsonify(message='User {} authentication successful'.format(username)), 200
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


@app.route('/get-user-details', endpoint='get-user-details', methods=['GET'])
def get_user_details():
    """
    Get details for a specified user
    :return:
    """
    username = request.args.get('user')

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400

    result = UserDetail.get_user_detail(username)

    if result:
        return jsonify(message=UserDetail.object_as_dict(result)), 200
    else:
        return jsonify(message='User {} not found'.format(username)), 500


@app.route('/get-user-dispositions', endpoint='get-user-dispositions', methods=['GET'])
def get_user_dispositions():
    """
    Get dispositions for a specified user
    :return:
    """
    username = request.args.get('user')

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400

    result = UserDetail.get_user_dispositions(username)

    if result:
        return jsonify(message=result), 200
    else:
        return jsonify(message='User {} not found'.format(username)), 500


@app.route('/create-user-details', endpoint='create-user-details', methods=['POST'])
def create_user_details():
    """
    Create user details for new user
    :return:
    """
    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    email_address = request.json.get('email_address', None)
    user_type = request.json.get('user_type', None)

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400
    if not first_name:
        print('uri=/login error="Missing first name parameter"')
        return jsonify({"msg": "Missing first name parameter"}), 400
    if not last_name:
        print('uri=/login error="Missing last name parameter"')
        return jsonify({"msg": "Missing last name parameter"}), 400
    if not email_address:
        print('uri=/login error="Missing email address parameter"')
        return jsonify({"msg": "Missing email address parameter"}), 400
    if not user_type:
        print('uri=/login error="Missing user type parameter"')
        return jsonify({"msg": "Missing user type parameter"}), 400

    if not UserDetail.get_user_detail(username):
        new_user_detail = UserDetail()
        result = new_user_detail.create_user_detail(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            user_type=user_type
        )
    else:
        return jsonify(message='Detail record already exists for {}'.format(username)), 500

    if result:
        return jsonify(message='User {} creation successful'.format(username)), 200
    else:
        return jsonify(message='User {} creation failed'.format(username)), 500


@app.route('/update-user-details', endpoint='update-user-details', methods=['POST'])
def update_user_details():
    """
    Update details for user that does exist
    :return:
    """
    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    email_address = request.json.get('email_address', None)

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400
    if not first_name:
        print('uri=/login error="Missing first name parameter"')
        return jsonify({"msg": "Missing first name parameter"}), 400
    if not last_name:
        print('uri=/login error="Missing last name parameter"')
        return jsonify({"msg": "Missing last name parameter"}), 400
    if not email_address:
        print('uri=/login error="Missing email address parameter"')
        return jsonify({"msg": "Missing email address parameter"}), 400

    if UserDetail.get_user_detail(username):
        result = UserDetail.update_user_detail(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email_address=email_address
        )
    else:
        return jsonify(message='User {} does not exist'.format(username)), 500

    if result:
        return jsonify(message='User {} detail update successful'.format(username)), 200
    else:
        return jsonify(message='User {} detail update failed'.format(username)), 500


@app.route('/update-user-dispositions', endpoint='update-user-dispositions', methods=['POST'])
def update_user_dispositions():
    """
    Update dispositions for a specific user
    :return:
    """
    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    dispositions = request.json.get('dispositions', None)

    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400
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
