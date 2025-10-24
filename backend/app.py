from flask import Flask
from extension import mongo, jwt, limiter, init_redis
from config import Config
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)
    redis_client = init_redis(app)

    app.register_blueprint(auth_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
