from app import app
from .controllers import transaction_start,transaction_end
from flask import request
from flask_cors import cross_origin

@cross_origin
@app.route('/api/init_transaction/', methods=['POST'])
def init_transaction():
    return transaction_start(request)

@app.route('/api/transaction_return', methods=['POST'])
def transaction_return():
    return transaction_end(request)