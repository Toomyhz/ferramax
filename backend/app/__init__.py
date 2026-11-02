from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from extensions import db, migrate
from app.modules.brands.routes import brands_bp


def create_app(config_class=Config):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    
    # Import models
    from app.modules.users.models import User
    migrate.init_app(app, db)

    CORS(app, resources=app.config["CORS_RESOURCES"])

    app.register_blueprint(brands_bp)


    return app