import re
from app import connection
from flask import jsonify

def validar_correo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None

def validarFromDatabase(correo):
    cursor = connection.cursor()
    temp_row = []
    try:
        cursor.execute(f"SELECT correo FROM SUSCRIPCIONES")
        rows = cursor.fetchall()
        for i in rows:
            temp_row.append((i[0]))
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
    
    if correo in temp_row:
        return jsonify(error='Email ya existe')

    else:
        return jsonify(email_valido=correo)
        