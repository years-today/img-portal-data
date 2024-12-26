from flask import Flask, jsonify
import os
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""
Get todays videos
"""
@app.route("/api/videos/today", methods=["GET"])
def get_videos_today():

    # Path:
    data_file_path = os.path.join("DB", "videos.json")
    
    if not os.path.exists(data_file_path):
        return jsonify({"error": "No data available for today."}), 404
    
    with open(data_file_path, "r", encoding="utf-8") as f:
        videos_list = json.load(f)  # This will be a list of dictionaries
    
    # wrap a dict
    return jsonify({"videos": videos_list})

"""
Get todays videos
"""
@app.route("/api/videos/archive", methods=["GET"])
def get_videos_archive():

    # Path:
    data_file_path = os.path.join("DB", "old_videos.json")
    
    if not os.path.exists(data_file_path):
        return jsonify({"error": "No data available for today."}), 404
    
    with open(data_file_path, "r", encoding="utf-8") as f:
        videos_list = json.load(f)  # This will be a list of dictionaries
    
    # wrap a dict
    return jsonify({"videos": videos_list})


# tests
@app.route("/")
def index():
    return "Flask service is up."

if __name__ == "__main__":
    # Run Flask in debug mode (for development)
    app.run(debug=True, host="0.0.0.0", port=5050)