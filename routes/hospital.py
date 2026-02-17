
from flask import Blueprint, request, jsonify

hospital_bp = Blueprint("hospital", __name__)

@hospital_bp.route("/recommend-hospital", methods=["POST"])
def recommend():
    return jsonify({
        "hospitals": [
            {"name": "Apollo Clinic", "distance": "1.2 km"},
            {"name": "City Care Hospital", "distance": "2.5 km"}
        ]
    })
