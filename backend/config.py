import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()
class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DB = os.getenv("DB")

    REDIS_IP = os.getenv("REDIS_IP")
    REDIS_PORT = os.getenv("REDIS_PORT")
    REDIS_CONN = f"redis://{REDIS_IP}:{REDIS_PORT}"

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_SAMESITE = "None"
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_COOKIE_PATH = "/"
    JWT_SESSION_COOKIE = False
