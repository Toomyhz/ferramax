from app import connection
from flask import jsonify
def saveDb(email):
    cursor = connection.cursor()
    try:
        cursor.execute(f"insert into suscripciones values ('{email}')")
        connection.commit()
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        return jsonify(email_valido=email), 200