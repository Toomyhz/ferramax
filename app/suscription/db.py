from app import connection
from flask import jsonify
def saveDb(email,contrasena):
    cursor = connection.cursor()
    try:
        cursor.execute(f"insert into usuarios(correo,contrasenia_hash) values ('{email}','{contrasena}')")
        connection.commit()
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        return jsonify(email_valido=email), 200