from datetime import date, datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, SelectField, DateField, \
    TimeField, TextAreaField
from wtforms.validators import DataRequired, Length


class Login(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class PostStudent(FlaskForm):
    first_name = StringField('first name', validators=[DataRequired(), Length(min=1, max=64)])
    last_name = StringField('last name', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Add')


class PostStudentEdit(FlaskForm):
    first_name = StringField('first name', validators=[DataRequired(), Length(min=1, max=64)])
    last_name = StringField('last name', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Save')


class PostClassroom(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Add')


class PostClassroomEdit(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Save')


class PostAddStudentsToClassroom(FlaskForm):
    students = SelectField('Students', validators=[DataRequired()], render_kw={'autofocus': True})
    submit = SubmitField('Add')


class PostAddStudentsToUser(FlaskForm):
    students = SelectField('Students', validators=[DataRequired()])
    submit = SubmitField('Add')


class PostStudentContact(FlaskForm):
    contact_date = DateField('Contact Date', default=date.today, validators=[DataRequired()])
    contact_start_time = TimeField('Start Time', default=datetime.now(), validators=[DataRequired()])
    contact_end_time = TimeField('End Time', default=datetime.now(), validators=[DataRequired()])
    contact_types = SelectField('Contact Type', validators=[DataRequired()])
    services_offered = SelectField('Service Offered', validators=[DataRequired()])
    classroom_list = SelectField('Classes', validators=[DataRequired()])
    notes = TextAreaField('Additional Notes', validators=[Length(max=4000)])
    absent = BooleanField('Absent')
    submit = SubmitField('Add')

    def validate_times(self):
        if self.contact_start_time.data > self.contact_end_time.data:
            return False
        else:
            return True


class PostClassContact(FlaskForm):
    student_list = SelectMultipleField('Students', validators=[DataRequired()], id="select_student")
    absent_student_list = SelectMultipleField('Absent Students', id="select_absent")
    contact_date = DateField('Contact Date', default=date.today, validators=[DataRequired()])
    contact_start_time = TimeField('Start Time', default=datetime.now(), validators=[DataRequired()])
    contact_end_time = TimeField('End Time', default=datetime.now(), validators=[DataRequired()])
    contact_types = SelectField('Contact Type', validators=[DataRequired()])
    services_offered = SelectField('Service Offered', validators=[DataRequired()])
    notes = TextAreaField('Additional Notes', validators=[Length(max=4000)])
    submit = SubmitField('Add')

    def validate_times(self):
        if self.contact_start_time.data > self.contact_end_time.data:
            return False
        else:
            return True


class PostContactType(FlaskForm):
    name = StringField('Contact Type', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Add')


class PostContactTypeEdit(FlaskForm):
    name = StringField('Contact Type', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Save')


class PostServicesOffered(FlaskForm):
    name = StringField('Service Offered', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Add')


class PostServicesOfferedEdit(FlaskForm):
    name = StringField('Service Offered', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Save')


class PostEditContact(FlaskForm):
    contact_date = DateField('Contact Date', default=date.today, validators=[DataRequired()])
    contact_start_time = TimeField('Start Time', default=datetime.now(), validators=[DataRequired()])
    contact_end_time = TimeField('End Time', default=datetime.now(), validators=[DataRequired()])
    contact_types = SelectField('Contact Type', validators=[DataRequired()])
    services_offered = SelectField('Service Offered', validators=[DataRequired()])
    classroom_list = SelectField('Classes', validators=[DataRequired()])
    notes = TextAreaField('Additional Notes', validators=[Length(max=4000)])
    absent = BooleanField('Absent')
    submit = SubmitField('Save')

    def validate_times(self):
        if self.contact_start_time.data > self.contact_end_time.data:
            return False
        else:
            return True
