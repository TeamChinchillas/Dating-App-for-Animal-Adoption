import datetime
from flask.helpers import send_from_directory
from animal_adoption import app, Shelter, User, UserDetail, ShelterWorker, Adopter
from flask import jsonify, make_response, redirect, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, set_access_cookies, unset_access_cookies
)


app.config['JWT_SECRET_KEY'] = 'JofJtRHKzQmFRXGI4v60'
JWT_TOKEN_LOCATION = ['cookies']
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=1800)
JWT_COOKIE_NAME = "ACCESS-COOKIE"
jwt = JWTManager(app)


@app.route('/', endpoint='', methods=['GET'])
def index():
    """
    Index
    :return:
    """
    return send_from_directory(app.static_folder, 'index.html')


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
        response = jsonify(message='Login Succeeded!')
        set_access_cookies(response, access_token)
        return response
    else:
        return jsonify(message='Bad username or password'), 401


@app.route('/logout', endpoint='logout', methods=['GET'])
@jwt_required(locations='cookies')
def logout():
    """
    Logout
    :return:
    """
    response = jsonify(message='Logout Succeeded')
    unset_access_cookies(response)
    return response


# @app.route('/create-user', endpoint='create-user', methods=['POST'])
# def create_user():
#     """
#     Create a new user with the provided credentials
#     :return:
#     """
#     if not request.is_json:
#         print('uri=/login error="Missing JSON in request"')
#         return jsonify({"msg": "Missing JSON in request"}), 400
#
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#
#     if not username:
#         print('uri=/login error="Missing username parameter"')
#         return jsonify({"msg": "Missing username parameter"}), 400
#     if not password:
#         print('uri=/login error="Missing password parameter"')
#         return jsonify({"msg": "Missing password parameter"}), 400
#
#     new_user = User()
#     result = new_user.create_user(username=username, password=password)
#     if result:
#         return jsonify(message='User {} creation successful'.format(username)), 200
#     else:
#         return jsonify(message='User {} creation failed'.format(username)), 500


# @app.route('/create-user-with-details', endpoint='create_user_with_details', methods=['POST'])
# def create_user_with_details():
#     """
#     Create a new user with the provided credentials and details
#     :return:
#     """
#     if not request.is_json:
#         print('uri=/login error="Missing JSON in request"')
#         return jsonify({"msg": "Missing JSON in request"}), 400
#
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     first_name = request.json.get('first_name', None)
#     last_name = request.json.get('last_name', None)
#     user_type = request.json.get('user_type', None)
#     shelter_name = request.json.get('shelter_name', None)
#
#     if not username:
#         print('uri=/login error="Missing username parameter"')
#         return jsonify({"msg": "Missing username parameter"}), 400
#     if not password:
#         print('uri=/login error="Missing password parameter"')
#         return jsonify({"msg": "Missing password parameter"}), 400
#     if not first_name:
#         print('uri=/login error="Missing first name parameter"')
#         return jsonify({"msg": "Missing first name parameter"}), 400
#     if not last_name:
#         print('uri=/login error="Missing last name parameter"')
#         return jsonify({"msg": "Missing last name parameter"}), 400
#     if not user_type:
#         print('uri=/login error="Missing user type parameter"')
#         return jsonify({"msg": "Missing user type parameter"}), 400
#     if user_type == 'shelter worker':
#         if not shelter_name:
#             print('uri=/login error="Missing shelter name parameter for shelter worker"')
#             return jsonify({"msg": "Missing shelter name parameter for shelter worker"}), 400
#
#     new_user = User()
#     create_user_result = new_user.create_user(username=username, password=password)
#
#     existing_user_detail = UserDetail.get_user_detail(username)
#
#     if not existing_user_detail:
#         new_user_detail = UserDetail()
#         create_user_detail_result = new_user_detail.create_user_detail(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             user_type=user_type
#         )
#
#         if user_type == 'shelter worker':
#             pass
#
#         if create_user_result and create_user_detail_result:
#             return jsonify(message='User account and details for {} created successfully'.format(username)), 200
#     else:
#         return jsonify(message='User account and details for {} failed'.format(username)), 500


@app.route('/create-user-with-all-details', endpoint='create_user_with_all_details', methods=['POST'])
def create_user_with_all_details():
    """
    Create a new user with the provided credentials and details
    :return:
    """
    if not request.is_json:
        print('uri=/login error="Missing JSON in request"')
        return jsonify({"msg": "Missing JSON in request"}), 400

    # return jsonify({"msg": str(request)}), 417
    print(request.json)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    first_name = request.json.get('firstName', None)
    last_name = request.json.get('lastName', None)
    user_type = request.json.get('userType', None)
    shelter_name = request.json.get('shelterName', None)
    dispositions = request.json.get('dispositions', None)
    good_with_animals = request.json.get('goodWithAnimals', None)
    good_with_children = request.json.get('goodWithChildren', None)
    animal_leashed = request.json.get('animalLeashed', None)
    animal_preference = request.json.get('animalPreference', None)

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
    if user_type == 'shelter worker':
        if not shelter_name:
            print('uri=/login error="Missing shelter name parameter for shelter worker"')
            return jsonify({"msg": "Missing shelter name parameter for shelter worker"}), 400

    response = {
        'create_user_result': False,
        'create_user_detail_result': False,
        'assign user as adopter': False,
        'assign_user_to_shelter': False,
        'assign_dispositions': False,
        'animal_preference': False
    }

    new_user = User()
    create_user_result = new_user.create_user(username=username, password=password)

    response['create_user_result'] = create_user_result

    existing_user_detail = UserDetail.get_user_detail(username)

    if not existing_user_detail:
        new_user_detail = UserDetail()
        create_user_detail_result = new_user_detail.create_user_detail(
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type
        )
        response['create_user_detail_result'] = create_user_detail_result

    if user_type == 'adopter':
        try:
            assign_adopter_result = Adopter.assign_user_by_username(username)
            response['assign user as adopter'] = assign_adopter_result
        except Exception as e:
            return jsonify(message=e), 500

        if animal_preference:
            try:
                adopter = Adopter.get_adopter_by_name(username)
                assign_animal_preference_result = adopter.assign_animal_preference_by_name(animal_preference)
                response['animal_preference'] = assign_animal_preference_result
            except Exception as e:
                return jsonify(message=e), 501
        else:
            return jsonify(message='Animal preference required for adopter'), 502
    elif user_type == 'shelter worker':
        if shelter_name:
            assign_shelter_worker_result = ShelterWorker.assign_user_by_username(username, shelter_name)
            response['assign_user_to_shelter'] = assign_shelter_worker_result
            if assign_shelter_worker_result:
                print('User {} assigned to shelter {}'.format(username, shelter_name))
    else:
        return jsonify(message='User type {} not found'.format(user_type)), 503

    if not dispositions:
        dispositions = []
        if good_with_animals:
            dispositions.append('Good with other animals')
        if good_with_children:
            dispositions.append('Good with children')
        if animal_leashed:
            dispositions.append('Animal must be leashed at all times')

    if UserDetail.get_user_detail(username):
        try:
            dispo_result = UserDetail.update_user_dispositions(
                username=username,
                dispositions=dispositions
            )
            response['assign_dispositions'] = dispo_result
        except Exception as e:
            return jsonify(message=e), 504
    else:
        response['assign_dispositions'] = False

    if response['create_user_result'] and response['create_user_detail_result']:
        return jsonify(message=response), 200
    else:
        return jsonify(message=response), 505


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
    try:
        result = UserDetail.get_printable_user_detail(username)
    except Exception as e:
        return jsonify(message=e), 500

    try:
        animal_preference = Adopter.get_animal_preference(username)
        result['animalPreference'] = animal_preference
    except Exception as e:
        return jsonify(message=e), 500

    try:
        dispositions = UserDetail.get_user_dispositions(User.get_username_by_id(current_user))
        result['dispositions'] = dispositions['dispositions']
    except Exception as e:
        return jsonify(message=e), 500

    if result:
        return jsonify(message=result), 200
    else:
        return jsonify(message='User {} not found'.format(username)), 500


# @app.route('/create-user-details', endpoint='create-user-details', methods=['POST'])
# @jwt_required(locations='cookies')
# def create_user_details():
#     """
#     Create user details for new user
#     :return:
#     """
#     current_user = get_jwt_identity()
#
#     if not current_user:
#         print('uri=/login error="Missing username parameter"')
#         return jsonify({"msg": "Missing username parameter"}), 400
#
#     if not request.is_json:
#         print('uri=/login error="Missing JSON in request"')
#         return jsonify({"msg": "Missing JSON in request"}), 400
#
#     username = User.get_username_by_id(current_user)
#     first_name = request.json.get('first_name', None)
#     last_name = request.json.get('last_name', None)
#     user_type = request.json.get('user_type', None)
#
#     if not username:
#         print('uri=/login error="User {} not found"'.format(username))
#         return jsonify({"msg": "User {} not found".format(username)}), 400
#     if not first_name:
#         print('uri=/login error="Missing first name parameter"')
#         return jsonify({"msg": "Missing first name parameter"}), 400
#     if not last_name:
#         print('uri=/login error="Missing last name parameter"')
#         return jsonify({"msg": "Missing last name parameter"}), 400
#     if not user_type:
#         print('uri=/login error="Missing user type parameter"')
#         return jsonify({"msg": "Missing user type parameter"}), 400
#
#     existing_user_detail = UserDetail.get_user_detail(username)
#
#     if not existing_user_detail:
#         new_user_detail = UserDetail()
#         result = new_user_detail.create_user_detail(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             user_type=user_type
#         )
#         if result:
#             return jsonify(message='User details for {} created successfully'.format(username)), 200
#     else:
#         return jsonify(message='User details for {} failed'.format(username)), 500


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

    username = request.json.get('username', None)
    first_name = request.json.get('firstName', None)
    last_name = request.json.get('lastName', None)
    dispositions = request.json.get('dispositions', None)
    good_with_animals = request.json.get('goodWithAnimals', None)
    good_with_children = request.json.get('goodWithChildren', None)
    animal_leashed = request.json.get('animalLeashed', None)
    animal_preference = request.json.get('animalPreference', None)


    if not username:
        print('uri=/login error="Missing username parameter"')
        return jsonify({"msg": "Missing username parameter"}), 400
    if not first_name:
        print('uri=/login error="Missing first name parameter"')
        return jsonify({"msg": "Missing first name parameter"}), 400
    if not last_name:
        print('uri=/login error="Missing last name parameter"')
        return jsonify({"msg": "Missing last name parameter"}), 400

    response = {
        'update_user_detail_result': False,
        'update_dispositions': False,
        'update_preference': False
    }

    if UserDetail.get_user_detail(User.get_username_by_id(current_user)):
        result = UserDetail.update_user_detail(
            current_user,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        if result:
            response['update_user_detail_result'] = result

    if animal_preference:
        adopter = Adopter.get_adopter_by_name(username)
        assign_animal_preference_result = adopter.assign_animal_preference_by_name(animal_preference)
        response['animal_preference'] = assign_animal_preference_result

    if not dispositions:
        dispositions = []
        if good_with_animals:
            dispositions.append('Good with other animals')
        if good_with_children:
            dispositions.append('Good with children')
        if animal_leashed:
            dispositions.append('Animal must be leashed at all times')

    if UserDetail.get_user_detail(username):
        dispo_result = UserDetail.update_user_dispositions(
            username=username,
            dispositions=dispositions
        )
        response['assign_dispositions'] = dispo_result
    else:
        response['assign_dispositions'] = False

    if response['update_user_detail_result'] or response['update_dispositions'] or response['update_preference']:
        return jsonify(message=response), 200
    else:
        return jsonify(message=response), 500


# @app.route('/get-user-dispositions', endpoint='get-user-dispositions', methods=['GET'])
# @jwt_required(locations='cookies')
# def get_user_dispositions():
#     """
#     Get dispositions for a specified user
#     :return:
#     """
#     current_user = get_jwt_identity()
#
#     if not current_user:
#         print('uri=/login error="Missing username parameter"')
#         return jsonify({"msg": "Missing username parameter"}), 400
#
#     result = UserDetail.get_user_dispositions(User.get_username_by_id(current_user))
#
#     if result:
#         return jsonify(message=result), 200
#     else:
#         return jsonify(message='User {} not found'.format(current_user)), 500


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


@app.route('/get-shelters', endpoint='get_shelter', methods=['GET'])
def get_shelters():
    """
    Return a list of shelters with details
    :return:
    """
    shelters = Shelter.get_shelters()

    if shelters:
        return jsonify(message=shelters), 200
    else:
        return jsonify(message='Failed to get shelters'), 500


@app.route('/assign-user-to-shelter', endpoint='assign_user_to_shelter', methods=['POST'])
@jwt_required(locations='cookies')
def assign_user_to_shelter():
    """
    Route to assign a logged in user to a shelter
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
    shelter_name = request.json.get('shelter_name', None)

    if not shelter_name:
        print('uri=/assign-user-to-shelter error="Missing shelter parameter"')
        return jsonify({"msg": "Missing shelter parameter"}), 400

    result = ShelterWorker.assign_user_by_username(username, shelter_name)

    if result:
        return jsonify(message='User {} assigned to shelter {} successfully'.format(username, shelter_name)), 200
    else:
        return jsonify(message='User {} assignment to shelter {} failed'.format(username, shelter_name)), 500
