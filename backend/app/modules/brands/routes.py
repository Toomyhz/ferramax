from .controllers import get_all_marcas, get_marca
from flask import Blueprint, request, make_response

brands_bp = Blueprint('brands', __name__)

@brands_bp.route('/marcas/', methods =['GET'])
def get_marcas_route():
    return get_all_marcas()

@brands_bp.route('/marcas/<id>', methods=['GET'])
def get_marca_route(id):
    return get_marca(id)