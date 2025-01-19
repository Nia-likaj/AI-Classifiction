import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'hackathon_secret_key')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'hackathon_jwt_secret')
    UPLOAD_FOLDER = 'uploads'
    S3_BUCKET = os.environ.get('S3_BUCKET', 'your-s3-bucket-name')
    S3_KEY = os.environ.get('S3_KEY', 'your-s3-access-key')
    S3_SECRET = os.environ.get('S3_SECRET', 'your-s3-secret-key')
    S3_REGION = os.environ.get('S3_REGION', 'us-east-1')
