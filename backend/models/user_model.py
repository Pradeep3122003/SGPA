from bson import ObjectId
from flask import current_app
from extension import mongo

class User:
    @staticmethod
    def collection():
        # Safely get database after Flask app is initialized
        db = mongo.cx[current_app.config["DB"]]
        return db["users"]

    def __init__(self, f_name, l_name, email, password):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password

    def save(self):
        self.collection().insert_one({
            "f_name": self.f_name,
            "l_name": self.l_name,
            "email": self.email,
            "password": self.password
        })

    @staticmethod
    def find_by_email(email):
        return User.collection().find_one({"email": email})

    @staticmethod
    def find_by_id(user_id):
        return User.collection().find_one({"_id": ObjectId(user_id)})
