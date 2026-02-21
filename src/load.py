import pandas as pd
import os
import boto3
from dotenv import load_dotenv

# Loads hidden keys from the .env file
load_dotenv()

def save_data(df, file_path):
    # Ensure the 'data' directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Save as Parquet
    df.to_parquet(file_path, engine="pyarrow", compression='snappy')
    print(f"File saved to {file_path}")

def upload_to_s3(file_path, bucket_name):
    # Boto3 automatically looks for aws_access_key_id
    # and aws_secret_access_key in your environment/ .env
    s3 = boto3.client('s3')

    # We want the file name (inflation_2023.parquet), not the whole path
    file_name = os.path.basename(file_path)

    try:
        s3.upload_file(file_path, bucket_name, file_name)
        print(f"Cloud success: Uploaded to s3://{bucket_name}/{file_name}")
    except Exception as e:
        print(f"Cloud error: AWS Upload failed. {e}")

