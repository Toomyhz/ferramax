from .controllers import get_all_categories
from flask import Blueprint, request, make_response

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/categories/', methods =['GET'])
def get_categories_route():
    response = get_all_categories()
    return response