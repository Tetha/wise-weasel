
from flask import Flask
from flask.testing import FlaskClient
import pytest

import wise_weasel


@pytest.fixture()
def app() -> Flask:
    return wise_weasel.app

@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()