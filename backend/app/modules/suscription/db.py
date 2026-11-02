from app import connection
from flask import jsonify
def saveDb(email, contrasena):
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (correo, contrasenia_hash) VALUES (:email, :contrasena)",
            email=email,
            contrasena=contrasena,
        )
        connection.commit()  
    except Exception as e:
        raise Exception(e)
    finally:
        cursor.close()

def get_user_by_email(email):
    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT id_usuario, correo, contrasenia_hash FROM usuarios WHERE correo = :email",
            {"email": email}
        )
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "correo": row[1],
                "contrasenia_hash": row[2]
            }
        else:
            return None
    finally:
        cursor.close()