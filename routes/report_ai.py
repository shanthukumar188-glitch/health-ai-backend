from flask import Blueprint, request, jsonify
import pdfplumber
import os

report_bp = Blueprint("report_ai", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@report_bp.route("/analyze-report", methods=["POST"])
def analyze_report():

    if "report" not in request.files:
        return jsonify({
            "disease": "No PDF Uploaded",
            "causes": "Report not provided",
            "effects": "Cannot analyze",
            "precautions": "Upload valid PDF",
            "treatment": "Retry",
        })

    file = request.files["report"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    text = text.lower()

    if "hemoglobin" in text:
        disease = "Anemia (Low Hemoglobin)"
        causes = "Iron deficiency, blood loss."
        effects = "Fatigue, weakness, pale skin."
        precautions = "Increase iron-rich foods."
        treatment = "Iron supplements after doctor consultation."
    else:
        disease = "No Major Abnormality Found"
        causes = "Report appears normal."
        effects = "No immediate concern."
        precautions = "Maintain healthy diet."
        treatment = "Regular checkups."

    return jsonify({
        "disease_name": disease,
        "causes": causes,
        "effects": effects,
        "precautions": precautions,
        "treatment": treatment
    })
