from flask import Flask
from app.routes import profile_bp
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    # Configuración de JWT
    app.config["JWT_SECRET_KEY"] = "profile-management-secret"  # Puedes mover esto al .env si lo prefieres
    jwt = JWTManager(app)

    # Registro de blueprints
    app.register_blueprint(profile_bp, url_prefix="/profile")

    return app
