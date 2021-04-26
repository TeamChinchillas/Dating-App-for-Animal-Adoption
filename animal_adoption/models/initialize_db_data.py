from animal_adoption import app, User, UserType, UserDetail, Disposition, Shelter


def create_users():
    users = [
        {'username': 'johndoe@abc.com', 'password': 'test1'},
        {'username': 'jimdoe@abc.com', 'password': 'test2'},
        {'username': 'jeandoe@abc.com', 'password': 'test3'},
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
            'username': 'johndoe@abc.com',
            'first_name': 'john',
            'last_name': 'doe',
            'user_type': 'adopter'
        },
        {
            'username': 'janedoe@abc.com',
            'first_name': 'jane',
            'last_name': 'doe',
            'user_type': 'adopter'
        },
        {
            'username': 'jimdoe@abc.com',
            'first_name': 'jim',
            'last_name': 'doe',
            'user_type': 'invalid'
        },
        {
            'username': 'jimdoe@abc.com',
            'first_name': 'jim',
            'last_name': 'doe',
            'user_type': 'shelter worker'
        },
        {
            'username': 'jeandoe@abc.com',
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


def create_shelters():
    shelters = [
        {
            'name': 'Critters and Creatures',
            'physical_address': '123 Bark Ave',
            'phone_number': '123-456-7890',
            'email_address': 'info@candc.com'
        },
        {
            'name': 'Creature Comforts',
            'physical_address': '555 Feline Way',
            'phone_number': '999-867-5309',
            'email_address': 'adopt@creaturecomforts.com'
        },
        {
            'name': 'Save a Pet',
            'physical_address': '789 Rover Pkwy',
            'phone_number': '111-222-3456',
            'email_address': 'rescue@saveapet.com'
        }
    ]

    for shelter in shelters:
        new_shelter = Shelter()
        result = new_shelter.create_new_shelter(
            shelter['name'],
            shelter['physical_address'],
            shelter['phone_number'],
            shelter['email_address']
        )
        print('Create new shelter {}: {}'.format(shelter['name'], result))


def initialize_db():
    print('Creating users')
    create_users()
    print('Creating user types')
    create_user_types()
    print('Creating dispositions')
    create_dispositions()
    print('Creating user details')
    create_user_details()
    print('Updating user details')
    update_user_details()
    print('Creating shelters')
    create_shelters()


if __name__ == '__main__':
    with app.app_context():
        initialize_db()
