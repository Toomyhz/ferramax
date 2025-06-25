import re
from app import connection
from flask import jsonify

def validar_correo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None

def validarFromDatabase(correo):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT 1 FROM usuarios WHERE correo = :correo", correo=correo)
        existe = cursor.fetchone()
        return existe is None  # True si NO existe
    except Exception as e:
        raise Exception(e)
    finally:
        cursor.close()