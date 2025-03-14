from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Persistent storage directory
STORAGE_DIR = "/shail_PV_dir"
os.makedirs(STORAGE_DIR, exist_ok=True)

@app.route('/')
def home():
    return jsonify({"message": "Container is running."}), 200

@app.route('/store-file', methods=['POST'])
def store_file():
    data = request.get_json()

    if not data or 'file' not in data or 'data' not in data:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400

    file_name = data['file']
    file_content = data['data']

    if not file_name.strip():
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400

    file_path = os.path.join(STORAGE_DIR, file_name)

    try:
        with open(file_path, 'w') as f:
            f.write(file_content)

        return jsonify({"file": file_name, "message": "Success."}), 201
    except Exception as e:
        return jsonify({"file": file_name, "error": "Error while storing the file to the storage."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
