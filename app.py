from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse

app = Flask(__name__)

# Simulated threat scoring based on domain keywords
THREAT_KEYWORDS = ['login', 'secure', 'free', 'download', 'paypal', 'gift-card', 'support', 'bank']

def analyze_url(url):
    parsed_url = urlparse(url.lower())
    domain = parsed_url.netloc
    path = parsed_url.path

    full_url = domain + path
    threat_score = 10
    threats_found = []

    for keyword in THREAT_KEYWORDS:
        if keyword in full_url:
            threat_score -= 2
            threats_found.append(keyword.capitalize())

    threat_score = max(threat_score, 1)

    result = {
        'trust_score': threat_score,
        'analysis_details': f"URL contains suspicious patterns: {', '.join(threats_found)}" if threats_found else "No obvious threat patterns detected.",
        'threats_found': threats_found if threats_found else None,
        'recommendation': 'Avoid clicking or sharing this link.' if threats_found else 'This URL appears safe.',
        'blocked': threat_score <= 3
    }
    return result

@app.route('/')
def index():
    return render_template('SL.html')  # Put SL.html in the `templates/` folder

@app.route('/analyze-url', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url', '')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    result = analyze_url(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
