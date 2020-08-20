import base64
import json

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from os import environ
import flask_web.auth.authentication as authentication

bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
    app.config["OIDC_COOKIE_SECURE"] = False
    app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
    app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
    app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
    app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
    app.config["OKTA_ORG_URL"] = environ.get("OKTA_ORG_URL")
    app.config["OKTA_AUTH_TOKEN"] = environ.get("OKTA_AUTH_TOKEN")

    authentication.oidc.init_app(app)
    bootstrap.init_app(app)

    from flask_web.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from flask_web.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from flask_web.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
