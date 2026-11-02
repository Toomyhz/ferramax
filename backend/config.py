import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"


    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CORS_RESOURCES = {
        r"/api/*": {
            "origins": ["http://localhost:5173", "http://localhost:4173"],
            "methods": ["POST", "GET"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True,
        },
        r"/suscribe/*": {"origins": ["http://localhost:5173", "http://localhost:4173"]},
        r"/tools/*": {"origins": ["http://localhost:5173", "http://localhost:4173"]},
        r"/categories/*": {"origins": ["http://localhost:5173", "http://localhost:4173"]},
        r"/marcas/*": {"origins": ["http://localhost:5173", "http://localhost:4173"]},
        r"/users/*": {
            "origins": ["http://localhost:5173", "http://localhost:4173"],
            "methods": ["POST", "GET", "OPTIONS"],
        },
    }