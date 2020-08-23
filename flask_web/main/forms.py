from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, Length


class Login(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class PostStudent(FlaskForm):
        first_name = StringField('first name', validators=[
            DataRequired(), Length(min=1, max=64)])
        last_name = StringField('last name', validators=[
            DataRequired(), Length(min=1, max=64)])
        submit = SubmitField('Submit')


class PostClassroom(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Submit')


class PostAddStudentsToClassroom(FlaskForm):
    students = SelectField('Students')
    submit = SubmitField('Submit')


class PostAddStudentsToUser(FlaskForm):
    students = SelectField('Students')
    submit = SubmitField('Submit')


class PostStudentContact(FlaskForm):
    submit = SubmitField('Submit')


class PostContactType(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Submit')


class PostServicesOffered(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Submit')

