# this file is for extensions that we want to use in our app, such as SQLAlchemy for database management. We can initialize the extension here and then import it in our app.py file to use it.
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()  # we did this instead of doing db = SQLAlchemy(app) because we want to initialize the extension in the create_app function in app.py, otherwise it will throw an error because the extension will try to access the app before it is created.

bcrypt = Bcrypt()

login_manager = LoginManager()
