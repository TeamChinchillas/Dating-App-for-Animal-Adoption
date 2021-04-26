from animal_adoption import db
from flask_sqlalchemy import inspect
from werkzeug.security import generate_password_hash, \
     check_password_hash


user_disposition_relationship = db.Table(
    'UserDispositionRelationshipTable',
    db.Column('user_detail_id', db.Integer, db.ForeignKey('UserDetailTable.id_user_detail')),
    db.Column('disposition_id', db.Integer, db.ForeignKey('DispositionTable.id_disposition'))
)

animal_disposition_relationship = db.Table(
    'AnimalDispositionRelationshipTable',
    db.Column('animal_id', db.Integer, db.ForeignKey('AnimalTable.id_animal')),
    db.Column('disposition_id', db.Integer, db.ForeignKey('DispositionTable.id_disposition'))
)


class User(db.Model):
    __tablename__ = 'UserTable'
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))

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
            return True
        else:
            print('Username \'{}\' already exists'.format(username))
            return False

    @staticmethod
    def get_id_by_username(username):
        user = User.query.filter_by(username=username).first()
        if user:
            return user.id_user
        else:
            return None

    @staticmethod
    def get_username_by_id(user_id):
        user = User.query.filter_by(id_user=user_id).first()
        if user:
            return user.username
        else:
            return None

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


class UserDetail(db.Model):
    __tablename__ = 'UserDetailTable'
    id_user_detail = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    user_id = db.Column(db.Integer, db.ForeignKey('UserTable.id_user'))
    user_type_id = db.Column(db.Integer, db.ForeignKey('UserTypeTable.id_user_type'))
    user_dispositions = db.relationship(
        'Disposition',
        secondary=user_disposition_relationship
    )

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.user_id = None
        self.user_type_id = None

    def __repr__(self):
        return '<Name: {} {} id: {} type: {} dispositions: {}>'.format(
            self.first_name,
            self.last_name,
            self.user_id,
            self.user_type_id,
            self.user_dispositions
        )

    @staticmethod
    def object_as_dict(obj):
        return {column.key: getattr(obj, column.key) for column in inspect(obj).mapper.column_attrs}

    @staticmethod
    def get_user_detail(username):
        user_detail = UserDetail.query.filter_by(id_user_detail=User.get_id_by_username(username)).first()
        return user_detail

    @staticmethod
    def get_user_dispositions(username):
        disposition_list = []
        user_detail = UserDetail.get_user_detail(username)
        if user_detail:
            for user_disposition in user_detail.user_dispositions:
                if user_disposition:
                    disposition_list.append(user_disposition.disposition)

        return {'dispositions': disposition_list}

    def create_user_detail(self, username, first_name, last_name, user_type):
        self.user_id = User.get_id_by_username(username)
        self.user_type_id = UserType.get_user_type_id_by_name(user_type)
        if not UserDetail.get_user_detail(username):
            if self.user_id:
                if self.user_type_id:
                    if not UserDetail.get_user_detail(username):
                        self.first_name = first_name
                        self.last_name = last_name
                        db.session.add(self)
                        db.session.commit()
                        return True
                    else:
                        print('User detail for \'{}\' already exists'.format(username))
                else:
                    print('User type \'{}\' does not exist'.format(user_type))
            else:
                print('Username \'{}\' not found'.format(username))
        else:
            print('Detail for username \'{}\' already exists'.format(username))

        return False

    @staticmethod
    def update_user_detail(username, first_name=None, last_name=None, dispositions=None):
        changed = False
        if not first_name and not last_name and not dispositions:
            print('No fields to update')
        user_detail = UserDetail.get_user_detail(username)
        if user_detail:
            if first_name:
                if user_detail.first_name != first_name:
                    changed = True
                    user_detail.first_name = first_name
            if last_name:
                if user_detail.last_name != last_name:
                    changed = True
                    user_detail.last_name = last_name
            if dispositions:
                for disposition in dispositions:
                    changed = True
                    dispo = Disposition.get_disposition_by_name(disposition)
                    user_detail.user_dispositions.append(dispo)
            if changed:
                db.session.add(user_detail)
                db.session.commit()
                return True
            else:
                print('No changes made for \'{}\''.format(username))
                return True
        else:
            print('Username\'{}\' not found to update details'.format(username))

        return False

    @staticmethod
    def update_user_dispositions(username, dispositions):
        user_detail = UserDetail.get_user_detail(username)
        existing_dispositions = UserDetail.get_user_dispositions(username)
        for existing_disposition in existing_dispositions['dispositions']:
            if existing_disposition not in dispositions:
                dispo = Disposition.get_disposition_by_name(existing_disposition)
                user_detail.user_dispositions.remove(dispo)
        for disposition in dispositions:
            dispo = Disposition.get_disposition_by_name(disposition)
            user_detail.user_dispositions.append(dispo)
        db.session.add(user_detail)
        db.session.commit()

        return True


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
    shelter_id = db.Column(db.Integer, db.ForeignKey('ShelterTable.id_shelter'))
    adopter_id = db.Column(db.Integer, db.ForeignKey('AdopterTable.id_adopter'))
    animal_dispositions = db.relationship(
        'Disposition',
        secondary=animal_disposition_relationship
    )


class Disposition(db.Model):
    __tablename__ = 'DispositionTable'
    id_disposition = db.Column(db.Integer, primary_key=True)
    disposition = db.Column(db.String(32))

    def __init__(self):
        self.disposition = None

    def create_disposition(self, name):
        if not Disposition.get_disposition_by_name(name):
            self.disposition = name
            db.session.add(self)
            db.session.commit()
        else:
            print('Animal disposition \'{}\' already exists'.format(name))

    @staticmethod
    def get_disposition_by_name(disposition_name):
        disposition_record = Disposition.query.filter_by(disposition=disposition_name).first()
        if disposition_record:
            return disposition_record
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
