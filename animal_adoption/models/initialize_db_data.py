from animal_adoption import app, User, UserType, UserDetail, Disposition


def create_users():
    users = [
        {'username': 'user0', 'password': 'test0'},
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


def create_user_details():
    user_details = [
        {
            'username': 'user1',
            'first_name': 'john',
            'last_name': 'doe',
            'email_address': 'johndoe@a.com',
            'user_type': 'adopter'
        },
        {
            'username': 'user0',
            'first_name': 'jane',
            'last_name': 'doe',
            'email_address': 'janedoe@a.com',
            'user_type': 'adopter'
        },
        {
            'username': 'user2',
            'first_name': 'jim',
            'last_name': 'doe',
            'email_address': 'jimdoe@a.com',
            'user_type': 'invalid'
        },
        {
            'username': 'user2',
            'first_name': 'jim',
            'last_name': 'doe',
            'email_address': 'jimdoe@a.com',
            'user_type': 'shelter_worker'
        },
        {
            'username': 'user3',
            'first_name': 'jean',
            'last_name': 'doe',
            'email_address': 'jeandoe@a.com',
            'user_type': 'administrator'
        }
    ]

    for user_detail in user_details:
        new_user_detail = UserDetail()
        new_user_detail.create_user_detail(
            user_detail['username'],
            user_detail['first_name'],
            user_detail['last_name'],
            user_detail['email_address'],
            user_detail['user_type']
        )


def update_user_details():
    user_updates = [
        {
            'username': 'user1',
            'first_name': 'john',
            'last_name': 'doe',
            'email_address': 'johndoe@abc.com',
            'dispositions': []
        },
        {
            'username': 'user0',
            'first_name': 'jane',
            'last_name': 'doe',
            'email_address': 'janedoe@a.com',
            'dispositions': []
        },
        {
            'username': 'user2',
            'first_name': 'jim',
            'last_name': 'doe',
            'email_address': 'jimdoe@abc.com',
            'dispositions': ['Good with other animals']
        },
        {
            'username': 'user3',
            'first_name': 'jean',
            'last_name': 'doe',
            'email_address': 'jeandoe@abc.com',
            'dispositions': []
        }
    ]

    for user_update in user_updates:
        UserDetail.update_user_detail(
            user_update['username'],
            user_update['first_name'],
            user_update['last_name'],
            user_update['email_address'],
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


def initialize_db():
    create_users()
    create_user_types()
    create_user_details()
    update_user_details()
    create_dispositions()


if __name__ == '__main__':
    with app.app_context():
        initialize_db()
