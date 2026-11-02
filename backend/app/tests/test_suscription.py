
import pytest
from flask import jsonify
from unittest.mock import patch, MagicMock


#Mockear la función que valida el correo en la base de datos
def mock_validarFromDatabase(email):
    mock_db = MagicMock()
    temp_row = ["algo@gmail.com", "test@gmail.com"]
    if email in temp_row:
        mock_db.cursor().execute.return_value = jsonify(error='Email ya existe')
    else:
        mock_db.cursor().execute.return_value = jsonify(email_valido=email)
    return mock_db.cursor().execute()

# Mock para simular el guardado de un correo electrónico en la base de datos
def mock_cargarDb(email):
    mock_db = MagicMock()
    mock_db.cursor().execute.return_value = jsonify(email_valido=email)
    return mock_db.cursor().execute()


def test_suscribe_valid_email(client, monkeypatch):
    # Correo válido
    test_email = "nuevovalido@gmail.com"


    # Aplicar el patch para usar el mock
    monkeypatch.setattr('app.suscription.controllers.saveDb', mock_cargarDb)
    monkeypatch.setattr('app.suscription.controllers.validarFromDatabase', mock_validarFromDatabase)

    # Realizar la solicitud POST con el correo válido
    response = client.post('/suscribe/', json={'email': test_email})
    response_data = response.get_json()

    # Verificar que la respuesta sea correcta
    assert response.status_code == 200
    assert response_data == {'email_valido': test_email}

def test_suscribe_exist_email(client, monkeypatch):
    # Correo válido
    test_email = "algo@gmail.com"

    # Aplicar el patch para usar el mock
    monkeypatch.setattr('app.suscription.controllers.saveDb', mock_cargarDb)
    monkeypatch.setattr('app.suscription.controllers.validarFromDatabase', mock_validarFromDatabase)

    # Realizar la solicitud POST con el correo válido
    response = client.post('/suscribe/', json={'email': test_email})
    response_data = response.get_json()

    # Verificar que la respuesta sea correcta
    assert response.status_code == 200
    assert response_data == {'error': 'Email ya existe'}

def test_suscribe_invalid_email_format(client):
    # Correo con formato inválido
    test_email = "correo_invalido.com"
    response = client.post('/suscribe/', json={'email': test_email})
    response_data = response.get_json()
    assert response.status_code == 200
    assert response_data == {'error': 'Correo electronico no valido'}


def test_suscribe_empty_email(client):
    # Correo con campo vacío
    test_email = ""
    response = client.post('/suscribe/', json={'email': test_email})
    response_data = response.get_json()
    assert response.status_code == 200
    assert response_data == {'error': 'Campo correo vacio'}
