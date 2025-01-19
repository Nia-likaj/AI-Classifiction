import boto3
from botocore.exceptions import NoCredentialsError
from config import Config

s3 = boto3.client(
    's3',
    aws_access_key_id=Config.S3_KEY,
    aws_secret_access_key=Config.S3_SECRET,
    region_name=Config.S3_REGION,
)

def upload_to_s3(file_path, filename):
    try:
        s3.upload_file(file_path, Config.S3_BUCKET, filename)
        return generate_s3_url(filename)
    except NoCredentialsError:
        raise Exception("AWS S3 credentials not found")

def generate_s3_url(filename):
    return f"https://{Config.S3_BUCKET}.s3.{Config.S3_REGION}.amazonaws.com/{filename}"
