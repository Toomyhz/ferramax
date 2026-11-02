from flask import jsonify
from app import connection

def get_all_marcas():
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT id_marca, marca, imagen FROM marcas")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return jsonify(MARCAS = data), 200
    except Exception as e:                                                                                             
        return jsonify({'error': str(e)}), 500                   
    finally:
        cursor.close()

def get_marca(id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT id_marca, marca, imagen FROM marcas WHERE id_marca = {id}")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        if data == []:
            raise Exception(f"No se encontro ninguna marca con el id {id}")
        else:
            return jsonify(data), 200
    except Exception as e:                                                                                             
        return jsonify({'error': str(e)}), 500                   
    finally:
        cursor.close()