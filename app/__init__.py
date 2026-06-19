# this is the package initializer file, it will be executed when the package is imported
from flask import Flask
from .extensions import db, bcrypt


def create_app():

    # print(__name__)

    app = Flask(__name__)

    from .auth import auth_bp

    app.register_blueprint(auth_bp)  # removed this for now , url_prefix="/auth"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///barber.db"
    db.init_app(app)

    bcrypt.init_app(app)

    # @app.route("/")
    # def home():
    #     return "Welcome to the barber shop"

    @app.route("/about")
    def about():
        return "About Page"

    from .models import (
        User,
    )  ##import the model after initializing the app and the database, otherwise it will throw an error because the model will try to access the database before it is initialized

    return app
