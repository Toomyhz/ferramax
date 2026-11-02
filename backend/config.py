import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"

    USER_FERRAMAX = os.getenv("USER_FERRAMAX")
    PASSWORD_FERRAMAX = os.getenv("PASSWORD_FERRAMAX")
    WALLET_PASSWORD = os.getenv("WALLET_PASSWORD")

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