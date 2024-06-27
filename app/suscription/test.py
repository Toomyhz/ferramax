from unittest.mock import Mock, patch
from flask import jsonify


from validations import validar_correo, validarFromDatabase

def testSuma():
    assert validar_correo("algo") == None
