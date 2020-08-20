from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    from flask_web.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from flask_web.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
