from .getDolar import getDolar
import schedule
import threading
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

    def update_value(self):
        self.value = getDolar()

    def schedule_daily_update(self):
        schedule.every().day.at("04:00").do(self.update_value)

        thread = threading.Thread(target=self.run_schedule)
        thread.daemon = True
        thread.start()

    def run_schedule(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
