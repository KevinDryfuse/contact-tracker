import enum

from sqlalchemy import Table, Column, Integer, ForeignKey

from flask_web import db
from flask_login import UserMixin
from flask_web import login
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates, relationship

classroom_student_association_table = Table('classroom_student', db.Model.metadata,
                                            Column('classroom_id', Integer, ForeignKey('classroom.id')),
                                            Column('student_id', Integer, ForeignKey('student.id'))
                                            )

user_student_association_table = Table('user_student', db.Model.metadata,
                                            Column('user_id', Integer, ForeignKey('user.id')),
                                            Column('student_id', Integer, ForeignKey('student.id'))
                                            )


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
    classrooms = db.relationship('Classroom', backref='Teacher', lazy='select')
    students = relationship(
        "Student",
        secondary=user_student_association_table,
        back_populates="users",
        lazy='select')
    contacts = relationship("Contact", back_populates="user")

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
    classrooms = relationship(
        "Classroom",
        secondary=classroom_student_association_table,
        back_populates="students", lazy='select')
    users = relationship(
        "User",
        secondary=user_student_association_table,
        back_populates="students", lazy='select')
    contacts = relationship("Contact", back_populates="student")

    def __repr__(self):
        return '<Student {} {}>'.format(self.first_name, self.last_name)


class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(36), index=True, unique=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    students = relationship(
        "Student",
        secondary=classroom_student_association_table,
        back_populates="classrooms",
        lazy='select')

    def __repr__(self):
        return '<Class {}>'.format(self.name)


class ContactType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(36), index=True, unique=True)
    name = db.Column(db.String(64))
    # TODO: Description?

    def __repr__(self):
        return '<Contact Type {}>'.format(self.name)


class ServiceOffered(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(36), index=True, unique=True)
    name = db.Column(db.String(64))
    # TODO: Description?

    def __repr__(self):
        return '<Service Offered {}>'.format(self.name)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(36), index=True, unique=True)
    student_id = db.Column(Integer, ForeignKey('student.id'))
    student = relationship("Student", back_populates="contacts")
    user_id = db.Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="contacts")
    contact_date = db.Column(db.Date())
    contact_start_time = db.Column(db.Time())
    contact_end_time = db.Column(db.Time())
    service_offered = db.Column(db.String(64))  # Why not a direct relationship?! Because I want to preserve history
    contact_type = db.Column(db.String(64))
    notes = db.Column(db.Text)


