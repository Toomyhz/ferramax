import unittest
from unittest.mock import patch, MagicMock
from app.transbank.controllers import transaction_start, transaction_end


@patch('app.transbank.controllers.Transaction.create')
def testcrear_transaccion(mock_create):
    # Simular respuesta de Transbank
    return {
        'url': 'https://webpay3gint.transbank.cl/webpayserver/initTransaction',
        'token': 'mock_token'
    }

def test_init_transaction(client):
    response = client.post('/api/init_transaction/', json={"amount": 1000, "buy_order": "", "session_id": "", "return_url": ""})
    response_data = response.get_json()

    assert response.status_code == 200
    assert response_data['url'] == 'https://webpay3gint.transbank.cl/webpayserver/initTransaction'
    assert response_data['token'] == 'mock_token'

@patch('app.transbank.controllers.Transaction.commit')
def test_confirmar_transaccion(mock_commit,client):
    # Simular respuesta de Transbank
    mock_commit.return_value = {
        'status': 'AUTHORIZED',
        'amount': 10000,
        'buy_order': 'order12345',
        'transaction_date': '2024-07-04T12:00:00Z'
    }

    response = transaction_end(client)
    response.data = response.get_json()
    assert response.status_code == 200

    assert response['status'] == 'AUTHORIZED'
    assert response['amount'] == 10000
    assert response['buy_order'] == 'order12345'