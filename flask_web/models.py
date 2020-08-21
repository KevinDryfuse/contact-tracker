from flask_web import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(36), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(36), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    def __repr__(self):
        return '<Student {} {}>'.format(self.first_name, self.last_name)