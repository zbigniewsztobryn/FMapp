import os
from dotenv import load_dotenv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
env_file = base_dir / '.env'
load_dotenv(env_file)

class Config:
    DEBUG = True
    SECRET_KEY      = os.environ.get('SECRET_KEY')
    SECRET_NAME     = os.environ.get('SECRET_NAME')
    SECRET_USER     = os.environ.get('SECRET_USER')
    SECRET_PASSWORD = os.environ.get('SECRET_PASSWORD')
    SECRET_HOST     = os.environ.get('SECRET_HOST')

    AWS_ACCESS_KEY_ID       = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY   = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

