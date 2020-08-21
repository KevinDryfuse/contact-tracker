from flask import render_template, flash, redirect, url_for
from uuid import uuid4

from flask_web import db
from flask_web.main import bp
from flask_web.main.forms import Login, PostStudent
from flask_web.models import Student


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    user = {"firstName": "Kevin", "lastName": "Dryfuse"}
    return render_template("index.html", user=user)


@bp.route("/student", methods=["GET"])
def students():
    user = {"firstName": "Kevin", "lastName": "Dryfuse"}
    s = Student.query.all()
    return render_template("students.html", user=user, students=s)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/student/add', methods=['GET', 'POST'])
def add_student():
    form = PostStudent()
    if form.validate_on_submit():
        uuid = str(uuid4())
        student = Student(external_id=uuid, first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main.students'))

    return render_template("poststudent.html", title='Home Page', form=form)