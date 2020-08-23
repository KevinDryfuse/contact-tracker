from operator import attrgetter, and_

from flask import render_template, flash, redirect, url_for
from uuid import uuid4


from flask_web import db
from flask_web.main import bp
from flask_web.main.forms import Login, PostStudent, PostClassroom, PostAddStudentsToClassroom, PostAddStudentsToUser
from flask_web.models import Student, User, Classroom
from flask_login import current_user, login_user, logout_user, login_required


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
@login_required
def index():
    user = {"firstName": current_user.first_name, "lastName": current_user.last_name}
    return render_template("index.html", user=user)

# TODO: Do this later, this is not MVP .. however would like to update user info and update profile pic and stuff
# @bp.route('/profile', methods=["GET", "POST"])
# @login_required
# def user():
#     user = User.query.filter_by(User.id==current_user.id).first_or_404()
#
#     return render_template('user.html', user=user, posts=posts)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route("/students", methods=["GET", 'POST'])
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


@bp.route('/students/<string:external_id>/edit', methods=['GET', 'POST'])
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


@bp.route('/students/<string:external_id>/delete', methods=['GET'])
@login_required
def delete_student(external_id):
    # Note, I don't want a delete endpoint like this really ... but I'm not sure how I want to handle it yet.
    db.session.query(Student).filter(Student.external_id == external_id).delete()
    db.session.commit()
    return redirect(url_for('main.students'))


@bp.route("/classes", methods=["GET", 'POST'])
@login_required
def classrooms():
    form = PostClassroom()
    if form.validate_on_submit():
        uuid = str(uuid4())
        classroom = Classroom(external_id=uuid, name=form.name.data, user_id=current_user.id)
        db.session.add(classroom)
        db.session.commit()
        return redirect(url_for('main.classrooms'))

    user = {"firstName": current_user.first_name, "lastName": current_user.last_name}
    c = Classroom.query.filter(Classroom.user_id == current_user.id)
    return render_template("classrooms.html", title='Classrooms', user=user, classrooms=c, form=form)


@bp.route('/classes/<string:external_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_classroom(external_id):
    form = PostClassroom()
    if form.validate_on_submit():
        db.session.query(Classroom).filter(Classroom.external_id == external_id).update({Classroom.name: form.name.data}, synchronize_session=False)
        db.session.commit()
        return redirect(url_for('main.classrooms'))

    user = {"firstName": current_user.first_name, "lastName": current_user.last_name}
    c = db.session.query(Classroom).filter(Classroom.external_id == external_id).one()
    form.name.data = c.name

    return render_template("edit_classroom.html", title='Edit Class', user=user, classroom=c, form=form)


@bp.route('/classes/<string:external_id>/delete', methods=['GET'])
@login_required
def delete_classroom(external_id):
    # Note, I don't want a delete endpoint like this really ... but I'm not sure how I want to handle it yet.
    db.session.query(Classroom).filter(Classroom.external_id == external_id).delete()
    db.session.commit()
    return redirect(url_for('main.classrooms'))


@bp.route('/classes/<string:external_id>/addstudents', methods=['GET', 'POST'])
@login_required
def add_students_to_classroom(external_id):
    user = {"firstName": current_user.first_name, "lastName": current_user.last_name}
    form = PostAddStudentsToClassroom()
    c = Classroom.query.filter(and_(Classroom.user_id == current_user.id, Classroom.external_id == external_id)).one()
    u = db.session.query(User).filter(User.id == current_user.id).one()
    available_students = list(set(u.students) - set(c.students))
    available_students.sort(key=attrgetter('last_name', 'first_name'))
    form.students.choices = [(g.id, str(g.id) + " - " + g.last_name + ", " + g.first_name) for g in available_students]
    form.students.choices.insert(0, ('', 'Select One'))
    if form.validate_on_submit():
        student = db.session.query(Student).filter(Student.id == form.students.data).one()
        c.students.append(student)
        db.session.add(c)
        db.session.commit()
        return redirect('/classes/' + external_id + '/addstudents')

    return render_template("manage_classroom.html", title='Add Students to Class', user=user, classroom=c, students=c.students, form=form)


@bp.route("/classes/<string:classroom_external_id>/students/<string:student_external_id>/remove", methods=["GET"])
@login_required
def remove_student_from_classroom(classroom_external_id, student_external_id):
    c = db.session.query(Classroom).filter(and_(Classroom.user_id == current_user.id, Classroom.external_id == classroom_external_id)).one()
    s = db.session.query(Student).filter(Student.external_id == student_external_id).one()
    c.students.remove(s)
    db.session.add(c)
    db.session.commit()
    return redirect('/classes/' + classroom_external_id + '/addstudents')


@bp.route("/mystudents", methods=["GET", 'POST'])
@login_required
def my_students():
    user = {"firstName": current_user.first_name, "lastName": current_user.last_name}
    form = PostAddStudentsToUser()
    u = db.session.query(User).filter(User.id == current_user.id).one()
    s = u.students
    available_students = list(set(db.session.query(Student).all()) - set(u.students))
    available_students.sort(key=attrgetter('last_name', 'first_name'))
    form.students.choices = [(g.id, str(g.id) + " - " + g.last_name + ", " + g.first_name) for g in available_students]
    form.students.choices.insert(0, ('', 'Select One'))
    if form.validate_on_submit():
        student = db.session.query(Student).filter(Student.id == form.students.data).one()
        u.students.append(student)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('main.my_students'))

    return render_template("mystudents.html", title='Students', user=user, students=s, form=form)


@bp.route("/mystudents/<string:external_id>/remove", methods=["GET"])
@login_required
def remove_student_from_user(external_id):
    u = db.session.query(User).filter(User.id == current_user.id).one()
    s = db.session.query(Student).filter(Student.external_id == external_id).one()
    u.students.remove(s)
    classrooms = db.session.query(Classroom).filter(Classroom.user_id == current_user.id).all()
    for c in classrooms:
        if s in c.students:
            c.students.remove(s)
            db.session.add(c)
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('main.my_students'))
