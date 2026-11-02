
from .models import Brand

def get_all_marcas():
    marcas = Brand.query.all()
    return marcas, 200

def get_marca(id):
    marca = Brand.query.get(id)
    return marca, 200