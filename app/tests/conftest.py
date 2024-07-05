# conftest.py

import pytest
from flask import Flask
from unittest.mock import patch, MagicMock
from app.suscription.routes import suscribe_route

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    app.add_url_rule('/suscribe/', view_func=suscribe_route, methods=['POST'])
    return app

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='module', autouse=True)
def mock_db_connect():
    with patch('app.connect') as mock_connect:
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "Tool1", "Description1"),
            (2, "Tool2", "Description2")
        ]
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection
        yield mock_connect
