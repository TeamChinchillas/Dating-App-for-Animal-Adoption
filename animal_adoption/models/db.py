from animal_adoption import db
from werkzeug.security import generate_password_hash, \
     check_password_hash


adoption_relationship = db.Table(
    'RelationshipTable',
    db.Column('adopter_id', db.Integer, db.ForeignKey('AdoptersTable.id_adopters')),
    db.Column('animal_id', db.Integer, db.ForeignKey('AnimalsTable.id_animals'))
)


class Users(db.Model):
    __tablename__ = 'UsersTable'
    id_users = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    user_details_id = db.Column(db.Integer, db.ForeignKey('UserDetailsTable.id_user_details'))

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
        self.username = username
        self.hash_password(password)
        db.session.add(self)
        db.session.commit()

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

        user = Users.query.filter_by(username=username).first()
        if user is None:
            raise ValueError('User %s does not exist' % username)

        if not user.check_password(password):
            return False

        return True


class UserDetails(db.Model):
    __tablename__ = 'UserDetailsTable'
    id_user_details = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email_address = db.Column(db.String(32))
    user_type_id = db.Column(db.Integer, db.ForeignKey('UserTypeTable.id_user_type'))

    def __repr__(self):
        return '<First name {} Last Name {} email address {} user type {}>'.format(
            self.first_name,
            self.last_name,
            self.email_address,
            self.user_type_id
        )


class UserType(db.Model):
    __tablename__ = 'UserTypeTable'
    id_user_type = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(32))


class Adopters(db.Model):
    __tablename__ = 'AdoptersTable'
    id_adopters = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('UsersTable.id_users'))


class ShelterWorkers(db.Model):
    __tablename__ = 'ShelterWorkersTable'
    id_shelter_workers = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('UsersTable.id_users'))
    shelter_id = db.Column(db.Integer, db.ForeignKey('SheltersTable.id_shelters'))


class Administrators(db.Model):
    __tablename__ = 'AdministratorsTable'
    id_administrators = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('UsersTable.id_users'))


class Shelters(db.Model):
    __tablename__ = 'SheltersTable'
    id_shelters = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    physical_address = db.Column(db.String(32))
    phone_number = db.Column(db.String(32))
    email_address = db.Column(db.String(32))


class Animals(db.Model):
    __tablename__ = 'AnimalsTable'
    id_animals = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    age = db.Column(db.String(32))
    description_link = db.Column(db.String(32))
    image_link = db.Column(db.String(32))
    animal_species_id = db.Column(db.Integer, db.ForeignKey('AnimalSpeciesTable.id_animal_species'))
    adoption_status_id = db.Column(db.Integer, db.ForeignKey('AdoptionStatusTable.id_adoption_status'))
    animal_disposition_id = db.Column(db.Integer, db.ForeignKey('AnimalDispositionsTable.id_animal_dispositions'))
    shelter_id = db.Column(db.Integer, db.ForeignKey('SheltersTable.id_shelters'))


class AnimalDispositions(db.Model):
    __tablename__ = 'AnimalDispositionsTable'
    id_animal_dispositions = db.Column(db.Integer, primary_key=True)
    disposition = db.Column(db.String(32))


class AnimalSpecies(db.Model):
    __tablename__ = 'AnimalSpeciesTable'
    id_animal_species = db.Column(db.Integer, primary_key=True)
    animal_species = db.Column(db.String(32))
    animal_class_id = db.Column(db.Integer, db.ForeignKey('AnimalClassesTable.id_animal_classes'))


class AnimalClasses(db.Model):
    __tablename__ = 'AnimalClassesTable'
    id_animal_classes = db.Column(db.Integer, primary_key=True)
    animal_class = db.Column(db.String(32))


class AdoptionStatus(db.Model):
    __tablename__ = 'AdoptionStatusTable'
    id_adoption_status = db.Column(db.Integer, primary_key=True)
