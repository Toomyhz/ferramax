from flask import request
from .controllers import create_user
from app import app

@app.route('/users/', methods=['POST'])
def create_user_route():
    return create_user(request)