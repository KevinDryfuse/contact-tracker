from flask_web import db
from flask_login import UserMixin
from flask_web import login
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(36), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    @validates('email')
    def convert_lower(self, key, value):
        return value.lower()

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(36), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    def __repr__(self):
        return '<Student {} {}>'.format(self.first_name, self.last_name)