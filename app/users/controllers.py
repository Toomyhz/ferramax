from flask import jsonify
from..suscription.validations import validar_correo, validarFromDatabase
from ..suscription.db import saveDb
import hashlib
def create_user(request):
    data = request.json
    email = data['email']
    contrasena = data['contrasena']

    # Validar que se envio un correo
    if not email or not contrasena:
        return jsonify({"message": "Missing email or password"}), 400
    
    #Validar formato correo
    email_valido = validar_correo(email)
    if email_valido == False:
        return jsonify(error="Correo electronico no valido"), 400

    # Validar que no exista correo en DB
    resp = validarFromDatabase(email)
    if resp.json.get('error'):
        print(resp.json.get('error'))
        return jsonify(error = resp.json['error']), 200
    elif resp.json.get('email_valido'):
        contrasena_segura = hashlib.sha256(contrasena.encode()).hexdigest()
        # Una vez validado todo, guardar en DB
        return saveDb(email, contrasena_segura)
