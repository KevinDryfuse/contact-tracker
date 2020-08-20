from flask import render_template, g
from flask_web.main import bp
import flask_web.auth.authentication as authentication


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
@authentication.oidc.require_login
def index():
    user = authentication.okta_client.get_user(g.user.id)
    return render_template("index.html", user=user)


@bp.before_request
def before_request():
    """
    Load a user object into `g.user` before each request.
    """
    if authentication.oidc.user_loggedin:
        g.user = authentication.okta_client.get_user(authentication.oidc.user_getfield("sub"))
    else:
        g.user = None