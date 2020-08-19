from flask import Blueprint

bp = Blueprint('errors', __name__)

from flask_web.errors import handlers
