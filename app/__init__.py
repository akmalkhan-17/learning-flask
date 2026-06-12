# this is the package initializer file, it will be executed when the package is imported
from flask import Flask


def create_app():

    # print(__name__)

    app = Flask(__name__)

    from .auth import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.route("/")
    def home():
        return "Welcome to the barber shop"

    @app.route("/about")
    def about():
        return "About Page"

    return app
