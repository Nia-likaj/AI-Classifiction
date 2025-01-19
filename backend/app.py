import os
import os
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.utils import secure_filename
from classifiers.ml_model import classify_file
from services.s3_service import upload_to_s3
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

# Endpoint for user login (Mocked for hackathon)
@app.route('/auth/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Mock authentication
    if username == "admin" and password == "password":
        token = create_access_token(identity=username)
        return jsonify(access_token=token)

    return jsonify({"error": "Invalid credentials"}), 401

# File upload and classification
@app.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    if 'files[]' not in request.files:
        return jsonify({"error": "No files provided"}), 400

    files = request.files.getlist('files[]')
    classifications = {}

    for file in files:
        filename = secure_filename(file.filename)
        local_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(local_path)

        # Classify file
        classification = classify_file(local_path)
        classifications[filename] = classification

        # Upload to S3
        s3_url = upload_to_s3(local_path, filename)
        classifications[filename] = {"classification": classification, "s3_url": s3_url}

        # Cleanup local file
        os.remove(local_path)

    return jsonify({"message": "Files classified successfully", "classifications": classifications})

if __name__ == '__main__':
    app.run(debug=True)

from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.utils import secure_filename
from classifiers.ml_model import classify_file
from services.s3_service import upload_to_s3, generate_s3_url
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

# Endpoint for user login (Mocked for hackathon)
@app.route('/auth/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Mock authentication
    if username == "admin" and password == "password":
        token = create_access_token(identity=username)
        return jsonify(access_token=token)

    return jsonify({"error": "Invalid credentials"}), 401

# File upload and classification
@app.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    if 'files[]' not in request.files:
        return jsonify({"error": "No files provided"}), 400

    files = request.files.getlist('files[]')
    classifications = {}

    for file in files:
        filename = secure_filename(file.filename)
        local_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(local_path)

        # Classify file
        classification = classify_file(local_path)
        classifications[filename] = classification

        # Upload to S3
        s3_url = upload_to_s3(local_path, filename)
        classifications[filename] = {"classification": classification, "s3_url": s3_url}

        # Cleanup local file
        os.remove(local_path)

    return jsonify({"message": "Files classified successfully", "classifications": classifications})

if __name__ == '__main__':
    app.run(debug=True)
