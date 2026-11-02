from flask import jsonify
def get_all_categories():
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT id_categoria, categoria FROM categorias")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return jsonify(CATEGORIAS = data), 200
    except Exception as e:                                                                                             
        return jsonify({'error': str(e)}), 500                   
    finally:
        cursor.close()