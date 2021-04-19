from animal_adoption import db
from werkzeug.security import generate_password_hash, \
     check_password_hash


adoption_relationship = db.Table(
    'AdoptionRelationshipTable',
    db.Column('adopter_id', db.Integer, db.ForeignKey('AdopterTable.id_adopter')),
    db.Column('animal_id', db.Integer, db.ForeignKey('AnimalTable.id_animal'))
)

disposition_relationship = db.Table(
    'DispositionRelationshipTable',
    db.Column('adopter_id', db.Integer, db.ForeignKey('AdopterTable.id_adopter')),
    db.Column('disposition_id', db.Integer, db.ForeignKey('AnimalDispositionTable.id_animal_disposition'))
)


class User(db.Model):
    __tablename__ = 'UserTable'
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    user_detail_id = db.Column(db.Integer, db.ForeignKey('UserDetailTable.id_user_detail'))

    def __init__(self):
        self.username = None
        self.password_hash = None

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def create_user(self, username, password):
        """
        Create a new user and hash the password
        :param username:
        :param password:
        :return:
        """
        if not User.get_id_by_username(username):
            self.username = username
            self.hash_password(password)
            db.session.add(self)
            db.session.commit()
        else:
            print('Username \'{}\' already exists'.format(username))

    def hash_password(self, password):
        """
        Hash password and store it in instance variable
        :param password:
        :return:
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check that user provided password when hashed matches the saved password hash
        :param password:
        :return:
        """
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def authenticate_user(username, password):
        """
        Check if the user exists in the database and verify the hash of the
        supplied password matches the hash in the database
        :param username:
        :param password:
        :return:
        """
        if username is None or password is None:
            raise ValueError('Username and password may not be empty')

        user = User.query.filter_by(username=username).first()
        if user is None:
            raise ValueError('User %s does not exist' % username)

        if not user.check_password(password):
            return False

        return True

    @staticmethod
    def get_id_by_username(username):
        user = User.query.filter_by(username=username).first()
        if user:
            return user.id_user
        else:
            return None


class UserDetail(db.Model):
    __tablename__ = 'UserDetailTable'
    id_user_detail = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email_address = db.Column(db.String(32))
    user_type_id = db.Column(db.Integer, db.ForeignKey('UserTypeTable.id_user_type'))
    animal_disposition_id = db.Column(db.Integer, db.ForeignKey('AnimalDispositionTable.id_animal_disposition'))

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email_address = None
        self.user_type_id = None
        # self.animal_disposition_id = None

    def __repr__(self):
        return '<First name {} Last Name {} email address {} user type {}>'.format(
            self.first_name,
            self.last_name,
            self.email_address,
            self.user_type_id
        )

    @staticmethod
    def get_user_detail(username):
        user_detail = UserDetail.query.filter_by(id_user_detail=User.get_id_by_username(username)).first()
        return user_detail

    def update_user_detail(self, first_name, last_name, email_address, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.user_type_id = UserType.get_user_type_id_by_name(user_type)
        # self.animal_disposition_id = AnimalDisposition.get_animal_disposition_id_by_name(animal_disposition)


class UserType(db.Model):
    __tablename__ = 'UserTypeTable'
    id_user_type = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(32))

    def __init__(self):
        self.user_type = None

    def __repr__(self):
        return '<UserType {}>'.format(self.user_type)

    def create_user_type(self, name):
        user_type_record = UserType.get_user_type_id_by_name(name)
        if not user_type_record:
            self.user_type = name
            db.session.add(self)
            db.session.commit()
        else:
            print('User type \'{}\' already exists'.format(name))

    @staticmethod
    def get_user_type_id_by_name(user_type_name):
        user_type_record = UserType.query.filter_by(user_type=user_type_name).first()
        if user_type_record:
            return user_type_record.id_user_type
        else:
            return None


class Adopter(db.Model):
    __tablename__ = 'AdopterTable'
    id_adopter = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('UserTable.id_user'))


class ShelterWorker(db.Model):
    __tablename__ = 'ShelterWorkerTable'
    id_shelter_worker = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('UserTable.id_user'))
    shelter_id = db.Column(db.Integer, db.ForeignKey('ShelterTable.id_shelter'))


class Administrator(db.Model):
    __tablename__ = 'AdministratorTable'
    id_administrator = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('UserTable.id_user'))


class Shelter(db.Model):
    __tablename__ = 'ShelterTable'
    id_shelter = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    physical_address = db.Column(db.String(32))
    phone_number = db.Column(db.String(32))
    email_address = db.Column(db.String(32))


class Animal(db.Model):
    __tablename__ = 'AnimalTable'
    id_animal = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    age = db.Column(db.String(32))
    description_link = db.Column(db.String(32))
    image_link = db.Column(db.String(32))
    animal_species_id = db.Column(db.Integer, db.ForeignKey('AnimalSpeciesTable.id_animal_species'))
    adoption_status_id = db.Column(db.Integer, db.ForeignKey('AdoptionStatusTable.id_adoption_status'))
    animal_disposition_id = db.Column(db.Integer, db.ForeignKey('AnimalDispositionTable.id_animal_disposition'))
    shelter_id = db.Column(db.Integer, db.ForeignKey('ShelterTable.id_shelter'))


class AnimalDisposition(db.Model):
    __tablename__ = 'AnimalDispositionTable'
    id_animal_disposition = db.Column(db.Integer, primary_key=True)
    disposition = db.Column(db.String(32))

    def __init__(self):
        self.disposition = None

    def create_disposition(self, name):
        if not AnimalDisposition.get_animal_disposition_id_by_name(name):
            self.disposition = name
            db.session.add(self)
            db.session.commit()
        else:
            print('Animal disposition \'{}\' already exists'.format(name))

    @staticmethod
    def get_animal_disposition_id_by_name(disposition_name):
        animal_disposition_record = AnimalDisposition.query.filter_by(disposition=disposition_name).first()
        if animal_disposition_record:
            return animal_disposition_record.id_animal_disposition
        else:
            return None


class AnimalSpecies(db.Model):
    __tablename__ = 'AnimalSpeciesTable'
    id_animal_species = db.Column(db.Integer, primary_key=True)
    animal_species = db.Column(db.String(32))
    animal_class_id = db.Column(db.Integer, db.ForeignKey('AnimalClassTable.id_animal_class'))


class AnimalClass(db.Model):
    __tablename__ = 'AnimalClassTable'
    id_animal_class = db.Column(db.Integer, primary_key=True)
    animal_class = db.Column(db.String(32))


class AdoptionStatus(db.Model):
    __tablename__ = 'AdoptionStatusTable'
    id_adoption_status = db.Column(db.Integer, primary_key=True)
