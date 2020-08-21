from flask import Blueprint

bp = Blueprint('main', __name__)

from flask_web.main import routes
from flask_web.main import forms
