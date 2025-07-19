from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

# Simulated malicious keyword matching
threat_database = {
    "paypal": {
        "trust_score": 1,
        "analysis_details": "Detected phishing page mimicking PayPal.",
        "threats_found": ["Phishing"],
        "blocked": True,
        "recommendation": "Avoid entering credentials here."
    },
    "wikipedia": {
        "trust_score": 9,
        "analysis_details": "Verified safe source.",
        "threats_found": [],
        "blocked": False,
        "recommendation": "Safe to browse."
    }
}

@app.route('/analyze-url', methods=['POST'])
def analyze_url():
    data = request.json
    url = data.get("url", "").lower()

    time.sleep(1.2)  # Simulate processing time

    for keyword, result in threat_database.items():
        if keyword in url:
            return jsonify(result)

    # Default: simulate a random result
    trust_score = random.randint(1, 10)
    return jsonify({
        "trust_score": trust_score,
        "analysis_details": "Simulated analysis completed.",
        "threats_found": ["Suspicious Script"] if trust_score <= 4 else [],
        "blocked": trust_score <= 3,
        "recommendation": "Exercise caution." if trust_score <= 6 else "Safe to use."
    })


@app.route('/analyze-media', methods=['POST'])
def analyze_media():
    manipulation_score = random.randint(0, 100)

    result = {
        "manipulation_score": manipulation_score,
        "technical_analysis": "Simulated forensic pattern scan.",
        "detected_techniques": ["Face Swap", "Lip Sync AI"] if manipulation_score >= 70 else [],
        "recommendation": "Do not trust this media." if manipulation_score >= 70 else (
            "Further verification advised." if manipulation_score >= 30 else "Authentic visual media.")
    }

    return jsonify(result)


@app.route('/')
def index():
    return "Silver Lining AI backend is running."

if __name__ == '__main__':
    app.run(debug=True)
