import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    # Add other configuration variables as needed

# Example usage:
# from config import Config
# print(Config.SECRET_KEY)