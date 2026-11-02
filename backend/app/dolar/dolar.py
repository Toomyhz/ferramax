from .getDolar import getDolar
import schedule
from threading import Thread
import time
#Clase para almacenar valor del dolar.
class Dolar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Dolar, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self,'value'):
            self.value = getDolar()
            self.dolar_schedule()

    def dolar_schedule(self):
        schedule.every(1).days.do(self.update_value)
        # Inicia un hilo para ejecutar el schedule en segundo plano
        thread = Thread(target=self.run_schedule, daemon=True)
        thread.start()

    def update_value(self):
        self.value = getDolar()
        print(f"Valor del dólar actualizado: {self.value}")

    def run_schedule(self):
        while True:
            schedule.run_pending()