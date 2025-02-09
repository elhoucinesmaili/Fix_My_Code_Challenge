#!/usr/bin/python3
"""
Fixed Flask Status API
"""
from flask import Flask, jsonify
from api.v1.views import app_views # Import the Blueprint object

app = Flask(__name__)
app.register_blueprint(app_views) # Register the Blueprint

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
 """Handles 404 errors"""
 return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)
