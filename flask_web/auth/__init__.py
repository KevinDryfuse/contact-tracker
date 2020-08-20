from flask import Blueprint

bp = Blueprint('auth', __name__)

from flask_web.auth import authentication
