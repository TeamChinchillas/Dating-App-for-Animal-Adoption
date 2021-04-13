from .. import db


class Users(db.Model):
    __tablename__ = 'UsersTable'
    id_users = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(128))
    user_details_id = db.Column(db.Integer, db.ForeignKey('UserDetailsTable.id_user_details'))


class UserDetails(db.Model):
    __tablename__ = 'UserDetailsTable'
    id_user_details = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email_address = db.Column(db.String(32))
    user_type_id = db.Column(db.Integer, db.ForeignKey('UserTypeTable.id_user_type'))


class UserType(db.Model):
    __tablename__ = 'UserTypeTable'
    id_user_type = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(32))
