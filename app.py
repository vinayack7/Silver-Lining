from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# List of suspicious keywords
suspicious_keywords = ['free', 'login', 'verify', 'click', 'password', 'bank', 'account', 'update']

@app.route('/')
def index():
    return render_template('SL.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url', '').lower()
    is_unsafe = any(keyword in url for keyword in suspicious_keywords)
    
    result = {
        'url': url,
        'status': 'Unsafe' if is_unsafe else 'Safe'
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
