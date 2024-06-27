from flask import request
from app import app
from .controllers import suscribe
@app.route('/suscribe/', methods=['POST'])
def suscribe_route():
    json = suscribe(request)
    return json