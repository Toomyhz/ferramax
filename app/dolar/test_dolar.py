import pytest
from flask import Flask
from app.dolar.getDolar import getDolar

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

def testGetDolar():
    test_date= "2024-01-02"
    assert getDolar(test_date)== '877.12'