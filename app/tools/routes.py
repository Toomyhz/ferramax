from flask import request
from .controllers import  get_all_tools, get_tool, get_all_categories,get_all_marcas 
from app import app

@app.route('/tools/', methods=['GET'])
def get_tools_route():
    return get_all_tools()

@app.route('/tools/<id>', methods=['GET'])
def get_tool_route(id):
    return get_tool(id)

@app.route('/categories/', methods =['GET'])
def get_categories_route():
    return get_all_categories()

@app.route('/marcas/', methods =['GET'])
def get_marcas_route():
    return get_all_marcas()