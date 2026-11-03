from flask import request, Blueprint, jsonify
from marshmallow import ValidationError

from app.modules.auth.schemas import RegisterSchema
from app.modules.auth.services import create_user, login_user

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
register_schema = RegisterSchema()


@auth_bp.route('/register/', methods=['POST'])
def register_user():
    try:
        data = register_schema.load(request.get_json() or {})
        user = create_user(data)
        return jsonify({"message": "Usuario creado correctamente", "user_id": user.id}), 201
    except ValidationError as e:
        return jsonify({"message": "Error al crear el usuario", "errors": e.messages}), 400

@auth_bp.route('/login/', methods=['POST','OPTIONS'])
def login_user_route():
    if request.method == 'OPTIONS':
        return '', 200 
    return login_user(request)