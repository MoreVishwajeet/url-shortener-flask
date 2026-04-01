from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

# In-memory storage
url_map = {}

# Home route
@app.route('/')
def home():
    return "URL Shortener Running 🚀"

# API to shorten URL
@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "No URL provided"}), 400

    short_id = str(len(url_map) + 1)
    url_map[short_id] = long_url

    short_url = f"http://localhost:5000/{short_id}"
    return jsonify({"short_url": short_url})

# Redirect route
@app.route('/<short_id>')
def redirect_url(short_id):
    long_url = url_map.get(short_id)

    if not long_url:
        return "Invalid URL ❌", 404

    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)