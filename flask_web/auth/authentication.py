from os import environ
from flask_web.auth import bp

from flask import redirect, current_app, url_for
from flask_oidc import OpenIDConnect
from okta import UsersClient

oidc = OpenIDConnect()
okta_client = UsersClient(environ.get("OKTA_ORG_URL"), environ.get("OKTA_AUTH_TOKEN"))


@bp.route("/login")
@oidc.require_login
def login():
    """
    Force the user to login, then redirect them to the dashboard.
    """
    return redirect(url_for("main.index"))


@bp.route("/profile")
@oidc.require_login
def profile():
    profile_request = current_app.config['OKTA_ORG_URL'] + "/enduser/settings"
    return redirect(profile_request)

# @bp.route("/logout", methods=["GET"])
# @oidc.require_login
# def logout():
#     """
#     Log the user out of their account.
#     """
#     from oauth2client.client import OAuth2Credentials
#     print(oidc.credentials_store)
#     id_token = OAuth2Credentials.from_json(oidc.credentials_store[g.oidc_id_token.get('sub')]).access_token
#     print(id_token)
#     base_url = "when this works, get this from the env file"
#     logout_request = base_url + "/oauth2/v1/logout?id_token_hint=" + str(id_token)
#     oidc.logout()
#     return redirect(logout_request)
