from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config

# compat temporal con código actual que hace `from app import connection`
connection = None

def create_app(config_class=Config):
    global connection

    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, resources=app.config["CORS_RESOURCES"])

    connection = connect(
        app.config["USER_FERRAMAX"],
        app.config["PASSWORD_FERRAMAX"],
        app.config["WALLET_PASSWORD"],
    )

    app.register_blueprint(tools_bp)


    return app