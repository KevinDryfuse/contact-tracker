from flask import render_template
from flask_web.main import bp

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    user = {'firstname': 'Kevin', 'lastname': 'Dryfuse'}
    return render_template("index.html", user=user)