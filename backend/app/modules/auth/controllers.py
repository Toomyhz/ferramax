from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..suscription.validations import validar_correo, validarFromDatabase
from ..suscription.db import saveDb, get_user_by_email

import jwt
from datetime import datetime, timedelta

def create_user(request):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    email = data.get('email')
    contrasena = data.get('contrasena')

    if not email or not contrasena:
        return jsonify({"error": "Faltan email o contraseña"}), 400

    # Validar formato del correo
    if not validar_correo(email):
        return jsonify({"error": "Correo electrónico no válido"}), 400

    # Verificar si el correo ya existe en la base de datos
    try:
        email_disponible = validarFromDatabase(email)  # devuelve True si está disponible
    except Exception as e:
        return jsonify({"error": f"Error de base de datos: {str(e)}"}), 500

    if not email_disponible:
        return jsonify({"error": "El correo ya existe en la base de datos"}), 409

    # Generar hash seguro de la contraseña
    contrasena_segura = generate_password_hash(contrasena)

    # Guardar en la base de datos
    try:
        saveDb(email, contrasena_segura)
        return jsonify({"message": "Usuario creado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": f"No se pudo guardar el usuario: {str(e)}"}), 500
    


SECRET_KEY = "supersecreto"  # Usa algo fuerte y almacénalo con seguridad

def login_user(request):
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

