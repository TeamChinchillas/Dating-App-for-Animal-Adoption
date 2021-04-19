from animal_adoption import app, User, UserType, AnimalDisposition


def create_users():
    users = [
        {'username': 'user1', 'password': 'test1'},
        {'username': 'user2', 'password': 'test2'},
        {'username': 'user3', 'password': 'test3'},
    ]

    for user in users:
        new_user = User()
        new_user.create_user(user['username'], user['password'])


def create_user_types():
    user_types = [
        'adopter',
        'shelter worker',
        'administrator',
    ]

    for user_type in user_types:
        new_user_type = UserType()
        new_user_type.create_user_type(user_type)


def create_dispositions():
    dispositions = [
        'Good with other animals',
        'Good with children',
        'Animal must be leashed at all times'
    ]

    for disposition in dispositions:
        new_dispo = AnimalDisposition()
        new_dispo.create_disposition(disposition)


def initialize_db():
    create_users()
    create_user_types()
    create_dispositions()


if __name__ == '__main__':
    with app.app_context():
        initialize_db()
