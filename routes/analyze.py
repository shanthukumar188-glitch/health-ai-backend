
from flask import Blueprint, request, jsonify
from database.db import vitals_collection
from datetime import datetime

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    hr = data.get("heartRate")
    spo2 = data.get("spo2")

    record = {
        "heartRate": hr,
        "spo2": spo2,
        "timestamp": datetime.utcnow()
    }

    vitals_collection.insert_one(record)

    if hr > 110 or spo2 < 90:
        return jsonify({"status": "Abnormal"})
    return jsonify({"status": "Normal"})
