import pytest
from flask import Flask
from app.suscription.validations import validarFromDatabase, validar_correo

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

def test_validarFormato_correcto():
    assert validar_correo("test@gmail.com") == True

def test_validarFormato_incorrecto():
    assert validar_correo("test") == False

def test_validarFromDatabase_correo_existente(app):
    with app.test_request_context():
        correo_existente = 'algo@gmail.com'
        result = validarFromDatabase(correo_existente)
        assert result.json == {'error': 'Email ya existe'}

def test_validarFromDatabase_correo_no_existente(app):
    with app.test_request_context():
        correo_existente = 'nuevocorreo333@gmail.com'
        result = validarFromDatabase(correo_existente)
        assert result.json == {'email_valido': correo_existente}