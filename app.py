import os
from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__, template_folder='.')


REAL_API_URL = "https://oxmzoo.taitanx.workers.dev/"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/search')
def proxy_search():
    mobile = request.args.get('mobile')
    if not mobile:
        return jsonify({"error": "No number provided"}), 400
    
    try:
   
        response = requests.get(f"{REAL_API_URL}?mobile={mobile}")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": "Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)