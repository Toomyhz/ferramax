from .controllers import get_all_marcas, get_marca
from flask import Blueprint

brands_bp = Blueprint('brands', __name__, url_prefix='/brands')

@brands_bp.route('/', methods =['GET'])
def get_marcas_route():
    return get_all_marcas()

@brands_bp.route('/<id>', methods=['GET'])
def get_marca_route(id):
    return get_marca(id)