import sys
import os
from unittest.mock import Mock, patch
from flask import jsonify

# Agregar la raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.suscription.controllers import suscribe

def test_suscribe_empty_email():
    request = Mock()
    request.json = {'email': ''}
    response = suscribe(request)
    assert response[1] == 400
    assert response[0].json == {'error': 'Campo correo vacio'}

@patch('app.suscription.validations.validar_correo', return_value=False)
def test_suscribe_invalid_email(mock_validar_correo):
    request = Mock()
    request.json = {'email': 'invalid-email'}
    response = suscribe(request)
    assert response[1] == 205
    assert response[0].json == {'error': 'Correo electronico no valido'}

@patch('app.suscription.validations.validar_correo', return_value=True)
@patch('app.suscription.validations.validarFromDatabase')
@patch('app.suscription.db.saveDb')
def test_suscribe_valid_email(mock_saveDb, mock_validarFromDatabase, mock_validar_correo):
    request = Mock()
    request.json = {'email': 'test@example.com'}
    mock_validarFromDatabase.return_value = jsonify(email_valido='test@example.com')
    mock_saveDb.return_value = jsonify(email_valido='test@example.com'), 200

    response = suscribe(request)
    assert response[1] == 200
    assert response[0].json == {'email_valido': 'test@example.com'}
    mock_saveDb.assert_called_once_with('test@example.com')
