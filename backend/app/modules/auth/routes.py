from flask import request, Blueprint, jsonify
from .services import create_user, login_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
@auth_bp.route('/register/', methods=['POST'])
def register_user():
    data = request.get_json()
    user = create_user(data)
    
    return jsonify({"message": "Usuario creado exitosamente", "user": user}), 201

@auth_bp.route('/login/', methods=['POST','OPTIONS'])
def login_user_route():
    if request.method == 'OPTIONS':
        return '', 200 
    return login_user(request)