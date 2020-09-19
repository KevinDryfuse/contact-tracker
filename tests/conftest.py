import pytest
from flask_web import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
