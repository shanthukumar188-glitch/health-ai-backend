
from flask import Flask
from flask_cors import CORS

from routes.analyze import analyze_bp
from routes.suggestions import suggestion_bp
from routes.image_ai import image_bp
from routes.report_ai import report_bp
from routes.hospital import hospital_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(analyze_bp)
app.register_blueprint(suggestion_bp)
app.register_blueprint(image_bp)
app.register_blueprint(report_bp)
app.register_blueprint(hospital_bp)



import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


