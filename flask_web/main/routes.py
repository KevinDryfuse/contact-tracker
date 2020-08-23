from flask import render_template, flash, redirect, url_for
from uuid import uuid4

from flask_web import db
from flask_web.main import bp
from flask_web.main.forms import Login, PostStudent
from flask_web.models import Student, User
from flask_login import current_user, login_user, logout_user, login_required


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
@login_required
def index():
    user = {"firstName": current_user.first_name, "lastName": current_user.last_name}
    return render_template("index.html", user=user)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route("/student", methods=["GET", 'POST'])
@login_required
def students():
    form = PostStudent()
    if form.validate_on_submit():
        uuid = str(uuid4())
        student = Student(external_id=uuid, first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main.students'))

    user = {"firstName": current_user.first_name, "lastName": current_user.last_name}
    s = Student.query.all()
    return render_template("students.html", title='Students', user=user, students=s, form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/student/<string:external_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_student(external_id):
    form = PostStudent()
    if form.validate_on_submit():
        db.session.query(Student).filter(Student.external_id == external_id).update({Student.first_name: form.first_name.data, Student.last_name: form.last_name.data}, synchronize_session=False)
        db.session.commit()
        return redirect(url_for('main.students'))

    user = {"firstName": current_user.first_name, "lastName": current_user.last_name}
    s = db.session.query(Student).filter(Student.external_id == external_id).one()
    form.first_name.data = s.first_name
    form.last_name.data = s.last_name

    return render_template("edit_student.html", title='Edit Student', user=user, student=s, form=form)


@bp.route('/student/<string:external_id>/delete', methods=['GET'])
@login_required
def delete_student(external_id):
    # Note, I don't want a delete endpoint like this really ... but I'm not sure how I want to handle it yet.
    db.session.query(Student).filter(Student.external_id == external_id).delete()
    db.session.commit()
    return redirect(url_for('main.students'))
