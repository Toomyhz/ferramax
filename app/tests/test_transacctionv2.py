import unittest
from unittest.mock import patch, MagicMock



class Mock_transaction:
    def __init__(self, options):
        self.options = options

    def create(self, buy_order, session_id, amount, return_url):
        return {
            'url': 'https://webpay3gint.transbank.cl/webpayserver/initTransaction',
            'token': 'mock_token'
        }

    def commit(self, token):
        return {
            'status': 'AUTHORIZED',
            'amount': 10000,
            'buy_order': 'order12345',
            'transaction_date': '2024-07-04T12:00:00Z',
            'card_detail': {'card_number': '**** **** **** 1234'},
            'accounting_date': '2024-07-04',
            'session_id': 'session123',
            'authorization_code': 'auth123'
        }    

def test_init_transaction(client,monkeypatch):
    monkeypatch.setattr('app.transbank.controllers.Transaction', Mock_transaction)

    response = client.post('/api/init_transaction/', json={"amount": 1000, "buy_order": "algo", "session_id": "algo", "return_url": "https://return.url"})
    response_data = response.get_json()

    assert response.status_code == 200
    assert response_data['url'] == 'https://webpay3gint.transbank.cl/webpayserver/initTransaction'
    assert response_data['token'] == 'mock_token'

def test_transaction_return(client,monkeypatch):
    monkeypatch.setattr('app.transbank.controllers.Transaction', Mock_transaction)

    response = client.post('/api/transaction_return/', json={"token_ws": "fake_token"})
    response_data = response.get_json()

    assert response.status_code == 200
    assert response_data['status'] == 'AUTHORIZED'
    assert response_data['amount'] == 10000
    assert response_data['buy_order'] == 'order12345'
    assert response_data['transaction_date'] == '2024-07-04T12:00:00Z'