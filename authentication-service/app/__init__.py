from flask import Flask
from config import Config
from app.routes import account_bp, auth_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(account_bp)
    app.register_blueprint(auth_bp)

    return app