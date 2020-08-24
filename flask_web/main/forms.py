from datetime import date, datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, SelectField, DateField, \
    TimeField, TextField, TextAreaField
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
    students = SelectField('Students', validators=[
        DataRequired()])
    submit = SubmitField('Submit')


class PostAddStudentsToUser(FlaskForm):
    students = SelectField('Students', validators=[
        DataRequired()])
    submit = SubmitField('Submit')


class PostStudentContact(FlaskForm):
    contact_date = DateField('Contact Date', default=date.today, validators=[
        DataRequired()])
    contact_start_time = TimeField('Contact Start Time', default=datetime.now(), validators=[
        DataRequired()])
    contact_end_time = TimeField('Contact End Time', default=datetime.now(), validators=[
        DataRequired()])
    contact_types = SelectField('Contact Type', validators=[
        DataRequired()])
    services_offered = SelectField('Service Offered', validators=[
        DataRequired()])
    notes = TextAreaField('Additional Notes', validators=[Length(max=4000)])
    submit = SubmitField('Submit')

    def validate_times(self):
        if self.contact_start_time.data > self.contact_end_time.data:
            return False
        else:
            return True


class PostClassContact(FlaskForm):
    student_list = SelectMultipleField('Students', validators=[DataRequired()])
    contact_date = DateField('Contact Date', default=date.today, validators=[
        DataRequired()])
    contact_start_time = TimeField('Contact Start Time', default=datetime.now(), validators=[
        DataRequired()])
    contact_end_time = TimeField('Contact End Time', default=datetime.now(), validators=[
        DataRequired()])
    contact_types = SelectField('Contact Type', validators=[
        DataRequired()])
    services_offered = SelectField('Service Offered', validators=[
        DataRequired()])
    notes = TextAreaField('Additional Notes', validators=[Length(max=4000)])
    submit = SubmitField('Submit')

    def validate_times(self):
        if self.contact_start_time.data > self.contact_end_time.data:
            return False
        else:
            return True

class PostContactType(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Submit')


class PostServicesOffered(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Submit')
