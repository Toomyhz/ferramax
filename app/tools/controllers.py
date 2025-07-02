from flask import jsonify
from app import connection
from app.dolar.dolar import Dolar


def get_all_tools():
    cursor = connection.cursor()
    try: 
        cursor.execute("SELECT id_herramienta, nombre, valor, imagen, cantidad, c.categoria ,id_marca,h.id_categoria FROM HERRAMIENTAS h JOIN CATEGORIAS c ON h.id_categoria = c.id_categoria")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        dolar = Dolar().value
        for tool in data:
            price = tool['VALOR']
            key = "VALOR_EN_DOLARES"
            value = round(price/float(dolar),2)
            tool[key] = value
        return jsonify(TOOLS = data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()

def get_tool(id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT id_herramienta, nombre, valor, imagen, cantidad, id_categoria, id_marca FROM herramientas where id_herramienta = {id}")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        if data == []:
            raise Exception(f"No se encontro ninguna herramienta con el id {id}")
        else:
            return jsonify(data), 200
    except Exception as e:                                                                                             
        return jsonify({'error': str(e)}), 500                   
    finally:
        cursor.close()

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

def create_tool(data):
    cursor = connection.cursor()
    try:
        # Validar datos necesarios, ejemplo: nombre, valor, id_categoria, id_marca, cantidad
        required = ['nombre', 'valor', 'id_categoria', 'id_marca', 'cantidad']
        if not all(key in data for key in required):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        cursor.execute("""
            INSERT INTO herramientas (
            nombre, valor, imagen, cantidad, id_categoria, id_marca
            ) VALUES (
              :nombre, :valor, :imagen, :cantidad, :id_categoria, :id_marca
            )
            """, {
                'nombre': data['nombre'],
                'valor': data['valor'],
                'id_categoria': data['id_categoria'],
                'id_marca': data['id_marca'],
                'cantidad': data['cantidad'],
                'imagen': data.get('imagen')  # puede ser null o string URL
            })
        connection.commit()
        return jsonify({"message": "Herramienta creada"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()

def update_tool(id, data):
    cursor = connection.cursor()
    try:
        # Puedes armar dinámicamente la consulta si quieres o actualizar todos los campos
        cursor.execute("""
            UPDATE herramientas
            SET nombre = :nombre,
                valor = :valor,
                id_categoria = :id_categoria,
                id_marca = :id_marca,
                cantidad = :cantidad,
                imagen = :imagen
            WHERE id_herramienta = :id
        """, {
            'nombre': data.get('nombre'),
            'valor': data.get('valor'),
            'id_categoria': data.get('id_categoria'),
            'id_marca': data.get('id_marca'),
            'cantidad': data.get('cantidad'),
            'imagen': data.get('imagen'),
            'id': id
        })
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Herramienta no encontrada"}), 404
        return jsonify({"message": "Herramienta actualizada"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()

def delete_tool(id):
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM herramientas WHERE id_herramienta = :id", {'id': id})
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Herramienta no encontrada"}), 404
        return jsonify({"message": "Herramienta eliminada"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
