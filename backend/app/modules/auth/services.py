from werkzeug.security import generate_password_hash, check_password_hash
import app.modules.users.repository as user_repository
import app.modules.users.services as user_services
import jwt
from datetime import datetime, timedelta
from extensions import db

def create_user(data):
    email = data.get('email')

    if user_repository.get_user_by_email(email):
        raise ValueError("El correo ya está registrado")

    password_hash = generate_password_hash(data.get('password'))

    try:
        user = user_repository.create_user({
            "email": email,
            "password_hash": password_hash,
            "first_name": data.get('first_name'),
            "last_name": data.get('last_name'),
        })

        role = user_repository.get_role_by_name("Customer")
        if role is None:
            raise ValueError("Rol de cliente no encontrado")
        
        user_repository.assign_role(user, role)
        db.session.commit()
        return user

    except Exception as e:
        db.session.rollback()
        raise ValueError("Error al crear el usuario")
    


def login_user(data):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    email = data.get('email')
    contrasena = data.get('contrasena')

    if not email or not contrasena:
        return jsonify({"error": "Faltan campos"}), 400

    # Obtener usuario desde la BD
    user = get_user_by_email(email)
    if not user:
        return jsonify({"error": "Credenciales inválidas"}), 401

    hash_guardado = user['contrasenia_hash']

    if not check_password_hash(hash_guardado, contrasena):
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Crear token
    payload = {
        "user_id": user["id"],
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return jsonify({
        "token": token,
        "email": user["correo"],
        "user_id": user["id"]
    }), 200

