from animal_adoption import app, User, UserType, UserDetail, Disposition


def create_users():
    users = [
        {'username': 'johndoe@a.com', 'password': 'test1'},
        {'username': 'jimdoe@a.com', 'password': 'test2'},
        {'username': 'jeandoe@a.com', 'password': 'test3'},
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


def create_user_details():
    user_details = [
        {
            'username': 'johndoe@a.com',
            'first_name': 'john',
            'last_name': 'doe',
            'user_type': 'adopter'
        },
        {
            'username': 'janedoe@a.com',
            'first_name': 'jane',
            'last_name': 'doe',
            'user_type': 'adopter'
        },
        {
            'username': 'jimdoe@a.com',
            'first_name': 'jim',
            'last_name': 'doe',
            'user_type': 'invalid'
        },
        {
            'username': 'jimdoe@a.com',
            'first_name': 'jim',
            'last_name': 'doe',
            'user_type': 'shelter_worker'
        },
        {
            'username': 'jeandoe@a.com',
            'first_name': 'jean',
            'last_name': 'doe',
            'user_type': 'administrator'
        }
    ]

    for user_detail in user_details:
        new_user_detail = UserDetail()
        new_user_detail.create_user_detail(
            user_detail['username'],
            user_detail['first_name'],
            user_detail['last_name'],
            user_detail['user_type']
        )


def update_user_details():
    user_updates = [
        {
            'username': 'johndoe@abc.com',
            'first_name': 'john',
            'last_name': 'doe',
            'dispositions': []
        },
        {
            'username': 'janedoe@a.com',
            'first_name': 'jane',
            'last_name': 'doe',
            'dispositions': []
        },
        {
            'username': 'jimdoe@abc.com',
            'first_name': 'jim',
            'last_name': 'doe',
            'dispositions': ['Good with other animals']
        },
        {
            'username': 'jeandoe@abc.com',
            'first_name': 'jean',
            'last_name': 'doe',
            'dispositions': []
        }
    ]

    for user_update in user_updates:
        UserDetail.update_user_detail(
            user_update['username'],
            user_update['first_name'],
            user_update['last_name'],
            user_update['dispositions']
        )
        print(UserDetail.get_user_detail(user_update['username']))
        print(UserDetail.get_user_dispositions(user_update['username']))


def create_dispositions():
    dispositions = [
        'Good with other animals',
        'Good with children',
        'Animal must be leashed at all times'
    ]

    for disposition in dispositions:
        new_dispo = Disposition()
        new_dispo.create_disposition(disposition)


def initialize_shelters():
    pass


def initialize_db():
    create_users()
    create_user_types()
    create_dispositions()
    create_user_details()
    update_user_details()
    initialize_shelters()


if __name__ == '__main__':
    with app.app_context():
        initialize_db()
