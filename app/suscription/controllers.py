from flask import jsonify
from .validations import validar_correo, validarFromDatabase
from .db import saveDb
def suscribe(request):
    data = request.json
    email = data['email']
    # Validar que se envio un correo
    if email=="":
        error = "Campo correo vacio"
        return jsonify(error=error), 200
    #Validar formato correo
    email_valido = validar_correo(email)
    print(email_valido)
    if email_valido == False:
        return jsonify(error="Correo electronico no valido"), 200
    # Validar que no exista correo en DB
    resp = validarFromDatabase(email)
    if resp.json.get('error'):
        print(resp.json.get('error'))
        return jsonify(error = resp.json['error']), 200
    elif resp.json.get('email_valido'):
        # Una vez validado todo, guardar en DB
        return saveDb(email)
            
    
