from flask import Blueprint, request, jsonify, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies, jwt_required, get_jwt_identity
from models.user_model import User
from utils.validators import RegisterSchema
from marshmallow import ValidationError
from datetime import timedelta
from utils.password import hash_password, verify_password
from extension import limiter

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1")
register_schema = RegisterSchema()

@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = register_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    if User.find_by_email(data["email"]):
        return jsonify({"error": "Email already registered"}), 400

    hashed_pw = hash_password(data["password"])
    user = User(f_name=data["first_name"], l_name=data["last_name"], email=data["email"], password=hashed_pw)
    user.save()
    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
@limiter.limit("1 per minute")
def login():
    data = request.get_json()
    user = User.find_by_email(data.get("email"))

    if not user or not verify_password(data.get("password"), user["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user["_id"]), expires_delta=timedelta(hours=12))

    response = make_response(jsonify({
        "message": "Login successful",
        "user": {"name": user["f_name"], "email": user["email"]}
    }))
    set_access_cookies(response, token)
    return response, 200


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    response = jsonify({"message": "Logged out successfully"})
    unset_jwt_cookies(response)
    return response, 200
