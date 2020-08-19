from flask import Blueprint

bp = Blueprint('main', __name__)

from flask_web.main import routes