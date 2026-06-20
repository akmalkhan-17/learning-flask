# this is the package initializer file, it will be executed when the package is imported
from flask import Flask
from config import Config
from app.models import User
from .extensions import db, bcrypt, login_manager


def create_app():

    # print(__name__)

    app = Flask(__name__)

    from .auth import auth_bp

    app.register_blueprint(auth_bp)  # removed this for now , url_prefix="/auth"

    app.config.from_object(Config)  # this will load the config from the Config class in config.py

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///barber.db" #this will create a sqlite database file named barber.db in the root directory of the project

    db.init_app(app)

    bcrypt.init_app(app)

    login_manager.init_app(app)

    # @app.route("/")
    # def home():
    #     return "Welcome to the barber shop"

    @app.route("/about")
    def about():
        return "About Page"

    from .models import User ##import the model after initializing the app and the database, otherwise it will throw an error because the model will try to access the database before it is initialized

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    login_manager.login_view = "auth.login"  # this will redirect the user to the login page if they try to access a protected route without being logged in || auth.login means auth is the bp and login is the route name of the login function in auth.py

    return app
