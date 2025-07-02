from flask import request, make_response
from .controllers import (get_all_tools, get_tool, get_all_categories,
                          get_all_marcas, get_marca,create_tool, update_tool, 
                          delete_tool,get_marca)
from app import app

@app.route('/tools/', methods=['GET'])
def get_tools_route():
    response = get_all_tools()
    return response

@app.route('/tools/<id>', methods=['GET'])
def get_tool_route(id):
    return get_tool(id)

@app.route('/categories/', methods =['GET'])
def get_categories_route():
    response = make_response(get_all_categories())
    return response

@app.route('/marcas/', methods =['GET'])
def get_marcas_route():
    return get_all_marcas()

@app.route('/marcas/<id>', methods=['GET'])
def get_marca_route(id):
    return get_marca(id)

@app.route('/tools/', methods=['POST'])
def create_tool_route():
    data = request.get_json()
    return create_tool(data)

@app.route('/tools/<int:id>', methods=['PUT', 'PATCH'])
def update_tool_route(id):
    data = request.get_json()
    return update_tool(id, data)

@app.route('/tools/<int:id>', methods=['DELETE'])
def delete_tool_route(id):
    return delete_tool(id)
