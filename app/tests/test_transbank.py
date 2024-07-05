import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, json

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_transaction_start(client):
    payload = {
        'amount': 10000,
        'buy_order': '123456',
        'session_id': 'abc123',
        'return_url': 'https://return.url'
    }
    headers = {'Content-Type': 'application/json'}

    with patch('app.transbank.controllers.Transaction.create') as mock_create:
        mock_create.return_value = {
            'url': 'https://payment.url',
            'token': 'fake_token'
        }

        response = client.post('/api/init_transaction/', data=json.dumps(payload), headers=headers)
        print(response.data)
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data['url'] == 'https://payment.url'
        assert data['token'] == 'fake_token'
        mock_create.assert_called_once_with('123456', 'abc123', 10000, 'https://return.url')


def test_transaction_end(client):
    payload = {'token_ws': 'fake_token'}
    headers = {'Content-Type': 'application/json'}

    with patch('app.transbank.controllers.Transaction.commit') as mock_commit:
        mock_commit.return_value = {
            'status': 'AUTHORIZED',
            'amount': 10000,
            'authorization_code': 'abc123',
            'transaction_date': '2022-01-01T12:00:00Z',
            'buy_order': '123456',
            'card_detail': {'card_number': '**** **** **** 1234'},
            'accounting_date': '2022-01-01',
            'session_id': 'abc123'
        }

        response = client.post('/api/transaction_return', data=json.dumps(payload), headers=headers)
        print (type(response.data))
        
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data['status'] == 'AUTHORIZED'
        assert data['amount'] == 10000
        assert data['authorization_code'] == 'abc123'
        assert data['transaction_date'] == '2022-01-01T12:00:00Z'
        assert data['buy_order'] == '123456'
        assert data['card_detail'] == {'card_number': '**** **** **** 1234'}
        assert data['accounting_date'] == '2022-01-01'
        assert data['session_id'] == 'abc123'
        mock_commit.assert_called_once_with('fake_token')