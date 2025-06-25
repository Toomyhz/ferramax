from flask import request
from .controllers import create_user, login_user
from app import app

@app.route('/users/register/', methods=['POST'])
def create_user_route():
    return create_user(request)

@app.route('/users/login/', methods=['POST','OPTIONS'])
def login_route():
    if request.method == 'OPTIONS':
        return '', 200  # respuesta válida para preflight
    return login_user(request)