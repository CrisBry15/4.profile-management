from flask import request, jsonify
from app.models import get_client_profile, get_organizer_profile

def get_profile():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    user_id = data.get("id")
    user_type = data.get("type")

    if not user_id or not user_type:
        return jsonify({"error": "Both 'id' and 'type' fields are required"}), 400

    try:
        if user_type == "client":
            profile = get_client_profile(user_id)
        elif user_type == "organizer":
            profile = get_organizer_profile(user_id)
        else:
            return jsonify({"error": "Invalid user type"}), 400

        if profile:
            return jsonify(profile), 200
        else:
            return jsonify({"error": "Profile not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
