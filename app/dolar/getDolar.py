import json
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv 
import os

#Credenciales para el Banco Central
load_dotenv()
user = os.getenv('USER_DOLAR')
pw = os.getenv('PASSWORD_DOLAR')

#Fecha actual
current_date = datetime.now().strftime("%Y-%m-%d")

#Función para restar un día
def restarDia(current_date):
    date = datetime.strptime(current_date, "%Y-%m-%d")
    new_date = date - timedelta(days=1)
    new_date = new_date.strftime("%Y-%m-%d")
    return new_date

#Funcion para extraer precio del dolar desde el Banco Central
def getDolar():
    current_date = datetime.now().strftime("%Y-%m-%d")
    while True:
        url = f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user={user}&pass={pw}&timeseries=F073.TCO.PRE.Z.D&firstdate={current_date}&lastdate={current_date}&function=GetSeries"
        response = requests.get(url)
        data = json.loads(response. text. encode("utf-8"))
        series = data["Series"]
        obs = series["Obs"]
        if obs != []:
            dolar = obs[0]['value']
            return dolar
        else:
            current_date = restarDia(current_date)
