from flask import Blueprint, jsonify
from app.profile_controller import get_profile

# Definir el blueprint
profile_bp = Blueprint('profile', __name__)

# Ruta de prueba
@profile_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Profile Management Microservice funcionando correctamente"}), 200

# Ruta para obtener el perfil de un usuario
@profile_bp.route('/get', methods=['POST'])
def profile_route():
    return get_profile()
