from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

# Load environment
load_dotenv()

app = Flask(__name__)
CORS(app, origins=[os.getenv("MYIP")])
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

# JWT + Rate limiting
jwt = JWTManager(app)
limiter = Limiter(get_remote_address, app=app, default_limits=[os.getenv("RATE_LIMIT")])

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB")]

# Import and register routes
from routes.auth import auth_bp
from routes.user import user_bp
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(user_bp, url_prefix="/api/user")

if __name__ == "__main__":
    app.run(debug=True)
