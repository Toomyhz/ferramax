import re
from app import connection
from flask import jsonify

def validar_correo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None

def validarFromDatabase(correo):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT correo FROM usuarios WHERE correo = '{correo}'")
        rows = cursor.fetchall()
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
    
    if len(rows) > 0:
        return jsonify(error="El correo ya existe en la base de datos")
    elif len(rows) == 0:
        return jsonify(email_valido=correo)