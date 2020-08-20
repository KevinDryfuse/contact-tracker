from flask import render_template
from flask_web.main import bp


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    user = {"firstName": "Kevin", "lastName": "Dryfuse"}
    return render_template("index.html", user=user)
