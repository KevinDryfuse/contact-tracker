from flask import render_template

from flask_web import app


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    user = {'firstname': 'Kevin', 'lastname': 'Dryfuse'}
    return render_template("index.html", user=user)