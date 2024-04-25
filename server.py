from flask import Flask, render_template, request, jsonify
from main import get_stock_data, get_macd_data, get_bb_data
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

CHATBOT_SERVICE_URL = 'http://localhost:9000/bot-response'

@app.route('/')
def home():
    return "<h1>Server is Up!</h1>"


@app.route('/api/data', methods=["GET", "POST"])
def api1():
    if request.method == 'POST':
        return get_stock_data()
    return "<h1>API running...</h1>"


@app.route('/api/macd', methods=["POST"])
def api2():
    if request.method == 'POST':
        return get_macd_data()


@app.route('/api/bb', methods=["POST"])
def api3():
    if request.method == 'POST':
        return get_bb_data()
    
@app.route('/api/chat', methods=["POST"])
def api4():
    if request.method == 'POST':
        body = request.json
        if 'prompt' in body:
            url = CHATBOT_SERVICE_URL
            response = requests.post(url, json=body)
            return response.json()
        else:
            return jsonify({'Error': 'Unprocessable Entity: prompt is required field in the body of request'}), 422


# Only for Dev
# if __name__ == "__main__":
#     app.run(host="localhost", port=8000, debug=True)
