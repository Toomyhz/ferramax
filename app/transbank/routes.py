from app import app
from .controllers import transaction_start,transaction_end
from flask import request


@app.route('/api/init_transaction/', methods=['POST'])
def init_transaction():
    json = transaction_start(request)
    return json

@app.route('/api/transaction_return', methods=['POST'])
def transaction_return():
    json = transaction_end(request)
    return json