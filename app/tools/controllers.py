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
        return jsonify(TOOLS = data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()

def get_tool(id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT id_herramienta, nombre, valor, imagen FROM herramientas where id_herramienta = {id}")
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