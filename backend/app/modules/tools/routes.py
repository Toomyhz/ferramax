from flask import Blueprint, request, make_response
from .controllers import (get_all_tools, get_tool, create_tool, update_tool, 
                          delete_tool)

tools_bp = Blueprint('tools', __name__)

@tools_bp.route('/tools/', methods=['GET'])
def get_tools_route():
    response = get_all_tools()
    return response

@tools_bp.route('/tools/<id>', methods=['GET'])
def get_tool_route(id):
    return get_tool(id)


@tools_bp.route('/tools/', methods=['POST'])
def create_tool_route():
    data = request.get_json()
    return create_tool(data)

@tools_bp.route('/tools/<int:id>', methods=['PUT', 'PATCH'])
def update_tool_route(id):
    data = request.get_json()
    return update_tool(id, data)

@tools_bp.route('/tools/<int:id>', methods=['DELETE'])
def delete_tool_route(id):
    return delete_tool(id)
    
