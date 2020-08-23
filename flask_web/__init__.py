from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login = LoginManager()
login.login_view = 'main.login'
login.login_message = 'Please log in to access this page.'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    bootstrap.init_app(app)

    from flask_web.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from flask_web.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


from flask_web import models
