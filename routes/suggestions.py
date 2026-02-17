
from flask import Blueprint, request, jsonify

suggestion_bp = Blueprint("suggestions", __name__)

@suggestion_bp.route("/daily-suggestions", methods=["POST"])
def suggestions():
    data = request.json
    suggestions = []

    if data.get("steps", 0) < 5000:
        suggestions.append("Walk at least 30 minutes today.")
    if data.get("spo2", 100) < 95:
        suggestions.append("Practice deep breathing exercises.")
    if data.get("heartRate", 60) > 95:
        suggestions.append("Avoid caffeine and relax.")

    if not suggestions:
        suggestions.append("Keep maintaining your healthy lifestyle!")

    return jsonify({"suggestions": suggestions})
