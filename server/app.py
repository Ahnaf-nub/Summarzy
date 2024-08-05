from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
app = Flask(__name__)
CORS(app)

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {api_key}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    if len(text) > 100:
        output = query({"inputs": text})
        summary = output[0]['summary_text'] if 'summary_text' in output[0] else "Error: Unable to summarize text"
    else:
        summary = "The text is too short to be summarized"
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
