import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from GDA Docker project",
                   version=os.getenv("APP_VERSION", "1.0"))

@app.route("/health")
def health():
    return jsonify(status="ok"), 200
