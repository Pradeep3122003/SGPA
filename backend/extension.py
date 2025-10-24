from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis

mongo = PyMongo()
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)

def init_redis(app):
    return redis.Redis(host=app.config['REDIS_IP'], port=app.config['REDIS_PORT'], db=0)
